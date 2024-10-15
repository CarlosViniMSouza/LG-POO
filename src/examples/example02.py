"""
Pages: 19
Image: 02
"""

class People:
    number_people = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        People.number_people += 1

    @classmethod
    def total_people(cls):
        print(f"Total people: {cls.number_people}")

people01 = People("Carlos", 22)
people02 = People("Vinicius", 23)
people03 = People("Souza", 24)

People.total_people()
