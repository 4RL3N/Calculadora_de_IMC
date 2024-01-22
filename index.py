import tkinter as tk
from tkinter import * #o "*" importa tudo da biblioteca tkinter

#Funcao que define o texto a ser exibido
def infos(x):
    if x < 18.5:
        texto = "O valor do seu IMC é considerado baixo, sendo assim, você está abaixo do peso ideal. Atenção!"
    elif 18.5 <= x < 24.9:
        texto = "O valor do seu IMC está normal, ou seja, você não está nem acima do peso, nem abaixo."
    elif 25 <= x <29.9:
        texto = "O valor do seu IMC é considerado acima do ideal, sendo assim você se enquadra em SOBREPESO. Atenção!"
    elif 30 <= x < 39.9:
        texto = "O valor do seu IMC é considerado acima do ideal, sendo assim você se enquadra em OBESIDADE 1. Atenção!"
    else:
        texto = "O valor do seu IMC é considerado acima do ideal, sendo assim você se enquadra em OBESIDADE 2. Atenção!"
    return texto

#Funcao responsavel pela janela popup
def janela_popup(x):
    popup = Toplevel()
    popup.geometry("450x100")
    popup.title("Resultado")
    Label(popup, text=f"Seu IMC é de '{x:.2f}'", font="Helvetica 15 bold").pack()
    texto = infos(x)
    #Exibindo o resultado
    Label(popup, text=texto, font="Helvetica 11").pack()
    #Fechando o popup
    Button(popup, text="Fechar", command=popup.destroy).pack(pady=5)

#Funcao que limpa os campos de peso e altura do formulário
def limpar():
    peso.set(options_peso[0])
    campo_altura.delete(0, "end")

#Funcao que realmente calcula o imc do usuario, com os dados fornecidos
def calcular_imc():
    p2 = int(peso.get())
    altura = float(campo_altura.get())
    imc = p2 / (altura**2)
    janela_popup(imc)

#Definindo a janela principal da aplicacao
janela = Tk()
janela.geometry("400x240")
janela.title("Calculadora de IMC")
tk.Label(janela, text="Vamos descobrir seu IMC", font="Helvetica 20 bold").pack(pady=10)
tk.Label(janela, text="Selecione seu peso (em kg):", font="Helvetica 15").pack(pady=5)

#Definindo o menu de opcoes para selecionar o peso do usuario em kg
peso = tk.StringVar(janela)
#Definindo as opcoes a serem selecionadas (a partir de 40kg até 200kg)
options_peso = [int(i) for i in range(40, 200)]
options_peso.insert(0, "Selecione")
peso.set(options_peso[0])
#descompactando as opcoes para serem selecionadas
tk.OptionMenu(janela, peso, *options_peso).pack()

tk.Label(janela, text="insira sua altura em M:", font="Helvetica 15").pack(pady=5)

#Criando um campo para entrada, para o usuário digitar sua altura em metros
campo_altura = Entry(janela, width=5)
campo_altura.pack()

#Criando um frame para colocar os botoes de "confirma" e "apagar" dentro
frame = tk.Frame(janela)
frame.pack(pady=10) #pady é o espaco, no caso 10 pixeis de espaço entre o frame e as bordas da janela

botao_confirma = Button(frame, text="Confirmar", command=calcular_imc)
botao_confirma.grid(row=0, column=1)
botao_apagar = Button(frame, text="Limpar", command=limpar)
botao_apagar.grid(row=0, column=0)

janela.mainloop()