# importing module sys for using sys.argv
import sys


# function or checking and returning the result of review
def check_input(str_):
    try:
        # returning the result of calculating got with the help of a build-in-function eval()
        # that evaluates the string read from the command line
        return eval(str_)
        # exceptions handler
    except (IOError, EOFError, TypeError, NameError, SyntaxError):
        return "Input error"


print(check_input(" ".join(sys.argv[1:])))

