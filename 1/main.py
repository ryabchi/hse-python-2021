operators={"+": lambda a,b: a + b, "-": lambda a,b: a - b, "*": lambda a,b: a * b, "/": lambda a,b: a / b}
try:
    f = operators[input("Введите оператор: ")]
except KeyError:
    print("Такого оператора не существует")
    exit()

a = input("Введите первое число: ")

b = input("Введите второе число: ")

try:
    result = f(int(a), int(b))
except ValueError:
    print("Один или оба значения не являются числом")
    exit()
except ZeroDivisionError
    print("Деление на ноль")
    exit()
    
print(f"Result: {result}")
