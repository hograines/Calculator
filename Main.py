from Operators import *


def convert_to_instance(expression):
    operators = {
        '+': Addition(),
        '-': Subtraction(),
        '*': Multiple(),
        '/': Divide(),
        '^': Power(),
        '%': Module(),
        '@': Average(),
        '$': Maximum(),
        '&': Minimum(),
        '!': Factorial(),
        '#': Summary(),
        '~': Tilda(),
        '(': '(',
        ')': ')'
    }

    fixed_expression = []
    current_char = ''

    for char in expression:
        if char.isnumeric() or char == '.':
            current_char += char
        elif char.isspace():
            continue
        elif current_char:
            fixed_expression.append(int(current_char) if current_char.isdigit() else operators.get(current_char,
                                                                                                   current_char))
            current_char = ''
            fixed_expression.append(operators.get(char, char))
        else:
            fixed_expression.append(operators.get(char, char))

    if current_char:
        fixed_expression.append(int(current_char) if current_char.isdigit() else operators.get(current_char,
                                                                                               current_char))

    return fixed_expression


# input_expression = "5*(3+4)"
# expression1 = convert_to_instance(input_expression)
# print(expression1)

def infix_to_postfix(infix_expression):
    postfix_expression = []
    stack = []
    flag = True

    for token in infix_expression:
        if token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix_expression.append(stack.pop())
            stack.pop()
        elif isinstance(token, int) or isinstance(token, str):
            postfix_expression.append(token)
        else:
            while stack and flag is True:
                if stack[-1] == '(':
                    stack.append(token)
                    flag = False
                elif stack[-1].priority >= token.priority:
                    postfix_expression.append(stack.pop())
                elif stack[-1].priority < token.priority:
                    flag = False
                    stack.append(token)
            if not stack:
                stack.append(token)
            flag = True

    while stack:
        postfix_expression.append(stack.pop())

    return postfix_expression


def evaluation(postfix_expression):
    stack = []
    flag = False

    for token in postfix_expression:
        if isinstance(token, int) or isinstance(token, str):
            if isinstance(token, str):
                stack.append(float(token))
            else:
                stack.append(token)
        elif isinstance(token, BinaryOperator):
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(token.calc(num1, num2))
        elif isinstance(token, RightOperator) or isinstance(token, LeftOperator):
            try:
                stack.append(token.calc(stack.pop()))
            except ValueError as er:
                print(er)
                flag = True
        else:
            print("PROBLEM!")
    if flag is False:
        return stack[-1]


input_expression = "(5-6)!"
expression1 = convert_to_instance(input_expression)
expression1 = infix_to_postfix(expression1)
print(evaluation(expression1))
