import math


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def split(a, b):
    return a / b


def full_split(a, b):
    return a // b


def pow(a, b):
    return a ** b


def log_1(a, b):
    return math.log(a, b)


def ex(a):
    return math.exp(a)


def log_2(a):
    return math.log2(a)


def log_10(a):
    return math.log10(a)


def sqrt_(a):
    return math.sqrt(a)


def abs_(a):
    return math.fabs(a)


def fact_(a):
    return math.factorial(a)


operators = ['+', '-', '*', '/', '//', '**', 'log', 'exp', 'ln', 'lg', 'sqrt', 'abs', 'fact']
bin_op = ['+', '-', '*', '/', '//', '**', 'log']

print("Input operation, clac support: +,-,*,/,//,**,exp,ln,lg,sqrt,abs,fact\nIf you want end - input \"Bay\" ")
while True:
    print("Input operation")
    op = str(input())

    if op == 'Bay':
        print("Good Bay!")
        break

    if op not in operators:
        print("Error in operator!\nAgain please\n")
        continue

    elif op in bin_op:
        print("Input first param:")
        a = float(input())
        print("Input second param:")
        b = float(input())
        if op == '+':
            print('Answer = ' + str(plus(a, b)) + '\n')
        if op == '-':
            print('Answer = ' + str(minus(a, b)) + '\n')
        if op == '*':
            print('Answer = ' + str(multiply(a, b)) + '\n')
        if op == '/':
            print('Answer = ' + str(split(a, b)) + '\n')
        if op == '//':
            print('Answer = ' + str(full_split(a, b)) + '\n')
        if op == '**':
            print('Answer = ' + str(pow(a, b)) + '\n')
        if op == 'log':
            print('Answer = ' + str(log_1(a, b)) + '\n')

    else:
        print("Input param:")
        a = float(input())
        if op == 'exp':
            print('Answer = ' + str(ex(a)) + '\n')
        if op == 'ln':
            if a <= 0:
                print("Error, number should be positive!")
                continue
            print('Answer = ' + str(log_2(a)) + '\n')
        if op == 'lg':
            if a <= 0:
                print("Error, number should be positive!")
                continue
            print('Answer = ' + str(log_10(a)) + '\n')
        if op == 'sqrt':
            if a <= 0:
                print("Error, number should be positive!")
                continue
            print('Answer = ' + str(sqrt_(a)) + '\n')
        if op == 'abs':
            print('Answer = ' + str(abs_(a)) + '\n')
        if op == 'fact':
            a = int(a)
            print('Answer = ' + str(fact_(a)) + '\n')
