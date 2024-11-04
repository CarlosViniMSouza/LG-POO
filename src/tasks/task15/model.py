from functools import reduce
import json, csv, pickle

class Book:
    def __init__(self, title: str, author: str, year_published: int, gender: str) -> None:
        self.title = title
        self.author = author
        self.year_published = year_published
        self.gender = gender


class BookStore:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book) -> None:
        self.books.append(book)

    def list_books(self) -> None:
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Year_published: {book.year_published}, Gender: {book.gender}")

    def list_books_by_author(self, author: str) -> list:
        return list(filter(lambda book: book.author == author, self.books))
    
        # return books_author

    def count_books_by_gender(self, gender: str) -> int:
        return reduce(lambda count, book: count + (1 if book.gender == gender else 0), self.books, 0)

    ## Save File (JSON) ##

    def save_json(self, file_title="./assets/books/books.json") -> None:
        data = [
            {
                "title": book.title,
                "author": book.author,
                "year_published": book.year_published, 
                "gender": book.gender
            } for book in self.books
        ]

        with open(file_title, "w") as file_json:
            json.dump(data, file_json)
        
        print(f"Data saved in {file_title}")

    def load_json(self, file_title="./assets/books/books.json") -> None:
        with open(file_title, "r") as file_json:
            data = json.load(file_json)
            self.books = [Book(**book) for book in data]

        print(f"Data loaded from {file_title}")

    ## Save File (CSV) ##

    def save_csv(self, file_title="./assets/books/books.csv") -> None:
        with open(file_title, "w", newline="") as file_csv:
            writer = csv.writer(file_csv)
            writer.writerow(["title", "author", "year_published", "gender"])

            for book in self.books:
                writer.writerow([book.title, book.author, book.year_published, book.gender])

            print(f"Data saved in {file_title}")

    #NOTE: I need to see how to do line 69 #
    def load_csv(self, file_title="./assets/books/books.csv") -> None:
        with open(file_title, "r") as file_csv:
            reader = csv.reader(file_csv)
            next(reader)  # Skip Header

            self.books = [Book(line[0], line[1], line[2], line[3]) for line in reader]

        print(f"Data loaded from {file_title}")

    ## Save File (PICKLE) ##

    def save_pickle(self, file_title="./assets/books/books.pkl") -> None:
        with open(file_title, "wb") as file:
            pickle.dump(self.books, file)

        print(f"Data saved in {file_title}")

    def load_pickle(self, file_title="./assets/books/books.pkl") -> None:
        with open(file_title, "rb") as file:
            self.books = pickle.load(file)

        print(f"Data loaded from {file_title}")

    ## Functional Reports ##

    def list_all_titles(self) -> list:
        list_titles = list(map(lambda book: book.title, self.books))

        return list_titles

    def total_books_by_gender(self, gender):
        for book in self.books:
            total_books = reduce(lambda gender, book: gender == book.gender, self.books, 0)

        return total_books