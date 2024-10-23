class Author:
    def __init__(self, name: str):
        self._name = name
        self._list_books = []

    def add_book(self, book):
        self._list_books.append(book)
        print(f'The book "{book._title}" was add to list books')

    def show_books(self) -> None:
        if len(self._list_books) == 0:
            print("The list is empty")
        else:
            print("\nBookstore has the books:")

            for book in self._list_books:
                book.show_infos()

    def get_name(self) -> str: 
        return self._name

    def get_list_books(self) -> list:
        return self._list_books

    def set_name(self, name) -> None:
        self._name = name

class Book:
    def __init__(self, title: str, author: str, code: int):
        self._title = title
        # self.author = Author(author)
        self.author = author
        self._code = code
        self._available = True

    def get_title(self) -> str:
        return self._title

    def get_author(self) -> str:
        return self.author

    def get_code(self) -> int:
        return self._code

    def get_available(self) -> bool:
        return self._available

    def set_title(self, title) -> None:
        self._title = title

    def set_author(self, author) -> None:
        # self.author = Author(author)
        self.author = author
        
    def set_code(self, code) -> None:
        self._code = code

    def set_available(self, available) -> None:
        self._available = available

    def to_loan(self) -> None:
        if self._available:
            self._available = False
            print(f'The book "{self._title}" from "{self.author.get_name()}" was loaned')
        else:
            print(f'The book "{self._title}" from "{self.author.get_name()}" is not available')

    def return_book(self) -> None:
        self._available = True
        print(f"The book {self._title} was returned!")

class BookStore:
    _total_books = 0

    def __init__(self, name: str) -> None:
        self.name = name
        self._books = []
        self._loans = {
            "code": Book("Title 01", "Author 01", "Code 01"),
            "name": "client name"
        } # improve this

    def add_book(self, book) -> None:
        self._books.append(book)
        BookStore._total_books += 1

        print(f'The book "{book._title}" was add to inventory!')

    def register_loan(self, title) -> None:
        for book in self._books:
            if book._title == title:
                book.to_loan()
                return None

        print(f'The book "{title}" was not found in inventory!')

    def register_return(self, title) -> None:
        for book in self._books:
            if book._title == title:
                book.return_book()
                return None

        print(f'The book "{title}" was not found in inventory!')

    def show_available_books(self) -> None:
        for book in self._books:
            if book._available == True:
                print(f"Book available: {book._title}")
    
    @classmethod
    def show_total_books(cls) -> None:
        print(f"Total books founded: {cls._total_books}")
        
"""   
author = Author("The Man")
bookstore = BookStore("My Personal BookStore")

# Adicionando books à bookstore e a classe 'Author'
book1 = Book("The C++ Programming Language", author, 100)
book2 = Book("The Big Start of Python", author, 101)

bookstore.add_book(book1)
bookstore.add_book(book2)
print("\n")

author.add_book(book1)
author.add_book(book2)
print("\n")

bookstore.show_total_books()
print("\n")

bookstore.show_available_books()
print("\n")

bookstore.register_loan("The C++ Programming Language")
bookstore.register_loan("The C++ Programming Language")
bookstore.register_loan("The C++ Great Programming Language")
print("\n")

book1.return_book()
book2.return_book()
print("\n")

bookstore.register_return("The C++ Programming Language")
bookstore.register_return("The Big Start of Python")

bookstore.register_return("The C++ Great Programming Language")
print("\n")

bookstore.show_available_books() # Exibindo livros disponiveis    
"""