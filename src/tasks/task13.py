import tkinter as tk
from tkinter import messagebox

class EmployeePaymentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Funcionários e Pagamentos")
        
        # Labels e Entradas para o cadastro de funcionários
        self.name_label = tk.Label(root, text="Nome do Funcionário:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)
        
        self.salary_label = tk.Label(root, text="Salário:")
        self.salary_label.grid(row=1, column=0)
        self.salary_entry = tk.Entry(root)
        self.salary_entry.grid(row=1, column=1)
        
        # Botão para adicionar funcionário
        self.add_button = tk.Button(root, text="Adicionar Funcionário", command=self.add_employee)
        self.add_button.grid(row=2, columnspan=2)
        
        # Lista de funcionários
        self.employee_listbox = tk.Listbox(root)
        self.employee_listbox.grid(row=3, columnspan=2)
        
        # Botão para processar pagamentos
        self.process_button = tk.Button(root, text="Processar Pagamentos", command=self.process_payments)
        self.process_button.grid(row=4, columnspan=2)

    def add_employee(self):
        name = self.name_entry.get()
        salary = self.salary_entry.get()
        if name and salary:
            self.employee_listbox.insert(tk.END, f"{name} - R${salary}")
            self.name_entry.delete(0, tk.END)
            self.salary_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")

    def process_payments(self):
        employees = self.employee_listbox.get(0, tk.END)
        if employees:
            messagebox.showinfo("Pagamento Processado", "Pagamentos processados com sucesso!")
        else:
            messagebox.showwarning("Atenção", "Nenhum funcionário cadastrado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeePaymentApp(root)
    root.mainloop()
