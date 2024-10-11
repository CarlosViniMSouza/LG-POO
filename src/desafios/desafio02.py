class People:
    def __init__(self, name, age, heigth, weigth):
        self.name = name
        self.age = age
        self.heigth = heigth
        self.weigth = weigth

    # Getting old, getting fat, getting thin, growing up.
    # 

    def calculate_height(self):
        final_heigth = self.heigth

        for value in range(1, self.age):
            if self.age < 21:
                final_heigth += 0.05 # 0,5cm -> 0,05 m
                self.age += 1
            else:
                break

        return final_heigth

user_name = input("Seu nome: ")
user_age = int(input("Sua idade: "))
user_height = float(input("Sua altura: "))
user_weight = float(input("Seu peso: "))
people = People(user_name, user_age, user_height, user_weight)

print(f"\n{people.name}, sua altura final eh {people.calculate_height()}cm")
