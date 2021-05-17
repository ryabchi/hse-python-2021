# Python practice №1

print('To stop print stop')
while True:
    operation = input('Print whole expression (1 + 2): ')
    if operation == 'stop':
        exit(0)
    else:
        a, b = int(operation.split()[0]), int(operation.split()[2])
        if operation.split()[1] == '+':
            print(a + b)
        elif operation.split()[1] == '-':
            print(a - b)
        elif operation.split()[1] == '*':
            print(a * b)
        elif operation.split()[1] == '/':
            print(a / b)
        else:
            print('Wrong operation')
            exit(1)
        print()
