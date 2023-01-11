from tkinter import *

number = '0'
prime = 0
sinal = ''
secun = 0

def digitar(num:str):
    global number
    if number != '0':
        number = number + num
        operacao.config(text= f'{number}')
        
    else:
        number= num
        operacao.config(text=f'{number}')
    
def numero1():
    digitar('1')

def numero2():
    digitar('2')

def numero3():
    digitar('3')

def numero4():
    digitar('4')

def numero5():
    digitar('5')

def numero6():
    digitar('6')

def numero7():
    digitar('7')

def numero8():
    digitar('8')

def numero9():
    digitar('9')

def numero0():
    digitar('0')

def mais():
    digitar('+')

def menos():
    digitar('-')

def divi():
    digitar('/')

def multi():
    digitar('*')

def ponto():
    digitar('.')

def calcular(texto:str):
    global prime
    global secun
    global sinal
    global number
    if texto.find('+') != -1:
        separado = texto.split('+')
        prime = float(separado[0])
        sinal = '+'
        secun = float(separado[1])
        resultado = prime + secun
        operacao.config(text=f'{number} = {resultado}')
    elif texto.find('-') != -1:
        separado = texto.split('-')
        prime = float(separado[0])
        sinal = '-'
        secun = float(separado[1])
        resultado = prime - secun
        operacao.config(text=f'{number} = {resultado}')
    elif texto.find('/') != -1:
        separado = texto.split('/')
        prime = float(separado[0])
        sinal = '/'
        secun = float(separado[1])
        resultado = prime / secun
        operacao.config(text=f'{number} = {resultado}')
    elif texto.find('*') != -1:
        separado = texto.split('*')
        prime = float(separado[0])
        sinal = '*'
        secun = float(separado[1])
        resultado = prime * secun
        operacao.config(text=f'{number} = {resultado}')

def igualar():
    calcular(number)


janela = Tk()
janela.title('Calculadora')


operacao = Label(janela, width=30, height=2)
operacao.grid(row=0, column=0, columnspan=4)
num1 = Button(janela, text='1', height=2, width=5, command=numero1)
num1.grid(row=1, column=0)
num2 = Button(janela, text='2', height=2, width=5, command=numero2)
num2.grid(row=1, column=1)
num3 = Button(janela, text='3', height=2, width=5, command=numero3)
num3.grid(row=1, column=2)
num4 = Button(janela, text='4', height=2, width=5, command=numero4)
num4.grid(row=2, column=0)
num5 = Button(janela, text='5', height=2, width=5, command=numero5)
num5.grid(row=2, column=1)
num6 = Button(janela, text='6', height=2, width=5, command=numero6)
num6.grid(row=2, column=2)
num7 = Button(janela, text='7', height=2, width=5, command=numero7)
num7.grid(row=3, column=0)
num8 = Button(janela, text='8', height=2, width=5, command=numero8)
num8.grid(row=3, column=1)
num9 = Button(janela, text='9', height=2, width=5, command=numero9)
num9.grid(row=3, column=2)
num0 = Button(janela, text='0', height=2, width=5, command=numero0)
num0.grid(row=4, column=1)
sinmais = Button(janela, text='+', height=2, width=5, command=mais)
sinmais.grid(row=4, column=3)
sinmenos = Button(janela, text='-', height=2, width=5, command=menos)
sinmenos.grid(row=3, column=3)
sindivi = Button(janela, text='/', height=2, width=5, command=divi)
sindivi.grid(row=2, column=3)
sinmulti = Button(janela, text='*', height=2, width=5, command=multi)
sinmulti.grid(row=1, column=3)
pont = Button(janela, text='.', height=2, width=5, command=ponto)
pont.grid(row=4, column=0)
igual = Button(janela, text='=', height=2, width=5, command=igualar)
igual.grid(row=4, column=2)



janela.mainloop()