# function for printing a result of checking and calculating
def print_data(a, b):
    print('(', a, ',', b, ')')


# function for checking the correction of formula
# it gets string and searches for '+' and '-' signs and replace them with replace() function
# than check if the result is a digit and if there isn't repetitions '++'
def checking(expression):
    return expression.replace('+', '').replace('-', '').isdigit() and '++' not in expression.replace('-', '+')


# function for printing the result of checking a formula and calculating the correct one
def output(str_):
    try:
        result_str = checking(str_)
        return (result_str, eval(str_)) if result_str else (result_str, None)
    except (EOFError, IndexError, SyntaxError, TypeError, KeyError, NameError, KeyboardInterrupt):
        return False, None


# getting the formula from user
result = output(input())

print_data(result[0], result[1])





# return (checking(str_), eval(str_)) if checking(str_) else (checking(str_), None)




# def print_data(a, b):
#     print('(', a, ',', b, ')')
#
#
# # function for checking the correction of formula
# # it gets string and searches for '+' and '-' signs and replace them with replace() function
# # than check if the result is a digit and if there isn't repetitions '++'
# def checking(expression):
#     return expression.replace('+', '').replace('-', '').isdigit() and '++' not in expression.replace('-', '+')
#
#
# # function for printing the result of checking a formula and calculating the correct one
# def output(str_):
#     try:
#         print_data(checking(str_), eval(str_)) if checking(str_) else print_data(checking(str_), None)
#     except (EOFError, IndexError, SyntaxError, TypeError, KeyError, NameError, KeyboardInterrupt):
#         print_data(False, None)
#
#
# #getting the formula from user
# output(input())
