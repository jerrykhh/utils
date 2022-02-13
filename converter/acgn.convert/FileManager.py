import os
import requests
import time
import gc
from concurrent.futures import ThreadPoolExecutor, as_completed

from PIL import Image, UnidentifiedImageError
from urllib3.exceptions import ProtocolError


class FileManager:

    @staticmethod
    def url_convert_Image(index: int, url: str):
        can_continue: bool = False
        while not can_continue:
            try:
                print(f"--->{url}")
                image = Image.open(requests.get(url, stream=True).raw)
                image.convert('RGB')
                can_continue = True
            except UnidentifiedImageError:
                print("Request Error: try again now")
            except ProtocolError:
                print("Request Error: try again now")
                

        return _ThreadReturnImage(index, image)

    @staticmethod
    def download_images_and_save_PDF(path, title: str, html_attr_obj_urls: list):

        if not os.path.exists(path):
            os.mkdir(path)

        if len(html_attr_obj_urls) == 0:
            print("Book not found.")
            return

        images = FileManager.download_images(html_attr_obj_urls)

        return FileManager.save_PDF(path, title, images)
    
    @staticmethod
    def save_PDF(path, title:str, images: list):
        if not os.path.exists(path):
            os.mkdir(path)

        if len(images) == 0:
            print("Book not found.")
            return
        
        if len(images) > 1:
            images[0].save(f"{path}/{title}.pdf", save_all=True, append_images=images[1::])
        else:
            images[0].save(f"{path}/{title}.pdf")

        page_count = len(images)
        print(f"{title}", end=": ")
        print(f"{page_count} page found.")
        del images

        return page_count

    @staticmethod
    def download_images(html_attr_obj_urls: list) -> list:
        if len(html_attr_obj_urls) == 0:
            print("Book not found.")
            return
        with ThreadPoolExecutor(max_workers=18) as t:
            threads = []
            index = 0
            for html_attr_obj in html_attr_obj_urls:
                if "http" in html_attr_obj.content:
                    thread = t.submit(FileManager.url_convert_Image, index, html_attr_obj.content)
                    threads.append(thread)
                    index += 1

            thread_returned_images = []
            for future in as_completed(threads):
                thread_returned_images.append(future.result())

            thread_returned_images = sorted(thread_returned_images, key=lambda x: x.index)
            get_image = lambda thread_return_image: thread_return_image.image
            images = [get_image(img) for img in thread_returned_images]
            return images

    @staticmethod
    def save_book(path:str, book):
        if book.images == None or len(book.images) > 1:
            book.images[0].save(f"{path}/{book.title}.pdf", save_all=True, append_images=book.images[1::])
        else:
            book.images[0].save(f"{path}/{book.title}.pdf")
        
        del book.images
        gc.collect()
        return book

    @staticmethod
    def save_books(path, books) -> None:
        if not os.path.exists(path):
            os.mkdir(path)

        if len(books) == 0:
            print("Book not found.")
            return
        
        threads = []
        saved_books = []
        with ThreadPoolExecutor(max_workers=3) as t:
            for book in books:
                threads.append(t.submit(FileManager.save_book, path, book))
            
            for future in as_completed(threads):
                saved_books.append(future.result())
        
        del books
        gc.collect()
        return saved_books


class _ThreadReturnImage:

    def __init__(self, index, image):
        self.index = index
        self.image = image

    def __str__(self):
        return f"{self.index}: {self.image}"
