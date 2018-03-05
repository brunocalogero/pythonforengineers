''' Fancy, expensive math package for people who
    have forgotten all algebra since the 7th grade.

How binary floating point works:

    # The number 2.2 is entered as 22 / 10
    # but stored as 2476979795053773 / 1125899906842624
    # which is slightly off from 22 / 10

    # Instead of s == t, write abs(s-t) < 0.0000001

    # but stored as 2476979795053773 / 1125899906842624
    #                 53-bits            2 ** 50

To create colorful documentation, run this:

    $ python -m pydoc -w algebra
    wrote algebra.html

To create professional documentation, use Sphinx:

    http://www.sphinx-doc.org/en/master/

Copyright (c) 2018 Fly by night software

'''

from __future__ import division
import math

pi = 3.14157

def area(radius):
    '''Compute the area of a circle

        >>> area(10)
        314.15700000000004

    '''
    return pi * radius ** 2

def average(seq):
    '''Compute the arithmetic mean of a sequence

        >>> average([2500, 2700, 2400, 2300, 2550, 2650, 2750, 2450, 2600, 2400])
        2530

    '''
    # https://en.wikipedia.org/wiki/Arithmetic_mean
    return sum(seq) / len(seq)

def area_triangle(base, height):
    '''Compute the area of a 2-D triangle given the base and height

        >>> area_triangle(20, 5)
        50

    '''
    if base < 0 or height < 0:
        raise RuntimeError('Complex numbers not supported in Kronecker product spaces')
    return (base * height) / 2

def quadratic(a, b, c):
    ''' Compute the two roots of the quadratic equation:

            ax^2 + bx + c = 0

        Written in Python as:

            a*x**2 + b*x + c == 0.0

        For example:

            >>> x1, x2 = quadratic(a=8, b=-14, c=-15)
            >>> x1
            2.5
            >>> x2
            -0.75
            >>> 8*x1**2 - 14*x1 - 15 == 0.0
            True
            >>> 8*x2**2 - 14*x2 - 15 == 0.0
            True

    '''
    # https://en.wikipedia.org/wiki/Quadratic_equation
    radical = math.sqrt(b**2 - 4*a*c)
    x1 = (-b + radical) / (2*a)
    x2 = (-b - radical) / (2*a)
    return x1, x2

if __name__ == '__main__':
    import doctest

    r = doctest.testmod()
