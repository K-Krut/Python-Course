import os.path
import random
import timeit

# file = open('Her.txt', 'w')
# while os.path.getsize('Her.txt')/1048576 < 50:
#     file.write(str(random.randint(0, 9)) + '\n')
# file.close()

print(os.path.getsize('Her.txt')/1048576)

str1 = """
with open('Her.txt') as file:
    for line in file.readlines():
        result = 0
        if line.strip().isdigit():
            result += int(line.strip())
"""


str2 = """
with open('Her.txt') as file:
    for line in file:
        result = 0
        if line.strip().isdigit():
            result += int(line.strip())
"""

str3 = """
with open('Her.txt') as file:
    result = sum(int(line.strip()) for line in file if line.strip().isdigit())
"""


# print(timeit.timeit(str1, number=50))
print(timeit.timeit(str1, number=1))
# print(timeit.timeit(str2, number=50))
print(timeit.timeit(str2, number=1))
# print(timeit.timeit(str3, number=50))
print(timeit.timeit(str3, number=1))
