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
        if char.isnumeric():
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

    for token in infix_expression:
        if isinstance(token, int):
            postfix_expression.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix_expression.append(stack.pop())
            stack.pop()
        else:
            while stack:
                if stack[-1] == '(':
                    stack.append(token)
                    break
                elif stack[-1].priority >= token.priority:
                    postfix_expression.append(stack.pop())
            if not stack:
                stack.append(token)

    while stack:
        postfix_expression.append(stack.pop())

    return postfix_expression


input_expression = "5*(3+4)"
expression1 = convert_to_instance(input_expression)
expression1 = infix_to_postfix(expression1)
print(expression1)
