class Book:
    def __init__(self, title: str, author: str, available: bool):
        self.title = title
        self.author = author
        self.available = available

    def to_loan(self) -> None:
        pass

    def return_book(self) -> None:
        pass

    def show_infos(self) -> None:
        pass

class Bookstore:
    books: Book

    def add_book(books) -> None:
        print(f"Add Book: {books}")

    def return_book(books) -> None:
        pass

    def show_inventory(books) -> None:
        pass
