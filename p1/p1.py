#!usr/bin/python

import numpy as np


def sum_multiples(n):
    """Sum multiples of 3 or 5 that are < n."""
    def f(x):
        return x if (x % 3 == 0 or x % 5 == 0) else 0
    return sum(np.array(list(map(f, np.arange(1, n)))))


if __name__ == "__main__":
    sum_multiples(1000)
