import tkinter as tk


def Soma():
    n1 = float(input1.get())
    n2 = float(input2.get())
    soma = n1+n2
    result.config(text = f'{soma}')

def Sub():
    n1 = float(input1.get())
    n2 = float(input2.get())
    Sub = n1-n2
    result.config(text = f'{Sub}')

def Mult():
    n1 = float(input1.get())
    n2 = float(input2.get())
    Mult = n1*n2
    result.config(text = f'{Mult}')

def Div():
    n1 = float(input1.get())
    n2 = float(input2.get())
    Div = n1/n2
    result.config(text = f'{Div}')


janela = tk.Tk()

janela.geometry('150x300')

janela.title("Calculadora")

texto = tk.Label(janela,text="Calculadora")
texto.grid(row = 1, column = 2, padx= 10)

input1 = tk.Entry(janela)
input1.grid(row = 2, column = 2, padx= 10)
input2 = tk.Entry(janela)
input2.grid(row = 3, column = 2, padx= 10)

result = tk.Label(janela, text="Resultado = ")
result.grid(row = 4, column = 2, padx= 10)

btn = tk.Button(janela, text='SOMA',command=Soma)
btn.grid(row=5,column=2, padx= 10)

btn1 = tk.Button(janela, text='SUBTRAÇÃO',command=Sub)
btn1.grid(row=6,column=2, padx= 10)

btn2 = tk.Button(janela, text='MULTIPLICAÇÃO',command=Mult)
btn2.grid(row=7,column=2, padx= 10)

btn2 = tk.Button(janela, text='DIVISÃO',command=Div)
btn2.grid(row=8,column=2, padx= 10)




janela.mainloop()