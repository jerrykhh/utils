from FileManager import FileManager
import os

# ACGNRequest GET request return object
class ACGHResponseHTML:
    def __init__(self, html):
        self.html = html
        self.title = None

    def find_source(self, attr: str):
        # Create the ListString obj check the char whether match
        ls = ListString(attr)
        content:str = ""
        
        sources = []
        
        # Loop all Char (GET request return response text[HTML])
        for char in list(self.html):
            
            # Check the ListString whether matched 
            if not ls.match():
                # Not match so it need to check
                ls.check(char)
            else:
                # if match required HTML attr
                content += char
                # len(content) > 2 for skip (=") or char is (<)
                if len(content) > 2 and char == '"' or char == "<":
                    if content.strip() != "":
                        if char == '"':
                            # for html Attr so need to skip ="content"
                            sources.append(HTMLAttrValue(content, 2, len(content)-1))
                        elif char == "<":
                            # for html tag skip "<h1>content<"
                            sources.append(HTMLAttrValue(content, 0, len(content)-1))
                    ls.clear()
                    content = ""

        return sources
    
    # get book title
    def get_title(self, attr:str ="<h1>"):
        if self.title is None:
            # it will return the list so the title will store in index 0
            self.title = self.find_source(attr)[0].content
        return self.title
    
    def download_image(self, image_urls) -> list:
        title = self.get_title()
        print(f"{title} download start")
        return Book(title, images=FileManager.download_images(image_urls)) 
    
    def save_PDF(self, images):
        title = self.get_title()
        page_count = FileManager.save_PDF(f"{os.path.dirname(__file__)}/output", title, images)
        return Book(title, page_count)

    def save_imageURL_PDF(self, images):
        title = self.get_title()
        # Save the image to the PDF
        page_count = FileManager.download_images_and_save_PDF(f"{os.path.dirname(__file__)}/output", title, images)
        return Book(title, page_count)


class ListString:
    
    def __init__(self, words) -> None:
        self.words = words
        self.pointer = 0

    def match(self) -> bool:
        # word index equal words.length == All Match
        if self.pointer == len(self.words):
            return True
        return False

    def check(self, char):
        # check words whether match char
        if self.words[self.pointer] == char:
            # move next index to let next time check next time
            self.pointer += 1
        else:
            # not match init the index
            self.pointer = 0
    
    def clear(self):
        self.pointer = 0


class HTMLAttrValue:
    
    def __init__(self, content, start_index, end_index):
        self.content = content[start_index: end_index]
    
    def __str__(self):
        return self.content

class Book:

    def __init__(self, title:str, page:int=None, images:list=None):
        self.title = title
        if images != None:
            self.page = len(images)
        else:
            self.page = page
        self.images = images

    def __str__(self):
        return f"{self.title}\t {self.page} pages"

    @staticmethod
    def save_books(books:list, path:str=None):
        if path == None:
            path = f"{os.path.dirname(__file__)}/output"
        return FileManager.save_books(path, books)

    @staticmethod
    def save_book(book, path:str=None):
        if path == None:
            path = f"{os.path.dirname(__file__)}/output"
        FileManager.save_book(path, book)