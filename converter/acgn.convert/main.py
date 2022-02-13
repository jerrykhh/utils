from ACGNRequest import ACGHRequest
from ACGNResponseHTML import Book
from concurrent.futures import ThreadPoolExecutor, as_completed
import time, gc

# print the url when the user input
def print_urls(urls: list):
    for (i, item) in enumerate(urls, start=1):
        print(f"[{i}]: {item}")

# print converted book list
def print_book_list(books: list):
    print("=========================")
    for book in books:
        print(book)
    print("=========================")

def main():
    print("ACGH.convert starting...")
    urls = []
    print("Please enter EXIT to start the PDF generate")
    
    # Let User input the urls
    while True:
        user_input = input("Please Enter the URL: ")
        if user_input == "EXIT":
            break
        urls.append(user_input)
        print_urls(urls)
    start_time = time.time()
    books = []
    threads = []
    threadPool = ThreadPoolExecutor(max_workers=3)

    for (i, url) in enumerate(urls, start=1):
        # Create the GET request it will return the ACGNResponseHTML object
        request = ACGHRequest(url).get()
        # find the attribute "_src" 
        image_urls = request.find_source("_src")
        # download all book pages (image)
        book = request.download_image(image_urls)
        books.append(book)

        if i % 3 == 0:
            threads.append(threadPool.submit(Book.save_books, books[0:3]))
            del books[0:3]
            gc.collect()
        elif i == len(urls):
            threads.append(threadPool.submit(Book.save_books, books[0::]))
            del books
            gc.collect()

    saved_books = []
    for future in as_completed(threads):
        saved_books += future.result()

    saved_books = sorted(saved_books, key=lambda x: x.title)

    # Save all image to .pdf
    print_book_list(saved_books)
    end_time = time.time()
    print(f"{end_time - start_time} runtime.")

if __name__ == "__main__":
    main()
