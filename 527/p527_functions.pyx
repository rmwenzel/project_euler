#!/usr/bin/python


def memoize(f):
    """Memoization decorator"""
    d = {}

    def f_dec(*args):
        if args in d:
            return d[args]
        else:
            d[args] = f(*args)
            return d[args]
    return f_dec


@memoize
def B(long double n):
    """Return avg iterations of standard binary search on array of len n."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        g = (n + 1) // 2
        return ((1/n) + ((g - 1) / n) * (B(g - 1) + 1) +
                ((n - g) / n) * (B(n - g) + 1))


def R(long double n):
    """Return avg iterations of random binary search on array of len n."""
    cdef long double R, i
    R, i = 1, 1
    while i < n + 1:
        R = (1 / i ** 2) * ((i**2 - 1)*R + 2*i - 1)
        i += 1
    return R
