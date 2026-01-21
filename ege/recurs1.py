# def print_n(count):
#     for i in range(count):
#         print("hello")

# print_n(10)


# def calc_y(a, b, c, x):
#     y = a * x * x + b * x + c
#     return y

# for x in range(-10, 10 + 1):
#     y = calc_y(2, 3, 1, x)
#     print(f"x = {x} y = {y}")

import sys

sys.setrecursionlimit(10000)


def print_hello(count):
    print(f"{count} hello")
    count += 1

    if count < 5000:
        print_hello(count)


print_hello(1)
