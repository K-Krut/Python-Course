# importing module sys for using sys.argv
import sys

# creating vocabulary structure for changing name of operation with its sign

operations = {
    "add": "+",
    "subtract": "-",
    "multiple": "*",
    'divide': "-",
}


def output_result():
    try:
        # printing the result of calculating got by eval function
        # which gets as an argument result of joining changed name of operation and operands
        print(eval(operations[sys.argv[1]].join(sys.argv[2:])))
        # input exceptions handler
    except (EOFError, IndexError, SyntaxError, TypeError, KeyError, NameError, KeyboardInterrupt):
        print("Invalid input")


output_result()
# # print(eval(operations[sys.argv[1]].join(sys.argv[2:])))
