# importing module sys for using sys.argv
import sys


def check_input(str_):
    try:
        # printing the result of calculating got with the help of a build-in-function eval()
        # that evaluates the string read from the command line
        print(eval(str_))
        # exceptions handler
    except (IOError, EOFError, TypeError, NameError, SyntaxError):
        print("Input error")


check_input(" ".join(sys.argv[1:]))

