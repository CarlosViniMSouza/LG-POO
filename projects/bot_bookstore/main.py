from botcity.web import WebBot, Browser
from webdriver_manager.chrome import ChromeDriverManager

from services.services import *

def main():
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()
    
    try:
        bot.browse("https://www.botcity.dev")
    
        author = Author("The Man") # Criando autor
        bookstore = BookStore("My Personal BookStore") # Criando a bookstore

        # Adicionando books à bookstore e a classe 'Author'
        book1 = Book("The C++ Programming Language", author, 100)
        book2 = Book("The Big Start of Python", author, 101)

        bookstore.add_book(book1)
        bookstore.add_book(book2)
        print("\n")

        author.add_book(book1)
        author.add_book(book2)
        print("\n")

        bookstore.show_total_books() # Exibindo total de livros
        print("\n")

        bookstore.show_available_books() # Exibindo o inventario
        print("\n")

        bookstore.register_loan("The C++ Programming Language") # Emprestando um livro
        bookstore.register_loan("The C++ Programming Language") # Emprestando o livro (de novo)
        bookstore.register_loan("The C++ Great Programming Language") # Emprestando livro não existente
        print("\n")

        # Devolvendo o livro
        book1.return_book()
        book2.return_book()
        print("\n")

        # Registrando devolucao
        bookstore.register_return("The C++ Programming Language")
        bookstore.register_return("The Big Start of Python")

        # Tentando devolver livro não existente
        bookstore.register_return("The C++ Great Programming Language")
        print("\n")

        bookstore.show_available_books() # Exibindo livros disponiveis
    
    except Exception as ex:
        print(ex)
        bot.save_screenshot(r'C:\Users\matutino\Documents\projects\lg-poo\projects\bot_bookstore\resources\erro.png')

    finally:
        bot.wait(3000)
        bot.stop_browser()

if __name__ == '__main__':
    main()
