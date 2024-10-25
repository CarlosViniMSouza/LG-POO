import tkinter as tk
from tkinter import messagebox

class Funcionario:
    def __init__(self, nome, tipo, pagamento):
        self.nome = nome
        self.tipo = tipo
        self.pagamento = pagamento

    def calcular_salario(self):
        pass

class Horista(Funcionario):
    def __init__(self, nome, horas_trabalhadas, valor_hora):
        super().__init__(nome, "Horista", horas_trabalhadas * valor_hora)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        return self.horas_trabalhadas * self.valor_hora

class Mensalista(Funcionario):
    def __init__(self, nome, salario_mensal):
        super().__init__(nome, "Mensalista", salario_mensal)

    def calcular_salario(self):
        return self.pagamento

class Comissionado(Funcionario):
    def __init__(self, nome, vendas, comissao):
        super().__init__(nome, "Comissionado", vendas * comissao)
        self.vendas = vendas
        self.comissao = comissao

    def calcular_salario(self):
        return self.vendas * self.comissao

funcionarios = []

def adicionar_horista():
    nome = entry_nome_horista.get()
    horas_trabalhadas = float(entry_horas.get())
    valor_hora = float(entry_valor_horista.get())
    func = Horista(nome, horas_trabalhadas, valor_hora)
    funcionarios.append(func)
    messagebox.showinfo("Sucesso", f"Funcionário {nome} adicionado!")

def adicionar_mensalista():
    nome = entry_nome_mensalista.get()
    salario_mensal = float(entry_valor_mensalista.get())
    func = Mensalista(nome, salario_mensal)
    funcionarios.append(func)
    messagebox.showinfo("Sucesso", f"Funcionário {nome} adicionado!")

def adicionar_comissionado():
    nome = entry_nome_comissionado.get()
    vendas = float(entry_vendas.get())
    comissao = float(entry_comissao.get())
    func = Comissionado(nome, vendas, comissao)
    funcionarios.append(func)
    messagebox.showinfo("Sucesso", f"Funcionário {nome} adicionado!")

def mostrar_salarios():
    salarios = ""
    for func in funcionarios:
        salarios += f"{func.nome} ({func.tipo}): R${func.calcular_salario()}\n"
    messagebox.showinfo("Salários dos Funcionários", salarios)

app = tk.Tk()
app.title("Cadastro de Funcionários")

# Seção para Horista
tk.Label(app, text="Nome Horista").grid(row=0, column=0)
tk.Label(app, text="Horas Trabalhadas").grid(row=1, column=0)
tk.Label(app, text="Valor Hora").grid(row=2, column=0)

entry_nome_horista = tk.Entry(app)
entry_horas = tk.Entry(app)
entry_valor_horista = tk.Entry(app)

entry_nome_horista.grid(row=0, column=1)
entry_horas.grid(row=1, column=1)
entry_valor_horista.grid(row=2, column=1)

tk.Button(app, text="Adicionar Horista", command=adicionar_horista).grid(row=3, column=1)

# Seção para Mensalista
tk.Label(app, text="Nome Mensalista").grid(row=4, column=0)
tk.Label(app, text="Salário Mensal").grid(row=5, column=0)

entry_nome_mensalista = tk.Entry(app)
entry_valor_mensalista = tk.Entry(app)

entry_nome_mensalista.grid(row=4, column=1)
entry_valor_mensalista.grid(row=5, column=1)

tk.Button(app, text="Adicionar Mensalista", command=adicionar_mensalista).grid(row=6, column=1)

# Seção para Comissionado
tk.Label(app, text="Nome Comissionado").grid(row=7, column=0)
tk.Label(app, text="Vendas").grid(row=8, column=0)
tk.Label(app, text="Comissão").grid(row=9, column=0)

entry_nome_comissionado = tk.Entry(app)
entry_vendas = tk.Entry(app)
entry_comissao = tk.Entry(app)

entry_nome_comissionado.grid(row=7, column=1)
entry_vendas.grid(row=8, column=1)
entry_comissao.grid(row=9, column=1)

tk.Button(app, text="Adicionar Comissionado", command=adicionar_comissionado).grid(row=10, column=1)

# Botão para mostrar os salários
tk.Button(app, text="Mostrar Salários", command=mostrar_salarios).grid(row=11, column=1)

app.mainloop()
