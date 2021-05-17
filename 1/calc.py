operator = ['+', '-', '*', '/']
print('Input operator')
x = input()

if x not in operator:
    print('Error. This operator does not exist')
    exit()
print('Input two numbers')
a = float(input())
b = float(input())

if x == '+':
    print(f'{a}+{b}={a+b}')
elif x == '-':
    print(f'{a}-{b}={a-b}')
elif x == '*':
    print(f'{a}*{b}={a*b}')
else:
    print(f'{a}/{b}={a/b}')

