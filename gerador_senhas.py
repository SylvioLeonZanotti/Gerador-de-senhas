import tkinter as tk
import random
import string
import pyperclip

senha_gerada = ""

def gerar_senhas():
    global senha_gerada
    length_str = length_entry.get()
    if length_str.isdigit() and int(length_str) > 0:
        length = int(length_str)
        exclude_characters = exclude_entry.get()
        characters = ''.join(c for c in string.ascii_letters + string.digits + string.punctuation if c not in exclude_characters)
        password = ''.join(random.choice(characters) for i in range(length))
        result_label.config(text="Senha aleatória: " + password)
        senha_gerada = password
    else:
        result_label.config(text="Por favor, insira um valor mínimo para a senha.")

def copiar_senha():
    pyperclip.copy(senha_gerada)
    result_label.config(text="Senha copiada com sucesso!")

root = tk.Tk()
root.title("Gerador de senha aleatória")

length_label = tk.Label(root, text="Comprimento da senha:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

exclude_label = tk.Label(root, text="Caracteres a serem excluídos:")
exclude_label.grid(row=1, column=0, padx=10, pady=10)

exclude_entry = tk.Entry(root)
exclude_entry.grid(row=1, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Gerar Senha", command=gerar_senhas)
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

copy_button = tk.Button(root, text="Copiar Senha", command=copiar_senha)
copy_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

label = tk.Label(root, text="Este é um exemplo tkinter, random e pyperclip.")
label.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()