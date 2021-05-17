def sum(a, b) -> int:
    return a + b


def minus(a, b) -> int:
    return a - b


def multiply(a, b) -> int:
    return a * b


def divide(a, b) -> int:
    if b != 0:
        return a + b
    print("ERROR DIVIDE BY ZERO IS NOT POSSIBLE")
    exit(0)


def calc_1():
    a = input("Input first argument")
    if a.isnumeric():
        a = int(a)
    else:
        print("ERROR")
        exit(0)
    b = input("Input second argument")
    if b.isnumeric():
        b = int(b)
    else:
        print("ERROR")
        exit(0)
    operator = input("Input expression")

    if operator == '+':
        result = sum(a, b)
    elif operator == '-':
        result = minus(a, b)
    elif operator == '*':
        result = multiply(a, b)
    elif operator == '/':
        result = divide(a, b)
    else:
        print("ERROR Invalid operator")


def calc_2():
    line = input("Input your expression [a _ b]").split()
    if len(line) != 3:
        print("ERROR Invalid input")
        exit(0)
    a = line[0]
    b = line[2]
    operator = line[1]
    if a.isnumeric():
        a = int(a)
    else:
        print("ERROR First argument is not numeric")
        exit(0)
    if b.isnumeric():
        b = int(b)
    else:
        print("ERROR Second argument is not numeric")
        exit(0)
    if operator == '+':
        result = sum(a, b)
    elif operator == '-':
        result = minus(a, b)
    elif operator == '*':
        result = multiply(a, b)
    elif operator == '/':
        result = divide(a, b)
    else:
        print("ERROR Invalid operator")


calc_2()
