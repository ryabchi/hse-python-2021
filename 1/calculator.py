ifNum = "1234567890."

def infix2postfix(infix):
    infix += ' '
    operatorStack = []
    post = []
    numb = ""
    for symb in infix:
        if ifNum.find(symb) == -1 and numb != "":
            post.append(float(numb))
            numb = ""
        if symb == '(':
            operatorStack += symb
        elif symb == ')':
            while len(operatorStack) != 0 and operatorStack[-1] != '(':
                post.append(operatorStack.pop())
            if operatorStack[-1] == '(':
                operatorStack.pop()
        elif ifNum.find(symb) != -1:
            numb += symb
        elif symb == '/' or symb == '*':
            while len(operatorStack) != 0 and operatorStack[-1] != '(' and operatorStack[-1] != '+' and operatorStack[-1] != '-':
                post.append(operatorStack.pop())
            operatorStack.append(symb)
        elif symb == '+' or symb == '-':
            while len(operatorStack) != 0 and operatorStack[-1] != '(':
                post.append(operatorStack.pop())
            operatorStack.append(symb)
    while len(operatorStack) != 0:
        post += operatorStack.pop() + ' '
    post.pop()
    return post


def calc(infix):
    post = infix2postfix(infix)
    stack = []
    for symb in post:
        if symb == '+':
            stack.append(stack.pop() + stack.pop())
        elif symb == '*':
            stack.append(stack.pop() * stack.pop())
        elif symb == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif symb == '/':
            a = stack.pop()
            b = stack.pop()
            stack.append(b / a)
        else:
            stack.append(symb)
    return float(stack[0])


s1 = "(1 + 7 * 3) / (15 - 2 * 2)"
s2 = str(infix2postfix(s1)) + '\n'
print(s2)
print(calc(s1))