# -*- coding: utf-8 -*-
import doctest


def sum_divisors(n):
    """
    Solution for Problem 1 of Project Euler
    http://projecteuler.net/problem=1

    >>> sum_divisors(10)
    23
    """
    sequence = (x for x in xrange(1, n) if x % 3 == 0 or x % 5 == 0)
    return reduce(lambda x, y: x + y, sequence)


if __name__ == '__main__':
    doctest.testmod()
    print sum_divisors(1000)
