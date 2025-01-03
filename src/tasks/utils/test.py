"""
## Example 01 - numeric fuction

double = lambda x: x * 3

print(double(5))
"""

"""
## Example 02 - sort tuples by age

folks = [("Carlos", 23), ("Vinicius", 20), ("Souza", 26)]
folks_sorted = sorted(folks, key=lambda people: people[1])

print(folks_sorted)
"""

"""
## Example 03 - lambda with dict

products = [
    {
        "name": "T-shirt", 
        "price": 15
    },
    {
        "name": "Jeans", 
        "price": 40.6
    },
    {
        "name": "Blues", 
        "price": 32.4
    }
]

products_sorted = sorted(
    products, 
    key=lambda product: product["price"]
)

products_sorted_inverted = sorted(
    products, 
    key=lambda product: product["price"], 
    reverse=True
)

print(products_sorted, "\n")
print(products_sorted_inverted)
"""

"""
## Example 04 - map()

numbers = [1, 2, 3, 4, 5]

doubles = list(map(lambda x: x * 3, numbers))
print(doubles)

temp_celsius = [0 ,20, 30, 40, 50]
temps_celsius = list(map(lambda x: x * 9/5 + 32, temp_celsius))
print(temps_celsius)

numbers_pot = list(map(lambda x: x ** 2, numbers))
print(numbers_pot)
"""

"""
## Example 05 - filter()

numbers = [1, 2, 3, 4, 5]

pares = list(filter(lambda x: x % 2 == 0, numbers))
print(pares)

words = ["Python", "Java", "JavaScript", "Go"]
long_words = list(filter(lambda x: len(x) >= 5, words))
print(long_words)
"""

"""
## Example 06 - reduce()

numbers = [1, 2, 3, 4, 5]

from functools import reduce

sum = reduce(lambda x, y: x + y, numbers)
print(sum)

long_num = reduce(lambda x, y: x if x > y else y, numbers)
print(long_num)
"""

"""
### Example 07 - list comprehensions

import json

numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]
print(squares, "\n")

squares_dict = {x: x ** 2 for x in numbers}
json_squares = json.dumps(squares_dict)
print(json_squares, "\n")

squares_set = {x ** 2 for x in numbers}
print(squares_set, "\n")

squares_tuple = (lambda x: x ** 2 for x in numbers)
print(squares_tuple) # it's dont work so well ...
"""

"""
## Example 08 - decorators

def welcome(func):
    def wrapper(name):
        print("Hello")
        func(name)
        print("Have a good day!")

    return wrapper

@welcome
def welcome_user(name):
    print(f"Hy {name}, you're welcome")

welcome_user("Carlos")
"""

"""

## Example 09 - decorators parametized

def product_number(number):
    def decorator(func):
        def wrapper(x):
            return func(x) * number
        return wrapper
    return decorator

@product_number(number=3)
def sum_two(num01):
    return num01 + 2

print(f"The sum is {sum_two(5)}")
"""

"""

## Example 10 - Generators

def generate_pares(limit):
    n = 0

    while n <= limit:
        yield n
        n += 4

for number in generate_pares(100):
    print(number, end=" ")
"""

"""

class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.limit:
            result = self.n
            self.n += 1

            return result
        else:
            raise StopIteration

counter = Counter(3)

for number in counter:
    print(number, end=" ")
"""

"""
class IteratorNames:
    def __init__(self, names):
        self.names = names
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.names):
            name = self.names[self.index].upper()
            self.index += 1

            return name
        else:
            raise StopIteration

names = ["Carlos", "Andre", "Beatriz", "Marley", "William"]

for name in names:
    print(name, end=" ")
"""

