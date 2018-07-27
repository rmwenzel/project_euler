#!usr/bin/python

import numpy as np


def fib_list(upper_bound):
    """Generate an ordered ndarray of Fibonnacis <= upper_bound."""
    """Assumes upper_bound >= 2."""
    fibs = np.array([1, 1])
    while fibs[-1] <= upper_bound:
        fibs = np.append(fibs, fibs[-1] + fibs[-2])
    return fibs[:-1]


if __name__ == "__main__":
    fibs = fib_list(4*10**6)
    ans = sum(fibs[fibs % 2 == 0])
    print("The answer is {}".format(ans))
