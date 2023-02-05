

def check_fermat(a, b, c, n):
    if n > 2:
        if a ** n + b ** n == c ** n:
            print('Holy smokes, Fermat was wrong')
        else:
            print('No, that does not work')
    else:
        print('n é menor que 2')

def digite_valores():
    a = int(input('digite o valor de a: '))
    b = int(input('digite o valor de b: '))
    c = int(input('digite o valor de c: '))
    n = int(input('digite o valor de n, que seja maior que 2:'))
    valores = [a, b, c, n]
    return valores

valores = digite_valores()
check_fermat(valores[0], valores[1], valores[2], valores[3])


