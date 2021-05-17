# import

def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def mult(a, b):
    return a * b


def division(a, b):
    return a / b


def power(a, b):
    return a ** b


def calculate(a, znak, b):
    if type(a) == int and type(b) == int:
        if znak == '+':
            return plus(a=a, b=b)
        elif znak == '-':
            return minus(a=a, b=b)
        elif znak == '*':
            return mult(a=a, b=b)
        elif znak == '/':
            return division(a=a, b=b)
        elif znak == '^':
            return power(a=a, b=b)
        else:
            return 'Your expression is incorrect'
    else:
        return 'Yor expression is incorrect'


if __name__ == '__main__':
    print('Enter your expression with space')
    expr = input()
    i, j = 0, 0

    while expr[j] != ' ':
        j += 1
    num1 = int(expr[i:j])
    i = j + 1
    j = j + 2

    while expr[j] != ' ':
        j += 1
    znack = expr[i:j]
    i = j + 1
    j = j + 2

    num2 = int(expr[i:len(expr)])

    print(calculate(a=num1, znak=znack, b=num2))
