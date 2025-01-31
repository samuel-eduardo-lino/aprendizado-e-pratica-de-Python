from tkinter import *
from math import sqrt
from tkinter import messagebox


number = ''
prime = 0
secun = 0
sinaldigitado = False
calculou = False
colocouponto = False
numero = 0


def digitar(num:str):
    global number
    if number != '':
        number = number + num
        operacao.delete(0, END)
        operacao.insert(0, number)
        
    else:
        number= num
        operacao.delete(0, END)
        operacao.insert(0, number)
      
    
def numero1():
    global numero
    numero = 1
    digitar('1')
    

def numero2():
    global numero
    numero = 1
    digitar('2')


def numero3():
    global numero
    numero = 1
    digitar('3')


def numero4():
    global numero
    numero = 1
    digitar('4')


def numero5():
    global numero
    numero = 1
    digitar('5')


def numero6():
    global numero
    numero = 1
    digitar('6')


def numero7():
    global numero
    numero = 1
    digitar('7')


def numero8():
    global numero
    numero = 1
    digitar('8')


def numero9():
    global numero
    numero = 1
    digitar('9')


def numero0():
    global numero
    numero = 1
    digitar('0')


def mais():
    global sinaldigitado
    global colocouponto
    global numero
    if sinaldigitado:
        return
    else:
        if numero == 1:
            digitar('+')
            sinaldigitado = True
            colocouponto = False
            numero = 0


def menos():
    global sinaldigitado
    global colocouponto
    global numero
    global number
    if sinaldigitado:
        if number[1:].find('-') == -1:
            digitar('-')
        else:
            return
    else:
        digitar('-')
        if numero == 0:
            return
        else:
            sinaldigitado = True
            colocouponto = False
            numero = 0


def divi():
    global sinaldigitado
    global colocouponto
    global numero
    if sinaldigitado:
        return
    else:
        if numero == 1:
            digitar('/')
            sinaldigitado = True
            colocouponto = False
            numero = 0


def multi():
    global sinaldigitado
    global colocouponto
    global numero
    if sinaldigitado:
        return
    else:
        if numero == 1:
            digitar('*')
            sinaldigitado = True
            colocouponto = False
            numero = 0


def ponto():
    global colocouponto
    global numero
    if numero == 1:
        if colocouponto == False:
            digitar('.')
            colocouponto = True


def porcent():
    global sinaldigitado
    global colocouponto
    global numero
    if sinaldigitado:
        return
    else:
        digitar('%*')
        sinaldigitado = True
        colocouponto = False
        numero = 0
        

def calcular(texto:str):
    global prime
    global secun
    global number
    global calculou
    if texto.find('+') != -1:
        separado = texto.split('+')
        if separado[0].isnumeric() and separado[1].isnumeric():
            prime = float(separado[0])
            secun = float(separado[1])
            resultado = prime + secun
            operacao.delete(0, END)
            operacao.insert(0, f'{number} = {resultado}')
            calculou = True
        else:
            messagebox.showerror('ERRO', 'a operção é invalida')
    elif texto.find('/') != -1:
        separado = texto.split('/')
        if separado[0].isnumeric() and separado[1].isnumeric():
            prime = float(separado[0])
            secun = float(separado[1])
            resultado = prime / secun
            operacao.delete(0, END)
            operacao.insert(0, f'{number} = {resultado}')
            calculou = True
        else:
            messagebox.showerror('ERRO', 'a operção é invalida')
    elif texto.find('%') != -1:
        separado = texto.split('%')
        if separado[0].isnumeric() and separado[1].isnumeric():
            prime = float(separado[0])
            secun = float(separado[1][1:])
            resultado = (prime * secun) / 100
            operacao.delete(0, END)
            operacao.insert(0, f'{number} = {resultado}')
            calculou = True
        else:
            messagebox.showerror('ERRO', 'a operção é invalida')
    elif texto.find('*') != -1:
        separado = texto.split('*')
        if separado[0].isnumeric() and separado[1].isnumeric():
            prime = float(separado[0])
            secun = float(separado[1])
            resultado = prime * secun
            operacao.delete(0, END)
            operacao.insert(0, f'{number} = {resultado}')
            calculou = True
        else:
            messagebox.showerror('ERRO', 'a operção é invalida')
    elif texto.find('-') != -1:
        separado = texto.split('-')
        if separado[0].isnumeric() and separado[1].isnumeric():
            if texto[0] == '-':
                prime = float(separado[1])
                secun = float(separado[2])
                resultado = -prime - secun
            else:
                prime = float(separado[0])
                secun = float(separado[1])
                resultado = prime - secun
            operacao.delete(0, END)
            operacao.insert(0, f'{number} = {resultado}')
            calculou = True
        else:
            messagebox.showerror('ERRO', 'a operção é invalida')
    else:
        messagebox.showerror('ERRO', 'a operção é invalida')


