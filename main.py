while True:
    operator = input('Enter operator: ')
    operators=['+', '-', '*', '/']
    if operator not in operators:
        exit(1)
    a=int(input("a="))
    b=int(input("b="))
    if operator == '+':
        result=a+b
    if operator == '-':
        result = a - b
    if operator == '*':
        result = a * b
    if operator == '/':
        if b==0:
            print('Division by 0')
            exit(1)
        result = a / b
    print (f'{a}{operator}{b}={result}')
