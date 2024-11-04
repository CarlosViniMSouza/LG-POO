## Exercicio 02

class User:
    def __init__(self, name: str, age: int, email: str) -> None:
        if not name: 
            raise ValueError("Name cannot be empty.") 
        if not isinstance(age, int): # type(age) != int (?)
            raise TypeError("Age must be an integer.") 
        if "@" not in email: 
            raise ValueError("Email must contain an '@'")

        self.name = name
        self.age = age
        self.email = email

def create_users():
    # Exemplos de uso: 
    try: 
        user = User("", 25, "user@example.com") 
    except ValueError as ve: 
        print(f"Error: {ve}") 
        
    try:
        user = User("Ana", "25", "user@example.com") 
    except TypeError as te: 
        print(f"Error: {te}") 
        
    try: 
        user = User("Carlos", 30, "userexample.com") 
    except ValueError as ve: 
        print(f"Error: {ve}") 
    
    # Isso deve funcionar sem erros: 
    user = User("Luiza", 28, "luiza@example.com") 
    print(f"User created: {user.name}, {user.age}, {user.email}")