"""
class Produto:
    def __init__(self, name, preco, categoria):
        self.name = name
        self.preco = preco
        self.categoria = categoria

# Criando uma lista de produtos
produtos = [
    Produto("Camisa", 50, "Vestuário"),
    Produto("Calça", 100, "Vestuário"),
    Produto("Notebook", 3000, "Eletrônicos"),
    Produto("Celular", 1500, "Eletrônicos")
]

# Usando `filter` para selecionar apenas produtos eletrônicos
eletronicos = list(filter(lambda p: p.categoria == "Eletrônicos", produtos))
print("Produtos eletrônicos:", [p.name for p in eletronicos])

# Usando `map` para aplicar um desconto de 10% em todos os produtos
produtos_com_desconto = list(map(lambda p: Produto(p.name, p.preco * 0.9, p.categoria), produtos))
print("Produtos com desconto:", [(p.name, p.preco) for p in produtos_com_desconto])
"""

"""
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Executando {func.__name__} com argumentos {args[1:]}")
        resultado = func(*args, **kwargs)
        print(f"Resultado de {func.__name__}: {resultado}")
        return resultado
    return wrapper

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    @log_decorator
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    @log_decorator
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
            return self.saldo
        self.saldo -= valor
        return self.saldo

# Exemplo de uso
conta = ContaBancaria("Alice", 1000)
conta.depositar(200)
conta.sacar(150)
"""

"""
class Transacao:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

class HistoricoDeTransacoes:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def gerar_extrato(self):
        for transacao in self.transacoes:
            yield f"{transacao.tipo}: {transacao.valor}"

# Exemplo de uso
historico = HistoricoDeTransacoes()
historico.adicionar_transacao(Transacao("Depósito", 200))
historico.adicionar_transacao(Transacao("Saque", 100))

for transacao in historico.gerar_extrato():
    print(transacao)
"""

import json, csv, pickle

class Student:
    def __init__(self, name: str, age: int, notes: list) -> None:
        self.name = name
        self.age = age
        self.notes = notes

    def calculate_mean(self):
        return sum(self.notes) / len(self.notes)


class ManagerStudents:
    def __init__(self) -> None:
        self.students = []

    def add_students(self, student) -> None:
        self.students.append(student)

    def save_json(self, file_name="students.json") -> None:
        data = [
            {
                "name": student.name, 
                "age": student.age, 
                "notes": student.notes
            } for student in self.students
        ]

        with open(file_name, "w") as file_json:
            json.dump(data, file_json)
        
        print(f"Data saved in {file_name}")

    def load_json(self, file_name="students.json") -> None:
        with open(file_name, "r") as file_json:
            data = json.load(file_json)
            self.students = [Student(**student) for student in data]

        print(f"Data loaded from {file_name}")

    def save_csv(self, file_name="students.csv") -> None:
        with open(file_name, "w", newline="") as file_csv:
            writer = csv.writer(file_csv)
            writer.writerow(["Name", "Age", "Notes"])

            for student in self.students:
                writer.writerow([student.name, student.age, student.notes])

            print(f"Data saved in {file_name}")

    def load_csv(self, file_name="students.csv") -> None:
        with open(file_name, "r") as file_csv:
            reader = csv.reader(file_csv)
            next(reader)  # Pular cabeçalho

            self.students = [Student(line[0], int(line[1]), eval(line[2])) for line in reader]

        print(f"Data loaded from {file_name}")

    def save_pickle(self, file_name="students.pkl") -> None:
        with open(file_name, "wb") as file:
            pickle.dump(self.students, file)

        print(f"Data saved in {file_name}")

    def load_pickle(self, file_name="students.pkl") -> None:
        with open(file_name, "rb") as file:
            self.students = pickle.load(file)

        print(f"Data loaded from {file_name}")

    def list_students(self) -> None:
        for student in self.students:
            print(f"Name: {student.name}, Age: {student.age}, Mean: {student.calculate_mean():.2f}")

# Criando instância do manager e adicionando alunos
manager = ManagerStudents()
manager.add_students(Student("Alice", 20, [8, 7.5, 9]))
manager.add_students(Student("Bob", 22, [6, 5, 7]))

# Salvando e carregando Data em JSON
manager.save_json()
manager.load_json()
manager.list_students()

# Salvando e carregando Data em CSV
manager.save_csv()
manager.load_csv()
manager.list_students()

# Salvando e carregando Data com pickle
manager.save_pickle()
manager.load_pickle()
manager.list_students()
