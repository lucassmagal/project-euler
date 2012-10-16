# -*- coding: utf-8 -*-


def sum_fibonacci_even_terms():
    """
    Solution of problem 2 of Project Euler
    http://projecteuler.net/problem=2
    """
    result = 0
    a, b = 1, 2

    while True:
        if a > 4000000:
            return result
        if a % 2 == 0:
            result += a
        a, b = b, a + b


if __name__ == '__main__':
    print sum_fibonacci_even_terms()
