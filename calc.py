def calc(num1, num2, flag):
    if flag == "+":
        out = num1 + num2
    elif flag == "-":
        out = num1 - num2
    elif flag == "/" and num2 != 0:
        out = num1 / num2
    elif flag == "*":
        out = num1 * num2
    return out


if __name__ == '__main__':
    a, b = [int(x) for x in input('Enter two numbers: ').split(' ')]
    operator = input('Enter operator: ')
    print(f'Output:', calc(a, b, operator))
