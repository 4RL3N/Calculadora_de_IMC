import tkinter as tk
from tkinter import *

def infos(x):
    if x < 18.5:
        texto = "O valor do seu IMC é considerado baixo"
        texto2 = "sendo assim, você está abaixo do peso ideal. Atenção!"
    elif 18.5 <= x < 24.9:
        texto = "O valor do seu IMC está normal"
        texto2 = "ou seja, você não está nem acima do peso, nem abaixo."
    elif 25 <= x <29.9:
        texto = "O valor do seu IMC é considerado acima do ideal"
        texto2 = "sendo assim você se enquadra em SOBREPESO. Atenção!"
    elif 30 <= x < 39.9:
        texto = "O valor do seu IMC é considerado acima do ideal"
        texto2 = "sendo assim você se enquadra em OBESIDADE 1. Atenção!"
    else:
        texto = "O valor do seu IMC é considerado acima do ideal"
        texto2 = "sendo assim você se enquadra em OBESIDADE 2. Atenção!"
    return texto, texto2

def janela_popup(x):
    popup = Toplevel()
    popup.geometry("450x125")
    popup.title("Resultado")
    Label(popup, text=f"Seu IMC é de '{x:.2f}'", font="Helvetica 15 bold").pack()
    texto, texto2 = infos(x)
    #Exibindo o resultado
    Label(popup, text=texto, font="Helvetica 12 bold").pack()
    Label(popup, text=texto2, font="Helvetica 11").pack()
    #Fechando o popup
    Button(popup, text="Fechar", command=popup.destroy).pack(pady=5)

def limpar():
    peso.set(options_peso[0])
    campo_altura.delete(0, "end")

def calcular_imc():
    p2 = int(peso.get())
    altura = float(campo_altura.get())
    imc = p2 / (altura**2)
    janela_popup(imc)

janela = tk.Tk()
janela.geometry("400x240")
janela.title("Calculadora de IMC")
tk.Label(janela, text="Vamos descobrir seu IMC", font="Helvetica 20 bold").pack(pady=10)
tk.Label(janela, text="Selecione seu peso (em kg):", font="Helvetica 15").pack(pady=5)

peso = tk.StringVar(janela)
options_peso = [int(i) for i in range(40, 200)]
options_peso.insert(0, "Selecione")
peso.set(options_peso[0])
tk.OptionMenu(janela, peso, *options_peso).pack()

tk.Label(janela, text="insira sua altura em M:", font="Helvetica 15").pack(pady=5)

campo_altura = Entry(janela, width=5)
campo_altura.pack()

frame = tk.Frame(janela)
frame.pack(pady=10)

botao_confirma = Button(frame, text="Confirmar", command=calcular_imc)
botao_confirma.grid(row=0, column=1)
botao_apagar = Button(frame, text="Limpar", command=limpar)
botao_apagar.grid(row=0, column=0)

janela.mainloop()