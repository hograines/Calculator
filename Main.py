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
            try:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(token.calc(num1, num2))
            except Exception:
                print("Invalid expression")
                exit()
        elif isinstance(token, RightOperator) or isinstance(token, LeftOperator):
            try:
                stack.append(token.calc(stack.pop()))
            except ValueError as er:
                print(er)
                flag = True
            except Exception:
                print("Invalid expression")
                exit()
        else:
            print("PROBLEM!")
    if flag is False:
        return stack[-1]


def how_much(lst, token):
    counter = 0
    for tok in lst:
        if tok == token:
            counter += 1
    return counter


def balanced_parentheses(unchecked):
    counter = 0
    balanced = False
    for char in unchecked:
        if char == "(":
            counter += 1
        elif char == ")":
            counter -= 1
        if counter < 0:
            return balanced
    if counter == 0:
        return not balanced
    return balanced


def check_fact_tilda(unchecked):
    for i in range(len(unchecked)):
        if unchecked[i] == '~':
            if i > 0 and unchecked[i - 1].isdigit():
                return False
        elif unchecked[i] == '!':
            if i < len(unchecked) - 1 and unchecked[i + 1].isdigit():
                return False
    return True


def minus_gathering(unchecked):
    result = []
    minus_counter = 0
    for char in unchecked:
        if char == '-':
            minus_counter += 1
        else:
            if minus_counter % 2 == 1:
                result.append('-')
            result.append(char)
            minus_counter = 0

    if minus_counter:
        if minus_counter % 2 == 1:
            result.append('-')
    return ''.join(result)


def check_input(unchecked):
    unchecked.replace(" ", "")
    unchecked = minus_gathering(unchecked)
    if check_fact_tilda(unchecked) and balanced_parentheses(unchecked):
        return True
    return False


input_expression = ""

if check_input(input_expression):
    expression1 = convert_to_instance(input_expression)
    expression1 = infix_to_postfix(expression1)
    print(evaluation(expression1))
else:
    print("Invalid Expression")
