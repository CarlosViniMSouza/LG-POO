class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.available = True

    def to_loan(self) -> None:
        if self.available:
            self.available = False
            print(f'The book "{self.title}" was loaned')
        else:
            print(f'The book "{self.title}" is not available')

    def return_book(self) -> None:
        self.available = True
        print(f"The book {self.title} was returned!")

    def show_infos(self) -> None:
        available = "disponível" if self.available else "emprestado"
        print(f'Title: {self.title}, Author: {self.author}, Available: {self.available} \n')

class BookStore:
    def __init__(self):
        self.inventory = []

    def add_book(self, book) -> None:
        self.inventory.append(book)
        print(f'The book "{book.title}" was add to inventory!')

    def to_loan_book(self, title) -> None:
        for book in self.inventory:
            if book.title == title:
                book.to_loan()
                return None

        print(f'The book "{title}" was not found in inventory!')

    def show_inventory(self) -> None:
        if len(self.inventory) == 0:
            print("The inventory is empty")
        else:
            print("\nBookstore Inventory:")

            for book in self.inventory:
                book.show_infos()

# Execute
if __name__ == "__main__":
    # Criando a bookstore
    bookstore = BookStore()

    # Adicionando books à bookstore
    book1 = Book("The C++ Programming Language", "Bjarne Stroustrup")
    book2 = Book("The Big Start of Python", "Guido van Rossum")
    book3 = Book("The Java Programming Language", "James Arthur Gosling")

    bookstore.add_book(book1)
    bookstore.add_book(book2)
    bookstore.add_book(book3)

    # Exibindo o inventory
    bookstore.show_inventory()

    # Emprestando um book
    bookstore.to_loan_book("The C++ Programming Language")

    # Tentando emprestar novamente o mesmo book
    bookstore.to_loan_book("The C++ Programming Language")

    # Tentando emprestar um livro não existente
    bookstore.to_loan_book("The C++ Great Programming Language")

    # Devolvendo o book
    book1.return_book()
    book2.return_book()
    book3.return_book()

    # Exibindo o inventory novamente
    bookstore.show_inventory()