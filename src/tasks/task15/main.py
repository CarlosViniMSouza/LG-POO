from model import *

bookstore = BookStore()

# Atividade 01 - Adicionar Novos Livros
bookstore.add_book(Book("Programming with Python", "Python Creator", 1983, "Education"))
bookstore.add_book(Book("Programming with C++", "C++ Creator", 1992, "Education"))
bookstore.add_book(Book("Programming with Java", "Java Creator", 1994, "Education"))

# Atividade Extra - Listar todos os títulos de livro
print(f"All titles: {bookstore.list_all_titles()}")

# Atividade 02 - Consultar livros por autor
search_author = bookstore.list_books_by_author("C++ Creator")

for book in search_author:
    print(f"Books from C++ Creator: {book.title}")

# Atividade 03 - Consultar livros por autor
search_gender = bookstore.count_books_by_gender("Education")

print(f"Total 'Education' Books: {search_gender}")

print("\n")

# Atividade 04 - Exportar e Importar arquivos JSON, CSV e PICKLE
bookstore.save_json()
bookstore.load_json()

bookstore.save_csv()
bookstore.load_csv()

bookstore.save_pickle()
bookstore.load_pickle()

print("\n")

# Atividade 05 - Verificar consistência
bookstore.list_books()