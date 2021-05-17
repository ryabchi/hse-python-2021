
def operator_plus(a,b):
    return a+b
def operator_minus(a,b):
    return a-b
def operator_multiplication(a,b):
    return a*b
def operator_division(a,b):
    return a/b

print("Please write operation(plus, minus,multi,division)")
operation_input = input()
print("please write first number")
a=int(input())
print("please write second number")
b=int(input())
if operation_input == "plus":
    print(operator_plus(a,b))
elif operation_input == "minus":
    print(operator_minus(a,b))
elif operation_input == "multi":
    print(operator_multiplication(a,b))
else:
    print(operator_division(a,b))

