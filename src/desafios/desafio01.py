class User:
    def __init__(self, weigth, heigth):
        self.weigth = weigth
        self.heigth = heigth

    def calc_imc(self):
        result = self.weigth / (heigth * heigth)

        return float(round(result, 2))

    def show_result_table(self, resultIMC):

        if resultIMC < 17:
            print("Muito abaixo do peso")
        elif 17 <= resultIMC <= 18.49:
            print("Abaixo do peso")
        elif 18.5 <= resultIMC <= 24.99:
            print("Peso normal")
        elif 25 <= resultIMC <= 29.99:
            print("Acima do peso")
        elif 30 <= resultIMC <= 34.99:
            print("Obsidade 1")
        elif 35 <= resultIMC <= 39.99:
            print("Obsidade 2 (Severa)")
        elif 40 <= resultIMC:
            print("Obsidade 3 (Mórbida)")

heigth = float(input("Insira sua altura: "))
weigth = float(input("Insira seu peso: "))

user = User(weigth, heigth)
user_imc = user.calc_imc()

print(f"Seu IMC eh: {user_imc}")
user.show_result_table(user_imc)