from functools import *


def f(n):
    if n > 40:
        return f(n - 4) + 3020
    else:
        return 3 * (g(n - 2) - 15)


@lru_cache(None)
def g(n):
    if n >= 301208:
        return n * 10 + 50
    else:
        return g(n + 7) - 21


for i in reversed(range(301210)):
    g(i)

print(f(2026))
