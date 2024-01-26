from Operators import *


def convert_to_instance(expression):
    '''
    :param expression: Mostly valid math expression
    :return: A list that contains the same math expression, where the operators have been replaced by their class
    instances
    '''
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
                if '.' in current_char:
                     raise Exception("Invalid Expression")
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


def infix_to_postfix(infix_expression):
    '''
    :param infix_expression: A list that contains an infix math expression
    :return: A list that contains the same expression but in postfix
    '''
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
    '''
    :param postfix_expression: A list that contains a postfix math expression
    :return: The value of the math expression
    '''
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
            stack.append(token.calc(stack.pop()))
        else:
            print("PROBLEM!")
    if flag is False:
        return stack[-1]


def balanced_parentheses(unchecked):
    '''
    :param unchecked: A math expression
    :return: Whether the parentheses in the expression are balanced and correct
    '''
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
    '''
    :param unchecked: A math expression
    :return: Whether the operators Tilda, Sum and Factorial were places correctly in the expression
    '''
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
    '''
    :param unchecked: A math expression
    :return: The same math expression after gathering excess minuses
    '''
    result = []
    minus_counter = 0
    for char in unchecked:
        if char == '-':
            minus_counter += 1
        else:
            if minus_counter % 2 == 1:
                result.append('-')
            elif minus_counter != 0:
                result.append('--')
            result.append(char)
            minus_counter = 0

    if minus_counter:
        if minus_counter % 2 == 1:
            result.append('-')
    return ''.join(result)


def check_input(unchecked):
    '''
    :param unchecked: A math expression
    :return: Whether the expression is valid or not (not entirely, checks everything not operator related)
    '''
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


def input_ready(expression):
    '''
    A function for the pytest
    :param expression: A math expression
    :return: The value of the math expression (if valid)
    '''
    expression.replace(" ", "")
    expression_new = minus_gathering(expression)
    if check_input(expression_new):
        expression_new = convert_to_instance(expression_new)
        expression_new = infix_to_postfix(expression_new)
        return evaluation(expression_new)
    else:
        raise Exception("Invalid")


if __name__ == "__main__":
    try:
        while True:
            input_expression = input("Enter a math expression.\n")
            input_ready(input_expression)
    except Exception:
        print("Invalid Expression!")
    except KeyboardInterrupt:
        print("You interrupted the program!")
