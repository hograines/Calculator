from Operators import *


def convert_to_instance(expression):
    operators = {
        '+': Addition(),
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


input_expression = "5*(3+4)"
expression1 = convert_to_instance(input_expression)
print(expression1)
