def sum(a,b):
    return a+b


def substraction(a,b):
    return a-b


def multiplication(a,b):
    return a*b


def divide(a,b):
    if b == 0:
        raise ZeroDivisionError
    return a/b


def ifSign(symb):
    if symb == '+' or symb == '-' or symb == '*' or symb == '/':
        return True
    return False

def calc(symbol, a, b):
    var = 0
    if symbol == '+':
        var = sum(a, b)
    elif symbol == '-':
        var = substraction(a, b)
    elif symbol == '*':
        var = multiplication(a, b)
    elif symbol == '/':
        var = divide(a, b)
    return var

def calculate():
    a = int(input("Input first variable -> "))
    b = int(input("Input second variable -> "))
    symbol = input("Choose operation from list [+,-,*,/] -> ")
    var = 0
    calc(symbol, a, b)
    print(f"Result is {var}")


def calculate_ver2():
    string = input("enter a*math_sign*b -> ")
    symbol_list = ['+', '-', '*', '/']
    symbol = ''
    for i in string:
        if i in symbol_list:
            symbol = i
            break
    pos = string.find(symbol)
    a = int(string[:pos])
    b = int(string[pos+1:])
    print(calc(symbol,a,b))

#calculate()
calculate_ver2()

