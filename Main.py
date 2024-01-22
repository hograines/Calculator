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
        if char.isnumeric() or char == '.':
            if char == '.':
                try:
                    if '.' in current_char:
                        raise Exception("Invalid Expression")
                except Exception:
                    print("Invalid expression")
                    exit()
            current_char += char
        elif char == '-':
            if current_char:
                fixed_expression.append(int(current_char) if current_char.isdigit() else operators.get(current_char,
                                                                                                       current_char))
                current_char = ''
            if not fixed_expression:
                fixed_expression.append(MinusUnary())
            elif fixed_expression[-1] == '(':
                fixed_expression.append(MinusUnary())
            elif isinstance(fixed_expression[-1], Operator):
                fixed_expression.append(MinusSign())
            else:
                fixed_expression.append(Subtraction())
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


def check_fact_tilda_sum(unchecked):
    for i in range(len(unchecked)):
        if unchecked[i] == '~':
            if i > 0 and unchecked[i - 1].isdigit():
                return False
        elif unchecked[i] == '!':
            if i < len(unchecked) - 1 and unchecked[i + 1].isdigit():
                return False
        elif unchecked[i] == '#':
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
    if (check_fact_tilda_sum(unchecked) and
            balanced_parentheses(unchecked) and
            unchecked and
            not unchecked.isspace() and
            "()" not in unchecked and
            not any(char.isalpha() for char in unchecked) and
            not (unchecked[0] == '-' and unchecked[1] == '~') and
            not (unchecked[unchecked.find('(') + 1] == '-' and unchecked[unchecked.find('(') + 2] == '~') and not
             (isinstance(unchecked[unchecked.find('(') + 1], BinaryOperator))):
        return True
    return False

try:
    while True:
        input_expression = input("Enter a math expression.\n")
        input_expression.replace(" ", "")
        stable_input_expression = minus_gathering(input_expression)
        if check_input(stable_input_expression):
            expression1 = convert_to_instance(stable_input_expression)
            expression1 = infix_to_postfix(expression1)
            print(evaluation(expression1))
        else:
            print("Invalid Expression")
except KeyboardInterrupt:
    print("You interrupted the program!")

'''
expression1 = convert_to_instance(input_expression)
expression1 = infix_to_postfix(expression1)
print(evaluation(expression1))
'''