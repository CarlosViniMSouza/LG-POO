class Book:
    def __init__(self, title, author):
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
        print(f'Title: {self.title}, Author: {self.author}, Available: {self.available}')

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
                return

        print(f'O book "{title}" was not found in inventory!')

    def show_inventory(self) -> None:
        if len(self.inventory) == 0:
            print("The inventory is empty")
        else:
            print("Bookstore Inventory:")

            for book in self.inventory:
                book.show_infos()

# Execute
if __name__ == "__main__":
    # Criando a bookstore
    bookstore = BookStore()

    # Adicionando books à bookstore
    book1 = Book("1984", "George Orwell")
    book2 = Book("Dom Casmurro", "Machado de Assis")

    bookstore.add_book(book1)
    bookstore.add_book(book2)

    # Exibindo o inventory
    bookstore.show_inventory()

    # Emprestando um book
    bookstore.to_loan_book("1984")

    # Tentando emprestar novamente o mesmo book
    bookstore.to_loan_book("1984")

    # Devolvendo o book
    book1.return_book()

    # Exibindo o inventory novamente
    bookstore.show_inventory()