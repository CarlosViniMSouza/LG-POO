class People:
    def __init__(self, name, age, weigth, heigth):
        self.name = name
        self.age = age
        self.weigth = weigth
        self.heigth = heigth

    # Getting old, getting fat, getting thin, growing up.
    # 

    def getting_old(self):
        final_heigth = self.heigth

        for value in range(1, self.age):
            if self.age < 21:
                final_heigth += 0.05 # 0,5cm -> 0,05 m
                self.age += 1
            else:
                break

        return final_heigth

people = People("Carlos", 20, 65.6, 1.78)
print(f"Sua altura final: {people.getting_old()} cm")
