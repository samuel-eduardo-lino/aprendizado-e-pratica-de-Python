


def check_triagulo(a, b, c):
    res = ''
    if a + b > c and b + c > a and a + c > b:
        res = 'sim'
    else:
        res = 'não'
    return res


def digite_valores():
    a = int(input('digite o primeiro valor '))
    b = int(input('digite o segundo valor '))
    c = int(input('digite o terceiro valor '))
    print(check_triagulo(a, b, c))

digite_valores()