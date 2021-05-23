#  Copyright 2021 kisozinov
operators = ['+','-','*','/','^','mod']
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
op = input('Enter the operation: ')
if op in operators:
  if op == '+':
    res = a + b
  elif op == '-':
    res = a - b
  elif op == '*':
    res = a * b
  elif op == '/':
    res = a / b
  elif op == '^':
    res = a ** b
  elif op == 'mod':
    res = a % b
  print('Result is', res)
else:
  print("You've entered wrong operation")