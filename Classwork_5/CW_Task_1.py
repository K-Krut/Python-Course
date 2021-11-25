

def factorial(n):
    numbers = [1]

    def find():
        while n > len(numbers):
            print((len(numbers) + 1) * numbers[len(numbers) - 1])
            numbers.append((len(numbers) + 1) * numbers[len(numbers) - 1])
        return numbers[n - 1]
    # print(numbers)
    return find


x = factorial(5)
print(x())
