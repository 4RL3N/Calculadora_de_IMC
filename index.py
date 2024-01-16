import tkinter as tk
from tkinter import *

def infos(i):
    ...

def resultado(x):
    popup = Toplevel()
    popup.geometry("200x150")
    popup.title("Resultado")
    Label(popup, text=f"Seu IMC é {x:.2f}", font="Helvetica 15 bold").pack()
    Button(popup, text="Fechar", command=popup.destroy).pack(pady=5)

def calcular_imc():
    p2 = int(peso.get())
    altura = float(campo_altura.get())
    imc = p2 / (altura**2)
    resultado(imc)

janela = tk.Tk()
janela.geometry("400x250")
janela.title("Calculadora de IMC")
tk.Label(janela, text="Vamos descobrir seu IMC", font="Helvetica 20 bold").pack(pady=10)
tk.Label(janela, text="Selecione seu peso (em kg):", font="Helvetica 15").pack(pady=5)

peso = tk.StringVar(janela)
options_peso = [int(i) for i in range(40, 200)] #
options_peso.insert(0, "Selecione")
peso.set(options_peso[0])
tk.OptionMenu(janela, peso, *options_peso).pack()

tk.Label(janela, text="insira sua altura em M:", font="Helvetica 15").pack(pady=5)

campo_altura = Entry(janela, width=5)
campo_altura.pack()

options_peso.remove("Selecione")
botao = Button(janela, text="Confirmar", command=calcular_imc).pack(pady=5)





















janela.mainloop()