def igualar():
    global calculou
    global number
    global numero
    global sinaldigitado
    global colocouponto
    number = operacao.get()
    calcular(number)
    if calculou == True:
        number = ''
        numero = 0
        calculou = False
        sinaldigitado = False
        colocouponto = False


def apagar_anterior():
    global number
    tamanho = len(number)
    posi = tamanho - 1
    novo_number = number[0:posi]
    number = novo_number
    operacao.delete(0, END)
    operacao.insert(0, number)


def raiz():
    global number
    if number.isnumeric():
        resultado = sqrt(int(number))
        operacao.delete(0, END)
        operacao.insert(0, f'\u221A{number} = {resultado}')
        number = ''


def fatorial():
    global number
    if number.isnumeric():
        valor = int(number)
        resultado = int(number)
        for n in range(1, valor):
            resultado = resultado * (valor - 1)
            valor -= 1
        operacao.delete(0, END)
        operacao.insert(0, f'{number}! = {resultado}')
        number = ''


janela = Tk()
janela.title('Calculadora')
janela.resizable(False, False)


operacao = Entry(janela, text='', width=40)
operacao.grid(row=0, column=0, columnspan=5)
scroll = Scrollbar(janela, orient='horizontal', width=10)
scroll.grid(row=1, column=0, columnspan=5)
operacao.config(xscrollcommand=scroll.set)
scroll.config(command=operacao.xview)

num1 = Button(janela, text='1', height=2, width=5, command=numero1)
num1.grid(row=2, column=0)

num2 = Button(janela, text='2', height=2, width=5, command=numero2)
num2.grid(row=2, column=1)

num3 = Button(janela, text='3', height=2, width=5, command=numero3)
num3.grid(row=2, column=2)

num4 = Button(janela, text='4', height=2, width=5, command=numero4)
num4.grid(row=3, column=0)

num5 = Button(janela, text='5', height=2, width=5, command=numero5)
num5.grid(row=3, column=1)

num6 = Button(janela, text='6', height=2, width=5, command=numero6)
num6.grid(row=3, column=2)

num7 = Button(janela, text='7', height=2, width=5, command=numero7)
num7.grid(row=4, column=0)

num8 = Button(janela, text='8', height=2, width=5, command=numero8)
num8.grid(row=4, column=1)

num9 = Button(janela, text='9', height=2, width=5, command=numero9)
num9.grid(row=4, column=2)

num0 = Button(janela, text='0', height=2, width=5, command=numero0)
num0.grid(row=5, column=1)

sinmais = Button(janela, text='+', height=2, width=5, command=mais)
sinmais.grid(row=5, column=3)

sinmenos = Button(janela, text='-', height=2, width=5, command=menos)
sinmenos.grid(row=4, column=3)

sindivi = Button(janela, text='/', height=2, width=5, command=divi)
sindivi.grid(row=3, column=3)

sinmulti = Button(janela, text='*', height=2, width=5, command=multi)
sinmulti.grid(row=2, column=3)

pont = Button(janela, text='.', height=2, width=5, command=ponto)
pont.grid(row=5, column=0)

igual = Button(janela, text='=', height=2, width=5, command=igualar)
igual.grid(row=5, column=2)

apagar = Button(janela, text='<-', height=2, width=5, command=apagar_anterior)
apagar.grid(row=2, column=4)

raizq = Button(janela, text='\u221A', height=2, width=5, command=raiz)
raizq.grid(row=3, column=4)

fatori = Button(janela, text='!', height=2, width=5, command=fatorial)
fatori.grid(row=4, column=4)

percent = Button(janela, text='%', height=2, width=5, command=porcent)
percent.grid(row=5, column=4)

janela.mainloop()