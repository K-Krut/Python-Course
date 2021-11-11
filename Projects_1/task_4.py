# function for calculating the maximum bars weight could be packed.
# The function gets KS_capacity -- capacity of the
# knapsack, bars - list with the all bars weights and size - number of bars
def calculating(KS_capacity, bars, size):
    # creating 2d array and initializing with 0
    Arr = [[0 for x in range(KS_capacity + 1)] for x in range(size + 1)]

    # two loops for filling the array with the max weight that could be packed at certain steep -- K[i][j] element
    for i in range(size + 1):
        for j in range(KS_capacity + 1):
            # checking if the weight of the i-th el <= all weight in cell j
            # checking if the weight of the i-th el <= weight that in cell j
            # choosing the Arr[i - 1][j] when the weight of i-th el >= j
            Arr[i][j] = max(bars[i - 1] + Arr[i - 1][j - bars[i - 1]], Arr[i - 1][j]) if bars[i - 1] <= j else \
                Arr[i - 1][j]
    # returning the last cell of the array that contains the max weight
    return Arr[size][KS_capacity]


# function for getting weights of bars
def input_data():
    # creating list with bars
    data = []
    try:
        data = [int(i) for i in input().split()]
    except (EOFError, IndexError, ValueError, SyntaxError, TypeError, KeyError, NameError, KeyboardInterrupt):
        print("Invalid input")
    # return tuple with bars weights and len of list
    return data, len(data)


bars_ = input_data()
# printing result of calculating
try:
    print("Result: ", calculating(int(input()), bars_[0], bars_[1]))
except (EOFError, IndexError, ValueError, SyntaxError, TypeError, KeyError, NameError, KeyboardInterrupt):
    print("Invalid data input")
