Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 12:01:12) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> # bit.ly/python-sj178a
>>> # http://bit.ly/python-sj178a
>>> 
# http://bit.ly/python-sj178c
>>> # Start gently and build-up speed
>>> # Review old material
>>> # Pay attention to smaller details
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
>>> __name__
'__main__'
>>> 
>>> # Dunder --> double-underscore
>>> import algebra
>>> algebra.__name__
'algebra'
>>> 
>>> __doc__
' Fancy, expensive math package for people who\n    have forgotten all algebra since the 7th grade.\n'
>>> 
>>> # mkdir pyclass2
>>> # cd pyclass
>>> # python2.7 -m idlelib.idle
>>> 
>>> 
>>> 
>>> # What does import do?
>>> # * Scans the current direct and standary library for a py file
>>> # * Runs all the code in its own namespace
>>> # * Wraps it in a module object
>>> # * Makes an assignment to globals
>>> 
>>> import xyzpdq

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    import xyzpdq
ImportError: No module named xyzpdq
>>> import Algebra

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    import Algebra
ImportError: No module named Algebra
>>> import xyzpdq

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    import xyzpdq
ImportError: No module named xyzpdq
>>> import os
>>> os.getcwd()
'/Users/raymond/Dropbox/Public/sj178'
>>> 
>>> 
>>> # So, when you get an ImportError for No module named algebra.
>>> # 1) You named the file something other than "algebra.py"
>>> # 2) You saves the file in a different (unfindable directory)
>>> 
>>> os.chdir('notes')

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    os.chdir('notes')
OSError: [Errno 2] No such file or directory: 'notes'
>>> os.chdir('notes2')
>>> import xyzpdq

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    import xyzpdq
ImportError: No module named xyzpdq
>>> os.chdir('..')
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj178/notes2/xyzpdq.py =======
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj178/notes2/xyzpdq.py =======
>>> dir()
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'ac', 'pi']
>>> __file__
'/Users/raymond/Dropbox/Public/sj178/notes2/xyzpdq.py'
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
>>> __name__
'__main__'
>>> __package__ is None
True
>>> import xml.etree
>>> xml.etree.__package__
>>> 
>>> 
>>> 
>>> dir()
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'ac', 'pi', 'xml']
>>> pi
3.14157
>>> ac(float('Nan'))
nan
>>> ac(float('Infinity'))
inf
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
>>> area(10)
314.15700000000004
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
>>> help(area)
Help on function area in module __main__:

area(radius)
    Compute the area of a circle

>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
>>> # a*x**2 + b*x + c
>>> # a*x**2+b*x+c
>>> # a * x ** 2 + b * x + c
>>> b * x + c

Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    b * x + c
NameError: name 'b' is not defined
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
>>> area(10)
314.15700000000004
>>> 10 ** 2
100
>>> 
>>> # binary floating point intrinsically has
>>> # "representation error"
>>> 
>>> # Write a number in decimal floating point
>>> # it make not be exactly storable in binary floating point
>>> 
>>> # 1
>>> # 2
>>> # 3
>>> # 12
>>> # 1234
>>> #    ^-- 1
>>> #   ^--- 10
>>> # MCCXXXIV
>>> # 1234.56
>>> #      ^---- 1/10
>>> #       ^--- 1/100
>>> 
>>> # 123456 / 100   <-- decimal fraction      n / 10**m
>>> # 1234.56 == 123456 * 10 ** -2
>>> 
>>> 0b101
5
>>> #   ^-- 1
>>> #  ^--- 2
>>> # ^---- 4
>>> # 101.11
>>> #      ^-- 1/4
>>> #     ^----1/2
>>> 4 + 1 + 0.5 + 0.25
5.75
>>> 0b10111
23
>>> 23.0 / 4
5.75
>>> # 101.11   <-- binary faction    10111 / 4       23 / 4     n / 2 ** m
>>> 
>>> x = 5.75                # 575 / 100
>>> x.as_integer_ratio()
(23, 4)
>>> bin(23)
'0b10111'
>>> 
>>> # You type in numbers as decimal fractions but they are stored as binary fractions
>>> x = 5.75                # 575 / 100    ==     23 / 4
>>> x = 2.2
>>> #                       #  22 / 10     -->   n / 2 ** m
>>> #                                            ^-- 53 bits
>>> x.as_integer_ratio()
(2476979795053773, 1125899906842624)
>>> import math
>>> math.log(1125899906842624, 2)
50.0
>>> 2 ** 50
1125899906842624
>>> bin(2476979795053773)
'0b1000110011001100110011001100110011001100110011001101'
>>> 2476979795053773 * 2 ** -50
2.2
>>> 
>>> s = 1.1 + 2.2
>>> t = 3.3
>>> s == t
False
>>> s - t
4.440892098500626e-16
>>> 
>>> abs(s - t) < 0.0000001
True
>>> [ 0.1 ]
[0.1]
>>> [ 0.1 ] * 10
[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
>>> sum([ 0.1 ] * 10) == 1.00
False
>>> sum([ 0.1 ] * 10)
0.9999999999999999
>>> (1.1).as_integer_ratio()
(2476979795053773, 2251799813685248)
>>> abs(sum([ 0.1 ] * 10) - 1.00) < 0.00000001
True
>>> x.as_integer_ratio()
(2476979795053773, 1125899906842624)
>>> 
>>> 
>>> 
>>> # The number 2.2 is entered as 22 / 10
>>> # but stored as 2476979795053773 / 1125899906842624
>>> # which is slightly off from 22 / 10
>>> 
>>> # Instead of s == t, write abs(s-t) < 0.0000001
>>> 
>>> # but stored as 2476979795053773 / 1125899906842624
>>> #                 53-bits            2 ** 50
>>> 
>>> area(10)
314.15700000000004
>>> pi.as_integer_ratio()
(7074186740679165, 2251799813685248)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
>>> area(10)
314.15700000000004
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
>>> help(area)
Help on function area in module __main__:

area(radius)
    Compute the area of a circle
    
    >>> area(10)
    314.15700000000004

>>> area(10)
314.15700000000004
>>> area(10) == 314.15700000000004
True
>>> __doc__
' Fancy, expensive math package for people who\n    have forgotten all algebra since the 7th grade.\n\nHow binary floating point works:\n\n    # The number 2.2 is entered as 22 / 10\n    # but stored as 2476979795053773 / 1125899906842624\n    # which is slightly off from 22 / 10\n\n    # Instead of s == t, write abs(s-t) < 0.0000001\n\n    # but stored as 2476979795053773 / 1125899906842624\n    #                 53-bits            2 ** 50\n'
>>> __name__
'__main__'
>>> area
<function area at 0x1004ec500>
>>> dir(area)
['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', '__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name']
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
>>> dir()
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'area', 'pi']
>>> 
>>> area.__name__
'area'
>>> area.__doc__
'Compute the area of a circle\n\n        >>> area(10)\n        314.15700000000004\n\n    '
>>> s = area.__doc__
>>> s
'Compute the area of a circle\n\n        >>> area(10)\n        314.15700000000004\n\n    '
>>> print s
Compute the area of a circle

        >>> area(10)
        314.15700000000004

    
>>> # repr has quotes and \n
>>> # str is expanded
>>> 
>>> s = """hello world"""
>>> s
'hello world'
>>> 
>>> 'hello world'
'hello world'
>>> 'hello world'
'hello world'
>>> 10 + 30
40
>>> 40
40
>>> 
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
>>> s = area.__doc__
>>> s
'Compute the area of a circle\n\n        >>> area(10)\n        314.15700000000004\n\n    '
>>> i = s.index('>>> ')
>>> i
38
>>> s.index('\n')
28
>>> s.index('\n', 38)
50
>>> 
>>> 
>>> s = area.__doc__
>>> i = s.index('>>> ')
>>> j = s.index('\n', i+1)
>>> k = s.index('\n', j+1)
>>> s[i:j]
'>>> area(10)'
>>> len('>>> ')
4
>>> 
>>> 
>>> prefix = '>>> '
>>> s = area.__doc__
>>> i = s.index(prefix)
>>> j = s.index('\n', i+1)
>>> k = s.index('\n', j+1)
>>> command = s[i+len(prefix) : j]
>>> command
'area(10)'
>>> s[j:k]
'\n        314.15700000000004'
>>> help(str.strip)
Help on method_descriptor:

strip(...)
    S.strip([chars]) -> string or unicode
    
    Return a copy of the string S with leading and trailing
    whitespace removed.
    If chars is given and not None, remove characters in chars instead.
    If chars is unicode, S will be converted to unicode before stripping

>>> help(str.rstrip)
Help on method_descriptor:

rstrip(...)
    S.rstrip([chars]) -> string or unicode
    
    Return a copy of the string S with trailing whitespace removed.
    If chars is given and not None, remove characters in chars instead.
    If chars is unicode, S will be converted to unicode before stripping

>>> help(str.lstrip)
Help on method_descriptor:

lstrip(...)
    S.lstrip([chars]) -> string or unicode
    
    Return a copy of the string S with leading whitespace removed.
    If chars is given and not None, remove characters in chars instead.
    If chars is unicode, S will be converted to unicode before stripping

>>> expected = s[j:k].lstrip()
>>> 
>>> 
>>> 
>>> command
'area(10)'
>>> expected
'314.15700000000004'
>>> 
>>> 30 + 40*2
110
>>> print 30 + 40*2
110
>>> # printf("%d\n", 30 + 40*2);
>>> 
>>> game = raw_input('Do you want to play a game? ')
Do you want to play a game? Global Thermonuclear War
>>> game
'Global Thermonuclear War'
>>> 
>>> 
>>> expr = raw_input('Enter an expression: ')
Enter an expression: 30 + 40*2
>>> 
>>> expr
'30 + 40*2'
>>> # printf("Enter an expression: ")
>>> # scanf("%s", %expr)
>>> # scanf("%s", &expr)
>>> 
>>> 
>>> # source --(compiler)--> executable
>>> #   x         x
>>> #                          runs
>>> #            ^-- smart
>>> #  ^-- smart
>>> 
>>> 
>>> # source --(interpreter)--> runs
>>> #               ^-- smart
>>> #  keep       keep      <-----|
>>> 
>>> help(area)
Help on function area in module __main__:

area(radius)
    Compute the area of a circle
    
    >>> area(10)
    314.15700000000004

>>> expr
'30 + 40*2'
>>> eval(expr)
110
>>> repr(eval(expr))
'110'
>>> print repr(eval(expr))
110
>>> expr
'30 + 40*2'
>>> actual = repr(eval(expr))
>>> 
>>> 
>>> command
'area(10)'
>>> expected
'314.15700000000004'
>>> actual
'110'
>>> actual = repr(eval(command))
>>> actual
'314.15700000000004'
>>> expected == actual
True
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
TestResults(failed=0, attempted=1)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
TestResults(failed=0, attempted=1)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
**********************************************************************
File "/Users/raymond/Dropbox/Public/sj178/algebra.py", line 21, in __main__.area
Failed example:
    area(10)
Expected:
    314.15700000000004
Got:
    395.5002305930203
**********************************************************************
1 items had failures:
   1 of   1 in __main__.area
***Test Failed*** 1 failures.
TestResults(failed=1, attempted=1)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
TestResults(failed=0, attempted=1)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
TestResults(failed=0, attempted=1)
>>> avg('nx200g')

Traceback (most recent call last):
  File "<pyshell#241>", line 1, in <module>
    avg('nx200g')
  File "/Users/raymond/Dropbox/Public/sj178/algebra.py", line 29, in avg
    return sum(s)/len(s)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
>>> 
>>> # Generally, don't abbrev.
>>> # Unless there is a strong, widespread cultural standard
>>> 
>>> # sd  std dev    std_dev  stddev  stdev
>>> 
>>> # 3(mgt)   (4 mgmt)   5(mgmnt)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
TestResults(failed=0, attempted=1)
>>> # unless there is an unequivocal abbrev:  seq
>>> # unless the full word is hard to spell
>>> 
>>> average([2500, 2700, 2400, 23000, 2550, 2650, 2750, 2450, 2600, 2400])
4600
>>> average([2500, 2700, 2400, 2300, 2550, 2650, 2750, 2450, 2600, 2400])
2530
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
TestResults(failed=0, attempted=2)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
**********************************************************************
File "/Users/raymond/Dropbox/Public/sj178/algebra.py", line 30, in __main__.average
Failed example:
    average([2500, 2700, 2400, 2300, 2550, 2650, 2750, 2450, 2600, 2400])
Expected:
    2530
Got:
    2531
**********************************************************************
1 items had failures:
   1 of   1 in __main__.average
***Test Failed*** 1 failures.
TestResults(failed=1, attempted=2)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
TestResults(failed=0, attempted=2)
>>> help(average)
Help on function average in module __main__:

average(seq)
    Compute the arithmetic mean of a sequence
    
    >>> average([2500, 2700, 2400, 2300, 2550, 2650, 2750, 2450, 2600, 2400])
    2530

>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
TestResults(failed=0, attempted=2)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
TestResults(failed=0, attempted=2)
>>> area_triangle(20, 5)
50
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
TestResults(failed=0, attempted=3)
>>> area_triangle(-20, 5)
-50
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
TestResults(failed=0, attempted=3)
>>> area_triangle(-20, 5)

Traceback (most recent call last):
  File "<pyshell#258>", line 1, in <module>
    area_triangle(-20, 5)
  File "/Users/raymond/Dropbox/Public/sj178/algebra.py", line 45, in area_triangle
    raise RuntimeError('Complex numbers not supported in Kronecker product spaces')
RuntimeError: Complex numbers not supported in Kronecker product spaces
>>> 
>>> 
>>> 
>>> # x, y are unknowns
>>> # z for an unknown variable that is complex
>>> 
>>> def f(x):
	return 3*x + 2

>>> def f(z):
	return z * (3 - 5j)

>>> # a, b, c are polynomial coefficients
>>> # i, j, k are typically integer indices
>>> for i in range(8):
	for j in range(8):
		print '%02d' % (i*j),
	print

	
00 00 00 00 00 00 00 00
00 01 02 03 04 05 06 07
00 02 04 06 08 10 12 14
00 03 06 09 12 15 18 21
00 04 08 12 16 20 24 28
00 05 10 15 20 25 30 35
00 06 12 18 24 30 36 42
00 07 14 21 28 35 42 49
>>> for i in range(8):
	for j in range(8):
		print '%2d' % (i*j),
	print

	
 0  0  0  0  0  0  0  0
 0  1  2  3  4  5  6  7
 0  2  4  6  8 10 12 14
 0  3  6  9 12 15 18 21
 0  4  8 12 16 20 24 28
 0  5 10 15 20 25 30 35
 0  6 12 18 24 30 36 42
 0  7 14 21 28 35 42 49
>>> for i in range(8):
	for j in range(8):
		print '%2d' % i*j,
	print

	
  0  0 0  0 0 0  0 0 0 0  0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0 0
  1  1 1  1 1 1  1 1 1 1  1 1 1 1 1  1 1 1 1 1 1  1 1 1 1 1 1 1
  2  2 2  2 2 2  2 2 2 2  2 2 2 2 2  2 2 2 2 2 2  2 2 2 2 2 2 2
  3  3 3  3 3 3  3 3 3 3  3 3 3 3 3  3 3 3 3 3 3  3 3 3 3 3 3 3
  4  4 4  4 4 4  4 4 4 4  4 4 4 4 4  4 4 4 4 4 4  4 4 4 4 4 4 4
  5  5 5  5 5 5  5 5 5 5  5 5 5 5 5  5 5 5 5 5 5  5 5 5 5 5 5 5
  6  6 6  6 6 6  6 6 6 6  6 6 6 6 6  6 6 6 6 6 6  6 6 6 6 6 6 6
  7  7 7  7 7 7  7 7 7 7  7 7 7 7 7  7 7 7 7 7 7  7 7 7 7 7 7 7
>>> 'The answer is %d today' % 10
'The answer is 10 today'
>>> 'The answer is %d today' % 2 * 5
'The answer is 2 todayThe answer is 2 todayThe answer is 2 todayThe answer is 2 todayThe answer is 2 today'
>>> 'The answer is %d today' % (2 * 5)
'The answer is 10 today'
>>> # n is total number of items
>>> # m, n
>>> # p, q
>>> # n, k
>>> # n, r
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
TestResults(failed=0, attempted=3)
>>> a = 10
>>> b = -4
>>> c = 5
>>> x = 2.5
>>> ax^2 + bx + c = 0
SyntaxError: can't assign to operator
>>> ax^2 + bx + c == 0

Traceback (most recent call last):
  File "<pyshell#294>", line 1, in <module>
    ax^2 + bx + c == 0
NameError: name 'ax' is not defined
>>> a*x^2 + b*x + c == 0

Traceback (most recent call last):
  File "<pyshell#295>", line 1, in <module>
    a*x^2 + b*x + c == 0
TypeError: unsupported operand type(s) for ^: 'float' and 'float'
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
TestResults(failed=0, attempted=3)
>>> x1, x2 = quadratic(a=8, b=-14, c=-15)
>>> x1
2.5
>>> x2
-0.75
>>> a*x1**2 + b*x1 + c == 0.0

Traceback (most recent call last):
  File "<pyshell#299>", line 1, in <module>
    a*x1**2 + b*x1 + c == 0.0
NameError: name 'a' is not defined
>>> 8*x1**2 - 14*x1 - 15 == 0.0
True
>>> 8*x2**2 - 14*x2 - 15 == 0.0
True
>>> x1, x2 = quadratic(a=8, b=-14, c=-15)
>>> x1
2.5
>>> x2
-0.75
>>> 8*x1**2 - 14*x1 - 15 == 0.0
True
>>> 8*x2**2 - 14*x2 - 15 == 0.0
True
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
TestResults(failed=0, attempted=8)
>>> 2 ** 20
1048576
>>> import algebra
>>> help(algebra)
Help on module algebra:

NAME
    algebra

FILE
    /Users/raymond/Dropbox/Public/sj178/algebra.py

DESCRIPTION
    Fancy, expensive math package for people who
        have forgotten all algebra since the 7th grade.
    
    How binary floating point works:
    
        # The number 2.2 is entered as 22 / 10
        # but stored as 2476979795053773 / 1125899906842624
        # which is slightly off from 22 / 10
    
        # Instead of s == t, write abs(s-t) < 0.0000001
    
        # but stored as 2476979795053773 / 1125899906842624
        #                 53-bits            2 ** 50

FUNCTIONS
    area(radius)
        Compute the area of a circle
        
        >>> area(10)
        314.15700000000004
    
    area_triangle(base, height)
        Compute the area of a 2-D triangle given the base and height
        
        >>> area_triangle(20, 5)
        50
    
    average(seq)
        Compute the arithmetic mean of a sequence
        
        >>> average([2500, 2700, 2400, 2300, 2550, 2650, 2750, 2450, 2600, 2400])
        2530
    
    quadratic(a, b, c)
        Compute the two roots of the quadratic equation:
        
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

DATA
    pi = 3.14157


>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/algebra.py ==========
TestResults(failed=0, attempted=8)
>>> # 314.15926535898
>>> area(10)
314.15700000000004
>>> average([10, 20, 60])
30
>>> average([10, 20, 61])
30
>>> 91 / 3
30
>>> 91 / 3.90
23.333333333333332
>>> 91 / 3.0
30.333333333333332
>>> 
>>> 
>>> 
>>> area_triangle(5, 20)
50
>>> area_triangle(5, 7)
17
>>> 35 / 2
17
>>> 
>>> 
>>> area_triangle(-5, 20)

Traceback (most recent call last):
  File "<pyshell#325>", line 1, in <module>
    area_triangle(-5, 20)
  File "/Users/raymond/Dropbox/Public/sj178/algebra.py", line 58, in area_triangle
    raise RuntimeError('Complex numbers not supported in Kronecker product spaces')
RuntimeError: Complex numbers not supported in Kronecker product spaces
>>> quadratic(a=8, b=-14, c=-15)
(2.5, -0.75)
>>> quadratic(a=8, b=5, c=-15)
(1.0920128158902644, -1.7170128158902644)
>>> quadratic(a=8, b=5, c=15)

Traceback (most recent call last):
  File "<pyshell#328>", line 1, in <module>
    quadratic(a=8, b=5, c=15)
  File "/Users/raymond/Dropbox/Public/sj178/algebra.py", line 84, in quadratic
    radical = math.sqrt(b**2 - 4*a*c)
ValueError: math domain error
>>> math.sqrt(-5)

Traceback (most recent call last):
  File "<pyshell#329>", line 1, in <module>
    math.sqrt(-5)
ValueError: math domain error
>>> # 1:20
>>> # http://bit.ly/python-sj178c
>>> 
>>> 
>>> 
>>> 
>>> # http://bit.ly/python-sj178c
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/download.py ==========
================================= Source: http://10.155.72.249:8080/sj172/links.txt =================================
                                    Starting download at Mon Feb 26 13:25:23 2018                                    
304  Not Modified     http://10.155.72.249:8080/shared/IntermediatePython.pdf
304  Not Modified     http://10.155.72.249:8080/sj172/download.py
304  Not Modified     http://10.155.72.249:8080/sj172/links.txt
304  Not Modified     http://10.155.72.249:8080/sj172/autodiff.py
304  Not Modified     http://10.155.72.249:8080/sj172/day1.py
304  Not Modified     http://10.155.72.249:8080/sj172/algebra.py
304  Not Modified     http://10.155.72.249:8080/sj172/circuitous.py
304  Not Modified     http://10.155.72.249:8080/sj172/client_code.py
304  Not Modified     http://10.155.72.249:8080/sj172/day2.py
304  Not Modified     http://10.155.72.249:8080/sj172/day3.py
304  Not Modified     http://10.155.72.249:8080/sj172/decorator_intro.py
304  Not Modified     http://10.155.72.249:8080/sj172/clean_circuitous.py
304  Not Modified     http://10.155.72.249:8080/sj172/multithreading_demo.py
304  Not Modified     http://10.155.72.249:8080/sj172/lannisters.html
304  Not Modified     http://10.155.72.249:8080/sj172/templating_demo.py
304  Not Modified     http://10.155.72.249:8080/sj172/day4.py
304  Not Modified     http://10.155.72.249:8080/sj172/hettingers.dot
304  Not Modified     http://10.155.72.249:8080/sj172/hettingers.svg
304  Not Modified     http://10.155.72.249:8080/sj172/subprocess_demo.py
304  Not Modified     http://10.155.72.249:8080/sj172/monkey_patching.py
304  Not Modified     http://10.155.72.249:8080/sj172/cisco_training.db
304  Not Modified     http://10.155.72.249:8080/sj172/sqlite_demo.py
304  Not Modified     http://10.155.72.249:8080/sj172/sqlite_demo.py
304  Not Modified     http://10.155.72.249:8080/sj172/rest_api_server.py
304  Not Modified     http://10.155.72.249:8080/sj172/links.txt
304  Not Modified     http://10.155.72.249:8080/shared/PythonTips.pdf
304  Not Modified     http://10.155.72.249:8080/shared/PythonAwesome.pdf
304  Not Modified     http://10.155.72.249:8080/shared/pexpect.py
304  Not Modified     http://10.155.72.249:8080/shared/big.txt
304  Not Modified     http://10.155.72.249:8080/shared/spelling.py
304  Not Modified     http://10.155.72.249:8080/shared/mpl_demo.py
304  Not Modified     http://10.155.72.249:8080/shared/itty.py
304  Not Modified     http://10.155.72.249:8080/shared/bottle.py
304  Not Modified     http://10.155.72.249:8080/shared/lru_cache.py
304  Not Modified     http://10.155.72.249:8080/shared/quadratic.tpl
304  Not Modified     http://10.155.72.249:8080/shared/graphviz.tpl
304  Not Modified     http://10.155.72.249:8080/shared/mytwitter.zip
304  Not Modified     http://10.155.72.249:8080/shared/__init__.py
304  Not Modified     http://10.155.72.249:8080/shared/hamlet.txt
304  Not Modified     http://10.155.72.249:8080/shared/common_passwords.txt
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/download.py ==========
================================= Source: http://10.155.72.249:8080/sj178/links.txt =================================
                                    Starting download at Mon Feb 26 13:25:42 2018                                    
304  Not Modified     http://10.155.72.249:8080/shared/IntermediatePython.pdf
304  Not Modified     http://10.155.72.249:8080/shared/PythonTips.pdf
304  Not Modified     http://10.155.72.249:8080/shared/PythonAwesome.pdf
304  Not Modified     http://10.155.72.249:8080/shared/pexpect.py
304  Not Modified     http://10.155.72.249:8080/shared/big.txt
304  Not Modified     http://10.155.72.249:8080/shared/spelling.py
304  Not Modified     http://10.155.72.249:8080/shared/mpl_demo.py
304  Not Modified     http://10.155.72.249:8080/shared/itty.py
304  Not Modified     http://10.155.72.249:8080/shared/bottle.py
304  Not Modified     http://10.155.72.249:8080/shared/lru_cache.py
304  Not Modified     http://10.155.72.249:8080/shared/quadratic.tpl
304  Not Modified     http://10.155.72.249:8080/shared/graphviz.tpl
304  Not Modified     http://10.155.72.249:8080/shared/mytwitter.zip
304  Not Modified     http://10.155.72.249:8080/shared/__init__.py
304  Not Modified     http://10.155.72.249:8080/shared/hamlet.txt
304  Not Modified     http://10.155.72.249:8080/shared/common_passwords.txt
200* OK               http://10.155.72.249:8080/sj178/algebra.py              --> notes2/algebra.py         (updated) 
200* OK               http://10.155.72.249:8080/sj178/day1.py                 --> notes2/day1.py            (updated) 
200* OK               http://10.155.72.249:8080/sj178/links.txt               --> notes2/links.txt          (updated) 
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/download.py ==========
================================= Source: http://10.155.72.249:8080/sj178/links.txt =================================
                                    Starting download at Mon Feb 26 13:26:33 2018                                    
304  Not Modified     http://10.155.72.249:8080/shared/IntermediatePython.pdf
304  Not Modified     http://10.155.72.249:8080/sj178/links.txt
304  Not Modified     http://10.155.72.249:8080/sj178/day1.py
304  Not Modified     http://10.155.72.249:8080/shared/PythonTips.pdf
304  Not Modified     http://10.155.72.249:8080/sj178/algebra.py
304  Not Modified     http://10.155.72.249:8080/shared/PythonAwesome.pdf
304  Not Modified     http://10.155.72.249:8080/shared/pexpect.py
304  Not Modified     http://10.155.72.249:8080/shared/spelling.py
304  Not Modified     http://10.155.72.249:8080/shared/mpl_demo.py
304  Not Modified     http://10.155.72.249:8080/shared/big.txt
304  Not Modified     http://10.155.72.249:8080/shared/itty.py
304  Not Modified     http://10.155.72.249:8080/shared/bottle.py
304  Not Modified     http://10.155.72.249:8080/shared/lru_cache.py
304  Not Modified     http://10.155.72.249:8080/shared/quadratic.tpl
304  Not Modified     http://10.155.72.249:8080/shared/mytwitter.zip
304  Not Modified     http://10.155.72.249:8080/shared/graphviz.tpl
304  Not Modified     http://10.155.72.249:8080/shared/__init__.py
304  Not Modified     http://10.155.72.249:8080/shared/hamlet.txt
304  Not Modified     http://10.155.72.249:8080/shared/common_passwords.txt
>>> print 'hello world'
hello world
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
0
>>> # 0 is happy.   1..n ways to be unhappy
>>> 
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
0
tcp:
	0 packet sent
		0 data packet (0 byte)
		0 data packet (0 byte) retransmitted
		0 resend initiated by MTU discovery
		0 ack-only packet (0 delayed)
		0 URG only packet
		0 window probe packet
		0 window update packet
		0 control packet
		0 data packet sent after flow control
		0 checksummed in software
			0 segment (0 byte) over IPv4
			0 segment (0 byte) over IPv6
	0 packet received
		0 ack (for 0 byte)
		0 duplicate ack
		0 ack for unsent data
		0 packet (0 byte) received in-sequence
		0 completely duplicate packet (0 byte)
		0 old duplicate packet
		0 received packet dropped due to low memory
		0 packet with some dup. data (0 byte duped)
		0 out-of-order packet (0 byte)
		0 packet (0 byte) of data after window
		0 window probe
		0 window update packet
		0 packet received after close
		0 bad reset
		0 discarded for bad checksum
		0 checksummed in software
			0 segment (0 byte) over IPv4
			0 segment (0 byte) over IPv6
		0 discarded for bad header offset field
		0 discarded because packet too short
	0 connection request
	0 connection accept
	0 bad connection attempt
	0 listen queue overflow
	0 connection established (including accepts)
	0 connection closed (including 0 drop)
		0 connection updated cached RTT on close
		0 connection updated cached RTT variance on close
		0 connection updated cached ssthresh on close
	0 embryonic connection dropped
	0 segment updated rtt (of 0 attempt)
	0 retransmit timeout
		0 connection dropped by rexmit timeout
		0 connection dropped after retransmitting FIN
	0 persist timeout
		0 connection dropped by persist timeout
	0 keepalive timeout
		0 keepalive probe sent
		0 connection dropped by keepalive
	0 correct ACK header prediction
	0 correct data packet header prediction
	0 SACK recovery episode
	0 segment rexmit in SACK recovery episodes
	0 byte rexmit in SACK recovery episodes
	0 SACK option (SACK blocks) received
	0 SACK option (SACK blocks) sent
	0 SACK scoreboard overflow
	0 LRO coalesced packet
		0 time LRO flow table was full
		0 collision in LRO flow table
		0 time LRO coalesced 2 packets
		0 time LRO coalesced 3 or 4 packets
		0 time LRO coalesced 5 or more packets
	0 limited transmit done
	0 early retransmit done
	0 time cumulative ack advanced along with SACK
	0 probe timeout
		0 time retransmit timeout triggered after probe
		0 time probe packets were sent for an interface
		0 time couldn't send probe packets for an interface
		0 time fast recovery after tail loss
		0 time recovered last packet 
		0 SACK based rescue retransmit
	0 client connection attempted to negotiate ECN
		0 client connection successfully negotiated ECN
		0 time graceful fallback to Non-ECN connection
		0 time lost ECN negotiating SYN, followed by retransmission
		0 server connection attempted to negotiate ECN
		0 server connection successfully negotiated ECN
		0 time lost ECN negotiating SYN-ACK, followed by retransmission
		0 time received congestion experienced (CE) notification
		0 time CWR was sent in response to ECE
		0 time sent ECE notification
		0 connection received CE atleast once
		0 connection received ECE atleast once
		0 connection using ECN have seen packet loss but no CE
		0 connection using ECN have seen packet loss and CE
		0 connection using ECN received CE but no packet loss
		0 connection fell back to non-ECN due to SYN-loss
		0 connection fell back to non-ECN due to reordering
		0 connection fell back to non-ECN due to excessive CE-markings
	0 time packet reordering was detected on a connection
		0 time transmitted packets were reordered
		0 time fast recovery was delayed to handle reordering
		0 time retransmission was avoided by delaying recovery
		0 retransmission not needed 
	0 time DSACK option was sent
		0 time DSACK option was received
		0 time DSACK was disabled on a connection
		0 time recovered from bad retransmission using DSACK
		0 time ignored DSACK due to ack loss
		0 time ignored old DSACK options
	0 time PMTU Blackhole detection, size reverted
	0 connection were dropped after long sleep
	0 time a TFO-cookie has been announced
	0 SYN with data and a valid TFO-cookie have been received
	0 SYN with TFO-cookie-request received
	0 time an invalid TFO-cookie has been received
	0 time we requested a TFO-cookie
		0 time the peer announced a TFO-cookie
	0 time we combined SYN with data and a TFO-cookie
		0 time our SYN with data has been acknowledged
	0 time a connection-attempt with TFO fell back to regular TCP
	0 time a TFO-connection blackhole'd
	0 time maximum segment size was changed to default
	0 time maximum segment size was changed to medium
	0 time maximum segment size was changed to low
	0 timer drift less or equal to 1 ms
	0 timer drift less or equal to 10 ms
	0 timer drift less or equal to 20 ms
	0 timer drift less or equal to 50 ms
	0 timer drift less or equal to 100 ms
	0 timer drift less or equal to 200 ms
	0 timer drift less or equal to 500 ms
	0 timer drift less or equal to 1000 ms
	0 timer drift greater than to 1000 ms
udp:
	498175 datagrams received
		0 with incomplete header
		0 with bad data length field
		0 with bad checksum
		54 with no checksum
		467136 checksummed in software
			233980 datagrams (74779282 bytes) over IPv4
			233156 datagrams (105071742 bytes) over IPv6
		5342 dropped due to no socket
		3618 broadcast/multicast datagrams undelivered
		0 time multicast source filter matched
		1 dropped due to full socket buffers
		0 not for hashed pcb
		489214 delivered
	141857 datagrams output
		148789 checksummed in software
			55027 datagrams (11676922 bytes) over IPv4
			93762 datagrams (20628874 bytes) over IPv6
icmp:
	1398 calls to icmp_error
	0 error not generated 'cuz old message was icmp
	Output histogram:
		echo reply: 38
		destination unreachable: 1398
	0 message with bad code fields
	0 message < minimum length
	1 bad checksum
	0 message with bad length
	0 multicast echo requests ignored
	0 multicast timestamp requests ignored
	Input histogram:
		destination unreachable: 2007
		echo: 38
		router advertisement: 147
	38 message responses generated
	ICMP address mask responses are disabled
igmp:
	1635 messages received
	0 message received with too few bytes
	0 message received with wrong TTL
	0 message received with bad checksum
	564 V1/V2 membership queries received
	287 V3 membership queries received
	0 membership queries received with invalid field(s)
	833 general queries received
	18 group queries received
	0 group-source queries received
	0 group-source queries dropped
	784 membership reports received
	0 membership report received with invalid field(s)
	784 membership reports received for groups to which we belong
	0 V3 report received without Router Alert
	889 membership reports sent
ipsec:
	0 inbound packet processed successfully
	0 inbound packet violated process security policy
	0 inbound packet with no SA available
	0 invalid inbound packet
	0 inbound packet failed due to insufficient memory
	0 inbound packet failed getting SPI
	0 inbound packet failed on AH replay check
	0 inbound packet failed on ESP replay check
	0 inbound packet considered authentic
	0 inbound packet failed on authentication
	0 outbound packet processed successfully
	0 outbound packet violated process security policy
	0 outbound packet with no SA available
	0 invalid outbound packet
	0 outbound packet failed due to insufficient memory
	0 outbound packet with no route
arp:
	1505 broadast ARP requests sent
	9 unicast ARP requests sent
	3318 ARP replies sent
	0 ARP announcement sent
	11628 ARP requests received
	1253 ARP replies received
	12883 total ARP packets received
	0 ARP conflict probe sent
	0 invalid ARP resolve request
	0 total packet dropped due to lack of memory
	0 total packet held awaiting ARP reply
	43 total packets dropped due to no ARP entry
	378 total packets dropped during ARP entry removal
	1391 ARP entries timed out
	0 Duplicate IP seen
mptcp:
	0 data packet sent
	0 data byte sent
	0 data packet received
	0 data byte received
	0 packet with an invalid MPCAP option
	0 packet with an invalid MPJOIN option
	0 time primary subflow fell back to TCP
	0 time secondary subflow fell back to TCP
	0 DSS option drop
	0 other invalid MPTCP option
	0 time the MPTCP subflow window was reduced
	0 bad DSS checksum
	0 time received out of order data 
	0 subflow switch
	0 subflow switch due to advisory
	0 subflow switch due to rtt
	0 subflow switch due to rto
	0 subflow switch due to peer
	0 number of subflow probe
ip6:
	736662 total packets received
		0 with size smaller than minimum
		0 with data size < data length
		0 with data size > data length
			0 packet forced to software checksum
		0 with bad options
		168 with incorrect version number
		6 fragments received
			0 dropped (dup or out of space)
			0 dropped after timeout
			0 exceeded limit
			3 reassembled ok
			0 atomic fragments received
		663922 packets for this host
		0 packet forwarded
		32229 packets not forwardable
		0 redirect sent
		32172 multicast packets which we don't join
		0 packet whose headers are not continuous
		0 tunneling packet that can't find gif
		0 packet discarded due to too may headers
		0 forward cache hit
		0 forward cache miss
		0 packet dropped due to no bufs for control data
	340486 packets sent from this host
		0 packet sent with fabricated ip header
		0 output packet dropped due to no bufs, etc.
		2291 output packets discarded due to no route
		0 output datagram fragmented
		0 fragment created
		0 datagram that can't be fragmented
		0 packet that violated scope rules
		0 packet dropped due to NECP policy
	Input histogram:
		hop by hop: 5598
		TCP: 421429
		UDP: 267291
		fragment: 6
		ICMP6: 41281
		PIM: 889
	Mbuf statistics:
		1787 one mbuf
		two or more mbuf:
			lo0= 10270
			utun1= 12
		724593 one ext mbuf
		0 two or more ext mbuf
		0 failure of source address selection
		source addresses on an outgoing I/F
			0 addresses scope=0
			0 node-local
			0 link-local
			0 addresses scope=3
			0 addresses scope=4
			0 site-local
			0 addresses scope=6
			0 addresses scope=7
			0 addresses scope=8
			0 addresses scope=9
			0 addresses scope=a
			0 addresses scope=b
			0 addresses scope=c
			0 addresses scope=d
			0 global
			0 addresses scope=f
		source addresses on a non-outgoing I/F
			0 addresses scope=0
			0 node-local
			0 link-local
			0 addresses scope=3
			0 addresses scope=4
			0 site-local
			0 addresses scope=6
			0 addresses scope=7
			0 addresses scope=8
			0 addresses scope=9
			0 addresses scope=a
			0 addresses scope=b
			0 addresses scope=c
			0 addresses scope=d
			0 global
			0 addresses scope=f
		source addresses of same scope
			0 addresses scope=0
			0 node-local
			0 link-local
			0 addresses scope=3
			0 addresses scope=4
			0 site-local
			0 addresses scope=6
			0 addresses scope=7
			0 addresses scope=8
			0 addresses scope=9
			0 addresses scope=a
			0 addresses scope=b
			0 addresses scope=c
			0 addresses scope=d
			0 global
			0 addresses scope=f
		source addresses of a different scope
			0 addresses scope=0
			0 node-local
			0 link-local
			0 addresses scope=3
			0 addresses scope=4
			0 site-local
			0 addresses scope=6
			0 addresses scope=7
			0 addresses scope=8
			0 addresses scope=9
			0 addresses scope=a
			0 addresses scope=b
			0 addresses scope=c
			0 addresses scope=d
			0 global
			0 addresses scope=f
		deprecated source addresses
			0 addresses scope=0
			0 node-local
			0 link-local
			0 addresses scope=3
			0 addresses scope=4
			0 site-local
			0 addresses scope=6
			0 addresses scope=7
			0 addresses scope=8
			0 addresses scope=9
			0 addresses scope=a
			0 addresses scope=b
			0 addresses scope=c
			0 addresses scope=d
			0 global
			0 addresses scope=f
		source address selection
			18047 rules default
			0 rule prefer same address
			4776 rules prefer appropriate scope
			0 rule avoid deprecated addresses
			0 rule prefer home addresses
			0 rule prefer outgoing interface
			10 rules prefer matching label
			47351 rules prefer temporary addresses
			0 rule prefer addresses on alive interfaces
			0 rule use longest matching prefix
		0 duplicate address detection collision
		0 duplicate address detection NS loop
		0 time ignored source on secondary expensive I/F
icmp6:
	1720 calls to icmp_error
	0 error not generated because old message was icmp error or so
	0 error not generated because rate limitation
	Output histogram:
		unreach: 1720
		MLDv1 listener report: 77
		MLDv1 listener done: 11
		router solicitation: 123
		neighbor solicitation: 5168
		neighbor advertisement: 4402
		MLDv2 listener report: 1119
	0 message with bad code fields
	0 message < minimum length
	0 bad checksum
	0 message with bad length
	Input histogram:
		unreach: 148
		multicast listener query: 1996
		router advertisement: 29546
		neighbor solicitation: 4402
		neighbor advertisement: 4320
	Histogram of error messages to be generated:
		0 no route
		0 administratively prohibited
		0 beyond scope
		148 address unreachable
		1572 port unreachable
		0 packet too big
		0 time exceed transit
		0 time exceed reassembly
		0 erroneous header field
		0 unrecognized next header
		0 unrecognized option
		0 redirect
		0 unknown
	0 message response generated
	0 message with too many ND options
	0 message with bad ND options
	0 bad neighbor solicitation message
	0 bad neighbor advertisement message
	0 bad router solicitation message
	0 bad router advertisement message
	0 bad redirect message
	0 path MTU change
	0 dropped fragmented NDP message
ipsec6:
	0 inbound packet processed successfully
	0 inbound packet violated process security policy
	0 inbound packet with no SA available
	0 invalid inbound packet
	0 inbound packet failed due to insufficient memory
	0 inbound packet failed getting SPI
	0 inbound packet failed on AH replay check
	0 inbound packet failed on ESP replay check
	0 inbound packet considered authentic
	0 inbound packet failed on authentication
	0 outbound packet processed successfully
	0 outbound packet violated process security policy
	0 outbound packet with no SA available
	0 invalid outbound packet
	0 outbound packet failed due to insufficient memory
	0 outbound packet with no route
rip6:
	0 message received
	0 checksum calculation on inbound
	0 message with bad checksum
	0 message dropped due to no socket
	0 multicast message dropped due to no socket
	0 message dropped due to full socket buffers
	0 delivered
	0 datagram output
pfkey:
	0 request sent to userland
	0 byte sent to userland
	0 message with invalid length field
	0 message with invalid version field
	0 message with invalid message type field
	0 message too short
	0 message with memory allocation failure
	0 message with duplicate extension
	0 message with invalid extension type
	0 message with invalid sa type
	0 message with invalid address extension
	0 request sent from userland
	0 byte sent from userland
	0 message toward single socket
	0 message toward all sockets
	0 message toward registered sockets
	0 message with memory allocation failure
kevt:
	24 current kernel control sockets
	18912 kernel control generation count
	0 bad vendor failure
	7271 message too big failures
	0 out of memory failure
	0 message dropped due to full socket buffers
	272345 messages posted
kctl:
	0 total kernel control module registered
	12 current kernel control modules registered
	55 current kernel control sockets
	1111 kernel control generation count
	577 connection attempts
	0 connection failure
	35 send failures
	0 send list failure
	0 enqueue failure
	0 packet dropped due to full socket buffers
xbkidle:
	1 max per process
	600 maximum time (seconds)
	131072 high water mark
	0 socket option not supported failure
	0 too many sockets failure
	0 total socket requested OK
	0 extended bk idle socket
	0 no cellular failure
	0 no time failures
	0 forced defunct socket
	0 resumed socket
	0 timeout expired failure
	0 timer rescheduled
	0 no delegated failure
net_api:
	2 interface filters currently attached
	2 interface filters attached since boot
	2 interface filters attached since boot by OS
	0 IP filter currently attached
	0 IP filter attached since boot
	0 IP filter attached since boot by OS
	4 socket filters currently attached
	4 socket filters attached since boot
	4 socket filters attached since boot by OS
	325381 sockets allocated since boot
	75 sockets allocated in-kernel since boot
	75 sockets allocated in-kernel by OS
	2458 sockets with NECP client UUID since boot
	103899 local domain sockets allocated since boot
	1199 route domain sockets allocated since boot
	124275 inet domain sockets allocated since boot
	59676 inet6 domain sockets allocated since boot
	10045 system domain sockets allocated since boot
	0 multipath domain socket allocated since boot
	0 key domain socket allocated since boot
	5 ndrv domain sockets allocated since boot
	0 other domains socket allocated since boot
	15529 IPv4 stream sockets created since boot
	108746 IPv4 datagram sockets created since boot
	10291 IPv4 datagram sockets connected
	37925 IPv4 DNS sockets
	102061 IPv4 datagram sockets without data
	7532 IPv6 stream sockets created since boot
	52144 IPv6 datagram sockets created since boot
	34768 IPv6 datagram sockets connected
	0 IPv6 DNS socket
	28156 IPv6 datagram sockets without data
	1115 socket multicast joins since boot
	1115 socket multicast joins since boot by OS
	0 IPv4 stream nexus flow added since boot
	0 IPv4 datagram nexus flow added since boot
	0 IPv6 stream nexus flow added since boot
	0 IPv6 datagram nexus flow added since boot
	12 interfaces currently allocated
	12 interfaces allocated since boot
	12 interfaces currently allocated by OS
	12 extended interfaces allocated since boot by OS
	2 PF addrule operations since boot
	0 PF addrule operation since boot by OS
	0 vmnet start since boot

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
0
TCP:
	0 PACKET SENT
		0 DATA PACKET (0 BYTE)
		0 DATA PACKET (0 BYTE) RETRANSMITTED
		0 RESEND INITIATED BY MTU DISCOVERY
		0 ACK-ONLY PACKET (0 DELAYED)
		0 URG ONLY PACKET
		0 WINDOW PROBE PACKET
		0 WINDOW UPDATE PACKET
		0 CONTROL PACKET
		0 DATA PACKET SENT AFTER FLOW CONTROL
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
	0 PACKET RECEIVED
		0 ACK (FOR 0 BYTE)
		0 DUPLICATE ACK
		0 ACK FOR UNSENT DATA
		0 PACKET (0 BYTE) RECEIVED IN-SEQUENCE
		0 COMPLETELY DUPLICATE PACKET (0 BYTE)
		0 OLD DUPLICATE PACKET
		0 RECEIVED PACKET DROPPED DUE TO LOW MEMORY
		0 PACKET WITH SOME DUP. DATA (0 BYTE DUPED)
		0 OUT-OF-ORDER PACKET (0 BYTE)
		0 PACKET (0 BYTE) OF DATA AFTER WINDOW
		0 WINDOW PROBE
		0 WINDOW UPDATE PACKET
		0 PACKET RECEIVED AFTER CLOSE
		0 BAD RESET
		0 DISCARDED FOR BAD CHECKSUM
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
		0 DISCARDED FOR BAD HEADER OFFSET FIELD
		0 DISCARDED BECAUSE PACKET TOO SHORT
	0 CONNECTION REQUEST
	0 CONNECTION ACCEPT
	0 BAD CONNECTION ATTEMPT
	0 LISTEN QUEUE OVERFLOW
	0 CONNECTION ESTABLISHED (INCLUDING ACCEPTS)
	0 CONNECTION CLOSED (INCLUDING 0 DROP)
		0 CONNECTION UPDATED CACHED RTT ON CLOSE
		0 CONNECTION UPDATED CACHED RTT VARIANCE ON CLOSE
		0 CONNECTION UPDATED CACHED SSTHRESH ON CLOSE
	0 EMBRYONIC CONNECTION DROPPED
	0 SEGMENT UPDATED RTT (OF 0 ATTEMPT)
	0 RETRANSMIT TIMEOUT
		0 CONNECTION DROPPED BY REXMIT TIMEOUT
		0 CONNECTION DROPPED AFTER RETRANSMITTING FIN
	0 PERSIST TIMEOUT
		0 CONNECTION DROPPED BY PERSIST TIMEOUT
	0 KEEPALIVE TIMEOUT
		0 KEEPALIVE PROBE SENT
		0 CONNECTION DROPPED BY KEEPALIVE
	0 CORRECT ACK HEADER PREDICTION
	0 CORRECT DATA PACKET HEADER PREDICTION
	0 SACK RECOVERY EPISODE
	0 SEGMENT REXMIT IN SACK RECOVERY EPISODES
	0 BYTE REXMIT IN SACK RECOVERY EPISODES
	0 SACK OPTION (SACK BLOCKS) RECEIVED
	0 SACK OPTION (SACK BLOCKS) SENT
	0 SACK SCOREBOARD OVERFLOW
	0 LRO COALESCED PACKET
		0 TIME LRO FLOW TABLE WAS FULL
		0 COLLISION IN LRO FLOW TABLE
		0 TIME LRO COALESCED 2 PACKETS
		0 TIME LRO COALESCED 3 OR 4 PACKETS
		0 TIME LRO COALESCED 5 OR MORE PACKETS
	0 LIMITED TRANSMIT DONE
	0 EARLY RETRANSMIT DONE
	0 TIME CUMULATIVE ACK ADVANCED ALONG WITH SACK
	0 PROBE TIMEOUT
		0 TIME RETRANSMIT TIMEOUT TRIGGERED AFTER PROBE
		0 TIME PROBE PACKETS WERE SENT FOR AN INTERFACE
		0 TIME COULDN'T SEND PROBE PACKETS FOR AN INTERFACE
		0 TIME FAST RECOVERY AFTER TAIL LOSS
		0 TIME RECOVERED LAST PACKET 
		0 SACK BASED RESCUE RETRANSMIT
	0 CLIENT CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 CLIENT CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME GRACEFUL FALLBACK TO NON-ECN CONNECTION
		0 TIME LOST ECN NEGOTIATING SYN, FOLLOWED BY RETRANSMISSION
		0 SERVER CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 SERVER CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME LOST ECN NEGOTIATING SYN-ACK, FOLLOWED BY RETRANSMISSION
		0 TIME RECEIVED CONGESTION EXPERIENCED (CE) NOTIFICATION
		0 TIME CWR WAS SENT IN RESPONSE TO ECE
		0 TIME SENT ECE NOTIFICATION
		0 CONNECTION RECEIVED CE ATLEAST ONCE
		0 CONNECTION RECEIVED ECE ATLEAST ONCE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS BUT NO CE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS AND CE
		0 CONNECTION USING ECN RECEIVED CE BUT NO PACKET LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO SYN-LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO REORDERING
		0 CONNECTION FELL BACK TO NON-ECN DUE TO EXCESSIVE CE-MARKINGS
	0 TIME PACKET REORDERING WAS DETECTED ON A CONNECTION
		0 TIME TRANSMITTED PACKETS WERE REORDERED
		0 TIME FAST RECOVERY WAS DELAYED TO HANDLE REORDERING
		0 TIME RETRANSMISSION WAS AVOIDED BY DELAYING RECOVERY
		0 RETRANSMISSION NOT NEEDED 
	0 TIME DSACK OPTION WAS SENT
		0 TIME DSACK OPTION WAS RECEIVED
		0 TIME DSACK WAS DISABLED ON A CONNECTION
		0 TIME RECOVERED FROM BAD RETRANSMISSION USING DSACK
		0 TIME IGNORED DSACK DUE TO ACK LOSS
		0 TIME IGNORED OLD DSACK OPTIONS
	0 TIME PMTU BLACKHOLE DETECTION, SIZE REVERTED
	0 CONNECTION WERE DROPPED AFTER LONG SLEEP
	0 TIME A TFO-COOKIE HAS BEEN ANNOUNCED
	0 SYN WITH DATA AND A VALID TFO-COOKIE HAVE BEEN RECEIVED
	0 SYN WITH TFO-COOKIE-REQUEST RECEIVED
	0 TIME AN INVALID TFO-COOKIE HAS BEEN RECEIVED
	0 TIME WE REQUESTED A TFO-COOKIE
		0 TIME THE PEER ANNOUNCED A TFO-COOKIE
	0 TIME WE COMBINED SYN WITH DATA AND A TFO-COOKIE
		0 TIME OUR SYN WITH DATA HAS BEEN ACKNOWLEDGED
	0 TIME A CONNECTION-ATTEMPT WITH TFO FELL BACK TO REGULAR TCP
	0 TIME A TFO-CONNECTION BLACKHOLE'D
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO DEFAULT
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO MEDIUM
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO LOW
	0 TIMER DRIFT LESS OR EQUAL TO 1 MS
	0 TIMER DRIFT LESS OR EQUAL TO 10 MS
	0 TIMER DRIFT LESS OR EQUAL TO 20 MS
	0 TIMER DRIFT LESS OR EQUAL TO 50 MS
	0 TIMER DRIFT LESS OR EQUAL TO 100 MS
	0 TIMER DRIFT LESS OR EQUAL TO 200 MS
	0 TIMER DRIFT LESS OR EQUAL TO 500 MS
	0 TIMER DRIFT LESS OR EQUAL TO 1000 MS
	0 TIMER DRIFT GREATER THAN TO 1000 MS
UDP:
	499912 DATAGRAMS RECEIVED
		0 WITH INCOMPLETE HEADER
		0 WITH BAD DATA LENGTH FIELD
		0 WITH BAD CHECKSUM
		54 WITH NO CHECKSUM
		468835 CHECKSUMMED IN SOFTWARE
			234926 DATAGRAMS (75053831 BYTES) OVER IPV4
			233909 DATAGRAMS (105296780 BYTES) OVER IPV6
		5343 DROPPED DUE TO NO SOCKET
		3618 BROADCAST/MULTICAST DATAGRAMS UNDELIVERED
		0 TIME MULTICAST SOURCE FILTER MATCHED
		1 DROPPED DUE TO FULL SOCKET BUFFERS
		0 NOT FOR HASHED PCB
		490950 DELIVERED
	141948 DATAGRAMS OUTPUT
		148897 CHECKSUMMED IN SOFTWARE
			55092 DATAGRAMS (11693791 BYTES) OVER IPV4
			93805 DATAGRAMS (20639376 BYTES) OVER IPV6
ICMP:
	1398 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED 'CUZ OLD MESSAGE WAS ICMP
	OUTPUT HISTOGRAM:
		ECHO REPLY: 38
		DESTINATION UNREACHABLE: 1398
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	1 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	0 MULTICAST ECHO REQUESTS IGNORED
	0 MULTICAST TIMESTAMP REQUESTS IGNORED
	INPUT HISTOGRAM:
		DESTINATION UNREACHABLE: 2007
		ECHO: 38
		ROUTER ADVERTISEMENT: 147
	38 MESSAGE RESPONSES GENERATED
	ICMP ADDRESS MASK RESPONSES ARE DISABLED
IGMP:
	1636 MESSAGES RECEIVED
	0 MESSAGE RECEIVED WITH TOO FEW BYTES
	0 MESSAGE RECEIVED WITH WRONG TTL
	0 MESSAGE RECEIVED WITH BAD CHECKSUM
	565 V1/V2 MEMBERSHIP QUERIES RECEIVED
	287 V3 MEMBERSHIP QUERIES RECEIVED
	0 MEMBERSHIP QUERIES RECEIVED WITH INVALID FIELD(S)
	834 GENERAL QUERIES RECEIVED
	18 GROUP QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES DROPPED
	784 MEMBERSHIP REPORTS RECEIVED
	0 MEMBERSHIP REPORT RECEIVED WITH INVALID FIELD(S)
	784 MEMBERSHIP REPORTS RECEIVED FOR GROUPS TO WHICH WE BELONG
	0 V3 REPORT RECEIVED WITHOUT ROUTER ALERT
	890 MEMBERSHIP REPORTS SENT
IPSEC:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
ARP:
	1513 BROADAST ARP REQUESTS SENT
	9 UNICAST ARP REQUESTS SENT
	3318 ARP REPLIES SENT
	0 ARP ANNOUNCEMENT SENT
	11628 ARP REQUESTS RECEIVED
	1261 ARP REPLIES RECEIVED
	12891 TOTAL ARP PACKETS RECEIVED
	0 ARP CONFLICT PROBE SENT
	0 INVALID ARP RESOLVE REQUEST
	0 TOTAL PACKET DROPPED DUE TO LACK OF MEMORY
	0 TOTAL PACKET HELD AWAITING ARP REPLY
	43 TOTAL PACKETS DROPPED DUE TO NO ARP ENTRY
	378 TOTAL PACKETS DROPPED DURING ARP ENTRY REMOVAL
	1391 ARP ENTRIES TIMED OUT
	0 DUPLICATE IP SEEN
MPTCP:
	0 DATA PACKET SENT
	0 DATA BYTE SENT
	0 DATA PACKET RECEIVED
	0 DATA BYTE RECEIVED
	0 PACKET WITH AN INVALID MPCAP OPTION
	0 PACKET WITH AN INVALID MPJOIN OPTION
	0 TIME PRIMARY SUBFLOW FELL BACK TO TCP
	0 TIME SECONDARY SUBFLOW FELL BACK TO TCP
	0 DSS OPTION DROP
	0 OTHER INVALID MPTCP OPTION
	0 TIME THE MPTCP SUBFLOW WINDOW WAS REDUCED
	0 BAD DSS CHECKSUM
	0 TIME RECEIVED OUT OF ORDER DATA 
	0 SUBFLOW SWITCH
	0 SUBFLOW SWITCH DUE TO ADVISORY
	0 SUBFLOW SWITCH DUE TO RTT
	0 SUBFLOW SWITCH DUE TO RTO
	0 SUBFLOW SWITCH DUE TO PEER
	0 NUMBER OF SUBFLOW PROBE
IP6:
	737664 TOTAL PACKETS RECEIVED
		0 WITH SIZE SMALLER THAN MINIMUM
		0 WITH DATA SIZE < DATA LENGTH
		0 WITH DATA SIZE > DATA LENGTH
			0 PACKET FORCED TO SOFTWARE CHECKSUM
		0 WITH BAD OPTIONS
		168 WITH INCORRECT VERSION NUMBER
		6 FRAGMENTS RECEIVED
			0 DROPPED (DUP OR OUT OF SPACE)
			0 DROPPED AFTER TIMEOUT
			0 EXCEEDED LIMIT
			3 REASSEMBLED OK
			0 ATOMIC FRAGMENTS RECEIVED
		664819 PACKETS FOR THIS HOST
		0 PACKET FORWARDED
		32301 PACKETS NOT FORWARDABLE
		0 REDIRECT SENT
		32244 MULTICAST PACKETS WHICH WE DON'T JOIN
		0 PACKET WHOSE HEADERS ARE NOT CONTINUOUS
		0 TUNNELING PACKET THAT CAN'T FIND GIF
		0 PACKET DISCARDED DUE TO TOO MAY HEADERS
		0 FORWARD CACHE HIT
		0 FORWARD CACHE MISS
		0 PACKET DROPPED DUE TO NO BUFS FOR CONTROL DATA
	340658 PACKETS SENT FROM THIS HOST
		0 PACKET SENT WITH FABRICATED IP HEADER
		0 OUTPUT PACKET DROPPED DUE TO NO BUFS, ETC.
		2291 OUTPUT PACKETS DISCARDED DUE TO NO ROUTE
		0 OUTPUT DATAGRAM FRAGMENTED
		0 FRAGMENT CREATED
		0 DATAGRAM THAT CAN'T BE FRAGMENTED
		0 PACKET THAT VIOLATED SCOPE RULES
		0 PACKET DROPPED DUE TO NECP POLICY
	INPUT HISTOGRAM:
		HOP BY HOP: 5600
		TCP: 421556
		UDP: 268127
		FRAGMENT: 6
		ICMP6: 41314
		PIM: 893
	MBUF STATISTICS:
		1787 ONE MBUF
		TWO OR MORE MBUF:
			LO0= 10287
			UTUN1= 12
		725578 ONE EXT MBUF
		0 TWO OR MORE EXT MBUF
		0 FAILURE OF SOURCE ADDRESS SELECTION
		SOURCE ADDRESSES ON AN OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES ON A NON-OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF SAME SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF A DIFFERENT SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		DEPRECATED SOURCE ADDRESSES
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESS SELECTION
			18067 RULES DEFAULT
			0 RULE PREFER SAME ADDRESS
			4796 RULES PREFER APPROPRIATE SCOPE
			0 RULE AVOID DEPRECATED ADDRESSES
			0 RULE PREFER HOME ADDRESSES
			0 RULE PREFER OUTGOING INTERFACE
			10 RULES PREFER MATCHING LABEL
			47351 RULES PREFER TEMPORARY ADDRESSES
			0 RULE PREFER ADDRESSES ON ALIVE INTERFACES
			0 RULE USE LONGEST MATCHING PREFIX
		0 DUPLICATE ADDRESS DETECTION COLLISION
		0 DUPLICATE ADDRESS DETECTION NS LOOP
		0 TIME IGNORED SOURCE ON SECONDARY EXPENSIVE I/F
ICMP6:
	1721 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED BECAUSE OLD MESSAGE WAS ICMP ERROR OR SO
	0 ERROR NOT GENERATED BECAUSE RATE LIMITATION
	OUTPUT HISTOGRAM:
		UNREACH: 1721
		MLDV1 LISTENER REPORT: 77
		MLDV1 LISTENER DONE: 11
		ROUTER SOLICITATION: 123
		NEIGHBOR SOLICITATION: 5170
		NEIGHBOR ADVERTISEMENT: 4402
		MLDV2 LISTENER REPORT: 1119
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	0 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	INPUT HISTOGRAM:
		UNREACH: 148
		MULTICAST LISTENER QUERY: 1996
		ROUTER ADVERTISEMENT: 29577
		NEIGHBOR SOLICITATION: 4402
		NEIGHBOR ADVERTISEMENT: 4322
	HISTOGRAM OF ERROR MESSAGES TO BE GENERATED:
		0 NO ROUTE
		0 ADMINISTRATIVELY PROHIBITED
		0 BEYOND SCOPE
		148 ADDRESS UNREACHABLE
		1573 PORT UNREACHABLE
		0 PACKET TOO BIG
		0 TIME EXCEED TRANSIT
		0 TIME EXCEED REASSEMBLY
		0 ERRONEOUS HEADER FIELD
		0 UNRECOGNIZED NEXT HEADER
		0 UNRECOGNIZED OPTION
		0 REDIRECT
		0 UNKNOWN
	0 MESSAGE RESPONSE GENERATED
	0 MESSAGE WITH TOO MANY ND OPTIONS
	0 MESSAGE WITH BAD ND OPTIONS
	0 BAD NEIGHBOR SOLICITATION MESSAGE
	0 BAD NEIGHBOR ADVERTISEMENT MESSAGE
	0 BAD ROUTER SOLICITATION MESSAGE
	0 BAD ROUTER ADVERTISEMENT MESSAGE
	0 BAD REDIRECT MESSAGE
	0 PATH MTU CHANGE
	0 DROPPED FRAGMENTED NDP MESSAGE
IPSEC6:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
RIP6:
	0 MESSAGE RECEIVED
	0 CHECKSUM CALCULATION ON INBOUND
	0 MESSAGE WITH BAD CHECKSUM
	0 MESSAGE DROPPED DUE TO NO SOCKET
	0 MULTICAST MESSAGE DROPPED DUE TO NO SOCKET
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	0 DELIVERED
	0 DATAGRAM OUTPUT
PFKEY:
	0 REQUEST SENT TO USERLAND
	0 BYTE SENT TO USERLAND
	0 MESSAGE WITH INVALID LENGTH FIELD
	0 MESSAGE WITH INVALID VERSION FIELD
	0 MESSAGE WITH INVALID MESSAGE TYPE FIELD
	0 MESSAGE TOO SHORT
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
	0 MESSAGE WITH DUPLICATE EXTENSION
	0 MESSAGE WITH INVALID EXTENSION TYPE
	0 MESSAGE WITH INVALID SA TYPE
	0 MESSAGE WITH INVALID ADDRESS EXTENSION
	0 REQUEST SENT FROM USERLAND
	0 BYTE SENT FROM USERLAND
	0 MESSAGE TOWARD SINGLE SOCKET
	0 MESSAGE TOWARD ALL SOCKETS
	0 MESSAGE TOWARD REGISTERED SOCKETS
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
KEVT:
	24 CURRENT KERNEL CONTROL SOCKETS
	18912 KERNEL CONTROL GENERATION COUNT
	0 BAD VENDOR FAILURE
	7277 MESSAGE TOO BIG FAILURES
	0 OUT OF MEMORY FAILURE
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	272435 MESSAGES POSTED
KCTL:
	0 TOTAL KERNEL CONTROL MODULE REGISTERED
	12 CURRENT KERNEL CONTROL MODULES REGISTERED
	55 CURRENT KERNEL CONTROL SOCKETS
	1111 KERNEL CONTROL GENERATION COUNT
	577 CONNECTION ATTEMPTS
	0 CONNECTION FAILURE
	35 SEND FAILURES
	0 SEND LIST FAILURE
	0 ENQUEUE FAILURE
	0 PACKET DROPPED DUE TO FULL SOCKET BUFFERS
XBKIDLE:
	1 MAX PER PROCESS
	600 MAXIMUM TIME (SECONDS)
	131072 HIGH WATER MARK
	0 SOCKET OPTION NOT SUPPORTED FAILURE
	0 TOO MANY SOCKETS FAILURE
	0 TOTAL SOCKET REQUESTED OK
	0 EXTENDED BK IDLE SOCKET
	0 NO CELLULAR FAILURE
	0 NO TIME FAILURES
	0 FORCED DEFUNCT SOCKET
	0 RESUMED SOCKET
	0 TIMEOUT EXPIRED FAILURE
	0 TIMER RESCHEDULED
	0 NO DELEGATED FAILURE
NET_API:
	2 INTERFACE FILTERS CURRENTLY ATTACHED
	2 INTERFACE FILTERS ATTACHED SINCE BOOT
	2 INTERFACE FILTERS ATTACHED SINCE BOOT BY OS
	0 IP FILTER CURRENTLY ATTACHED
	0 IP FILTER ATTACHED SINCE BOOT
	0 IP FILTER ATTACHED SINCE BOOT BY OS
	4 SOCKET FILTERS CURRENTLY ATTACHED
	4 SOCKET FILTERS ATTACHED SINCE BOOT
	4 SOCKET FILTERS ATTACHED SINCE BOOT BY OS
	325431 SOCKETS ALLOCATED SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL BY OS
	2458 SOCKETS WITH NECP CLIENT UUID SINCE BOOT
	103922 LOCAL DOMAIN SOCKETS ALLOCATED SINCE BOOT
	1199 ROUTE DOMAIN SOCKETS ALLOCATED SINCE BOOT
	124285 INET DOMAIN SOCKETS ALLOCATED SINCE BOOT
	59691 INET6 DOMAIN SOCKETS ALLOCATED SINCE BOOT
	10045 SYSTEM DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 MULTIPATH DOMAIN SOCKET ALLOCATED SINCE BOOT
	0 KEY DOMAIN SOCKET ALLOCATED SINCE BOOT
	5 NDRV DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 OTHER DOMAINS SOCKET ALLOCATED SINCE BOOT
	15530 IPV4 STREAM SOCKETS CREATED SINCE BOOT
	108755 IPV4 DATAGRAM SOCKETS CREATED SINCE BOOT
	10291 IPV4 DATAGRAM SOCKETS CONNECTED
	37935 IPV4 DNS SOCKETS
	102069 IPV4 DATAGRAM SOCKETS WITHOUT DATA
	7536 IPV6 STREAM SOCKETS CREATED SINCE BOOT
	52155 IPV6 DATAGRAM SOCKETS CREATED SINCE BOOT
	34772 IPV6 DATAGRAM SOCKETS CONNECTED
	0 IPV6 DNS SOCKET
	28161 IPV6 DATAGRAM SOCKETS WITHOUT DATA
	1115 SOCKET MULTICAST JOINS SINCE BOOT
	1115 SOCKET MULTICAST JOINS SINCE BOOT BY OS
	0 IPV4 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV4 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED
	12 INTERFACES ALLOCATED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED BY OS
	12 EXTENDED INTERFACES ALLOCATED SINCE BOOT BY OS
	2 PF ADDRULE OPERATIONS SINCE BOOT
	0 PF ADDRULE OPERATION SINCE BOOT BY OS
	0 VMNET START SINCE BOOT

>>> print '''
    radical = math.sqrt(b**2 - 4*a*c)
    x1 = (-b + radical) / (2*a)
    x2 = (-b - radical) / (2*a)
    return x1, x2
'''.upper()

    RADICAL = MATH.SQRT(B**2 - 4*A*C)
    X1 = (-B + RADICAL) / (2*A)
    X2 = (-B - RADICAL) / (2*A)
    RETURN X1, X2

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
0
TCP:
	0 PACKET SENT
		0 DATA PACKET (0 BYTE)
		0 DATA PACKET (0 BYTE) RETRANSMITTED
		0 RESEND INITIATED BY MTU DISCOVERY
		0 ACK-ONLY PACKET (0 DELAYED)
		0 URG ONLY PACKET
		0 WINDOW PROBE PACKET
		0 WINDOW UPDATE PACKET
		0 CONTROL PACKET
		0 DATA PACKET SENT AFTER FLOW CONTROL
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
	0 PACKET RECEIVED
		0 ACK (FOR 0 BYTE)
		0 DUPLICATE ACK
		0 ACK FOR UNSENT DATA
		0 PACKET (0 BYTE) RECEIVED IN-SEQUENCE
		0 COMPLETELY DUPLICATE PACKET (0 BYTE)
		0 OLD DUPLICATE PACKET
		0 RECEIVED PACKET DROPPED DUE TO LOW MEMORY
		0 PACKET WITH SOME DUP. DATA (0 BYTE DUPED)
		0 OUT-OF-ORDER PACKET (0 BYTE)
		0 PACKET (0 BYTE) OF DATA AFTER WINDOW
		0 WINDOW PROBE
		0 WINDOW UPDATE PACKET
		0 PACKET RECEIVED AFTER CLOSE
		0 BAD RESET
		0 DISCARDED FOR BAD CHECKSUM
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
		0 DISCARDED FOR BAD HEADER OFFSET FIELD
		0 DISCARDED BECAUSE PACKET TOO SHORT
	0 CONNECTION REQUEST
	0 CONNECTION ACCEPT
	0 BAD CONNECTION ATTEMPT
	0 LISTEN QUEUE OVERFLOW
	0 CONNECTION ESTABLISHED (INCLUDING ACCEPTS)
	0 CONNECTION CLOSED (INCLUDING 0 DROP)
		0 CONNECTION UPDATED CACHED RTT ON CLOSE
		0 CONNECTION UPDATED CACHED RTT VARIANCE ON CLOSE
		0 CONNECTION UPDATED CACHED SSTHRESH ON CLOSE
	0 EMBRYONIC CONNECTION DROPPED
	0 SEGMENT UPDATED RTT (OF 0 ATTEMPT)
	0 RETRANSMIT TIMEOUT
		0 CONNECTION DROPPED BY REXMIT TIMEOUT
		0 CONNECTION DROPPED AFTER RETRANSMITTING FIN
	0 PERSIST TIMEOUT
		0 CONNECTION DROPPED BY PERSIST TIMEOUT
	0 KEEPALIVE TIMEOUT
		0 KEEPALIVE PROBE SENT
		0 CONNECTION DROPPED BY KEEPALIVE
	0 CORRECT ACK HEADER PREDICTION
	0 CORRECT DATA PACKET HEADER PREDICTION
	0 SACK RECOVERY EPISODE
	0 SEGMENT REXMIT IN SACK RECOVERY EPISODES
	0 BYTE REXMIT IN SACK RECOVERY EPISODES
	0 SACK OPTION (SACK BLOCKS) RECEIVED
	0 SACK OPTION (SACK BLOCKS) SENT
	0 SACK SCOREBOARD OVERFLOW
	0 LRO COALESCED PACKET
		0 TIME LRO FLOW TABLE WAS FULL
		0 COLLISION IN LRO FLOW TABLE
		0 TIME LRO COALESCED 2 PACKETS
		0 TIME LRO COALESCED 3 OR 4 PACKETS
		0 TIME LRO COALESCED 5 OR MORE PACKETS
	0 LIMITED TRANSMIT DONE
	0 EARLY RETRANSMIT DONE
	0 TIME CUMULATIVE ACK ADVANCED ALONG WITH SACK
	0 PROBE TIMEOUT
		0 TIME RETRANSMIT TIMEOUT TRIGGERED AFTER PROBE
		0 TIME PROBE PACKETS WERE SENT FOR AN INTERFACE
		0 TIME COULDN'T SEND PROBE PACKETS FOR AN INTERFACE
		0 TIME FAST RECOVERY AFTER TAIL LOSS
		0 TIME RECOVERED LAST PACKET 
		0 SACK BASED RESCUE RETRANSMIT
	0 CLIENT CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 CLIENT CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME GRACEFUL FALLBACK TO NON-ECN CONNECTION
		0 TIME LOST ECN NEGOTIATING SYN, FOLLOWED BY RETRANSMISSION
		0 SERVER CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 SERVER CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME LOST ECN NEGOTIATING SYN-ACK, FOLLOWED BY RETRANSMISSION
		0 TIME RECEIVED CONGESTION EXPERIENCED (CE) NOTIFICATION
		0 TIME CWR WAS SENT IN RESPONSE TO ECE
		0 TIME SENT ECE NOTIFICATION
		0 CONNECTION RECEIVED CE ATLEAST ONCE
		0 CONNECTION RECEIVED ECE ATLEAST ONCE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS BUT NO CE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS AND CE
		0 CONNECTION USING ECN RECEIVED CE BUT NO PACKET LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO SYN-LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO REORDERING
		0 CONNECTION FELL BACK TO NON-ECN DUE TO EXCESSIVE CE-MARKINGS
	0 TIME PACKET REORDERING WAS DETECTED ON A CONNECTION
		0 TIME TRANSMITTED PACKETS WERE REORDERED
		0 TIME FAST RECOVERY WAS DELAYED TO HANDLE REORDERING
		0 TIME RETRANSMISSION WAS AVOIDED BY DELAYING RECOVERY
		0 RETRANSMISSION NOT NEEDED 
	0 TIME DSACK OPTION WAS SENT
		0 TIME DSACK OPTION WAS RECEIVED
		0 TIME DSACK WAS DISABLED ON A CONNECTION
		0 TIME RECOVERED FROM BAD RETRANSMISSION USING DSACK
		0 TIME IGNORED DSACK DUE TO ACK LOSS
		0 TIME IGNORED OLD DSACK OPTIONS
	0 TIME PMTU BLACKHOLE DETECTION, SIZE REVERTED
	0 CONNECTION WERE DROPPED AFTER LONG SLEEP
	0 TIME A TFO-COOKIE HAS BEEN ANNOUNCED
	0 SYN WITH DATA AND A VALID TFO-COOKIE HAVE BEEN RECEIVED
	0 SYN WITH TFO-COOKIE-REQUEST RECEIVED
	0 TIME AN INVALID TFO-COOKIE HAS BEEN RECEIVED
	0 TIME WE REQUESTED A TFO-COOKIE
		0 TIME THE PEER ANNOUNCED A TFO-COOKIE
	0 TIME WE COMBINED SYN WITH DATA AND A TFO-COOKIE
		0 TIME OUR SYN WITH DATA HAS BEEN ACKNOWLEDGED
	0 TIME A CONNECTION-ATTEMPT WITH TFO FELL BACK TO REGULAR TCP
	0 TIME A TFO-CONNECTION BLACKHOLE'D
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO DEFAULT
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO MEDIUM
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO LOW
	0 TIMER DRIFT LESS OR EQUAL TO 1 MS
	0 TIMER DRIFT LESS OR EQUAL TO 10 MS
	0 TIMER DRIFT LESS OR EQUAL TO 20 MS
	0 TIMER DRIFT LESS OR EQUAL TO 50 MS
	0 TIMER DRIFT LESS OR EQUAL TO 100 MS
	0 TIMER DRIFT LESS OR EQUAL TO 200 MS
	0 TIMER DRIFT LESS OR EQUAL TO 500 MS
	0 TIMER DRIFT LESS OR EQUAL TO 1000 MS
	0 TIMER DRIFT GREATER THAN TO 1000 MS
UDP:
	501873 DATAGRAMS RECEIVED
		0 WITH INCOMPLETE HEADER
		0 WITH BAD DATA LENGTH FIELD
		0 WITH BAD CHECKSUM
		54 WITH NO CHECKSUM
		470760 CHECKSUMMED IN SOFTWARE
			236012 DATAGRAMS (75327157 BYTES) OVER IPV4
			234748 DATAGRAMS (105519418 BYTES) OVER IPV6
		5343 DROPPED DUE TO NO SOCKET
		3618 BROADCAST/MULTICAST DATAGRAMS UNDELIVERED
		0 TIME MULTICAST SOURCE FILTER MATCHED
		1 DROPPED DUE TO FULL SOCKET BUFFERS
		0 NOT FOR HASHED PCB
		492911 DELIVERED
	142047 DATAGRAMS OUTPUT
		149011 CHECKSUMMED IN SOFTWARE
			55153 DATAGRAMS (11710578 BYTES) OVER IPV4
			93858 DATAGRAMS (20662478 BYTES) OVER IPV6
ICMP:
	1398 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED 'CUZ OLD MESSAGE WAS ICMP
	OUTPUT HISTOGRAM:
		ECHO REPLY: 38
		DESTINATION UNREACHABLE: 1398
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	1 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	0 MULTICAST ECHO REQUESTS IGNORED
	0 MULTICAST TIMESTAMP REQUESTS IGNORED
	INPUT HISTOGRAM:
		DESTINATION UNREACHABLE: 2007
		ECHO: 38
		ROUTER ADVERTISEMENT: 147
	38 MESSAGE RESPONSES GENERATED
	ICMP ADDRESS MASK RESPONSES ARE DISABLED
IGMP:
	1636 MESSAGES RECEIVED
	0 MESSAGE RECEIVED WITH TOO FEW BYTES
	0 MESSAGE RECEIVED WITH WRONG TTL
	0 MESSAGE RECEIVED WITH BAD CHECKSUM
	565 V1/V2 MEMBERSHIP QUERIES RECEIVED
	287 V3 MEMBERSHIP QUERIES RECEIVED
	0 MEMBERSHIP QUERIES RECEIVED WITH INVALID FIELD(S)
	834 GENERAL QUERIES RECEIVED
	18 GROUP QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES DROPPED
	784 MEMBERSHIP REPORTS RECEIVED
	0 MEMBERSHIP REPORT RECEIVED WITH INVALID FIELD(S)
	784 MEMBERSHIP REPORTS RECEIVED FOR GROUPS TO WHICH WE BELONG
	0 V3 REPORT RECEIVED WITHOUT ROUTER ALERT
	890 MEMBERSHIP REPORTS SENT
IPSEC:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
ARP:
	1519 BROADAST ARP REQUESTS SENT
	9 UNICAST ARP REQUESTS SENT
	3319 ARP REPLIES SENT
	0 ARP ANNOUNCEMENT SENT
	11629 ARP REQUESTS RECEIVED
	1267 ARP REPLIES RECEIVED
	12898 TOTAL ARP PACKETS RECEIVED
	0 ARP CONFLICT PROBE SENT
	0 INVALID ARP RESOLVE REQUEST
	0 TOTAL PACKET DROPPED DUE TO LACK OF MEMORY
	0 TOTAL PACKET HELD AWAITING ARP REPLY
	43 TOTAL PACKETS DROPPED DUE TO NO ARP ENTRY
	378 TOTAL PACKETS DROPPED DURING ARP ENTRY REMOVAL
	1410 ARP ENTRIES TIMED OUT
	0 DUPLICATE IP SEEN
MPTCP:
	0 DATA PACKET SENT
	0 DATA BYTE SENT
	0 DATA PACKET RECEIVED
	0 DATA BYTE RECEIVED
	0 PACKET WITH AN INVALID MPCAP OPTION
	0 PACKET WITH AN INVALID MPJOIN OPTION
	0 TIME PRIMARY SUBFLOW FELL BACK TO TCP
	0 TIME SECONDARY SUBFLOW FELL BACK TO TCP
	0 DSS OPTION DROP
	0 OTHER INVALID MPTCP OPTION
	0 TIME THE MPTCP SUBFLOW WINDOW WAS REDUCED
	0 BAD DSS CHECKSUM
	0 TIME RECEIVED OUT OF ORDER DATA 
	0 SUBFLOW SWITCH
	0 SUBFLOW SWITCH DUE TO ADVISORY
	0 SUBFLOW SWITCH DUE TO RTT
	0 SUBFLOW SWITCH DUE TO RTO
	0 SUBFLOW SWITCH DUE TO PEER
	0 NUMBER OF SUBFLOW PROBE
IP6:
	738784 TOTAL PACKETS RECEIVED
		0 WITH SIZE SMALLER THAN MINIMUM
		0 WITH DATA SIZE < DATA LENGTH
		0 WITH DATA SIZE > DATA LENGTH
			0 PACKET FORCED TO SOFTWARE CHECKSUM
		0 WITH BAD OPTIONS
		168 WITH INCORRECT VERSION NUMBER
		6 FRAGMENTS RECEIVED
			0 DROPPED (DUP OR OUT OF SPACE)
			0 DROPPED AFTER TIMEOUT
			0 EXCEEDED LIMIT
			3 REASSEMBLED OK
			0 ATOMIC FRAGMENTS RECEIVED
		665843 PACKETS FOR THIS HOST
		0 PACKET FORWARDED
		32366 PACKETS NOT FORWARDABLE
		0 REDIRECT SENT
		32309 MULTICAST PACKETS WHICH WE DON'T JOIN
		0 PACKET WHOSE HEADERS ARE NOT CONTINUOUS
		0 TUNNELING PACKET THAT CAN'T FIND GIF
		0 PACKET DISCARDED DUE TO TOO MAY HEADERS
		0 FORWARD CACHE HIT
		0 FORWARD CACHE MISS
		0 PACKET DROPPED DUE TO NO BUFS FOR CONTROL DATA
	340891 PACKETS SENT FROM THIS HOST
		0 PACKET SENT WITH FABRICATED IP HEADER
		0 OUTPUT PACKET DROPPED DUE TO NO BUFS, ETC.
		2291 OUTPUT PACKETS DISCARDED DUE TO NO ROUTE
		0 OUTPUT DATAGRAM FRAGMENTED
		0 FRAGMENT CREATED
		0 DATAGRAM THAT CAN'T BE FRAGMENTED
		0 PACKET THAT VIOLATED SCOPE RULES
		0 PACKET DROPPED DUE TO NECP POLICY
	INPUT HISTOGRAM:
		HOP BY HOP: 5603
		TCP: 421726
		UDP: 269041
		FRAGMENT: 6
		ICMP6: 41342
		PIM: 898
	MBUF STATISTICS:
		1787 ONE MBUF
		TWO OR MORE MBUF:
			LO0= 10304
			UTUN1= 12
		726681 ONE EXT MBUF
		0 TWO OR MORE EXT MBUF
		0 FAILURE OF SOURCE ADDRESS SELECTION
		SOURCE ADDRESSES ON AN OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES ON A NON-OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF SAME SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF A DIFFERENT SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		DEPRECATED SOURCE ADDRESSES
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESS SELECTION
			18096 RULES DEFAULT
			0 RULE PREFER SAME ADDRESS
			4821 RULES PREFER APPROPRIATE SCOPE
			0 RULE AVOID DEPRECATED ADDRESSES
			0 RULE PREFER HOME ADDRESSES
			0 RULE PREFER OUTGOING INTERFACE
			10 RULES PREFER MATCHING LABEL
			47351 RULES PREFER TEMPORARY ADDRESSES
			0 RULE PREFER ADDRESSES ON ALIVE INTERFACES
			0 RULE USE LONGEST MATCHING PREFIX
		0 DUPLICATE ADDRESS DETECTION COLLISION
		0 DUPLICATE ADDRESS DETECTION NS LOOP
		0 TIME IGNORED SOURCE ON SECONDARY EXPENSIVE I/F
ICMP6:
	1723 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED BECAUSE OLD MESSAGE WAS ICMP ERROR OR SO
	0 ERROR NOT GENERATED BECAUSE RATE LIMITATION
	OUTPUT HISTOGRAM:
		UNREACH: 1723
		MLDV1 LISTENER REPORT: 77
		MLDV1 LISTENER DONE: 11
		ROUTER SOLICITATION: 123
		NEIGHBOR SOLICITATION: 5179
		NEIGHBOR ADVERTISEMENT: 4402
		MLDV2 LISTENER REPORT: 1122
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	0 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	INPUT HISTOGRAM:
		UNREACH: 150
		MULTICAST LISTENER QUERY: 1999
		ROUTER ADVERTISEMENT: 29599
		NEIGHBOR SOLICITATION: 4402
		NEIGHBOR ADVERTISEMENT: 4326
	HISTOGRAM OF ERROR MESSAGES TO BE GENERATED:
		0 NO ROUTE
		0 ADMINISTRATIVELY PROHIBITED
		0 BEYOND SCOPE
		150 ADDRESS UNREACHABLE
		1573 PORT UNREACHABLE
		0 PACKET TOO BIG
		0 TIME EXCEED TRANSIT
		0 TIME EXCEED REASSEMBLY
		0 ERRONEOUS HEADER FIELD
		0 UNRECOGNIZED NEXT HEADER
		0 UNRECOGNIZED OPTION
		0 REDIRECT
		0 UNKNOWN
	0 MESSAGE RESPONSE GENERATED
	0 MESSAGE WITH TOO MANY ND OPTIONS
	0 MESSAGE WITH BAD ND OPTIONS
	0 BAD NEIGHBOR SOLICITATION MESSAGE
	0 BAD NEIGHBOR ADVERTISEMENT MESSAGE
	0 BAD ROUTER SOLICITATION MESSAGE
	0 BAD ROUTER ADVERTISEMENT MESSAGE
	0 BAD REDIRECT MESSAGE
	0 PATH MTU CHANGE
	0 DROPPED FRAGMENTED NDP MESSAGE
IPSEC6:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
RIP6:
	0 MESSAGE RECEIVED
	0 CHECKSUM CALCULATION ON INBOUND
	0 MESSAGE WITH BAD CHECKSUM
	0 MESSAGE DROPPED DUE TO NO SOCKET
	0 MULTICAST MESSAGE DROPPED DUE TO NO SOCKET
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	0 DELIVERED
	0 DATAGRAM OUTPUT
PFKEY:
	0 REQUEST SENT TO USERLAND
	0 BYTE SENT TO USERLAND
	0 MESSAGE WITH INVALID LENGTH FIELD
	0 MESSAGE WITH INVALID VERSION FIELD
	0 MESSAGE WITH INVALID MESSAGE TYPE FIELD
	0 MESSAGE TOO SHORT
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
	0 MESSAGE WITH DUPLICATE EXTENSION
	0 MESSAGE WITH INVALID EXTENSION TYPE
	0 MESSAGE WITH INVALID SA TYPE
	0 MESSAGE WITH INVALID ADDRESS EXTENSION
	0 REQUEST SENT FROM USERLAND
	0 BYTE SENT FROM USERLAND
	0 MESSAGE TOWARD SINGLE SOCKET
	0 MESSAGE TOWARD ALL SOCKETS
	0 MESSAGE TOWARD REGISTERED SOCKETS
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
KEVT:
	24 CURRENT KERNEL CONTROL SOCKETS
	18912 KERNEL CONTROL GENERATION COUNT
	0 BAD VENDOR FAILURE
	7281 MESSAGE TOO BIG FAILURES
	0 OUT OF MEMORY FAILURE
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	272479 MESSAGES POSTED
KCTL:
	0 TOTAL KERNEL CONTROL MODULE REGISTERED
	12 CURRENT KERNEL CONTROL MODULES REGISTERED
	55 CURRENT KERNEL CONTROL SOCKETS
	1111 KERNEL CONTROL GENERATION COUNT
	577 CONNECTION ATTEMPTS
	0 CONNECTION FAILURE
	35 SEND FAILURES
	0 SEND LIST FAILURE
	0 ENQUEUE FAILURE
	0 PACKET DROPPED DUE TO FULL SOCKET BUFFERS
XBKIDLE:
	1 MAX PER PROCESS
	600 MAXIMUM TIME (SECONDS)
	131072 HIGH WATER MARK
	0 SOCKET OPTION NOT SUPPORTED FAILURE
	0 TOO MANY SOCKETS FAILURE
	0 TOTAL SOCKET REQUESTED OK
	0 EXTENDED BK IDLE SOCKET
	0 NO CELLULAR FAILURE
	0 NO TIME FAILURES
	0 FORCED DEFUNCT SOCKET
	0 RESUMED SOCKET
	0 TIMEOUT EXPIRED FAILURE
	0 TIMER RESCHEDULED
	0 NO DELEGATED FAILURE
NET_API:
	2 INTERFACE FILTERS CURRENTLY ATTACHED
	2 INTERFACE FILTERS ATTACHED SINCE BOOT
	2 INTERFACE FILTERS ATTACHED SINCE BOOT BY OS
	0 IP FILTER CURRENTLY ATTACHED
	0 IP FILTER ATTACHED SINCE BOOT
	0 IP FILTER ATTACHED SINCE BOOT BY OS
	4 SOCKET FILTERS CURRENTLY ATTACHED
	4 SOCKET FILTERS ATTACHED SINCE BOOT
	4 SOCKET FILTERS ATTACHED SINCE BOOT BY OS
	325482 SOCKETS ALLOCATED SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL BY OS
	2458 SOCKETS WITH NECP CLIENT UUID SINCE BOOT
	103941 LOCAL DOMAIN SOCKETS ALLOCATED SINCE BOOT
	1199 ROUTE DOMAIN SOCKETS ALLOCATED SINCE BOOT
	124293 INET DOMAIN SOCKETS ALLOCATED SINCE BOOT
	59712 INET6 DOMAIN SOCKETS ALLOCATED SINCE BOOT
	10045 SYSTEM DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 MULTIPATH DOMAIN SOCKET ALLOCATED SINCE BOOT
	0 KEY DOMAIN SOCKET ALLOCATED SINCE BOOT
	5 NDRV DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 OTHER DOMAINS SOCKET ALLOCATED SINCE BOOT
	15532 IPV4 STREAM SOCKETS CREATED SINCE BOOT
	108761 IPV4 DATAGRAM SOCKETS CREATED SINCE BOOT
	10292 IPV4 DATAGRAM SOCKETS CONNECTED
	37948 IPV4 DNS SOCKETS
	102074 IPV4 DATAGRAM SOCKETS WITHOUT DATA
	7540 IPV6 STREAM SOCKETS CREATED SINCE BOOT
	52172 IPV6 DATAGRAM SOCKETS CREATED SINCE BOOT
	34784 IPV6 DATAGRAM SOCKETS CONNECTED
	0 IPV6 DNS SOCKET
	28170 IPV6 DATAGRAM SOCKETS WITHOUT DATA
	1115 SOCKET MULTICAST JOINS SINCE BOOT
	1115 SOCKET MULTICAST JOINS SINCE BOOT BY OS
	0 IPV4 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV4 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED
	12 INTERFACES ALLOCATED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED BY OS
	12 EXTENDED INTERFACES ALLOCATED SINCE BOOT BY OS
	2 PF ADDRULE OPERATIONS SINCE BOOT
	0 PF ADDRULE OPERATION SINCE BOOT BY OS
	0 VMNET START SINCE BOOT

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
0
TCP:
	0 PACKET SENT
		0 DATA PACKET (0 BYTE)
		0 DATA PACKET (0 BYTE) RETRANSMITTED
		0 RESEND INITIATED BY MTU DISCOVERY
		0 ACK-ONLY PACKET (0 DELAYED)
		0 URG ONLY PACKET
		0 WINDOW PROBE PACKET
		0 WINDOW UPDATE PACKET
		0 CONTROL PACKET
		0 DATA PACKET SENT AFTER FLOW CONTROL
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
	0 PACKET RECEIVED
		0 ACK (FOR 0 BYTE)
		0 DUPLICATE ACK
		0 ACK FOR UNSENT DATA
		0 PACKET (0 BYTE) RECEIVED IN-SEQUENCE
		0 COMPLETELY DUPLICATE PACKET (0 BYTE)
		0 OLD DUPLICATE PACKET
		0 RECEIVED PACKET DROPPED DUE TO LOW MEMORY
		0 PACKET WITH SOME DUP. DATA (0 BYTE DUPED)
		0 OUT-OF-ORDER PACKET (0 BYTE)
		0 PACKET (0 BYTE) OF DATA AFTER WINDOW
		0 WINDOW PROBE
		0 WINDOW UPDATE PACKET
		0 PACKET RECEIVED AFTER CLOSE
		0 BAD RESET
		0 DISCARDED FOR BAD CHECKSUM
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
		0 DISCARDED FOR BAD HEADER OFFSET FIELD
		0 DISCARDED BECAUSE PACKET TOO SHORT
	0 CONNECTION REQUEST
	0 CONNECTION ACCEPT
	0 BAD CONNECTION ATTEMPT
	0 LISTEN QUEUE OVERFLOW
	0 CONNECTION ESTABLISHED (INCLUDING ACCEPTS)
	0 CONNECTION CLOSED (INCLUDING 0 DROP)
		0 CONNECTION UPDATED CACHED RTT ON CLOSE
		0 CONNECTION UPDATED CACHED RTT VARIANCE ON CLOSE
		0 CONNECTION UPDATED CACHED SSTHRESH ON CLOSE
	0 EMBRYONIC CONNECTION DROPPED
	0 SEGMENT UPDATED RTT (OF 0 ATTEMPT)
	0 RETRANSMIT TIMEOUT
		0 CONNECTION DROPPED BY REXMIT TIMEOUT
		0 CONNECTION DROPPED AFTER RETRANSMITTING FIN
	0 PERSIST TIMEOUT
		0 CONNECTION DROPPED BY PERSIST TIMEOUT
	0 KEEPALIVE TIMEOUT
		0 KEEPALIVE PROBE SENT
		0 CONNECTION DROPPED BY KEEPALIVE
	0 CORRECT ACK HEADER PREDICTION
	0 CORRECT DATA PACKET HEADER PREDICTION
	0 SACK RECOVERY EPISODE
	0 SEGMENT REXMIT IN SACK RECOVERY EPISODES
	0 BYTE REXMIT IN SACK RECOVERY EPISODES
	0 SACK OPTION (SACK BLOCKS) RECEIVED
	0 SACK OPTION (SACK BLOCKS) SENT
	0 SACK SCOREBOARD OVERFLOW
	0 LRO COALESCED PACKET
		0 TIME LRO FLOW TABLE WAS FULL
		0 COLLISION IN LRO FLOW TABLE
		0 TIME LRO COALESCED 2 PACKETS
		0 TIME LRO COALESCED 3 OR 4 PACKETS
		0 TIME LRO COALESCED 5 OR MORE PACKETS
	0 LIMITED TRANSMIT DONE
	0 EARLY RETRANSMIT DONE
	0 TIME CUMULATIVE ACK ADVANCED ALONG WITH SACK
	0 PROBE TIMEOUT
		0 TIME RETRANSMIT TIMEOUT TRIGGERED AFTER PROBE
		0 TIME PROBE PACKETS WERE SENT FOR AN INTERFACE
		0 TIME COULDN'T SEND PROBE PACKETS FOR AN INTERFACE
		0 TIME FAST RECOVERY AFTER TAIL LOSS
		0 TIME RECOVERED LAST PACKET 
		0 SACK BASED RESCUE RETRANSMIT
	0 CLIENT CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 CLIENT CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME GRACEFUL FALLBACK TO NON-ECN CONNECTION
		0 TIME LOST ECN NEGOTIATING SYN, FOLLOWED BY RETRANSMISSION
		0 SERVER CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 SERVER CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME LOST ECN NEGOTIATING SYN-ACK, FOLLOWED BY RETRANSMISSION
		0 TIME RECEIVED CONGESTION EXPERIENCED (CE) NOTIFICATION
		0 TIME CWR WAS SENT IN RESPONSE TO ECE
		0 TIME SENT ECE NOTIFICATION
		0 CONNECTION RECEIVED CE ATLEAST ONCE
		0 CONNECTION RECEIVED ECE ATLEAST ONCE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS BUT NO CE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS AND CE
		0 CONNECTION USING ECN RECEIVED CE BUT NO PACKET LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO SYN-LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO REORDERING
		0 CONNECTION FELL BACK TO NON-ECN DUE TO EXCESSIVE CE-MARKINGS
	0 TIME PACKET REORDERING WAS DETECTED ON A CONNECTION
		0 TIME TRANSMITTED PACKETS WERE REORDERED
		0 TIME FAST RECOVERY WAS DELAYED TO HANDLE REORDERING
		0 TIME RETRANSMISSION WAS AVOIDED BY DELAYING RECOVERY
		0 RETRANSMISSION NOT NEEDED 
	0 TIME DSACK OPTION WAS SENT
		0 TIME DSACK OPTION WAS RECEIVED
		0 TIME DSACK WAS DISABLED ON A CONNECTION
		0 TIME RECOVERED FROM BAD RETRANSMISSION USING DSACK
		0 TIME IGNORED DSACK DUE TO ACK LOSS
		0 TIME IGNORED OLD DSACK OPTIONS
	0 TIME PMTU BLACKHOLE DETECTION, SIZE REVERTED
	0 CONNECTION WERE DROPPED AFTER LONG SLEEP
	0 TIME A TFO-COOKIE HAS BEEN ANNOUNCED
	0 SYN WITH DATA AND A VALID TFO-COOKIE HAVE BEEN RECEIVED
	0 SYN WITH TFO-COOKIE-REQUEST RECEIVED
	0 TIME AN INVALID TFO-COOKIE HAS BEEN RECEIVED
	0 TIME WE REQUESTED A TFO-COOKIE
		0 TIME THE PEER ANNOUNCED A TFO-COOKIE
	0 TIME WE COMBINED SYN WITH DATA AND A TFO-COOKIE
		0 TIME OUR SYN WITH DATA HAS BEEN ACKNOWLEDGED
	0 TIME A CONNECTION-ATTEMPT WITH TFO FELL BACK TO REGULAR TCP
	0 TIME A TFO-CONNECTION BLACKHOLE'D
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO DEFAULT
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO MEDIUM
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO LOW
	0 TIMER DRIFT LESS OR EQUAL TO 1 MS
	0 TIMER DRIFT LESS OR EQUAL TO 10 MS
	0 TIMER DRIFT LESS OR EQUAL TO 20 MS
	0 TIMER DRIFT LESS OR EQUAL TO 50 MS
	0 TIMER DRIFT LESS OR EQUAL TO 100 MS
	0 TIMER DRIFT LESS OR EQUAL TO 200 MS
	0 TIMER DRIFT LESS OR EQUAL TO 500 MS
	0 TIMER DRIFT LESS OR EQUAL TO 1000 MS
	0 TIMER DRIFT GREATER THAN TO 1000 MS
UDP:
	502471 DATAGRAMS RECEIVED
		0 WITH INCOMPLETE HEADER
		0 WITH BAD DATA LENGTH FIELD
		0 WITH BAD CHECKSUM
		54 WITH NO CHECKSUM
		471354 CHECKSUMMED IN SOFTWARE
			236361 DATAGRAMS (75414214 BYTES) OVER IPV4
			234993 DATAGRAMS (105589792 BYTES) OVER IPV6
		5343 DROPPED DUE TO NO SOCKET
		3618 BROADCAST/MULTICAST DATAGRAMS UNDELIVERED
		0 TIME MULTICAST SOURCE FILTER MATCHED
		1 DROPPED DUE TO FULL SOCKET BUFFERS
		0 NOT FOR HASHED PCB
		493509 DELIVERED
	142068 DATAGRAMS OUTPUT
		149033 CHECKSUMMED IN SOFTWARE
			55173 DATAGRAMS (11716207 BYTES) OVER IPV4
			93860 DATAGRAMS (20663168 BYTES) OVER IPV6
ICMP:
	1398 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED 'CUZ OLD MESSAGE WAS ICMP
	OUTPUT HISTOGRAM:
		ECHO REPLY: 38
		DESTINATION UNREACHABLE: 1398
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	1 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	0 MULTICAST ECHO REQUESTS IGNORED
	0 MULTICAST TIMESTAMP REQUESTS IGNORED
	INPUT HISTOGRAM:
		DESTINATION UNREACHABLE: 2007
		ECHO: 38
		ROUTER ADVERTISEMENT: 147
	38 MESSAGE RESPONSES GENERATED
	ICMP ADDRESS MASK RESPONSES ARE DISABLED
IGMP:
	1636 MESSAGES RECEIVED
	0 MESSAGE RECEIVED WITH TOO FEW BYTES
	0 MESSAGE RECEIVED WITH WRONG TTL
	0 MESSAGE RECEIVED WITH BAD CHECKSUM
	565 V1/V2 MEMBERSHIP QUERIES RECEIVED
	287 V3 MEMBERSHIP QUERIES RECEIVED
	0 MEMBERSHIP QUERIES RECEIVED WITH INVALID FIELD(S)
	834 GENERAL QUERIES RECEIVED
	18 GROUP QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES DROPPED
	784 MEMBERSHIP REPORTS RECEIVED
	0 MEMBERSHIP REPORT RECEIVED WITH INVALID FIELD(S)
	784 MEMBERSHIP REPORTS RECEIVED FOR GROUPS TO WHICH WE BELONG
	0 V3 REPORT RECEIVED WITHOUT ROUTER ALERT
	890 MEMBERSHIP REPORTS SENT
IPSEC:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
ARP:
	1523 BROADAST ARP REQUESTS SENT
	9 UNICAST ARP REQUESTS SENT
	3319 ARP REPLIES SENT
	0 ARP ANNOUNCEMENT SENT
	11629 ARP REQUESTS RECEIVED
	1271 ARP REPLIES RECEIVED
	12902 TOTAL ARP PACKETS RECEIVED
	0 ARP CONFLICT PROBE SENT
	0 INVALID ARP RESOLVE REQUEST
	0 TOTAL PACKET DROPPED DUE TO LACK OF MEMORY
	0 TOTAL PACKET HELD AWAITING ARP REPLY
	43 TOTAL PACKETS DROPPED DUE TO NO ARP ENTRY
	378 TOTAL PACKETS DROPPED DURING ARP ENTRY REMOVAL
	1410 ARP ENTRIES TIMED OUT
	0 DUPLICATE IP SEEN
MPTCP:
	0 DATA PACKET SENT
	0 DATA BYTE SENT
	0 DATA PACKET RECEIVED
	0 DATA BYTE RECEIVED
	0 PACKET WITH AN INVALID MPCAP OPTION
	0 PACKET WITH AN INVALID MPJOIN OPTION
	0 TIME PRIMARY SUBFLOW FELL BACK TO TCP
	0 TIME SECONDARY SUBFLOW FELL BACK TO TCP
	0 DSS OPTION DROP
	0 OTHER INVALID MPTCP OPTION
	0 TIME THE MPTCP SUBFLOW WINDOW WAS REDUCED
	0 BAD DSS CHECKSUM
	0 TIME RECEIVED OUT OF ORDER DATA 
	0 SUBFLOW SWITCH
	0 SUBFLOW SWITCH DUE TO ADVISORY
	0 SUBFLOW SWITCH DUE TO RTT
	0 SUBFLOW SWITCH DUE TO RTO
	0 SUBFLOW SWITCH DUE TO PEER
	0 NUMBER OF SUBFLOW PROBE
IP6:
	739179 TOTAL PACKETS RECEIVED
		0 WITH SIZE SMALLER THAN MINIMUM
		0 WITH DATA SIZE < DATA LENGTH
		0 WITH DATA SIZE > DATA LENGTH
			0 PACKET FORCED TO SOFTWARE CHECKSUM
		0 WITH BAD OPTIONS
		168 WITH INCORRECT VERSION NUMBER
		6 FRAGMENTS RECEIVED
			0 DROPPED (DUP OR OUT OF SPACE)
			0 DROPPED AFTER TIMEOUT
			0 EXCEEDED LIMIT
			3 REASSEMBLED OK
			0 ATOMIC FRAGMENTS RECEIVED
		666172 PACKETS FOR THIS HOST
		0 PACKET FORWARDED
		32414 PACKETS NOT FORWARDABLE
		0 REDIRECT SENT
		32357 MULTICAST PACKETS WHICH WE DON'T JOIN
		0 PACKET WHOSE HEADERS ARE NOT CONTINUOUS
		0 TUNNELING PACKET THAT CAN'T FIND GIF
		0 PACKET DISCARDED DUE TO TOO MAY HEADERS
		0 FORWARD CACHE HIT
		0 FORWARD CACHE MISS
		0 PACKET DROPPED DUE TO NO BUFS FOR CONTROL DATA
	340980 PACKETS SENT FROM THIS HOST
		0 PACKET SENT WITH FABRICATED IP HEADER
		0 OUTPUT PACKET DROPPED DUE TO NO BUFS, ETC.
		2291 OUTPUT PACKETS DISCARDED DUE TO NO ROUTE
		0 OUTPUT DATAGRAM FRAGMENTED
		0 FRAGMENT CREATED
		0 DATAGRAM THAT CAN'T BE FRAGMENTED
		0 PACKET THAT VIOLATED SCOPE RULES
		0 PACKET DROPPED DUE TO NECP POLICY
	INPUT HISTOGRAM:
		HOP BY HOP: 5611
		TCP: 421809
		UDP: 269325
		FRAGMENT: 6
		ICMP6: 41360
		PIM: 900
	MBUF STATISTICS:
		1787 ONE MBUF
		TWO OR MORE MBUF:
			LO0= 10305
			UTUN1= 12
		727075 ONE EXT MBUF
		0 TWO OR MORE EXT MBUF
		0 FAILURE OF SOURCE ADDRESS SELECTION
		SOURCE ADDRESSES ON AN OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES ON A NON-OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF SAME SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF A DIFFERENT SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		DEPRECATED SOURCE ADDRESSES
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESS SELECTION
			18099 RULES DEFAULT
			0 RULE PREFER SAME ADDRESS
			4826 RULES PREFER APPROPRIATE SCOPE
			0 RULE AVOID DEPRECATED ADDRESSES
			0 RULE PREFER HOME ADDRESSES
			0 RULE PREFER OUTGOING INTERFACE
			10 RULES PREFER MATCHING LABEL
			47351 RULES PREFER TEMPORARY ADDRESSES
			0 RULE PREFER ADDRESSES ON ALIVE INTERFACES
			0 RULE USE LONGEST MATCHING PREFIX
		0 DUPLICATE ADDRESS DETECTION COLLISION
		0 DUPLICATE ADDRESS DETECTION NS LOOP
		0 TIME IGNORED SOURCE ON SECONDARY EXPENSIVE I/F
ICMP6:
	1723 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED BECAUSE OLD MESSAGE WAS ICMP ERROR OR SO
	0 ERROR NOT GENERATED BECAUSE RATE LIMITATION
	OUTPUT HISTOGRAM:
		UNREACH: 1723
		MLDV1 LISTENER REPORT: 77
		MLDV1 LISTENER DONE: 11
		ROUTER SOLICITATION: 123
		NEIGHBOR SOLICITATION: 5180
		NEIGHBOR ADVERTISEMENT: 4403
		MLDV2 LISTENER REPORT: 1122
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	0 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	INPUT HISTOGRAM:
		UNREACH: 150
		MULTICAST LISTENER QUERY: 1999
		ROUTER ADVERTISEMENT: 29615
		NEIGHBOR SOLICITATION: 4403
		NEIGHBOR ADVERTISEMENT: 4327
	HISTOGRAM OF ERROR MESSAGES TO BE GENERATED:
		0 NO ROUTE
		0 ADMINISTRATIVELY PROHIBITED
		0 BEYOND SCOPE
		150 ADDRESS UNREACHABLE
		1573 PORT UNREACHABLE
		0 PACKET TOO BIG
		0 TIME EXCEED TRANSIT
		0 TIME EXCEED REASSEMBLY
		0 ERRONEOUS HEADER FIELD
		0 UNRECOGNIZED NEXT HEADER
		0 UNRECOGNIZED OPTION
		0 REDIRECT
		0 UNKNOWN
	0 MESSAGE RESPONSE GENERATED
	0 MESSAGE WITH TOO MANY ND OPTIONS
	0 MESSAGE WITH BAD ND OPTIONS
	0 BAD NEIGHBOR SOLICITATION MESSAGE
	0 BAD NEIGHBOR ADVERTISEMENT MESSAGE
	0 BAD ROUTER SOLICITATION MESSAGE
	0 BAD ROUTER ADVERTISEMENT MESSAGE
	0 BAD REDIRECT MESSAGE
	0 PATH MTU CHANGE
	0 DROPPED FRAGMENTED NDP MESSAGE
IPSEC6:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
RIP6:
	0 MESSAGE RECEIVED
	0 CHECKSUM CALCULATION ON INBOUND
	0 MESSAGE WITH BAD CHECKSUM
	0 MESSAGE DROPPED DUE TO NO SOCKET
	0 MULTICAST MESSAGE DROPPED DUE TO NO SOCKET
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	0 DELIVERED
	0 DATAGRAM OUTPUT
PFKEY:
	0 REQUEST SENT TO USERLAND
	0 BYTE SENT TO USERLAND
	0 MESSAGE WITH INVALID LENGTH FIELD
	0 MESSAGE WITH INVALID VERSION FIELD
	0 MESSAGE WITH INVALID MESSAGE TYPE FIELD
	0 MESSAGE TOO SHORT
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
	0 MESSAGE WITH DUPLICATE EXTENSION
	0 MESSAGE WITH INVALID EXTENSION TYPE
	0 MESSAGE WITH INVALID SA TYPE
	0 MESSAGE WITH INVALID ADDRESS EXTENSION
	0 REQUEST SENT FROM USERLAND
	0 BYTE SENT FROM USERLAND
	0 MESSAGE TOWARD SINGLE SOCKET
	0 MESSAGE TOWARD ALL SOCKETS
	0 MESSAGE TOWARD REGISTERED SOCKETS
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
KEVT:
	24 CURRENT KERNEL CONTROL SOCKETS
	18912 KERNEL CONTROL GENERATION COUNT
	0 BAD VENDOR FAILURE
	7281 MESSAGE TOO BIG FAILURES
	0 OUT OF MEMORY FAILURE
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	272511 MESSAGES POSTED
KCTL:
	0 TOTAL KERNEL CONTROL MODULE REGISTERED
	12 CURRENT KERNEL CONTROL MODULES REGISTERED
	55 CURRENT KERNEL CONTROL SOCKETS
	1111 KERNEL CONTROL GENERATION COUNT
	577 CONNECTION ATTEMPTS
	0 CONNECTION FAILURE
	35 SEND FAILURES
	0 SEND LIST FAILURE
	0 ENQUEUE FAILURE
	0 PACKET DROPPED DUE TO FULL SOCKET BUFFERS
XBKIDLE:
	1 MAX PER PROCESS
	600 MAXIMUM TIME (SECONDS)
	131072 HIGH WATER MARK
	0 SOCKET OPTION NOT SUPPORTED FAILURE
	0 TOO MANY SOCKETS FAILURE
	0 TOTAL SOCKET REQUESTED OK
	0 EXTENDED BK IDLE SOCKET
	0 NO CELLULAR FAILURE
	0 NO TIME FAILURES
	0 FORCED DEFUNCT SOCKET
	0 RESUMED SOCKET
	0 TIMEOUT EXPIRED FAILURE
	0 TIMER RESCHEDULED
	0 NO DELEGATED FAILURE
NET_API:
	2 INTERFACE FILTERS CURRENTLY ATTACHED
	2 INTERFACE FILTERS ATTACHED SINCE BOOT
	2 INTERFACE FILTERS ATTACHED SINCE BOOT BY OS
	0 IP FILTER CURRENTLY ATTACHED
	0 IP FILTER ATTACHED SINCE BOOT
	0 IP FILTER ATTACHED SINCE BOOT BY OS
	4 SOCKET FILTERS CURRENTLY ATTACHED
	4 SOCKET FILTERS ATTACHED SINCE BOOT
	4 SOCKET FILTERS ATTACHED SINCE BOOT BY OS
	325492 SOCKETS ALLOCATED SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL BY OS
	2458 SOCKETS WITH NECP CLIENT UUID SINCE BOOT
	103945 LOCAL DOMAIN SOCKETS ALLOCATED SINCE BOOT
	1199 ROUTE DOMAIN SOCKETS ALLOCATED SINCE BOOT
	124294 INET DOMAIN SOCKETS ALLOCATED SINCE BOOT
	59716 INET6 DOMAIN SOCKETS ALLOCATED SINCE BOOT
	10045 SYSTEM DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 MULTIPATH DOMAIN SOCKET ALLOCATED SINCE BOOT
	0 KEY DOMAIN SOCKET ALLOCATED SINCE BOOT
	5 NDRV DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 OTHER DOMAINS SOCKET ALLOCATED SINCE BOOT
	15533 IPV4 STREAM SOCKETS CREATED SINCE BOOT
	108761 IPV4 DATAGRAM SOCKETS CREATED SINCE BOOT
	10292 IPV4 DATAGRAM SOCKETS CONNECTED
	37951 IPV4 DNS SOCKETS
	102074 IPV4 DATAGRAM SOCKETS WITHOUT DATA
	7541 IPV6 STREAM SOCKETS CREATED SINCE BOOT
	52175 IPV6 DATAGRAM SOCKETS CREATED SINCE BOOT
	34787 IPV6 DATAGRAM SOCKETS CONNECTED
	0 IPV6 DNS SOCKET
	28173 IPV6 DATAGRAM SOCKETS WITHOUT DATA
	1115 SOCKET MULTICAST JOINS SINCE BOOT
	1115 SOCKET MULTICAST JOINS SINCE BOOT BY OS
	0 IPV4 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV4 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED
	12 INTERFACES ALLOCATED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED BY OS
	12 EXTENDED INTERFACES ALLOCATED SINCE BOOT BY OS
	2 PF ADDRULE OPERATIONS SINCE BOOT
	0 PF ADDRULE OPERATION SINCE BOOT BY OS
	0 VMNET START SINCE BOOT

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======

====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
TCP:
	0 PACKET SENT
		0 DATA PACKET (0 BYTE)
		0 DATA PACKET (0 BYTE) RETRANSMITTED
		0 RESEND INITIATED BY MTU DISCOVERY
		0 ACK-ONLY PACKET (0 DELAYED)
		0 URG ONLY PACKET
		0 WINDOW PROBE PACKET
		0 WINDOW UPDATE PACKET
		0 CONTROL PACKET
		0 DATA PACKET SENT AFTER FLOW CONTROL
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
	0 PACKET RECEIVED
		0 ACK (FOR 0 BYTE)
		0 DUPLICATE ACK
		0 ACK FOR UNSENT DATA
		0 PACKET (0 BYTE) RECEIVED IN-SEQUENCE
		0 COMPLETELY DUPLICATE PACKET (0 BYTE)
		0 OLD DUPLICATE PACKET
		0 RECEIVED PACKET DROPPED DUE TO LOW MEMORY
		0 PACKET WITH SOME DUP. DATA (0 BYTE DUPED)
		0 OUT-OF-ORDER PACKET (0 BYTE)
		0 PACKET (0 BYTE) OF DATA AFTER WINDOW
		0 WINDOW PROBE
		0 WINDOW UPDATE PACKET
		0 PACKET RECEIVED AFTER CLOSE
		0 BAD RESET
		0 DISCARDED FOR BAD CHECKSUM
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
		0 DISCARDED FOR BAD HEADER OFFSET FIELD
		0 DISCARDED BECAUSE PACKET TOO SHORT
	0 CONNECTION REQUEST
	0 CONNECTION ACCEPT
	0 BAD CONNECTION ATTEMPT
	0 LISTEN QUEUE OVERFLOW
	0 CONNECTION ESTABLISHED (INCLUDING ACCEPTS)
	0 CONNECTION CLOSED (INCLUDING 0 DROP)
		0 CONNECTION UPDATED CACHED RTT ON CLOSE
		0 CONNECTION UPDATED CACHED RTT VARIANCE ON CLOSE
		0 CONNECTION UPDATED CACHED SSTHRESH ON CLOSE
	0 EMBRYONIC CONNECTION DROPPED
	0 SEGMENT UPDATED RTT (OF 0 ATTEMPT)
	0 RETRANSMIT TIMEOUT
		0 CONNECTION DROPPED BY REXMIT TIMEOUT
		0 CONNECTION DROPPED AFTER RETRANSMITTING FIN
	0 PERSIST TIMEOUT
		0 CONNECTION DROPPED BY PERSIST TIMEOUT
	0 KEEPALIVE TIMEOUT
		0 KEEPALIVE PROBE SENT
		0 CONNECTION DROPPED BY KEEPALIVE
	0 CORRECT ACK HEADER PREDICTION
	0 CORRECT DATA PACKET HEADER PREDICTION
	0 SACK RECOVERY EPISODE
	0 SEGMENT REXMIT IN SACK RECOVERY EPISODES
	0 BYTE REXMIT IN SACK RECOVERY EPISODES
	0 SACK OPTION (SACK BLOCKS) RECEIVED
	0 SACK OPTION (SACK BLOCKS) SENT
	0 SACK SCOREBOARD OVERFLOW
	0 LRO COALESCED PACKET
		0 TIME LRO FLOW TABLE WAS FULL
		0 COLLISION IN LRO FLOW TABLE
		0 TIME LRO COALESCED 2 PACKETS
		0 TIME LRO COALESCED 3 OR 4 PACKETS
		0 TIME LRO COALESCED 5 OR MORE PACKETS
	0 LIMITED TRANSMIT DONE
	0 EARLY RETRANSMIT DONE
	0 TIME CUMULATIVE ACK ADVANCED ALONG WITH SACK
	0 PROBE TIMEOUT
		0 TIME RETRANSMIT TIMEOUT TRIGGERED AFTER PROBE
		0 TIME PROBE PACKETS WERE SENT FOR AN INTERFACE
		0 TIME COULDN'T SEND PROBE PACKETS FOR AN INTERFACE
		0 TIME FAST RECOVERY AFTER TAIL LOSS
		0 TIME RECOVERED LAST PACKET 
		0 SACK BASED RESCUE RETRANSMIT
	0 CLIENT CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 CLIENT CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME GRACEFUL FALLBACK TO NON-ECN CONNECTION
		0 TIME LOST ECN NEGOTIATING SYN, FOLLOWED BY RETRANSMISSION
		0 SERVER CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 SERVER CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME LOST ECN NEGOTIATING SYN-ACK, FOLLOWED BY RETRANSMISSION
		0 TIME RECEIVED CONGESTION EXPERIENCED (CE) NOTIFICATION
		0 TIME CWR WAS SENT IN RESPONSE TO ECE
		0 TIME SENT ECE NOTIFICATION
		0 CONNECTION RECEIVED CE ATLEAST ONCE
		0 CONNECTION RECEIVED ECE ATLEAST ONCE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS BUT NO CE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS AND CE
		0 CONNECTION USING ECN RECEIVED CE BUT NO PACKET LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO SYN-LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO REORDERING
		0 CONNECTION FELL BACK TO NON-ECN DUE TO EXCESSIVE CE-MARKINGS
	0 TIME PACKET REORDERING WAS DETECTED ON A CONNECTION
		0 TIME TRANSMITTED PACKETS WERE REORDERED
		0 TIME FAST RECOVERY WAS DELAYED TO HANDLE REORDERING
		0 TIME RETRANSMISSION WAS AVOIDED BY DELAYING RECOVERY
		0 RETRANSMISSION NOT NEEDED 
	0 TIME DSACK OPTION WAS SENT
		0 TIME DSACK OPTION WAS RECEIVED
		0 TIME DSACK WAS DISABLED ON A CONNECTION
		0 TIME RECOVERED FROM BAD RETRANSMISSION USING DSACK
		0 TIME IGNORED DSACK DUE TO ACK LOSS
		0 TIME IGNORED OLD DSACK OPTIONS
	0 TIME PMTU BLACKHOLE DETECTION, SIZE REVERTED
	0 CONNECTION WERE DROPPED AFTER LONG SLEEP
	0 TIME A TFO-COOKIE HAS BEEN ANNOUNCED
	0 SYN WITH DATA AND A VALID TFO-COOKIE HAVE BEEN RECEIVED
	0 SYN WITH TFO-COOKIE-REQUEST RECEIVED
	0 TIME AN INVALID TFO-COOKIE HAS BEEN RECEIVED
	0 TIME WE REQUESTED A TFO-COOKIE
		0 TIME THE PEER ANNOUNCED A TFO-COOKIE
	0 TIME WE COMBINED SYN WITH DATA AND A TFO-COOKIE
		0 TIME OUR SYN WITH DATA HAS BEEN ACKNOWLEDGED
	0 TIME A CONNECTION-ATTEMPT WITH TFO FELL BACK TO REGULAR TCP
	0 TIME A TFO-CONNECTION BLACKHOLE'D
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO DEFAULT
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO MEDIUM
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO LOW
	0 TIMER DRIFT LESS OR EQUAL TO 1 MS
	0 TIMER DRIFT LESS OR EQUAL TO 10 MS
	0 TIMER DRIFT LESS OR EQUAL TO 20 MS
	0 TIMER DRIFT LESS OR EQUAL TO 50 MS
	0 TIMER DRIFT LESS OR EQUAL TO 100 MS
	0 TIMER DRIFT LESS OR EQUAL TO 200 MS
	0 TIMER DRIFT LESS OR EQUAL TO 500 MS
	0 TIMER DRIFT LESS OR EQUAL TO 1000 MS
	0 TIMER DRIFT GREATER THAN TO 1000 MS
UDP:
	505087 DATAGRAMS RECEIVED
		0 WITH INCOMPLETE HEADER
		0 WITH BAD DATA LENGTH FIELD
		0 WITH BAD CHECKSUM
		54 WITH NO CHECKSUM
		473922 CHECKSUMMED IN SOFTWARE
			237770 DATAGRAMS (75849798 BYTES) OVER IPV4
			236152 DATAGRAMS (105970975 BYTES) OVER IPV6
		5344 DROPPED DUE TO NO SOCKET
		3618 BROADCAST/MULTICAST DATAGRAMS UNDELIVERED
		0 TIME MULTICAST SOURCE FILTER MATCHED
		1 DROPPED DUE TO FULL SOCKET BUFFERS
		0 NOT FOR HASHED PCB
		496124 DELIVERED
	142195 DATAGRAMS OUTPUT
		149181 CHECKSUMMED IN SOFTWARE
			55252 DATAGRAMS (11737549 BYTES) OVER IPV4
			93929 DATAGRAMS (20678079 BYTES) OVER IPV6
ICMP:
	1398 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED 'CUZ OLD MESSAGE WAS ICMP
	OUTPUT HISTOGRAM:
		ECHO REPLY: 38
		DESTINATION UNREACHABLE: 1398
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	1 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	0 MULTICAST ECHO REQUESTS IGNORED
	0 MULTICAST TIMESTAMP REQUESTS IGNORED
	INPUT HISTOGRAM:
		DESTINATION UNREACHABLE: 2007
		ECHO: 38
		ROUTER ADVERTISEMENT: 147
	38 MESSAGE RESPONSES GENERATED
	ICMP ADDRESS MASK RESPONSES ARE DISABLED
IGMP:
	1636 MESSAGES RECEIVED
	0 MESSAGE RECEIVED WITH TOO FEW BYTES
	0 MESSAGE RECEIVED WITH WRONG TTL
	0 MESSAGE RECEIVED WITH BAD CHECKSUM
	565 V1/V2 MEMBERSHIP QUERIES RECEIVED
	287 V3 MEMBERSHIP QUERIES RECEIVED
	0 MEMBERSHIP QUERIES RECEIVED WITH INVALID FIELD(S)
	834 GENERAL QUERIES RECEIVED
	18 GROUP QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES DROPPED
	784 MEMBERSHIP REPORTS RECEIVED
	0 MEMBERSHIP REPORT RECEIVED WITH INVALID FIELD(S)
	784 MEMBERSHIP REPORTS RECEIVED FOR GROUPS TO WHICH WE BELONG
	0 V3 REPORT RECEIVED WITHOUT ROUTER ALERT
	890 MEMBERSHIP REPORTS SENT
IPSEC:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
ARP:
	1532 BROADAST ARP REQUESTS SENT
	9 UNICAST ARP REQUESTS SENT
	3319 ARP REPLIES SENT
	0 ARP ANNOUNCEMENT SENT
	11629 ARP REQUESTS RECEIVED
	1280 ARP REPLIES RECEIVED
	12911 TOTAL ARP PACKETS RECEIVED
	0 ARP CONFLICT PROBE SENT
	0 INVALID ARP RESOLVE REQUEST
	0 TOTAL PACKET DROPPED DUE TO LACK OF MEMORY
	0 TOTAL PACKET HELD AWAITING ARP REPLY
	43 TOTAL PACKETS DROPPED DUE TO NO ARP ENTRY
	378 TOTAL PACKETS DROPPED DURING ARP ENTRY REMOVAL
	1410 ARP ENTRIES TIMED OUT
	0 DUPLICATE IP SEEN
MPTCP:
	0 DATA PACKET SENT
	0 DATA BYTE SENT
	0 DATA PACKET RECEIVED
	0 DATA BYTE RECEIVED
	0 PACKET WITH AN INVALID MPCAP OPTION
	0 PACKET WITH AN INVALID MPJOIN OPTION
	0 TIME PRIMARY SUBFLOW FELL BACK TO TCP
	0 TIME SECONDARY SUBFLOW FELL BACK TO TCP
	0 DSS OPTION DROP
	0 OTHER INVALID MPTCP OPTION
	0 TIME THE MPTCP SUBFLOW WINDOW WAS REDUCED
	0 BAD DSS CHECKSUM
	0 TIME RECEIVED OUT OF ORDER DATA 
	0 SUBFLOW SWITCH
	0 SUBFLOW SWITCH DUE TO ADVISORY
	0 SUBFLOW SWITCH DUE TO RTT
	0 SUBFLOW SWITCH DUE TO RTO
	0 SUBFLOW SWITCH DUE TO PEER
	0 NUMBER OF SUBFLOW PROBE
IP6:
	740728 TOTAL PACKETS RECEIVED
		0 WITH SIZE SMALLER THAN MINIMUM
		0 WITH DATA SIZE < DATA LENGTH
		0 WITH DATA SIZE > DATA LENGTH
			0 PACKET FORCED TO SOFTWARE CHECKSUM
		0 WITH BAD OPTIONS
		168 WITH INCORRECT VERSION NUMBER
		6 FRAGMENTS RECEIVED
			0 DROPPED (DUP OR OUT OF SPACE)
			0 DROPPED AFTER TIMEOUT
			0 EXCEEDED LIMIT
			3 REASSEMBLED OK
			0 ATOMIC FRAGMENTS RECEIVED
		667585 PACKETS FOR THIS HOST
		0 PACKET FORWARDED
		32498 PACKETS NOT FORWARDABLE
		0 REDIRECT SENT
		32441 MULTICAST PACKETS WHICH WE DON'T JOIN
		0 PACKET WHOSE HEADERS ARE NOT CONTINUOUS
		0 TUNNELING PACKET THAT CAN'T FIND GIF
		0 PACKET DISCARDED DUE TO TOO MAY HEADERS
		0 FORWARD CACHE HIT
		0 FORWARD CACHE MISS
		0 PACKET DROPPED DUE TO NO BUFS FOR CONTROL DATA
	341277 PACKETS SENT FROM THIS HOST
		0 PACKET SENT WITH FABRICATED IP HEADER
		0 OUTPUT PACKET DROPPED DUE TO NO BUFS, ETC.
		2291 OUTPUT PACKETS DISCARDED DUE TO NO ROUTE
		0 OUTPUT DATAGRAM FRAGMENTED
		0 FRAGMENT CREATED
		0 DATAGRAM THAT CAN'T BE FRAGMENTED
		0 PACKET THAT VIOLATED SCOPE RULES
		0 PACKET DROPPED DUE TO NECP POLICY
	INPUT HISTOGRAM:
		HOP BY HOP: 5616
		TCP: 422042
		UDP: 270582
		FRAGMENT: 6
		ICMP6: 41409
		PIM: 905
	MBUF STATISTICS:
		1787 ONE MBUF
		TWO OR MORE MBUF:
			LO0= 10326
			UTUN1= 12
		728603 ONE EXT MBUF
		0 TWO OR MORE EXT MBUF
		0 FAILURE OF SOURCE ADDRESS SELECTION
		SOURCE ADDRESSES ON AN OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES ON A NON-OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF SAME SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF A DIFFERENT SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		DEPRECATED SOURCE ADDRESSES
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESS SELECTION
			18129 RULES DEFAULT
			0 RULE PREFER SAME ADDRESS
			4861 RULES PREFER APPROPRIATE SCOPE
			0 RULE AVOID DEPRECATED ADDRESSES
			0 RULE PREFER HOME ADDRESSES
			0 RULE PREFER OUTGOING INTERFACE
			10 RULES PREFER MATCHING LABEL
			47351 RULES PREFER TEMPORARY ADDRESSES
			0 RULE PREFER ADDRESSES ON ALIVE INTERFACES
			0 RULE USE LONGEST MATCHING PREFIX
		0 DUPLICATE ADDRESS DETECTION COLLISION
		0 DUPLICATE ADDRESS DETECTION NS LOOP
		0 TIME IGNORED SOURCE ON SECONDARY EXPENSIVE I/F
ICMP6:
	1724 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED BECAUSE OLD MESSAGE WAS ICMP ERROR OR SO
	0 ERROR NOT GENERATED BECAUSE RATE LIMITATION
	OUTPUT HISTOGRAM:
		UNREACH: 1724
		MLDV1 LISTENER REPORT: 77
		MLDV1 LISTENER DONE: 11
		ROUTER SOLICITATION: 123
		NEIGHBOR SOLICITATION: 5185
		NEIGHBOR ADVERTISEMENT: 4403
		MLDV2 LISTENER REPORT: 1124
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	0 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	INPUT HISTOGRAM:
		UNREACH: 150
		MULTICAST LISTENER QUERY: 2002
		ROUTER ADVERTISEMENT: 29659
		NEIGHBOR SOLICITATION: 4403
		NEIGHBOR ADVERTISEMENT: 4332
	HISTOGRAM OF ERROR MESSAGES TO BE GENERATED:
		0 NO ROUTE
		0 ADMINISTRATIVELY PROHIBITED
		0 BEYOND SCOPE
		150 ADDRESS UNREACHABLE
		1574 PORT UNREACHABLE
		0 PACKET TOO BIG
		0 TIME EXCEED TRANSIT
		0 TIME EXCEED REASSEMBLY
		0 ERRONEOUS HEADER FIELD
		0 UNRECOGNIZED NEXT HEADER
		0 UNRECOGNIZED OPTION
		0 REDIRECT
		0 UNKNOWN
	0 MESSAGE RESPONSE GENERATED
	0 MESSAGE WITH TOO MANY ND OPTIONS
	0 MESSAGE WITH BAD ND OPTIONS
	0 BAD NEIGHBOR SOLICITATION MESSAGE
	0 BAD NEIGHBOR ADVERTISEMENT MESSAGE
	0 BAD ROUTER SOLICITATION MESSAGE
	0 BAD ROUTER ADVERTISEMENT MESSAGE
	0 BAD REDIRECT MESSAGE
	0 PATH MTU CHANGE
	0 DROPPED FRAGMENTED NDP MESSAGE
IPSEC6:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
RIP6:
	0 MESSAGE RECEIVED
	0 CHECKSUM CALCULATION ON INBOUND
	0 MESSAGE WITH BAD CHECKSUM
	0 MESSAGE DROPPED DUE TO NO SOCKET
	0 MULTICAST MESSAGE DROPPED DUE TO NO SOCKET
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	0 DELIVERED
	0 DATAGRAM OUTPUT
PFKEY:
	0 REQUEST SENT TO USERLAND
	0 BYTE SENT TO USERLAND
	0 MESSAGE WITH INVALID LENGTH FIELD
	0 MESSAGE WITH INVALID VERSION FIELD
	0 MESSAGE WITH INVALID MESSAGE TYPE FIELD
	0 MESSAGE TOO SHORT
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
	0 MESSAGE WITH DUPLICATE EXTENSION
	0 MESSAGE WITH INVALID EXTENSION TYPE
	0 MESSAGE WITH INVALID SA TYPE
	0 MESSAGE WITH INVALID ADDRESS EXTENSION
	0 REQUEST SENT FROM USERLAND
	0 BYTE SENT FROM USERLAND
	0 MESSAGE TOWARD SINGLE SOCKET
	0 MESSAGE TOWARD ALL SOCKETS
	0 MESSAGE TOWARD REGISTERED SOCKETS
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
KEVT:
	24 CURRENT KERNEL CONTROL SOCKETS
	18912 KERNEL CONTROL GENERATION COUNT
	0 BAD VENDOR FAILURE
	7302 MESSAGE TOO BIG FAILURES
	0 OUT OF MEMORY FAILURE
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	272613 MESSAGES POSTED
KCTL:
	0 TOTAL KERNEL CONTROL MODULE REGISTERED
	12 CURRENT KERNEL CONTROL MODULES REGISTERED
	55 CURRENT KERNEL CONTROL SOCKETS
	1111 KERNEL CONTROL GENERATION COUNT
	577 CONNECTION ATTEMPTS
	0 CONNECTION FAILURE
	35 SEND FAILURES
	0 SEND LIST FAILURE
	0 ENQUEUE FAILURE
	0 PACKET DROPPED DUE TO FULL SOCKET BUFFERS
XBKIDLE:
	1 MAX PER PROCESS
	600 MAXIMUM TIME (SECONDS)
	131072 HIGH WATER MARK
	0 SOCKET OPTION NOT SUPPORTED FAILURE
	0 TOO MANY SOCKETS FAILURE
	0 TOTAL SOCKET REQUESTED OK
	0 EXTENDED BK IDLE SOCKET
	0 NO CELLULAR FAILURE
	0 NO TIME FAILURES
	0 FORCED DEFUNCT SOCKET
	0 RESUMED SOCKET
	0 TIMEOUT EXPIRED FAILURE
	0 TIMER RESCHEDULED
	0 NO DELEGATED FAILURE
NET_API:
	2 INTERFACE FILTERS CURRENTLY ATTACHED
	2 INTERFACE FILTERS ATTACHED SINCE BOOT
	2 INTERFACE FILTERS ATTACHED SINCE BOOT BY OS
	0 IP FILTER CURRENTLY ATTACHED
	0 IP FILTER ATTACHED SINCE BOOT
	0 IP FILTER ATTACHED SINCE BOOT BY OS
	4 SOCKET FILTERS CURRENTLY ATTACHED
	4 SOCKET FILTERS ATTACHED SINCE BOOT
	4 SOCKET FILTERS ATTACHED SINCE BOOT BY OS
	325678 SOCKETS ALLOCATED SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL BY OS
	2458 SOCKETS WITH NECP CLIENT UUID SINCE BOOT
	104071 LOCAL DOMAIN SOCKETS ALLOCATED SINCE BOOT
	1199 ROUTE DOMAIN SOCKETS ALLOCATED SINCE BOOT
	124319 INET DOMAIN SOCKETS ALLOCATED SINCE BOOT
	59746 INET6 DOMAIN SOCKETS ALLOCATED SINCE BOOT
	10045 SYSTEM DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 MULTIPATH DOMAIN SOCKET ALLOCATED SINCE BOOT
	0 KEY DOMAIN SOCKET ALLOCATED SINCE BOOT
	5 NDRV DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 OTHER DOMAINS SOCKET ALLOCATED SINCE BOOT
	15536 IPV4 STREAM SOCKETS CREATED SINCE BOOT
	108783 IPV4 DATAGRAM SOCKETS CREATED SINCE BOOT
	10292 IPV4 DATAGRAM SOCKETS CONNECTED
	37978 IPV4 DNS SOCKETS
	102096 IPV4 DATAGRAM SOCKETS WITHOUT DATA
	7544 IPV6 STREAM SOCKETS CREATED SINCE BOOT
	52202 IPV6 DATAGRAM SOCKETS CREATED SINCE BOOT
	34793 IPV6 DATAGRAM SOCKETS CONNECTED
	0 IPV6 DNS SOCKET
	28179 IPV6 DATAGRAM SOCKETS WITHOUT DATA
	1115 SOCKET MULTICAST JOINS SINCE BOOT
	1115 SOCKET MULTICAST JOINS SINCE BOOT BY OS
	0 IPV4 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV4 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED
	12 INTERFACES ALLOCATED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED BY OS
	12 EXTENDED INTERFACES ALLOCATED SINCE BOOT BY OS
	2 PF ADDRULE OPERATIONS SINCE BOOT
	0 PF ADDRULE OPERATION SINCE BOOT BY OS
	0 VMNET START SINCE BOOT

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
TCP:
	0 PACKET SENT
		0 DATA PACKET (0 BYTE)
		0 DATA PACKET (0 BYTE) RETRANSMITTED
		0 RESEND INITIATED BY MTU DISCOVERY
		0 ACK-ONLY PACKET (0 DELAYED)
		0 URG ONLY PACKET
		0 WINDOW PROBE PACKET
		0 WINDOW UPDATE PACKET
		0 CONTROL PACKET
		0 DATA PACKET SENT AFTER FLOW CONTROL
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
	0 PACKET RECEIVED
		0 ACK (FOR 0 BYTE)
		0 DUPLICATE ACK
		0 ACK FOR UNSENT DATA
		0 PACKET (0 BYTE) RECEIVED IN-SEQUENCE
		0 COMPLETELY DUPLICATE PACKET (0 BYTE)
		0 OLD DUPLICATE PACKET
		0 RECEIVED PACKET DROPPED DUE TO LOW MEMORY
		0 PACKET WITH SOME DUP. DATA (0 BYTE DUPED)
		0 OUT-OF-ORDER PACKET (0 BYTE)
		0 PACKET (0 BYTE) OF DATA AFTER WINDOW
		0 WINDOW PROBE
		0 WINDOW UPDATE PACKET
		0 PACKET RECEIVED AFTER CLOSE
		0 BAD RESET
		0 DISCARDED FOR BAD CHECKSUM
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
		0 DISCARDED FOR BAD HEADER OFFSET FIELD
		0 DISCARDED BECAUSE PACKET TOO SHORT
	0 CONNECTION REQUEST
	0 CONNECTION ACCEPT
	0 BAD CONNECTION ATTEMPT
	0 LISTEN QUEUE OVERFLOW
	0 CONNECTION ESTABLISHED (INCLUDING ACCEPTS)
	0 CONNECTION CLOSED (INCLUDING 0 DROP)
		0 CONNECTION UPDATED CACHED RTT ON CLOSE
		0 CONNECTION UPDATED CACHED RTT VARIANCE ON CLOSE
		0 CONNECTION UPDATED CACHED SSTHRESH ON CLOSE
	0 EMBRYONIC CONNECTION DROPPED
	0 SEGMENT UPDATED RTT (OF 0 ATTEMPT)
	0 RETRANSMIT TIMEOUT
		0 CONNECTION DROPPED BY REXMIT TIMEOUT
		0 CONNECTION DROPPED AFTER RETRANSMITTING FIN
	0 PERSIST TIMEOUT
		0 CONNECTION DROPPED BY PERSIST TIMEOUT
	0 KEEPALIVE TIMEOUT
		0 KEEPALIVE PROBE SENT
		0 CONNECTION DROPPED BY KEEPALIVE
	0 CORRECT ACK HEADER PREDICTION
	0 CORRECT DATA PACKET HEADER PREDICTION
	0 SACK RECOVERY EPISODE
	0 SEGMENT REXMIT IN SACK RECOVERY EPISODES
	0 BYTE REXMIT IN SACK RECOVERY EPISODES
	0 SACK OPTION (SACK BLOCKS) RECEIVED
	0 SACK OPTION (SACK BLOCKS) SENT
	0 SACK SCOREBOARD OVERFLOW
	0 LRO COALESCED PACKET
		0 TIME LRO FLOW TABLE WAS FULL
		0 COLLISION IN LRO FLOW TABLE
		0 TIME LRO COALESCED 2 PACKETS
		0 TIME LRO COALESCED 3 OR 4 PACKETS
		0 TIME LRO COALESCED 5 OR MORE PACKETS
	0 LIMITED TRANSMIT DONE
	0 EARLY RETRANSMIT DONE
	0 TIME CUMULATIVE ACK ADVANCED ALONG WITH SACK
	0 PROBE TIMEOUT
		0 TIME RETRANSMIT TIMEOUT TRIGGERED AFTER PROBE
		0 TIME PROBE PACKETS WERE SENT FOR AN INTERFACE
		0 TIME COULDN'T SEND PROBE PACKETS FOR AN INTERFACE
		0 TIME FAST RECOVERY AFTER TAIL LOSS
		0 TIME RECOVERED LAST PACKET 
		0 SACK BASED RESCUE RETRANSMIT
	0 CLIENT CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 CLIENT CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME GRACEFUL FALLBACK TO NON-ECN CONNECTION
		0 TIME LOST ECN NEGOTIATING SYN, FOLLOWED BY RETRANSMISSION
		0 SERVER CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 SERVER CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME LOST ECN NEGOTIATING SYN-ACK, FOLLOWED BY RETRANSMISSION
		0 TIME RECEIVED CONGESTION EXPERIENCED (CE) NOTIFICATION
		0 TIME CWR WAS SENT IN RESPONSE TO ECE
		0 TIME SENT ECE NOTIFICATION
		0 CONNECTION RECEIVED CE ATLEAST ONCE
		0 CONNECTION RECEIVED ECE ATLEAST ONCE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS BUT NO CE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS AND CE
		0 CONNECTION USING ECN RECEIVED CE BUT NO PACKET LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO SYN-LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO REORDERING
		0 CONNECTION FELL BACK TO NON-ECN DUE TO EXCESSIVE CE-MARKINGS
	0 TIME PACKET REORDERING WAS DETECTED ON A CONNECTION
		0 TIME TRANSMITTED PACKETS WERE REORDERED
		0 TIME FAST RECOVERY WAS DELAYED TO HANDLE REORDERING
		0 TIME RETRANSMISSION WAS AVOIDED BY DELAYING RECOVERY
		0 RETRANSMISSION NOT NEEDED 
	0 TIME DSACK OPTION WAS SENT
		0 TIME DSACK OPTION WAS RECEIVED
		0 TIME DSACK WAS DISABLED ON A CONNECTION
		0 TIME RECOVERED FROM BAD RETRANSMISSION USING DSACK
		0 TIME IGNORED DSACK DUE TO ACK LOSS
		0 TIME IGNORED OLD DSACK OPTIONS
	0 TIME PMTU BLACKHOLE DETECTION, SIZE REVERTED
	0 CONNECTION WERE DROPPED AFTER LONG SLEEP
	0 TIME A TFO-COOKIE HAS BEEN ANNOUNCED
	0 SYN WITH DATA AND A VALID TFO-COOKIE HAVE BEEN RECEIVED
	0 SYN WITH TFO-COOKIE-REQUEST RECEIVED
	0 TIME AN INVALID TFO-COOKIE HAS BEEN RECEIVED
	0 TIME WE REQUESTED A TFO-COOKIE
		0 TIME THE PEER ANNOUNCED A TFO-COOKIE
	0 TIME WE COMBINED SYN WITH DATA AND A TFO-COOKIE
		0 TIME OUR SYN WITH DATA HAS BEEN ACKNOWLEDGED
	0 TIME A CONNECTION-ATTEMPT WITH TFO FELL BACK TO REGULAR TCP
	0 TIME A TFO-CONNECTION BLACKHOLE'D
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO DEFAULT
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO MEDIUM
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO LOW
	0 TIMER DRIFT LESS OR EQUAL TO 1 MS
	0 TIMER DRIFT LESS OR EQUAL TO 10 MS
	0 TIMER DRIFT LESS OR EQUAL TO 20 MS
	0 TIMER DRIFT LESS OR EQUAL TO 50 MS
	0 TIMER DRIFT LESS OR EQUAL TO 100 MS
	0 TIMER DRIFT LESS OR EQUAL TO 200 MS
	0 TIMER DRIFT LESS OR EQUAL TO 500 MS
	0 TIMER DRIFT LESS OR EQUAL TO 1000 MS
	0 TIMER DRIFT GREATER THAN TO 1000 MS
UDP:
	507166 DATAGRAMS RECEIVED
		0 WITH INCOMPLETE HEADER
		0 WITH BAD DATA LENGTH FIELD
		0 WITH BAD CHECKSUM
		54 WITH NO CHECKSUM
		475967 CHECKSUMMED IN SOFTWARE
			238930 DATAGRAMS (76206215 BYTES) OVER IPV4
			237037 DATAGRAMS (106264705 BYTES) OVER IPV6
		5345 DROPPED DUE TO NO SOCKET
		3618 BROADCAST/MULTICAST DATAGRAMS UNDELIVERED
		0 TIME MULTICAST SOURCE FILTER MATCHED
		1 DROPPED DUE TO FULL SOCKET BUFFERS
		0 NOT FOR HASHED PCB
		498202 DELIVERED
	142296 DATAGRAMS OUTPUT
		149296 CHECKSUMMED IN SOFTWARE
			55329 DATAGRAMS (11759797 BYTES) OVER IPV4
			93967 DATAGRAMS (20688140 BYTES) OVER IPV6
ICMP:
	1398 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED 'CUZ OLD MESSAGE WAS ICMP
	OUTPUT HISTOGRAM:
		ECHO REPLY: 38
		DESTINATION UNREACHABLE: 1398
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	1 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	0 MULTICAST ECHO REQUESTS IGNORED
	0 MULTICAST TIMESTAMP REQUESTS IGNORED
	INPUT HISTOGRAM:
		DESTINATION UNREACHABLE: 2007
		ECHO: 38
		ROUTER ADVERTISEMENT: 147
	38 MESSAGE RESPONSES GENERATED
	ICMP ADDRESS MASK RESPONSES ARE DISABLED
IGMP:
	1636 MESSAGES RECEIVED
	0 MESSAGE RECEIVED WITH TOO FEW BYTES
	0 MESSAGE RECEIVED WITH WRONG TTL
	0 MESSAGE RECEIVED WITH BAD CHECKSUM
	565 V1/V2 MEMBERSHIP QUERIES RECEIVED
	287 V3 MEMBERSHIP QUERIES RECEIVED
	0 MEMBERSHIP QUERIES RECEIVED WITH INVALID FIELD(S)
	834 GENERAL QUERIES RECEIVED
	18 GROUP QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES DROPPED
	784 MEMBERSHIP REPORTS RECEIVED
	0 MEMBERSHIP REPORT RECEIVED WITH INVALID FIELD(S)
	784 MEMBERSHIP REPORTS RECEIVED FOR GROUPS TO WHICH WE BELONG
	0 V3 REPORT RECEIVED WITHOUT ROUTER ALERT
	890 MEMBERSHIP REPORTS SENT
IPSEC:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
ARP:
	1538 BROADAST ARP REQUESTS SENT
	9 UNICAST ARP REQUESTS SENT
	3320 ARP REPLIES SENT
	0 ARP ANNOUNCEMENT SENT
	11630 ARP REQUESTS RECEIVED
	1286 ARP REPLIES RECEIVED
	12918 TOTAL ARP PACKETS RECEIVED
	0 ARP CONFLICT PROBE SENT
	0 INVALID ARP RESOLVE REQUEST
	0 TOTAL PACKET DROPPED DUE TO LACK OF MEMORY
	0 TOTAL PACKET HELD AWAITING ARP REPLY
	43 TOTAL PACKETS DROPPED DUE TO NO ARP ENTRY
	378 TOTAL PACKETS DROPPED DURING ARP ENTRY REMOVAL
	1410 ARP ENTRIES TIMED OUT
	0 DUPLICATE IP SEEN
MPTCP:
	0 DATA PACKET SENT
	0 DATA BYTE SENT
	0 DATA PACKET RECEIVED
	0 DATA BYTE RECEIVED
	0 PACKET WITH AN INVALID MPCAP OPTION
	0 PACKET WITH AN INVALID MPJOIN OPTION
	0 TIME PRIMARY SUBFLOW FELL BACK TO TCP
	0 TIME SECONDARY SUBFLOW FELL BACK TO TCP
	0 DSS OPTION DROP
	0 OTHER INVALID MPTCP OPTION
	0 TIME THE MPTCP SUBFLOW WINDOW WAS REDUCED
	0 BAD DSS CHECKSUM
	0 TIME RECEIVED OUT OF ORDER DATA 
	0 SUBFLOW SWITCH
	0 SUBFLOW SWITCH DUE TO ADVISORY
	0 SUBFLOW SWITCH DUE TO RTT
	0 SUBFLOW SWITCH DUE TO RTO
	0 SUBFLOW SWITCH DUE TO PEER
	0 NUMBER OF SUBFLOW PROBE
IP6:
	742035 TOTAL PACKETS RECEIVED
		0 WITH SIZE SMALLER THAN MINIMUM
		0 WITH DATA SIZE < DATA LENGTH
		0 WITH DATA SIZE > DATA LENGTH
			0 PACKET FORCED TO SOFTWARE CHECKSUM
		0 WITH BAD OPTIONS
		168 WITH INCORRECT VERSION NUMBER
		6 FRAGMENTS RECEIVED
			0 DROPPED (DUP OR OUT OF SPACE)
			0 DROPPED AFTER TIMEOUT
			0 EXCEEDED LIMIT
			3 REASSEMBLED OK
			0 ATOMIC FRAGMENTS RECEIVED
		668708 PACKETS FOR THIS HOST
		0 PACKET FORWARDED
		32636 PACKETS NOT FORWARDABLE
		0 REDIRECT SENT
		32579 MULTICAST PACKETS WHICH WE DON'T JOIN
		0 PACKET WHOSE HEADERS ARE NOT CONTINUOUS
		0 TUNNELING PACKET THAT CAN'T FIND GIF
		0 PACKET DISCARDED DUE TO TOO MAY HEADERS
		0 FORWARD CACHE HIT
		0 FORWARD CACHE MISS
		0 PACKET DROPPED DUE TO NO BUFS FOR CONTROL DATA
	341550 PACKETS SENT FROM THIS HOST
		0 PACKET SENT WITH FABRICATED IP HEADER
		0 OUTPUT PACKET DROPPED DUE TO NO BUFS, ETC.
		2291 OUTPUT PACKETS DISCARDED DUE TO NO ROUTE
		0 OUTPUT DATAGRAM FRAGMENTED
		0 FRAGMENT CREATED
		0 DATAGRAM THAT CAN'T BE FRAGMENTED
		0 PACKET THAT VIOLATED SCOPE RULES
		0 PACKET DROPPED DUE TO NECP POLICY
	INPUT HISTOGRAM:
		HOP BY HOP: 5622
		TCP: 422266
		UDP: 271607
		FRAGMENT: 6
		ICMP6: 41455
		PIM: 911
	MBUF STATISTICS:
		1787 ONE MBUF
		TWO OR MORE MBUF:
			LO0= 10340
			UTUN1= 12
		729896 ONE EXT MBUF
		0 TWO OR MORE EXT MBUF
		0 FAILURE OF SOURCE ADDRESS SELECTION
		SOURCE ADDRESSES ON AN OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES ON A NON-OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF SAME SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF A DIFFERENT SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		DEPRECATED SOURCE ADDRESSES
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESS SELECTION
			18148 RULES DEFAULT
			0 RULE PREFER SAME ADDRESS
			4885 RULES PREFER APPROPRIATE SCOPE
			0 RULE AVOID DEPRECATED ADDRESSES
			0 RULE PREFER HOME ADDRESSES
			0 RULE PREFER OUTGOING INTERFACE
			10 RULES PREFER MATCHING LABEL
			47351 RULES PREFER TEMPORARY ADDRESSES
			0 RULE PREFER ADDRESSES ON ALIVE INTERFACES
			0 RULE USE LONGEST MATCHING PREFIX
		0 DUPLICATE ADDRESS DETECTION COLLISION
		0 DUPLICATE ADDRESS DETECTION NS LOOP
		0 TIME IGNORED SOURCE ON SECONDARY EXPENSIVE I/F
ICMP6:
	1725 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED BECAUSE OLD MESSAGE WAS ICMP ERROR OR SO
	0 ERROR NOT GENERATED BECAUSE RATE LIMITATION
	OUTPUT HISTOGRAM:
		UNREACH: 1725
		MLDV1 LISTENER REPORT: 77
		MLDV1 LISTENER DONE: 11
		ROUTER SOLICITATION: 123
		NEIGHBOR SOLICITATION: 5189
		NEIGHBOR ADVERTISEMENT: 4403
		MLDV2 LISTENER REPORT: 1124
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	0 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	INPUT HISTOGRAM:
		UNREACH: 150
		MULTICAST LISTENER QUERY: 2002
		ROUTER ADVERTISEMENT: 29701
		NEIGHBOR SOLICITATION: 4403
		NEIGHBOR ADVERTISEMENT: 4336
	HISTOGRAM OF ERROR MESSAGES TO BE GENERATED:
		0 NO ROUTE
		0 ADMINISTRATIVELY PROHIBITED
		0 BEYOND SCOPE
		150 ADDRESS UNREACHABLE
		1575 PORT UNREACHABLE
		0 PACKET TOO BIG
		0 TIME EXCEED TRANSIT
		0 TIME EXCEED REASSEMBLY
		0 ERRONEOUS HEADER FIELD
		0 UNRECOGNIZED NEXT HEADER
		0 UNRECOGNIZED OPTION
		0 REDIRECT
		0 UNKNOWN
	0 MESSAGE RESPONSE GENERATED
	0 MESSAGE WITH TOO MANY ND OPTIONS
	0 MESSAGE WITH BAD ND OPTIONS
	0 BAD NEIGHBOR SOLICITATION MESSAGE
	0 BAD NEIGHBOR ADVERTISEMENT MESSAGE
	0 BAD ROUTER SOLICITATION MESSAGE
	0 BAD ROUTER ADVERTISEMENT MESSAGE
	0 BAD REDIRECT MESSAGE
	0 PATH MTU CHANGE
	0 DROPPED FRAGMENTED NDP MESSAGE
IPSEC6:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
RIP6:
	0 MESSAGE RECEIVED
	0 CHECKSUM CALCULATION ON INBOUND
	0 MESSAGE WITH BAD CHECKSUM
	0 MESSAGE DROPPED DUE TO NO SOCKET
	0 MULTICAST MESSAGE DROPPED DUE TO NO SOCKET
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	0 DELIVERED
	0 DATAGRAM OUTPUT
PFKEY:
	0 REQUEST SENT TO USERLAND
	0 BYTE SENT TO USERLAND
	0 MESSAGE WITH INVALID LENGTH FIELD
	0 MESSAGE WITH INVALID VERSION FIELD
	0 MESSAGE WITH INVALID MESSAGE TYPE FIELD
	0 MESSAGE TOO SHORT
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
	0 MESSAGE WITH DUPLICATE EXTENSION
	0 MESSAGE WITH INVALID EXTENSION TYPE
	0 MESSAGE WITH INVALID SA TYPE
	0 MESSAGE WITH INVALID ADDRESS EXTENSION
	0 REQUEST SENT FROM USERLAND
	0 BYTE SENT FROM USERLAND
	0 MESSAGE TOWARD SINGLE SOCKET
	0 MESSAGE TOWARD ALL SOCKETS
	0 MESSAGE TOWARD REGISTERED SOCKETS
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
KEVT:
	24 CURRENT KERNEL CONTROL SOCKETS
	18912 KERNEL CONTROL GENERATION COUNT
	0 BAD VENDOR FAILURE
	7310 MESSAGE TOO BIG FAILURES
	0 OUT OF MEMORY FAILURE
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	272697 MESSAGES POSTED
KCTL:
	0 TOTAL KERNEL CONTROL MODULE REGISTERED
	12 CURRENT KERNEL CONTROL MODULES REGISTERED
	55 CURRENT KERNEL CONTROL SOCKETS
	1111 KERNEL CONTROL GENERATION COUNT
	577 CONNECTION ATTEMPTS
	0 CONNECTION FAILURE
	35 SEND FAILURES
	0 SEND LIST FAILURE
	0 ENQUEUE FAILURE
	0 PACKET DROPPED DUE TO FULL SOCKET BUFFERS
XBKIDLE:
	1 MAX PER PROCESS
	600 MAXIMUM TIME (SECONDS)
	131072 HIGH WATER MARK
	0 SOCKET OPTION NOT SUPPORTED FAILURE
	0 TOO MANY SOCKETS FAILURE
	0 TOTAL SOCKET REQUESTED OK
	0 EXTENDED BK IDLE SOCKET
	0 NO CELLULAR FAILURE
	0 NO TIME FAILURES
	0 FORCED DEFUNCT SOCKET
	0 RESUMED SOCKET
	0 TIMEOUT EXPIRED FAILURE
	0 TIMER RESCHEDULED
	0 NO DELEGATED FAILURE
NET_API:
	2 INTERFACE FILTERS CURRENTLY ATTACHED
	2 INTERFACE FILTERS ATTACHED SINCE BOOT
	2 INTERFACE FILTERS ATTACHED SINCE BOOT BY OS
	0 IP FILTER CURRENTLY ATTACHED
	0 IP FILTER ATTACHED SINCE BOOT
	0 IP FILTER ATTACHED SINCE BOOT BY OS
	4 SOCKET FILTERS CURRENTLY ATTACHED
	4 SOCKET FILTERS ATTACHED SINCE BOOT
	4 SOCKET FILTERS ATTACHED SINCE BOOT BY OS
	325774 SOCKETS ALLOCATED SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL BY OS
	2460 SOCKETS WITH NECP CLIENT UUID SINCE BOOT
	104111 LOCAL DOMAIN SOCKETS ALLOCATED SINCE BOOT
	1199 ROUTE DOMAIN SOCKETS ALLOCATED SINCE BOOT
	124329 INET DOMAIN SOCKETS ALLOCATED SINCE BOOT
	59766 INET6 DOMAIN SOCKETS ALLOCATED SINCE BOOT
	10045 SYSTEM DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 MULTIPATH DOMAIN SOCKET ALLOCATED SINCE BOOT
	0 KEY DOMAIN SOCKET ALLOCATED SINCE BOOT
	5 NDRV DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 OTHER DOMAINS SOCKET ALLOCATED SINCE BOOT
	15537 IPV4 STREAM SOCKETS CREATED SINCE BOOT
	108792 IPV4 DATAGRAM SOCKETS CREATED SINCE BOOT
	10292 IPV4 DATAGRAM SOCKETS CONNECTED
	37993 IPV4 DNS SOCKETS
	102104 IPV4 DATAGRAM SOCKETS WITHOUT DATA
	7548 IPV6 STREAM SOCKETS CREATED SINCE BOOT
	52218 IPV6 DATAGRAM SOCKETS CREATED SINCE BOOT
	34800 IPV6 DATAGRAM SOCKETS CONNECTED
	0 IPV6 DNS SOCKET
	28187 IPV6 DATAGRAM SOCKETS WITHOUT DATA
	1115 SOCKET MULTICAST JOINS SINCE BOOT
	1115 SOCKET MULTICAST JOINS SINCE BOOT BY OS
	0 IPV4 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV4 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED
	12 INTERFACES ALLOCATED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED BY OS
	12 EXTENDED INTERFACES ALLOCATED SINCE BOOT BY OS
	2 PF ADDRULE OPERATIONS SINCE BOOT
	0 PF ADDRULE OPERATION SINCE BOOT BY OS
	0 VMNET START SINCE BOOT

PING ORIGIN-WWW.CISCO.COM (72.163.4.161): 56 DATA BYTES
64 BYTES FROM 72.163.4.161: ICMP_SEQ=0 TTL=243 TIME=43.418 MS
64 BYTES FROM 72.163.4.161: ICMP_SEQ=1 TTL=243 TIME=44.409 MS
64 BYTES FROM 72.163.4.161: ICMP_SEQ=2 TTL=243 TIME=43.536 MS

--- ORIGIN-WWW.CISCO.COM PING STATISTICS ---
3 PACKETS TRANSMITTED, 3 PACKETS RECEIVED, 0.0% PACKET LOSS
ROUND-TRIP MIN/AVG/MAX/STDDEV = 43.418/43.788/44.409/0.442 MS

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
TCP:
	0 PACKET SENT
		0 DATA PACKET (0 BYTE)
		0 DATA PACKET (0 BYTE) RETRANSMITTED
		0 RESEND INITIATED BY MTU DISCOVERY
		0 ACK-ONLY PACKET (0 DELAYED)
		0 URG ONLY PACKET
		0 WINDOW PROBE PACKET
		0 WINDOW UPDATE PACKET
		0 CONTROL PACKET
		0 DATA PACKET SENT AFTER FLOW CONTROL
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
	0 PACKET RECEIVED
		0 ACK (FOR 0 BYTE)
		0 DUPLICATE ACK
		0 ACK FOR UNSENT DATA
		0 PACKET (0 BYTE) RECEIVED IN-SEQUENCE
		0 COMPLETELY DUPLICATE PACKET (0 BYTE)
		0 OLD DUPLICATE PACKET
		0 RECEIVED PACKET DROPPED DUE TO LOW MEMORY
		0 PACKET WITH SOME DUP. DATA (0 BYTE DUPED)
		0 OUT-OF-ORDER PACKET (0 BYTE)
		0 PACKET (0 BYTE) OF DATA AFTER WINDOW
		0 WINDOW PROBE
		0 WINDOW UPDATE PACKET
		0 PACKET RECEIVED AFTER CLOSE
		0 BAD RESET
		0 DISCARDED FOR BAD CHECKSUM
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
		0 DISCARDED FOR BAD HEADER OFFSET FIELD
		0 DISCARDED BECAUSE PACKET TOO SHORT
	0 CONNECTION REQUEST
	0 CONNECTION ACCEPT
	0 BAD CONNECTION ATTEMPT
	0 LISTEN QUEUE OVERFLOW
	0 CONNECTION ESTABLISHED (INCLUDING ACCEPTS)
	0 CONNECTION CLOSED (INCLUDING 0 DROP)
		0 CONNECTION UPDATED CACHED RTT ON CLOSE
		0 CONNECTION UPDATED CACHED RTT VARIANCE ON CLOSE
		0 CONNECTION UPDATED CACHED SSTHRESH ON CLOSE
	0 EMBRYONIC CONNECTION DROPPED
	0 SEGMENT UPDATED RTT (OF 0 ATTEMPT)
	0 RETRANSMIT TIMEOUT
		0 CONNECTION DROPPED BY REXMIT TIMEOUT
		0 CONNECTION DROPPED AFTER RETRANSMITTING FIN
	0 PERSIST TIMEOUT
		0 CONNECTION DROPPED BY PERSIST TIMEOUT
	0 KEEPALIVE TIMEOUT
		0 KEEPALIVE PROBE SENT
		0 CONNECTION DROPPED BY KEEPALIVE
	0 CORRECT ACK HEADER PREDICTION
	0 CORRECT DATA PACKET HEADER PREDICTION
	0 SACK RECOVERY EPISODE
	0 SEGMENT REXMIT IN SACK RECOVERY EPISODES
	0 BYTE REXMIT IN SACK RECOVERY EPISODES
	0 SACK OPTION (SACK BLOCKS) RECEIVED
	0 SACK OPTION (SACK BLOCKS) SENT
	0 SACK SCOREBOARD OVERFLOW
	0 LRO COALESCED PACKET
		0 TIME LRO FLOW TABLE WAS FULL
		0 COLLISION IN LRO FLOW TABLE
		0 TIME LRO COALESCED 2 PACKETS
		0 TIME LRO COALESCED 3 OR 4 PACKETS
		0 TIME LRO COALESCED 5 OR MORE PACKETS
	0 LIMITED TRANSMIT DONE
	0 EARLY RETRANSMIT DONE
	0 TIME CUMULATIVE ACK ADVANCED ALONG WITH SACK
	0 PROBE TIMEOUT
		0 TIME RETRANSMIT TIMEOUT TRIGGERED AFTER PROBE
		0 TIME PROBE PACKETS WERE SENT FOR AN INTERFACE
		0 TIME COULDN'T SEND PROBE PACKETS FOR AN INTERFACE
		0 TIME FAST RECOVERY AFTER TAIL LOSS
		0 TIME RECOVERED LAST PACKET 
		0 SACK BASED RESCUE RETRANSMIT
	0 CLIENT CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 CLIENT CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME GRACEFUL FALLBACK TO NON-ECN CONNECTION
		0 TIME LOST ECN NEGOTIATING SYN, FOLLOWED BY RETRANSMISSION
		0 SERVER CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 SERVER CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME LOST ECN NEGOTIATING SYN-ACK, FOLLOWED BY RETRANSMISSION
		0 TIME RECEIVED CONGESTION EXPERIENCED (CE) NOTIFICATION
		0 TIME CWR WAS SENT IN RESPONSE TO ECE
		0 TIME SENT ECE NOTIFICATION
		0 CONNECTION RECEIVED CE ATLEAST ONCE
		0 CONNECTION RECEIVED ECE ATLEAST ONCE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS BUT NO CE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS AND CE
		0 CONNECTION USING ECN RECEIVED CE BUT NO PACKET LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO SYN-LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO REORDERING
		0 CONNECTION FELL BACK TO NON-ECN DUE TO EXCESSIVE CE-MARKINGS
	0 TIME PACKET REORDERING WAS DETECTED ON A CONNECTION
		0 TIME TRANSMITTED PACKETS WERE REORDERED
		0 TIME FAST RECOVERY WAS DELAYED TO HANDLE REORDERING
		0 TIME RETRANSMISSION WAS AVOIDED BY DELAYING RECOVERY
		0 RETRANSMISSION NOT NEEDED 
	0 TIME DSACK OPTION WAS SENT
		0 TIME DSACK OPTION WAS RECEIVED
		0 TIME DSACK WAS DISABLED ON A CONNECTION
		0 TIME RECOVERED FROM BAD RETRANSMISSION USING DSACK
		0 TIME IGNORED DSACK DUE TO ACK LOSS
		0 TIME IGNORED OLD DSACK OPTIONS
	0 TIME PMTU BLACKHOLE DETECTION, SIZE REVERTED
	0 CONNECTION WERE DROPPED AFTER LONG SLEEP
	0 TIME A TFO-COOKIE HAS BEEN ANNOUNCED
	0 SYN WITH DATA AND A VALID TFO-COOKIE HAVE BEEN RECEIVED
	0 SYN WITH TFO-COOKIE-REQUEST RECEIVED
	0 TIME AN INVALID TFO-COOKIE HAS BEEN RECEIVED
	0 TIME WE REQUESTED A TFO-COOKIE
		0 TIME THE PEER ANNOUNCED A TFO-COOKIE
	0 TIME WE COMBINED SYN WITH DATA AND A TFO-COOKIE
		0 TIME OUR SYN WITH DATA HAS BEEN ACKNOWLEDGED
	0 TIME A CONNECTION-ATTEMPT WITH TFO FELL BACK TO REGULAR TCP
	0 TIME A TFO-CONNECTION BLACKHOLE'D
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO DEFAULT
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO MEDIUM
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO LOW
	0 TIMER DRIFT LESS OR EQUAL TO 1 MS
	0 TIMER DRIFT LESS OR EQUAL TO 10 MS
	0 TIMER DRIFT LESS OR EQUAL TO 20 MS
	0 TIMER DRIFT LESS OR EQUAL TO 50 MS
	0 TIMER DRIFT LESS OR EQUAL TO 100 MS
	0 TIMER DRIFT LESS OR EQUAL TO 200 MS
	0 TIMER DRIFT LESS OR EQUAL TO 500 MS
	0 TIMER DRIFT LESS OR EQUAL TO 1000 MS
	0 TIMER DRIFT GREATER THAN TO 1000 MS
UDP:
	510547 DATAGRAMS RECEIVED
		0 WITH INCOMPLETE HEADER
		0 WITH BAD DATA LENGTH FIELD
		0 WITH BAD CHECKSUM
		54 WITH NO CHECKSUM
		479276 CHECKSUMMED IN SOFTWARE
			240811 DATAGRAMS (76740696 BYTES) OVER IPV4
			238465 DATAGRAMS (106705832 BYTES) OVER IPV6
		5345 DROPPED DUE TO NO SOCKET
		3618 BROADCAST/MULTICAST DATAGRAMS UNDELIVERED
		0 TIME MULTICAST SOURCE FILTER MATCHED
		1 DROPPED DUE TO FULL SOCKET BUFFERS
		0 NOT FOR HASHED PCB
		501583 DELIVERED
	142462 DATAGRAMS OUTPUT
		149491 CHECKSUMMED IN SOFTWARE
			55451 DATAGRAMS (11792685 BYTES) OVER IPV4
			94040 DATAGRAMS (20706468 BYTES) OVER IPV6
ICMP:
	1398 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED 'CUZ OLD MESSAGE WAS ICMP
	OUTPUT HISTOGRAM:
		ECHO REPLY: 38
		DESTINATION UNREACHABLE: 1398
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	1 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	0 MULTICAST ECHO REQUESTS IGNORED
	0 MULTICAST TIMESTAMP REQUESTS IGNORED
	INPUT HISTOGRAM:
		ECHO REPLY: 3
		DESTINATION UNREACHABLE: 2007
		ECHO: 38
		ROUTER ADVERTISEMENT: 147
	38 MESSAGE RESPONSES GENERATED
	ICMP ADDRESS MASK RESPONSES ARE DISABLED
IGMP:
	1636 MESSAGES RECEIVED
	0 MESSAGE RECEIVED WITH TOO FEW BYTES
	0 MESSAGE RECEIVED WITH WRONG TTL
	0 MESSAGE RECEIVED WITH BAD CHECKSUM
	565 V1/V2 MEMBERSHIP QUERIES RECEIVED
	287 V3 MEMBERSHIP QUERIES RECEIVED
	0 MEMBERSHIP QUERIES RECEIVED WITH INVALID FIELD(S)
	834 GENERAL QUERIES RECEIVED
	18 GROUP QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES DROPPED
	784 MEMBERSHIP REPORTS RECEIVED
	0 MEMBERSHIP REPORT RECEIVED WITH INVALID FIELD(S)
	784 MEMBERSHIP REPORTS RECEIVED FOR GROUPS TO WHICH WE BELONG
	0 V3 REPORT RECEIVED WITHOUT ROUTER ALERT
	890 MEMBERSHIP REPORTS SENT
IPSEC:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
ARP:
	1544 BROADAST ARP REQUESTS SENT
	9 UNICAST ARP REQUESTS SENT
	3320 ARP REPLIES SENT
	0 ARP ANNOUNCEMENT SENT
	11630 ARP REQUESTS RECEIVED
	1292 ARP REPLIES RECEIVED
	12924 TOTAL ARP PACKETS RECEIVED
	0 ARP CONFLICT PROBE SENT
	0 INVALID ARP RESOLVE REQUEST
	0 TOTAL PACKET DROPPED DUE TO LACK OF MEMORY
	0 TOTAL PACKET HELD AWAITING ARP REPLY
	43 TOTAL PACKETS DROPPED DUE TO NO ARP ENTRY
	378 TOTAL PACKETS DROPPED DURING ARP ENTRY REMOVAL
	1425 ARP ENTRIES TIMED OUT
	0 DUPLICATE IP SEEN
MPTCP:
	0 DATA PACKET SENT
	0 DATA BYTE SENT
	0 DATA PACKET RECEIVED
	0 DATA BYTE RECEIVED
	0 PACKET WITH AN INVALID MPCAP OPTION
	0 PACKET WITH AN INVALID MPJOIN OPTION
	0 TIME PRIMARY SUBFLOW FELL BACK TO TCP
	0 TIME SECONDARY SUBFLOW FELL BACK TO TCP
	0 DSS OPTION DROP
	0 OTHER INVALID MPTCP OPTION
	0 TIME THE MPTCP SUBFLOW WINDOW WAS REDUCED
	0 BAD DSS CHECKSUM
	0 TIME RECEIVED OUT OF ORDER DATA 
	0 SUBFLOW SWITCH
	0 SUBFLOW SWITCH DUE TO ADVISORY
	0 SUBFLOW SWITCH DUE TO RTT
	0 SUBFLOW SWITCH DUE TO RTO
	0 SUBFLOW SWITCH DUE TO PEER
	0 NUMBER OF SUBFLOW PROBE
IP6:
	743937 TOTAL PACKETS RECEIVED
		0 WITH SIZE SMALLER THAN MINIMUM
		0 WITH DATA SIZE < DATA LENGTH
		0 WITH DATA SIZE > DATA LENGTH
			0 PACKET FORCED TO SOFTWARE CHECKSUM
		0 WITH BAD OPTIONS
		168 WITH INCORRECT VERSION NUMBER
		6 FRAGMENTS RECEIVED
			0 DROPPED (DUP OR OUT OF SPACE)
			0 DROPPED AFTER TIMEOUT
			0 EXCEEDED LIMIT
			3 REASSEMBLED OK
			0 ATOMIC FRAGMENTS RECEIVED
		670439 PACKETS FOR THIS HOST
		0 PACKET FORWARDED
		32747 PACKETS NOT FORWARDABLE
		0 REDIRECT SENT
		32690 MULTICAST PACKETS WHICH WE DON'T JOIN
		0 PACKET WHOSE HEADERS ARE NOT CONTINUOUS
		0 TUNNELING PACKET THAT CAN'T FIND GIF
		0 PACKET DISCARDED DUE TO TOO MAY HEADERS
		0 FORWARD CACHE HIT
		0 FORWARD CACHE MISS
		0 PACKET DROPPED DUE TO NO BUFS FOR CONTROL DATA
	341917 PACKETS SENT FROM THIS HOST
		0 PACKET SENT WITH FABRICATED IP HEADER
		0 OUTPUT PACKET DROPPED DUE TO NO BUFS, ETC.
		2291 OUTPUT PACKETS DISCARDED DUE TO NO ROUTE
		0 OUTPUT DATAGRAM FRAGMENTED
		0 FRAGMENT CREATED
		0 DATAGRAM THAT CAN'T BE FRAGMENTED
		0 PACKET THAT VIOLATED SCOPE RULES
		0 PACKET DROPPED DUE TO NECP POLICY
	INPUT HISTOGRAM:
		HOP BY HOP: 5629
		TCP: 422540
		UDP: 273165
		FRAGMENT: 6
		ICMP6: 41510
		PIM: 919
	MBUF STATISTICS:
		1787 ONE MBUF
		TWO OR MORE MBUF:
			LO0= 10369
			UTUN1= 12
		731769 ONE EXT MBUF
		0 TWO OR MORE EXT MBUF
		0 FAILURE OF SOURCE ADDRESS SELECTION
		SOURCE ADDRESSES ON AN OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES ON A NON-OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF SAME SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF A DIFFERENT SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		DEPRECATED SOURCE ADDRESSES
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESS SELECTION
			18185 RULES DEFAULT
			0 RULE PREFER SAME ADDRESS
			4924 RULES PREFER APPROPRIATE SCOPE
			0 RULE AVOID DEPRECATED ADDRESSES
			0 RULE PREFER HOME ADDRESSES
			0 RULE PREFER OUTGOING INTERFACE
			10 RULES PREFER MATCHING LABEL
			47351 RULES PREFER TEMPORARY ADDRESSES
			0 RULE PREFER ADDRESSES ON ALIVE INTERFACES
			0 RULE USE LONGEST MATCHING PREFIX
		0 DUPLICATE ADDRESS DETECTION COLLISION
		0 DUPLICATE ADDRESS DETECTION NS LOOP
		0 TIME IGNORED SOURCE ON SECONDARY EXPENSIVE I/F
ICMP6:
	1725 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED BECAUSE OLD MESSAGE WAS ICMP ERROR OR SO
	0 ERROR NOT GENERATED BECAUSE RATE LIMITATION
	OUTPUT HISTOGRAM:
		UNREACH: 1725
		MLDV1 LISTENER REPORT: 77
		MLDV1 LISTENER DONE: 11
		ROUTER SOLICITATION: 123
		NEIGHBOR SOLICITATION: 5194
		NEIGHBOR ADVERTISEMENT: 4403
		MLDV2 LISTENER REPORT: 1129
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	0 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	INPUT HISTOGRAM:
		UNREACH: 150
		MULTICAST LISTENER QUERY: 2007
		ROUTER ADVERTISEMENT: 29751
		NEIGHBOR SOLICITATION: 4403
		NEIGHBOR ADVERTISEMENT: 4341
	HISTOGRAM OF ERROR MESSAGES TO BE GENERATED:
		0 NO ROUTE
		0 ADMINISTRATIVELY PROHIBITED
		0 BEYOND SCOPE
		150 ADDRESS UNREACHABLE
		1575 PORT UNREACHABLE
		0 PACKET TOO BIG
		0 TIME EXCEED TRANSIT
		0 TIME EXCEED REASSEMBLY
		0 ERRONEOUS HEADER FIELD
		0 UNRECOGNIZED NEXT HEADER
		0 UNRECOGNIZED OPTION
		0 REDIRECT
		0 UNKNOWN
	0 MESSAGE RESPONSE GENERATED
	0 MESSAGE WITH TOO MANY ND OPTIONS
	0 MESSAGE WITH BAD ND OPTIONS
	0 BAD NEIGHBOR SOLICITATION MESSAGE
	0 BAD NEIGHBOR ADVERTISEMENT MESSAGE
	0 BAD ROUTER SOLICITATION MESSAGE
	0 BAD ROUTER ADVERTISEMENT MESSAGE
	0 BAD REDIRECT MESSAGE
	0 PATH MTU CHANGE
	0 DROPPED FRAGMENTED NDP MESSAGE
IPSEC6:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
RIP6:
	0 MESSAGE RECEIVED
	0 CHECKSUM CALCULATION ON INBOUND
	0 MESSAGE WITH BAD CHECKSUM
	0 MESSAGE DROPPED DUE TO NO SOCKET
	0 MULTICAST MESSAGE DROPPED DUE TO NO SOCKET
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	0 DELIVERED
	0 DATAGRAM OUTPUT
PFKEY:
	0 REQUEST SENT TO USERLAND
	0 BYTE SENT TO USERLAND
	0 MESSAGE WITH INVALID LENGTH FIELD
	0 MESSAGE WITH INVALID VERSION FIELD
	0 MESSAGE WITH INVALID MESSAGE TYPE FIELD
	0 MESSAGE TOO SHORT
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
	0 MESSAGE WITH DUPLICATE EXTENSION
	0 MESSAGE WITH INVALID EXTENSION TYPE
	0 MESSAGE WITH INVALID SA TYPE
	0 MESSAGE WITH INVALID ADDRESS EXTENSION
	0 REQUEST SENT FROM USERLAND
	0 BYTE SENT FROM USERLAND
	0 MESSAGE TOWARD SINGLE SOCKET
	0 MESSAGE TOWARD ALL SOCKETS
	0 MESSAGE TOWARD REGISTERED SOCKETS
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
KEVT:
	24 CURRENT KERNEL CONTROL SOCKETS
	18912 KERNEL CONTROL GENERATION COUNT
	0 BAD VENDOR FAILURE
	7317 MESSAGE TOO BIG FAILURES
	0 OUT OF MEMORY FAILURE
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	272797 MESSAGES POSTED
KCTL:
	0 TOTAL KERNEL CONTROL MODULE REGISTERED
	12 CURRENT KERNEL CONTROL MODULES REGISTERED
	55 CURRENT KERNEL CONTROL SOCKETS
	1117 KERNEL CONTROL GENERATION COUNT
	580 CONNECTION ATTEMPTS
	0 CONNECTION FAILURE
	35 SEND FAILURES
	0 SEND LIST FAILURE
	0 ENQUEUE FAILURE
	0 PACKET DROPPED DUE TO FULL SOCKET BUFFERS
XBKIDLE:
	1 MAX PER PROCESS
	600 MAXIMUM TIME (SECONDS)
	131072 HIGH WATER MARK
	0 SOCKET OPTION NOT SUPPORTED FAILURE
	0 TOO MANY SOCKETS FAILURE
	0 TOTAL SOCKET REQUESTED OK
	0 EXTENDED BK IDLE SOCKET
	0 NO CELLULAR FAILURE
	0 NO TIME FAILURES
	0 FORCED DEFUNCT SOCKET
	0 RESUMED SOCKET
	0 TIMEOUT EXPIRED FAILURE
	0 TIMER RESCHEDULED
	0 NO DELEGATED FAILURE
NET_API:
	2 INTERFACE FILTERS CURRENTLY ATTACHED
	2 INTERFACE FILTERS ATTACHED SINCE BOOT
	2 INTERFACE FILTERS ATTACHED SINCE BOOT BY OS
	0 IP FILTER CURRENTLY ATTACHED
	0 IP FILTER ATTACHED SINCE BOOT
	0 IP FILTER ATTACHED SINCE BOOT BY OS
	4 SOCKET FILTERS CURRENTLY ATTACHED
	4 SOCKET FILTERS ATTACHED SINCE BOOT
	4 SOCKET FILTERS ATTACHED SINCE BOOT BY OS
	325878 SOCKETS ALLOCATED SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL BY OS
	2463 SOCKETS WITH NECP CLIENT UUID SINCE BOOT
	104161 LOCAL DOMAIN SOCKETS ALLOCATED SINCE BOOT
	1199 ROUTE DOMAIN SOCKETS ALLOCATED SINCE BOOT
	124341 INET DOMAIN SOCKETS ALLOCATED SINCE BOOT
	59797 INET6 DOMAIN SOCKETS ALLOCATED SINCE BOOT
	10048 SYSTEM DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 MULTIPATH DOMAIN SOCKET ALLOCATED SINCE BOOT
	0 KEY DOMAIN SOCKET ALLOCATED SINCE BOOT
	5 NDRV DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 OTHER DOMAINS SOCKET ALLOCATED SINCE BOOT
	15538 IPV4 STREAM SOCKETS CREATED SINCE BOOT
	108803 IPV4 DATAGRAM SOCKETS CREATED SINCE BOOT
	10293 IPV4 DATAGRAM SOCKETS CONNECTED
	38013 IPV4 DNS SOCKETS
	102112 IPV4 DATAGRAM SOCKETS WITHOUT DATA
	7556 IPV6 STREAM SOCKETS CREATED SINCE BOOT
	52241 IPV6 DATAGRAM SOCKETS CREATED SINCE BOOT
	34814 IPV6 DATAGRAM SOCKETS CONNECTED
	0 IPV6 DNS SOCKET
	28201 IPV6 DATAGRAM SOCKETS WITHOUT DATA
	1115 SOCKET MULTICAST JOINS SINCE BOOT
	1115 SOCKET MULTICAST JOINS SINCE BOOT BY OS
	0 IPV4 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV4 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED
	12 INTERFACES ALLOCATED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED BY OS
	12 EXTENDED INTERFACES ALLOCATED SINCE BOOT BY OS
	2 PF ADDRULE OPERATIONS SINCE BOOT
	0 PF ADDRULE OPERATION SINCE BOOT BY OS
	0 VMNET START SINCE BOOT

>>> # SHELLSHOCK
>>> # Bash runs its start up scripts profile.sh .bashrc
>>> # Inputs: echo ~/.txt
>>> # Parses and translates to: ['/usr/bin/echo', '/Users/raymond/.txt']
>>> # Runs the command
>>> # Capture the output to stdout
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
TCP:
	0 PACKET SENT
		0 DATA PACKET (0 BYTE)
		0 DATA PACKET (0 BYTE) RETRANSMITTED
		0 RESEND INITIATED BY MTU DISCOVERY
		0 ACK-ONLY PACKET (0 DELAYED)
		0 URG ONLY PACKET
		0 WINDOW PROBE PACKET
		0 WINDOW UPDATE PACKET
		0 CONTROL PACKET
		0 DATA PACKET SENT AFTER FLOW CONTROL
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
	0 PACKET RECEIVED
		0 ACK (FOR 0 BYTE)
		0 DUPLICATE ACK
		0 ACK FOR UNSENT DATA
		0 PACKET (0 BYTE) RECEIVED IN-SEQUENCE
		0 COMPLETELY DUPLICATE PACKET (0 BYTE)
		0 OLD DUPLICATE PACKET
		0 RECEIVED PACKET DROPPED DUE TO LOW MEMORY
		0 PACKET WITH SOME DUP. DATA (0 BYTE DUPED)
		0 OUT-OF-ORDER PACKET (0 BYTE)
		0 PACKET (0 BYTE) OF DATA AFTER WINDOW
		0 WINDOW PROBE
		0 WINDOW UPDATE PACKET
		0 PACKET RECEIVED AFTER CLOSE
		0 BAD RESET
		0 DISCARDED FOR BAD CHECKSUM
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
		0 DISCARDED FOR BAD HEADER OFFSET FIELD
		0 DISCARDED BECAUSE PACKET TOO SHORT
	0 CONNECTION REQUEST
	0 CONNECTION ACCEPT
	0 BAD CONNECTION ATTEMPT
	0 LISTEN QUEUE OVERFLOW
	0 CONNECTION ESTABLISHED (INCLUDING ACCEPTS)
	0 CONNECTION CLOSED (INCLUDING 0 DROP)
		0 CONNECTION UPDATED CACHED RTT ON CLOSE
		0 CONNECTION UPDATED CACHED RTT VARIANCE ON CLOSE
		0 CONNECTION UPDATED CACHED SSTHRESH ON CLOSE
	0 EMBRYONIC CONNECTION DROPPED
	0 SEGMENT UPDATED RTT (OF 0 ATTEMPT)
	0 RETRANSMIT TIMEOUT
		0 CONNECTION DROPPED BY REXMIT TIMEOUT
		0 CONNECTION DROPPED AFTER RETRANSMITTING FIN
	0 PERSIST TIMEOUT
		0 CONNECTION DROPPED BY PERSIST TIMEOUT
	0 KEEPALIVE TIMEOUT
		0 KEEPALIVE PROBE SENT
		0 CONNECTION DROPPED BY KEEPALIVE
	0 CORRECT ACK HEADER PREDICTION
	0 CORRECT DATA PACKET HEADER PREDICTION
	0 SACK RECOVERY EPISODE
	0 SEGMENT REXMIT IN SACK RECOVERY EPISODES
	0 BYTE REXMIT IN SACK RECOVERY EPISODES
	0 SACK OPTION (SACK BLOCKS) RECEIVED
	0 SACK OPTION (SACK BLOCKS) SENT
	0 SACK SCOREBOARD OVERFLOW
	0 LRO COALESCED PACKET
		0 TIME LRO FLOW TABLE WAS FULL
		0 COLLISION IN LRO FLOW TABLE
		0 TIME LRO COALESCED 2 PACKETS
		0 TIME LRO COALESCED 3 OR 4 PACKETS
		0 TIME LRO COALESCED 5 OR MORE PACKETS
	0 LIMITED TRANSMIT DONE
	0 EARLY RETRANSMIT DONE
	0 TIME CUMULATIVE ACK ADVANCED ALONG WITH SACK
	0 PROBE TIMEOUT
		0 TIME RETRANSMIT TIMEOUT TRIGGERED AFTER PROBE
		0 TIME PROBE PACKETS WERE SENT FOR AN INTERFACE
		0 TIME COULDN'T SEND PROBE PACKETS FOR AN INTERFACE
		0 TIME FAST RECOVERY AFTER TAIL LOSS
		0 TIME RECOVERED LAST PACKET 
		0 SACK BASED RESCUE RETRANSMIT
	0 CLIENT CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 CLIENT CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME GRACEFUL FALLBACK TO NON-ECN CONNECTION
		0 TIME LOST ECN NEGOTIATING SYN, FOLLOWED BY RETRANSMISSION
		0 SERVER CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 SERVER CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME LOST ECN NEGOTIATING SYN-ACK, FOLLOWED BY RETRANSMISSION
		0 TIME RECEIVED CONGESTION EXPERIENCED (CE) NOTIFICATION
		0 TIME CWR WAS SENT IN RESPONSE TO ECE
		0 TIME SENT ECE NOTIFICATION
		0 CONNECTION RECEIVED CE ATLEAST ONCE
		0 CONNECTION RECEIVED ECE ATLEAST ONCE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS BUT NO CE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS AND CE
		0 CONNECTION USING ECN RECEIVED CE BUT NO PACKET LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO SYN-LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO REORDERING
		0 CONNECTION FELL BACK TO NON-ECN DUE TO EXCESSIVE CE-MARKINGS
	0 TIME PACKET REORDERING WAS DETECTED ON A CONNECTION
		0 TIME TRANSMITTED PACKETS WERE REORDERED
		0 TIME FAST RECOVERY WAS DELAYED TO HANDLE REORDERING
		0 TIME RETRANSMISSION WAS AVOIDED BY DELAYING RECOVERY
		0 RETRANSMISSION NOT NEEDED 
	0 TIME DSACK OPTION WAS SENT
		0 TIME DSACK OPTION WAS RECEIVED
		0 TIME DSACK WAS DISABLED ON A CONNECTION
		0 TIME RECOVERED FROM BAD RETRANSMISSION USING DSACK
		0 TIME IGNORED DSACK DUE TO ACK LOSS
		0 TIME IGNORED OLD DSACK OPTIONS
	0 TIME PMTU BLACKHOLE DETECTION, SIZE REVERTED
	0 CONNECTION WERE DROPPED AFTER LONG SLEEP
	0 TIME A TFO-COOKIE HAS BEEN ANNOUNCED
	0 SYN WITH DATA AND A VALID TFO-COOKIE HAVE BEEN RECEIVED
	0 SYN WITH TFO-COOKIE-REQUEST RECEIVED
	0 TIME AN INVALID TFO-COOKIE HAS BEEN RECEIVED
	0 TIME WE REQUESTED A TFO-COOKIE
		0 TIME THE PEER ANNOUNCED A TFO-COOKIE
	0 TIME WE COMBINED SYN WITH DATA AND A TFO-COOKIE
		0 TIME OUR SYN WITH DATA HAS BEEN ACKNOWLEDGED
	0 TIME A CONNECTION-ATTEMPT WITH TFO FELL BACK TO REGULAR TCP
	0 TIME A TFO-CONNECTION BLACKHOLE'D
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO DEFAULT
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO MEDIUM
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO LOW
	0 TIMER DRIFT LESS OR EQUAL TO 1 MS
	0 TIMER DRIFT LESS OR EQUAL TO 10 MS
	0 TIMER DRIFT LESS OR EQUAL TO 20 MS
	0 TIMER DRIFT LESS OR EQUAL TO 50 MS
	0 TIMER DRIFT LESS OR EQUAL TO 100 MS
	0 TIMER DRIFT LESS OR EQUAL TO 200 MS
	0 TIMER DRIFT LESS OR EQUAL TO 500 MS
	0 TIMER DRIFT LESS OR EQUAL TO 1000 MS
	0 TIMER DRIFT GREATER THAN TO 1000 MS
UDP:
	523880 DATAGRAMS RECEIVED
		0 WITH INCOMPLETE HEADER
		0 WITH BAD DATA LENGTH FIELD
		0 WITH BAD CHECKSUM
		54 WITH NO CHECKSUM
		492357 CHECKSUMMED IN SOFTWARE
			247973 DATAGRAMS (78758044 BYTES) OVER IPV4
			244384 DATAGRAMS (108450781 BYTES) OVER IPV6
		5346 DROPPED DUE TO NO SOCKET
		3618 BROADCAST/MULTICAST DATAGRAMS UNDELIVERED
		0 TIME MULTICAST SOURCE FILTER MATCHED
		1 DROPPED DUE TO FULL SOCKET BUFFERS
		0 NOT FOR HASHED PCB
		514915 DELIVERED
	143025 DATAGRAMS OUTPUT
		150163 CHECKSUMMED IN SOFTWARE
			55850 DATAGRAMS (11906070 BYTES) OVER IPV4
			94313 DATAGRAMS (20792303 BYTES) OVER IPV6
ICMP:
	1398 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED 'CUZ OLD MESSAGE WAS ICMP
	OUTPUT HISTOGRAM:
		ECHO REPLY: 38
		DESTINATION UNREACHABLE: 1398
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	1 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	0 MULTICAST ECHO REQUESTS IGNORED
	0 MULTICAST TIMESTAMP REQUESTS IGNORED
	INPUT HISTOGRAM:
		ECHO REPLY: 3
		DESTINATION UNREACHABLE: 2007
		ECHO: 38
		ROUTER ADVERTISEMENT: 147
	38 MESSAGE RESPONSES GENERATED
	ICMP ADDRESS MASK RESPONSES ARE DISABLED
IGMP:
	1636 MESSAGES RECEIVED
	0 MESSAGE RECEIVED WITH TOO FEW BYTES
	0 MESSAGE RECEIVED WITH WRONG TTL
	0 MESSAGE RECEIVED WITH BAD CHECKSUM
	565 V1/V2 MEMBERSHIP QUERIES RECEIVED
	287 V3 MEMBERSHIP QUERIES RECEIVED
	0 MEMBERSHIP QUERIES RECEIVED WITH INVALID FIELD(S)
	834 GENERAL QUERIES RECEIVED
	18 GROUP QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES DROPPED
	784 MEMBERSHIP REPORTS RECEIVED
	0 MEMBERSHIP REPORT RECEIVED WITH INVALID FIELD(S)
	784 MEMBERSHIP REPORTS RECEIVED FOR GROUPS TO WHICH WE BELONG
	0 V3 REPORT RECEIVED WITHOUT ROUTER ALERT
	890 MEMBERSHIP REPORTS SENT
IPSEC:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
ARP:
	1583 BROADAST ARP REQUESTS SENT
	9 UNICAST ARP REQUESTS SENT
	3320 ARP REPLIES SENT
	0 ARP ANNOUNCEMENT SENT
	11630 ARP REQUESTS RECEIVED
	1331 ARP REPLIES RECEIVED
	12963 TOTAL ARP PACKETS RECEIVED
	0 ARP CONFLICT PROBE SENT
	0 INVALID ARP RESOLVE REQUEST
	0 TOTAL PACKET DROPPED DUE TO LACK OF MEMORY
	0 TOTAL PACKET HELD AWAITING ARP REPLY
	43 TOTAL PACKETS DROPPED DUE TO NO ARP ENTRY
	378 TOTAL PACKETS DROPPED DURING ARP ENTRY REMOVAL
	1454 ARP ENTRIES TIMED OUT
	0 DUPLICATE IP SEEN
MPTCP:
	0 DATA PACKET SENT
	0 DATA BYTE SENT
	0 DATA PACKET RECEIVED
	0 DATA BYTE RECEIVED
	0 PACKET WITH AN INVALID MPCAP OPTION
	0 PACKET WITH AN INVALID MPJOIN OPTION
	0 TIME PRIMARY SUBFLOW FELL BACK TO TCP
	0 TIME SECONDARY SUBFLOW FELL BACK TO TCP
	0 DSS OPTION DROP
	0 OTHER INVALID MPTCP OPTION
	0 TIME THE MPTCP SUBFLOW WINDOW WAS REDUCED
	0 BAD DSS CHECKSUM
	0 TIME RECEIVED OUT OF ORDER DATA 
	0 SUBFLOW SWITCH
	0 SUBFLOW SWITCH DUE TO ADVISORY
	0 SUBFLOW SWITCH DUE TO RTT
	0 SUBFLOW SWITCH DUE TO RTO
	0 SUBFLOW SWITCH DUE TO PEER
	0 NUMBER OF SUBFLOW PROBE
IP6:
	751292 TOTAL PACKETS RECEIVED
		0 WITH SIZE SMALLER THAN MINIMUM
		0 WITH DATA SIZE < DATA LENGTH
		0 WITH DATA SIZE > DATA LENGTH
			0 PACKET FORCED TO SOFTWARE CHECKSUM
		0 WITH BAD OPTIONS
		168 WITH INCORRECT VERSION NUMBER
		6 FRAGMENTS RECEIVED
			0 DROPPED (DUP OR OUT OF SPACE)
			0 DROPPED AFTER TIMEOUT
			0 EXCEEDED LIMIT
			3 REASSEMBLED OK
			0 ATOMIC FRAGMENTS RECEIVED
		676980 PACKETS FOR THIS HOST
		0 PACKET FORWARDED
		33310 PACKETS NOT FORWARDABLE
		0 REDIRECT SENT
		33253 MULTICAST PACKETS WHICH WE DON'T JOIN
		0 PACKET WHOSE HEADERS ARE NOT CONTINUOUS
		0 TUNNELING PACKET THAT CAN'T FIND GIF
		0 PACKET DISCARDED DUE TO TOO MAY HEADERS
		0 FORWARD CACHE HIT
		0 FORWARD CACHE MISS
		0 PACKET DROPPED DUE TO NO BUFS FOR CONTROL DATA
	342693 PACKETS SENT FROM THIS HOST
		0 PACKET SENT WITH FABRICATED IP HEADER
		0 OUTPUT PACKET DROPPED DUE TO NO BUFS, ETC.
		2291 OUTPUT PACKETS DISCARDED DUE TO NO ROUTE
		0 OUTPUT DATAGRAM FRAGMENTED
		0 FRAGMENT CREATED
		0 DATAGRAM THAT CAN'T BE FRAGMENTED
		0 PACKET THAT VIOLATED SCOPE RULES
		0 PACKET DROPPED DUE TO NECP POLICY
	INPUT HISTOGRAM:
		HOP BY HOP: 5667
		TCP: 423053
		UDP: 279709
		FRAGMENT: 6
		ICMP6: 41736
		PIM: 953
	MBUF STATISTICS:
		1787 ONE MBUF
		TWO OR MORE MBUF:
			LO0= 10478
			UTUN1= 12
		739015 ONE EXT MBUF
		0 TWO OR MORE EXT MBUF
		0 FAILURE OF SOURCE ADDRESS SELECTION
		SOURCE ADDRESSES ON AN OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES ON A NON-OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF SAME SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF A DIFFERENT SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		DEPRECATED SOURCE ADDRESSES
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESS SELECTION
			18334 RULES DEFAULT
			0 RULE PREFER SAME ADDRESS
			5002 RULES PREFER APPROPRIATE SCOPE
			0 RULE AVOID DEPRECATED ADDRESSES
			0 RULE PREFER HOME ADDRESSES
			0 RULE PREFER OUTGOING INTERFACE
			10 RULES PREFER MATCHING LABEL
			47351 RULES PREFER TEMPORARY ADDRESSES
			0 RULE PREFER ADDRESSES ON ALIVE INTERFACES
			0 RULE USE LONGEST MATCHING PREFIX
		0 DUPLICATE ADDRESS DETECTION COLLISION
		0 DUPLICATE ADDRESS DETECTION NS LOOP
		0 TIME IGNORED SOURCE ON SECONDARY EXPENSIVE I/F
ICMP6:
	1726 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED BECAUSE OLD MESSAGE WAS ICMP ERROR OR SO
	0 ERROR NOT GENERATED BECAUSE RATE LIMITATION
	OUTPUT HISTOGRAM:
		UNREACH: 1726
		MLDV1 LISTENER REPORT: 77
		MLDV1 LISTENER DONE: 11
		ROUTER SOLICITATION: 123
		NEIGHBOR SOLICITATION: 5220
		NEIGHBOR ADVERTISEMENT: 4405
		MLDV2 LISTENER REPORT: 1152
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	0 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	INPUT HISTOGRAM:
		UNREACH: 150
		MULTICAST LISTENER QUERY: 2032
		ROUTER ADVERTISEMENT: 29949
		NEIGHBOR SOLICITATION: 4405
		NEIGHBOR ADVERTISEMENT: 4367
	HISTOGRAM OF ERROR MESSAGES TO BE GENERATED:
		0 NO ROUTE
		0 ADMINISTRATIVELY PROHIBITED
		0 BEYOND SCOPE
		150 ADDRESS UNREACHABLE
		1576 PORT UNREACHABLE
		0 PACKET TOO BIG
		0 TIME EXCEED TRANSIT
		0 TIME EXCEED REASSEMBLY
		0 ERRONEOUS HEADER FIELD
		0 UNRECOGNIZED NEXT HEADER
		0 UNRECOGNIZED OPTION
		0 REDIRECT
		0 UNKNOWN
	0 MESSAGE RESPONSE GENERATED
	0 MESSAGE WITH TOO MANY ND OPTIONS
	0 MESSAGE WITH BAD ND OPTIONS
	0 BAD NEIGHBOR SOLICITATION MESSAGE
	0 BAD NEIGHBOR ADVERTISEMENT MESSAGE
	0 BAD ROUTER SOLICITATION MESSAGE
	0 BAD ROUTER ADVERTISEMENT MESSAGE
	0 BAD REDIRECT MESSAGE
	0 PATH MTU CHANGE
	0 DROPPED FRAGMENTED NDP MESSAGE
IPSEC6:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
RIP6:
	0 MESSAGE RECEIVED
	0 CHECKSUM CALCULATION ON INBOUND
	0 MESSAGE WITH BAD CHECKSUM
	0 MESSAGE DROPPED DUE TO NO SOCKET
	0 MULTICAST MESSAGE DROPPED DUE TO NO SOCKET
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	0 DELIVERED
	0 DATAGRAM OUTPUT
PFKEY:
	0 REQUEST SENT TO USERLAND
	0 BYTE SENT TO USERLAND
	0 MESSAGE WITH INVALID LENGTH FIELD
	0 MESSAGE WITH INVALID VERSION FIELD
	0 MESSAGE WITH INVALID MESSAGE TYPE FIELD
	0 MESSAGE TOO SHORT
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
	0 MESSAGE WITH DUPLICATE EXTENSION
	0 MESSAGE WITH INVALID EXTENSION TYPE
	0 MESSAGE WITH INVALID SA TYPE
	0 MESSAGE WITH INVALID ADDRESS EXTENSION
	0 REQUEST SENT FROM USERLAND
	0 BYTE SENT FROM USERLAND
	0 MESSAGE TOWARD SINGLE SOCKET
	0 MESSAGE TOWARD ALL SOCKETS
	0 MESSAGE TOWARD REGISTERED SOCKETS
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
KEVT:
	24 CURRENT KERNEL CONTROL SOCKETS
	18926 KERNEL CONTROL GENERATION COUNT
	0 BAD VENDOR FAILURE
	7335 MESSAGE TOO BIG FAILURES
	0 OUT OF MEMORY FAILURE
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	273456 MESSAGES POSTED
KCTL:
	0 TOTAL KERNEL CONTROL MODULE REGISTERED
	12 CURRENT KERNEL CONTROL MODULES REGISTERED
	55 CURRENT KERNEL CONTROL SOCKETS
	1117 KERNEL CONTROL GENERATION COUNT
	580 CONNECTION ATTEMPTS
	0 CONNECTION FAILURE
	35 SEND FAILURES
	0 SEND LIST FAILURE
	0 ENQUEUE FAILURE
	0 PACKET DROPPED DUE TO FULL SOCKET BUFFERS
XBKIDLE:
	1 MAX PER PROCESS
	600 MAXIMUM TIME (SECONDS)
	131072 HIGH WATER MARK
	0 SOCKET OPTION NOT SUPPORTED FAILURE
	0 TOO MANY SOCKETS FAILURE
	0 TOTAL SOCKET REQUESTED OK
	0 EXTENDED BK IDLE SOCKET
	0 NO CELLULAR FAILURE
	0 NO TIME FAILURES
	0 FORCED DEFUNCT SOCKET
	0 RESUMED SOCKET
	0 TIMEOUT EXPIRED FAILURE
	0 TIMER RESCHEDULED
	0 NO DELEGATED FAILURE
NET_API:
	2 INTERFACE FILTERS CURRENTLY ATTACHED
	2 INTERFACE FILTERS ATTACHED SINCE BOOT
	2 INTERFACE FILTERS ATTACHED SINCE BOOT BY OS
	0 IP FILTER CURRENTLY ATTACHED
	0 IP FILTER ATTACHED SINCE BOOT
	0 IP FILTER ATTACHED SINCE BOOT BY OS
	4 SOCKET FILTERS CURRENTLY ATTACHED
	4 SOCKET FILTERS ATTACHED SINCE BOOT
	4 SOCKET FILTERS ATTACHED SINCE BOOT BY OS
	326120 SOCKETS ALLOCATED SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL BY OS
	2469 SOCKETS WITH NECP CLIENT UUID SINCE BOOT
	104256 LOCAL DOMAIN SOCKETS ALLOCATED SINCE BOOT
	1199 ROUTE DOMAIN SOCKETS ALLOCATED SINCE BOOT
	124391 INET DOMAIN SOCKETS ALLOCATED SINCE BOOT
	59865 INET6 DOMAIN SOCKETS ALLOCATED SINCE BOOT
	10055 SYSTEM DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 MULTIPATH DOMAIN SOCKET ALLOCATED SINCE BOOT
	0 KEY DOMAIN SOCKET ALLOCATED SINCE BOOT
	5 NDRV DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 OTHER DOMAINS SOCKET ALLOCATED SINCE BOOT
	15550 IPV4 STREAM SOCKETS CREATED SINCE BOOT
	108841 IPV4 DATAGRAM SOCKETS CREATED SINCE BOOT
	10299 IPV4 DATAGRAM SOCKETS CONNECTED
	38071 IPV4 DNS SOCKETS
	102145 IPV4 DATAGRAM SOCKETS WITHOUT DATA
	7559 IPV6 STREAM SOCKETS CREATED SINCE BOOT
	52306 IPV6 DATAGRAM SOCKETS CREATED SINCE BOOT
	34857 IPV6 DATAGRAM SOCKETS CONNECTED
	0 IPV6 DNS SOCKET
	28244 IPV6 DATAGRAM SOCKETS WITHOUT DATA
	1115 SOCKET MULTICAST JOINS SINCE BOOT
	1115 SOCKET MULTICAST JOINS SINCE BOOT BY OS
	0 IPV4 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV4 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED
	12 INTERFACES ALLOCATED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED BY OS
	12 EXTENDED INTERFACES ALLOCATED SINCE BOOT BY OS
	2 PF ADDRULE OPERATIONS SINCE BOOT
	0 PF ADDRULE OPERATION SINCE BOOT BY OS
	0 VMNET START SINCE BOOT

>>> 
>>> 
>>> os.environ.keys()
['CPPFLAGS', 'LESS', 'TERM_PROGRAM_VERSION', 'LOGNAME', 'USER', 'HOME', 'PATH', 'PS1', 'TERM_PROGRAM', 'LANG', 'TERM', 'SHELL', 'COLORFGBG', 'SHLVL', 'MACOSX_DEPLOYMENT_TARGET', 'XPC_FLAGS', 'HISTSIZE', 'ITERM_SESSION_ID', 'EDITOR', 'LDFLAGS', 'HISTFILESIZE', 'TERM_SESSION_ID', 'XPC_SERVICE_NAME', 'COLORTERM', 'SSH_AUTH_SOCK', 'Apple_PubSub_Socket_Render', 'ITERM_PROFILE', '_', 'TMPDIR', 'HISTIGNORE', 'GREP_OPTIONS', 'OLDPWD', '__CF_USER_TEXT_ENCODING', 'PWD', 'VCS', 'CFLAGS']
>>> os.environ['USER']
'raymond'
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
TCP:
	0 PACKET SENT
		0 DATA PACKET (0 BYTE)
		0 DATA PACKET (0 BYTE) RETRANSMITTED
		0 RESEND INITIATED BY MTU DISCOVERY
		0 ACK-ONLY PACKET (0 DELAYED)
		0 URG ONLY PACKET
		0 WINDOW PROBE PACKET
		0 WINDOW UPDATE PACKET
		0 CONTROL PACKET
		0 DATA PACKET SENT AFTER FLOW CONTROL
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
	0 PACKET RECEIVED
		0 ACK (FOR 0 BYTE)
		0 DUPLICATE ACK
		0 ACK FOR UNSENT DATA
		0 PACKET (0 BYTE) RECEIVED IN-SEQUENCE
		0 COMPLETELY DUPLICATE PACKET (0 BYTE)
		0 OLD DUPLICATE PACKET
		0 RECEIVED PACKET DROPPED DUE TO LOW MEMORY
		0 PACKET WITH SOME DUP. DATA (0 BYTE DUPED)
		0 OUT-OF-ORDER PACKET (0 BYTE)
		0 PACKET (0 BYTE) OF DATA AFTER WINDOW
		0 WINDOW PROBE
		0 WINDOW UPDATE PACKET
		0 PACKET RECEIVED AFTER CLOSE
		0 BAD RESET
		0 DISCARDED FOR BAD CHECKSUM
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
		0 DISCARDED FOR BAD HEADER OFFSET FIELD
		0 DISCARDED BECAUSE PACKET TOO SHORT
	0 CONNECTION REQUEST
	0 CONNECTION ACCEPT
	0 BAD CONNECTION ATTEMPT
	0 LISTEN QUEUE OVERFLOW
	0 CONNECTION ESTABLISHED (INCLUDING ACCEPTS)
	0 CONNECTION CLOSED (INCLUDING 0 DROP)
		0 CONNECTION UPDATED CACHED RTT ON CLOSE
		0 CONNECTION UPDATED CACHED RTT VARIANCE ON CLOSE
		0 CONNECTION UPDATED CACHED SSTHRESH ON CLOSE
	0 EMBRYONIC CONNECTION DROPPED
	0 SEGMENT UPDATED RTT (OF 0 ATTEMPT)
	0 RETRANSMIT TIMEOUT
		0 CONNECTION DROPPED BY REXMIT TIMEOUT
		0 CONNECTION DROPPED AFTER RETRANSMITTING FIN
	0 PERSIST TIMEOUT
		0 CONNECTION DROPPED BY PERSIST TIMEOUT
	0 KEEPALIVE TIMEOUT
		0 KEEPALIVE PROBE SENT
		0 CONNECTION DROPPED BY KEEPALIVE
	0 CORRECT ACK HEADER PREDICTION
	0 CORRECT DATA PACKET HEADER PREDICTION
	0 SACK RECOVERY EPISODE
	0 SEGMENT REXMIT IN SACK RECOVERY EPISODES
	0 BYTE REXMIT IN SACK RECOVERY EPISODES
	0 SACK OPTION (SACK BLOCKS) RECEIVED
	0 SACK OPTION (SACK BLOCKS) SENT
	0 SACK SCOREBOARD OVERFLOW
	0 LRO COALESCED PACKET
		0 TIME LRO FLOW TABLE WAS FULL
		0 COLLISION IN LRO FLOW TABLE
		0 TIME LRO COALESCED 2 PACKETS
		0 TIME LRO COALESCED 3 OR 4 PACKETS
		0 TIME LRO COALESCED 5 OR MORE PACKETS
	0 LIMITED TRANSMIT DONE
	0 EARLY RETRANSMIT DONE
	0 TIME CUMULATIVE ACK ADVANCED ALONG WITH SACK
	0 PROBE TIMEOUT
		0 TIME RETRANSMIT TIMEOUT TRIGGERED AFTER PROBE
		0 TIME PROBE PACKETS WERE SENT FOR AN INTERFACE
		0 TIME COULDN'T SEND PROBE PACKETS FOR AN INTERFACE
		0 TIME FAST RECOVERY AFTER TAIL LOSS
		0 TIME RECOVERED LAST PACKET 
		0 SACK BASED RESCUE RETRANSMIT
	0 CLIENT CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 CLIENT CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME GRACEFUL FALLBACK TO NON-ECN CONNECTION
		0 TIME LOST ECN NEGOTIATING SYN, FOLLOWED BY RETRANSMISSION
		0 SERVER CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 SERVER CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME LOST ECN NEGOTIATING SYN-ACK, FOLLOWED BY RETRANSMISSION
		0 TIME RECEIVED CONGESTION EXPERIENCED (CE) NOTIFICATION
		0 TIME CWR WAS SENT IN RESPONSE TO ECE
		0 TIME SENT ECE NOTIFICATION
		0 CONNECTION RECEIVED CE ATLEAST ONCE
		0 CONNECTION RECEIVED ECE ATLEAST ONCE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS BUT NO CE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS AND CE
		0 CONNECTION USING ECN RECEIVED CE BUT NO PACKET LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO SYN-LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO REORDERING
		0 CONNECTION FELL BACK TO NON-ECN DUE TO EXCESSIVE CE-MARKINGS
	0 TIME PACKET REORDERING WAS DETECTED ON A CONNECTION
		0 TIME TRANSMITTED PACKETS WERE REORDERED
		0 TIME FAST RECOVERY WAS DELAYED TO HANDLE REORDERING
		0 TIME RETRANSMISSION WAS AVOIDED BY DELAYING RECOVERY
		0 RETRANSMISSION NOT NEEDED 
	0 TIME DSACK OPTION WAS SENT
		0 TIME DSACK OPTION WAS RECEIVED
		0 TIME DSACK WAS DISABLED ON A CONNECTION
		0 TIME RECOVERED FROM BAD RETRANSMISSION USING DSACK
		0 TIME IGNORED DSACK DUE TO ACK LOSS
		0 TIME IGNORED OLD DSACK OPTIONS
	0 TIME PMTU BLACKHOLE DETECTION, SIZE REVERTED
	0 CONNECTION WERE DROPPED AFTER LONG SLEEP
	0 TIME A TFO-COOKIE HAS BEEN ANNOUNCED
	0 SYN WITH DATA AND A VALID TFO-COOKIE HAVE BEEN RECEIVED
	0 SYN WITH TFO-COOKIE-REQUEST RECEIVED
	0 TIME AN INVALID TFO-COOKIE HAS BEEN RECEIVED
	0 TIME WE REQUESTED A TFO-COOKIE
		0 TIME THE PEER ANNOUNCED A TFO-COOKIE
	0 TIME WE COMBINED SYN WITH DATA AND A TFO-COOKIE
		0 TIME OUR SYN WITH DATA HAS BEEN ACKNOWLEDGED
	0 TIME A CONNECTION-ATTEMPT WITH TFO FELL BACK TO REGULAR TCP
	0 TIME A TFO-CONNECTION BLACKHOLE'D
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO DEFAULT
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO MEDIUM
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO LOW
	0 TIMER DRIFT LESS OR EQUAL TO 1 MS
	0 TIMER DRIFT LESS OR EQUAL TO 10 MS
	0 TIMER DRIFT LESS OR EQUAL TO 20 MS
	0 TIMER DRIFT LESS OR EQUAL TO 50 MS
	0 TIMER DRIFT LESS OR EQUAL TO 100 MS
	0 TIMER DRIFT LESS OR EQUAL TO 200 MS
	0 TIMER DRIFT LESS OR EQUAL TO 500 MS
	0 TIMER DRIFT LESS OR EQUAL TO 1000 MS
	0 TIMER DRIFT GREATER THAN TO 1000 MS
UDP:
	527730 DATAGRAMS RECEIVED
		0 WITH INCOMPLETE HEADER
		0 WITH BAD DATA LENGTH FIELD
		0 WITH BAD CHECKSUM
		54 WITH NO CHECKSUM
		496141 CHECKSUMMED IN SOFTWARE
			250020 DATAGRAMS (79344345 BYTES) OVER IPV4
			246121 DATAGRAMS (108966528 BYTES) OVER IPV6
		5346 DROPPED DUE TO NO SOCKET
		3618 BROADCAST/MULTICAST DATAGRAMS UNDELIVERED
		0 TIME MULTICAST SOURCE FILTER MATCHED
		1 DROPPED DUE TO FULL SOCKET BUFFERS
		0 NOT FOR HASHED PCB
		518765 DELIVERED
	143197 DATAGRAMS OUTPUT
		150363 CHECKSUMMED IN SOFTWARE
			55982 DATAGRAMS (11942158 BYTES) OVER IPV4
			94381 DATAGRAMS (20809955 BYTES) OVER IPV6
ICMP:
	1398 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED 'CUZ OLD MESSAGE WAS ICMP
	OUTPUT HISTOGRAM:
		ECHO REPLY: 38
		DESTINATION UNREACHABLE: 1398
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	1 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	0 MULTICAST ECHO REQUESTS IGNORED
	0 MULTICAST TIMESTAMP REQUESTS IGNORED
	INPUT HISTOGRAM:
		ECHO REPLY: 3
		DESTINATION UNREACHABLE: 2007
		ECHO: 38
		ROUTER ADVERTISEMENT: 147
	38 MESSAGE RESPONSES GENERATED
	ICMP ADDRESS MASK RESPONSES ARE DISABLED
IGMP:
	1636 MESSAGES RECEIVED
	0 MESSAGE RECEIVED WITH TOO FEW BYTES
	0 MESSAGE RECEIVED WITH WRONG TTL
	0 MESSAGE RECEIVED WITH BAD CHECKSUM
	565 V1/V2 MEMBERSHIP QUERIES RECEIVED
	287 V3 MEMBERSHIP QUERIES RECEIVED
	0 MEMBERSHIP QUERIES RECEIVED WITH INVALID FIELD(S)
	834 GENERAL QUERIES RECEIVED
	18 GROUP QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES DROPPED
	784 MEMBERSHIP REPORTS RECEIVED
	0 MEMBERSHIP REPORT RECEIVED WITH INVALID FIELD(S)
	784 MEMBERSHIP REPORTS RECEIVED FOR GROUPS TO WHICH WE BELONG
	0 V3 REPORT RECEIVED WITHOUT ROUTER ALERT
	890 MEMBERSHIP REPORTS SENT
IPSEC:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
ARP:
	1601 BROADAST ARP REQUESTS SENT
	9 UNICAST ARP REQUESTS SENT
	3320 ARP REPLIES SENT
	0 ARP ANNOUNCEMENT SENT
	11630 ARP REQUESTS RECEIVED
	1349 ARP REPLIES RECEIVED
	12981 TOTAL ARP PACKETS RECEIVED
	0 ARP CONFLICT PROBE SENT
	0 INVALID ARP RESOLVE REQUEST
	0 TOTAL PACKET DROPPED DUE TO LACK OF MEMORY
	0 TOTAL PACKET HELD AWAITING ARP REPLY
	43 TOTAL PACKETS DROPPED DUE TO NO ARP ENTRY
	378 TOTAL PACKETS DROPPED DURING ARP ENTRY REMOVAL
	1468 ARP ENTRIES TIMED OUT
	0 DUPLICATE IP SEEN
MPTCP:
	0 DATA PACKET SENT
	0 DATA BYTE SENT
	0 DATA PACKET RECEIVED
	0 DATA BYTE RECEIVED
	0 PACKET WITH AN INVALID MPCAP OPTION
	0 PACKET WITH AN INVALID MPJOIN OPTION
	0 TIME PRIMARY SUBFLOW FELL BACK TO TCP
	0 TIME SECONDARY SUBFLOW FELL BACK TO TCP
	0 DSS OPTION DROP
	0 OTHER INVALID MPTCP OPTION
	0 TIME THE MPTCP SUBFLOW WINDOW WAS REDUCED
	0 BAD DSS CHECKSUM
	0 TIME RECEIVED OUT OF ORDER DATA 
	0 SUBFLOW SWITCH
	0 SUBFLOW SWITCH DUE TO ADVISORY
	0 SUBFLOW SWITCH DUE TO RTT
	0 SUBFLOW SWITCH DUE TO RTO
	0 SUBFLOW SWITCH DUE TO PEER
	0 NUMBER OF SUBFLOW PROBE
IP6:
	753507 TOTAL PACKETS RECEIVED
		0 WITH SIZE SMALLER THAN MINIMUM
		0 WITH DATA SIZE < DATA LENGTH
		0 WITH DATA SIZE > DATA LENGTH
			0 PACKET FORCED TO SOFTWARE CHECKSUM
		0 WITH BAD OPTIONS
		168 WITH INCORRECT VERSION NUMBER
		6 FRAGMENTS RECEIVED
			0 DROPPED (DUP OR OUT OF SPACE)
			0 DROPPED AFTER TIMEOUT
			0 EXCEEDED LIMIT
			3 REASSEMBLED OK
			0 ATOMIC FRAGMENTS RECEIVED
		678976 PACKETS FOR THIS HOST
		0 PACKET FORWARDED
		33440 PACKETS NOT FORWARDABLE
		0 REDIRECT SENT
		33383 MULTICAST PACKETS WHICH WE DON'T JOIN
		0 PACKET WHOSE HEADERS ARE NOT CONTINUOUS
		0 TUNNELING PACKET THAT CAN'T FIND GIF
		0 PACKET DISCARDED DUE TO TOO MAY HEADERS
		0 FORWARD CACHE HIT
		0 FORWARD CACHE MISS
		0 PACKET DROPPED DUE TO NO BUFS FOR CONTROL DATA
	343000 PACKETS SENT FROM THIS HOST
		0 PACKET SENT WITH FABRICATED IP HEADER
		0 OUTPUT PACKET DROPPED DUE TO NO BUFS, ETC.
		2291 OUTPUT PACKETS DISCARDED DUE TO NO ROUTE
		0 OUTPUT DATAGRAM FRAGMENTED
		0 FRAGMENT CREATED
		0 DATAGRAM THAT CAN'T BE FRAGMENTED
		0 PACKET THAT VIOLATED SCOPE RULES
		0 PACKET DROPPED DUE TO NECP POLICY
	INPUT HISTOGRAM:
		HOP BY HOP: 5694
		TCP: 423284
		UDP: 281594
		FRAGMENT: 6
		ICMP6: 41800
		PIM: 961
	MBUF STATISTICS:
		1787 ONE MBUF
		TWO OR MORE MBUF:
			LO0= 10506
			UTUN1= 12
		741202 ONE EXT MBUF
		0 TWO OR MORE EXT MBUF
		0 FAILURE OF SOURCE ADDRESS SELECTION
		SOURCE ADDRESSES ON AN OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES ON A NON-OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF SAME SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF A DIFFERENT SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		DEPRECATED SOURCE ADDRESSES
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESS SELECTION
			18370 RULES DEFAULT
			0 RULE PREFER SAME ADDRESS
			5028 RULES PREFER APPROPRIATE SCOPE
			0 RULE AVOID DEPRECATED ADDRESSES
			0 RULE PREFER HOME ADDRESSES
			0 RULE PREFER OUTGOING INTERFACE
			10 RULES PREFER MATCHING LABEL
			47351 RULES PREFER TEMPORARY ADDRESSES
			0 RULE PREFER ADDRESSES ON ALIVE INTERFACES
			0 RULE USE LONGEST MATCHING PREFIX
		0 DUPLICATE ADDRESS DETECTION COLLISION
		0 DUPLICATE ADDRESS DETECTION NS LOOP
		0 TIME IGNORED SOURCE ON SECONDARY EXPENSIVE I/F
ICMP6:
	1726 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED BECAUSE OLD MESSAGE WAS ICMP ERROR OR SO
	0 ERROR NOT GENERATED BECAUSE RATE LIMITATION
	OUTPUT HISTOGRAM:
		UNREACH: 1726
		MLDV1 LISTENER REPORT: 77
		MLDV1 LISTENER DONE: 11
		ROUTER SOLICITATION: 123
		NEIGHBOR SOLICITATION: 5225
		NEIGHBOR ADVERTISEMENT: 4405
		MLDV2 LISTENER REPORT: 1170
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	0 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	INPUT HISTOGRAM:
		UNREACH: 150
		MULTICAST LISTENER QUERY: 2057
		ROUTER ADVERTISEMENT: 30008
		NEIGHBOR SOLICITATION: 4405
		NEIGHBOR ADVERTISEMENT: 4372
	HISTOGRAM OF ERROR MESSAGES TO BE GENERATED:
		0 NO ROUTE
		0 ADMINISTRATIVELY PROHIBITED
		0 BEYOND SCOPE
		150 ADDRESS UNREACHABLE
		1576 PORT UNREACHABLE
		0 PACKET TOO BIG
		0 TIME EXCEED TRANSIT
		0 TIME EXCEED REASSEMBLY
		0 ERRONEOUS HEADER FIELD
		0 UNRECOGNIZED NEXT HEADER
		0 UNRECOGNIZED OPTION
		0 REDIRECT
		0 UNKNOWN
	0 MESSAGE RESPONSE GENERATED
	0 MESSAGE WITH TOO MANY ND OPTIONS
	0 MESSAGE WITH BAD ND OPTIONS
	0 BAD NEIGHBOR SOLICITATION MESSAGE
	0 BAD NEIGHBOR ADVERTISEMENT MESSAGE
	0 BAD ROUTER SOLICITATION MESSAGE
	0 BAD ROUTER ADVERTISEMENT MESSAGE
	0 BAD REDIRECT MESSAGE
	0 PATH MTU CHANGE
	0 DROPPED FRAGMENTED NDP MESSAGE
IPSEC6:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
RIP6:
	0 MESSAGE RECEIVED
	0 CHECKSUM CALCULATION ON INBOUND
	0 MESSAGE WITH BAD CHECKSUM
	0 MESSAGE DROPPED DUE TO NO SOCKET
	0 MULTICAST MESSAGE DROPPED DUE TO NO SOCKET
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	0 DELIVERED
	0 DATAGRAM OUTPUT
PFKEY:
	0 REQUEST SENT TO USERLAND
	0 BYTE SENT TO USERLAND
	0 MESSAGE WITH INVALID LENGTH FIELD
	0 MESSAGE WITH INVALID VERSION FIELD
	0 MESSAGE WITH INVALID MESSAGE TYPE FIELD
	0 MESSAGE TOO SHORT
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
	0 MESSAGE WITH DUPLICATE EXTENSION
	0 MESSAGE WITH INVALID EXTENSION TYPE
	0 MESSAGE WITH INVALID SA TYPE
	0 MESSAGE WITH INVALID ADDRESS EXTENSION
	0 REQUEST SENT FROM USERLAND
	0 BYTE SENT FROM USERLAND
	0 MESSAGE TOWARD SINGLE SOCKET
	0 MESSAGE TOWARD ALL SOCKETS
	0 MESSAGE TOWARD REGISTERED SOCKETS
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
KEVT:
	24 CURRENT KERNEL CONTROL SOCKETS
	18940 KERNEL CONTROL GENERATION COUNT
	0 BAD VENDOR FAILURE
	7341 MESSAGE TOO BIG FAILURES
	0 OUT OF MEMORY FAILURE
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	273795 MESSAGES POSTED
KCTL:
	0 TOTAL KERNEL CONTROL MODULE REGISTERED
	12 CURRENT KERNEL CONTROL MODULES REGISTERED
	55 CURRENT KERNEL CONTROL SOCKETS
	1117 KERNEL CONTROL GENERATION COUNT
	580 CONNECTION ATTEMPTS
	0 CONNECTION FAILURE
	35 SEND FAILURES
	0 SEND LIST FAILURE
	0 ENQUEUE FAILURE
	0 PACKET DROPPED DUE TO FULL SOCKET BUFFERS
XBKIDLE:
	1 MAX PER PROCESS
	600 MAXIMUM TIME (SECONDS)
	131072 HIGH WATER MARK
	0 SOCKET OPTION NOT SUPPORTED FAILURE
	0 TOO MANY SOCKETS FAILURE
	0 TOTAL SOCKET REQUESTED OK
	0 EXTENDED BK IDLE SOCKET
	0 NO CELLULAR FAILURE
	0 NO TIME FAILURES
	0 FORCED DEFUNCT SOCKET
	0 RESUMED SOCKET
	0 TIMEOUT EXPIRED FAILURE
	0 TIMER RESCHEDULED
	0 NO DELEGATED FAILURE
NET_API:
	2 INTERFACE FILTERS CURRENTLY ATTACHED
	2 INTERFACE FILTERS ATTACHED SINCE BOOT
	2 INTERFACE FILTERS ATTACHED SINCE BOOT BY OS
	0 IP FILTER CURRENTLY ATTACHED
	0 IP FILTER ATTACHED SINCE BOOT
	0 IP FILTER ATTACHED SINCE BOOT BY OS
	4 SOCKET FILTERS CURRENTLY ATTACHED
	4 SOCKET FILTERS ATTACHED SINCE BOOT
	4 SOCKET FILTERS ATTACHED SINCE BOOT BY OS
	326226 SOCKETS ALLOCATED SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL BY OS
	2472 SOCKETS WITH NECP CLIENT UUID SINCE BOOT
	104288 LOCAL DOMAIN SOCKETS ALLOCATED SINCE BOOT
	1199 ROUTE DOMAIN SOCKETS ALLOCATED SINCE BOOT
	124409 INET DOMAIN SOCKETS ALLOCATED SINCE BOOT
	59887 INET6 DOMAIN SOCKETS ALLOCATED SINCE BOOT
	10062 SYSTEM DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 MULTIPATH DOMAIN SOCKET ALLOCATED SINCE BOOT
	0 KEY DOMAIN SOCKET ALLOCATED SINCE BOOT
	5 NDRV DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 OTHER DOMAINS SOCKET ALLOCATED SINCE BOOT
	15554 IPV4 STREAM SOCKETS CREATED SINCE BOOT
	108855 IPV4 DATAGRAM SOCKETS CREATED SINCE BOOT
	10299 IPV4 DATAGRAM SOCKETS CONNECTED
	38088 IPV4 DNS SOCKETS
	102157 IPV4 DATAGRAM SOCKETS WITHOUT DATA
	7562 IPV6 STREAM SOCKETS CREATED SINCE BOOT
	52325 IPV6 DATAGRAM SOCKETS CREATED SINCE BOOT
	34868 IPV6 DATAGRAM SOCKETS CONNECTED
	0 IPV6 DNS SOCKET
	28257 IPV6 DATAGRAM SOCKETS WITHOUT DATA
	1115 SOCKET MULTICAST JOINS SINCE BOOT
	1115 SOCKET MULTICAST JOINS SINCE BOOT BY OS
	0 IPV4 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV4 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED
	12 INTERFACES ALLOCATED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED BY OS
	12 EXTENDED INTERFACES ALLOCATED SINCE BOOT BY OS
	2 PF ADDRULE OPERATIONS SINCE BOOT
	0 PF ADDRULE OPERATION SINCE BOOT BY OS
	0 VMNET START SINCE BOOT

raymond

>>> os.path.expanduser('~/a.txt')
'/Users/raymond/a.txt'
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
TCP:
	0 PACKET SENT
		0 DATA PACKET (0 BYTE)
		0 DATA PACKET (0 BYTE) RETRANSMITTED
		0 RESEND INITIATED BY MTU DISCOVERY
		0 ACK-ONLY PACKET (0 DELAYED)
		0 URG ONLY PACKET
		0 WINDOW PROBE PACKET
		0 WINDOW UPDATE PACKET
		0 CONTROL PACKET
		0 DATA PACKET SENT AFTER FLOW CONTROL
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
	0 PACKET RECEIVED
		0 ACK (FOR 0 BYTE)
		0 DUPLICATE ACK
		0 ACK FOR UNSENT DATA
		0 PACKET (0 BYTE) RECEIVED IN-SEQUENCE
		0 COMPLETELY DUPLICATE PACKET (0 BYTE)
		0 OLD DUPLICATE PACKET
		0 RECEIVED PACKET DROPPED DUE TO LOW MEMORY
		0 PACKET WITH SOME DUP. DATA (0 BYTE DUPED)
		0 OUT-OF-ORDER PACKET (0 BYTE)
		0 PACKET (0 BYTE) OF DATA AFTER WINDOW
		0 WINDOW PROBE
		0 WINDOW UPDATE PACKET
		0 PACKET RECEIVED AFTER CLOSE
		0 BAD RESET
		0 DISCARDED FOR BAD CHECKSUM
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
		0 DISCARDED FOR BAD HEADER OFFSET FIELD
		0 DISCARDED BECAUSE PACKET TOO SHORT
	0 CONNECTION REQUEST
	0 CONNECTION ACCEPT
	0 BAD CONNECTION ATTEMPT
	0 LISTEN QUEUE OVERFLOW
	0 CONNECTION ESTABLISHED (INCLUDING ACCEPTS)
	0 CONNECTION CLOSED (INCLUDING 0 DROP)
		0 CONNECTION UPDATED CACHED RTT ON CLOSE
		0 CONNECTION UPDATED CACHED RTT VARIANCE ON CLOSE
		0 CONNECTION UPDATED CACHED SSTHRESH ON CLOSE
	0 EMBRYONIC CONNECTION DROPPED
	0 SEGMENT UPDATED RTT (OF 0 ATTEMPT)
	0 RETRANSMIT TIMEOUT
		0 CONNECTION DROPPED BY REXMIT TIMEOUT
		0 CONNECTION DROPPED AFTER RETRANSMITTING FIN
	0 PERSIST TIMEOUT
		0 CONNECTION DROPPED BY PERSIST TIMEOUT
	0 KEEPALIVE TIMEOUT
		0 KEEPALIVE PROBE SENT
		0 CONNECTION DROPPED BY KEEPALIVE
	0 CORRECT ACK HEADER PREDICTION
	0 CORRECT DATA PACKET HEADER PREDICTION
	0 SACK RECOVERY EPISODE
	0 SEGMENT REXMIT IN SACK RECOVERY EPISODES
	0 BYTE REXMIT IN SACK RECOVERY EPISODES
	0 SACK OPTION (SACK BLOCKS) RECEIVED
	0 SACK OPTION (SACK BLOCKS) SENT
	0 SACK SCOREBOARD OVERFLOW
	0 LRO COALESCED PACKET
		0 TIME LRO FLOW TABLE WAS FULL
		0 COLLISION IN LRO FLOW TABLE
		0 TIME LRO COALESCED 2 PACKETS
		0 TIME LRO COALESCED 3 OR 4 PACKETS
		0 TIME LRO COALESCED 5 OR MORE PACKETS
	0 LIMITED TRANSMIT DONE
	0 EARLY RETRANSMIT DONE
	0 TIME CUMULATIVE ACK ADVANCED ALONG WITH SACK
	0 PROBE TIMEOUT
		0 TIME RETRANSMIT TIMEOUT TRIGGERED AFTER PROBE
		0 TIME PROBE PACKETS WERE SENT FOR AN INTERFACE
		0 TIME COULDN'T SEND PROBE PACKETS FOR AN INTERFACE
		0 TIME FAST RECOVERY AFTER TAIL LOSS
		0 TIME RECOVERED LAST PACKET 
		0 SACK BASED RESCUE RETRANSMIT
	0 CLIENT CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 CLIENT CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME GRACEFUL FALLBACK TO NON-ECN CONNECTION
		0 TIME LOST ECN NEGOTIATING SYN, FOLLOWED BY RETRANSMISSION
		0 SERVER CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 SERVER CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME LOST ECN NEGOTIATING SYN-ACK, FOLLOWED BY RETRANSMISSION
		0 TIME RECEIVED CONGESTION EXPERIENCED (CE) NOTIFICATION
		0 TIME CWR WAS SENT IN RESPONSE TO ECE
		0 TIME SENT ECE NOTIFICATION
		0 CONNECTION RECEIVED CE ATLEAST ONCE
		0 CONNECTION RECEIVED ECE ATLEAST ONCE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS BUT NO CE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS AND CE
		0 CONNECTION USING ECN RECEIVED CE BUT NO PACKET LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO SYN-LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO REORDERING
		0 CONNECTION FELL BACK TO NON-ECN DUE TO EXCESSIVE CE-MARKINGS
	0 TIME PACKET REORDERING WAS DETECTED ON A CONNECTION
		0 TIME TRANSMITTED PACKETS WERE REORDERED
		0 TIME FAST RECOVERY WAS DELAYED TO HANDLE REORDERING
		0 TIME RETRANSMISSION WAS AVOIDED BY DELAYING RECOVERY
		0 RETRANSMISSION NOT NEEDED 
	0 TIME DSACK OPTION WAS SENT
		0 TIME DSACK OPTION WAS RECEIVED
		0 TIME DSACK WAS DISABLED ON A CONNECTION
		0 TIME RECOVERED FROM BAD RETRANSMISSION USING DSACK
		0 TIME IGNORED DSACK DUE TO ACK LOSS
		0 TIME IGNORED OLD DSACK OPTIONS
	0 TIME PMTU BLACKHOLE DETECTION, SIZE REVERTED
	0 CONNECTION WERE DROPPED AFTER LONG SLEEP
	0 TIME A TFO-COOKIE HAS BEEN ANNOUNCED
	0 SYN WITH DATA AND A VALID TFO-COOKIE HAVE BEEN RECEIVED
	0 SYN WITH TFO-COOKIE-REQUEST RECEIVED
	0 TIME AN INVALID TFO-COOKIE HAS BEEN RECEIVED
	0 TIME WE REQUESTED A TFO-COOKIE
		0 TIME THE PEER ANNOUNCED A TFO-COOKIE
	0 TIME WE COMBINED SYN WITH DATA AND A TFO-COOKIE
		0 TIME OUR SYN WITH DATA HAS BEEN ACKNOWLEDGED
	0 TIME A CONNECTION-ATTEMPT WITH TFO FELL BACK TO REGULAR TCP
	0 TIME A TFO-CONNECTION BLACKHOLE'D
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO DEFAULT
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO MEDIUM
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO LOW
	0 TIMER DRIFT LESS OR EQUAL TO 1 MS
	0 TIMER DRIFT LESS OR EQUAL TO 10 MS
	0 TIMER DRIFT LESS OR EQUAL TO 20 MS
	0 TIMER DRIFT LESS OR EQUAL TO 50 MS
	0 TIMER DRIFT LESS OR EQUAL TO 100 MS
	0 TIMER DRIFT LESS OR EQUAL TO 200 MS
	0 TIMER DRIFT LESS OR EQUAL TO 500 MS
	0 TIMER DRIFT LESS OR EQUAL TO 1000 MS
	0 TIMER DRIFT GREATER THAN TO 1000 MS
UDP:
	532159 DATAGRAMS RECEIVED
		0 WITH INCOMPLETE HEADER
		0 WITH BAD DATA LENGTH FIELD
		0 WITH BAD CHECKSUM
		54 WITH NO CHECKSUM
		500494 CHECKSUMMED IN SOFTWARE
			252356 DATAGRAMS (80011152 BYTES) OVER IPV4
			248138 DATAGRAMS (109555695 BYTES) OVER IPV6
		5346 DROPPED DUE TO NO SOCKET
		3618 BROADCAST/MULTICAST DATAGRAMS UNDELIVERED
		0 TIME MULTICAST SOURCE FILTER MATCHED
		1 DROPPED DUE TO FULL SOCKET BUFFERS
		0 NOT FOR HASHED PCB
		523194 DELIVERED
	143363 DATAGRAMS OUTPUT
		150563 CHECKSUMMED IN SOFTWARE
			56107 DATAGRAMS (11976191 BYTES) OVER IPV4
			94456 DATAGRAMS (20829404 BYTES) OVER IPV6
ICMP:
	1398 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED 'CUZ OLD MESSAGE WAS ICMP
	OUTPUT HISTOGRAM:
		ECHO REPLY: 38
		DESTINATION UNREACHABLE: 1398
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	1 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	0 MULTICAST ECHO REQUESTS IGNORED
	0 MULTICAST TIMESTAMP REQUESTS IGNORED
	INPUT HISTOGRAM:
		ECHO REPLY: 3
		DESTINATION UNREACHABLE: 2007
		ECHO: 38
		ROUTER ADVERTISEMENT: 147
	38 MESSAGE RESPONSES GENERATED
	ICMP ADDRESS MASK RESPONSES ARE DISABLED
IGMP:
	1636 MESSAGES RECEIVED
	0 MESSAGE RECEIVED WITH TOO FEW BYTES
	0 MESSAGE RECEIVED WITH WRONG TTL
	0 MESSAGE RECEIVED WITH BAD CHECKSUM
	565 V1/V2 MEMBERSHIP QUERIES RECEIVED
	287 V3 MEMBERSHIP QUERIES RECEIVED
	0 MEMBERSHIP QUERIES RECEIVED WITH INVALID FIELD(S)
	834 GENERAL QUERIES RECEIVED
	18 GROUP QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES DROPPED
	784 MEMBERSHIP REPORTS RECEIVED
	0 MEMBERSHIP REPORT RECEIVED WITH INVALID FIELD(S)
	784 MEMBERSHIP REPORTS RECEIVED FOR GROUPS TO WHICH WE BELONG
	0 V3 REPORT RECEIVED WITHOUT ROUTER ALERT
	890 MEMBERSHIP REPORTS SENT
IPSEC:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
ARP:
	1609 BROADAST ARP REQUESTS SENT
	9 UNICAST ARP REQUESTS SENT
	3320 ARP REPLIES SENT
	0 ARP ANNOUNCEMENT SENT
	11630 ARP REQUESTS RECEIVED
	1357 ARP REPLIES RECEIVED
	12989 TOTAL ARP PACKETS RECEIVED
	0 ARP CONFLICT PROBE SENT
	0 INVALID ARP RESOLVE REQUEST
	0 TOTAL PACKET DROPPED DUE TO LACK OF MEMORY
	0 TOTAL PACKET HELD AWAITING ARP REPLY
	43 TOTAL PACKETS DROPPED DUE TO NO ARP ENTRY
	378 TOTAL PACKETS DROPPED DURING ARP ENTRY REMOVAL
	1468 ARP ENTRIES TIMED OUT
	0 DUPLICATE IP SEEN
MPTCP:
	0 DATA PACKET SENT
	0 DATA BYTE SENT
	0 DATA PACKET RECEIVED
	0 DATA BYTE RECEIVED
	0 PACKET WITH AN INVALID MPCAP OPTION
	0 PACKET WITH AN INVALID MPJOIN OPTION
	0 TIME PRIMARY SUBFLOW FELL BACK TO TCP
	0 TIME SECONDARY SUBFLOW FELL BACK TO TCP
	0 DSS OPTION DROP
	0 OTHER INVALID MPTCP OPTION
	0 TIME THE MPTCP SUBFLOW WINDOW WAS REDUCED
	0 BAD DSS CHECKSUM
	0 TIME RECEIVED OUT OF ORDER DATA 
	0 SUBFLOW SWITCH
	0 SUBFLOW SWITCH DUE TO ADVISORY
	0 SUBFLOW SWITCH DUE TO RTT
	0 SUBFLOW SWITCH DUE TO RTO
	0 SUBFLOW SWITCH DUE TO PEER
	0 NUMBER OF SUBFLOW PROBE
IP6:
	756015 TOTAL PACKETS RECEIVED
		0 WITH SIZE SMALLER THAN MINIMUM
		0 WITH DATA SIZE < DATA LENGTH
		0 WITH DATA SIZE > DATA LENGTH
			0 PACKET FORCED TO SOFTWARE CHECKSUM
		0 WITH BAD OPTIONS
		168 WITH INCORRECT VERSION NUMBER
		8 FRAGMENTS RECEIVED
			0 DROPPED (DUP OR OUT OF SPACE)
			0 DROPPED AFTER TIMEOUT
			0 EXCEEDED LIMIT
			4 REASSEMBLED OK
			0 ATOMIC FRAGMENTS RECEIVED
		681255 PACKETS FOR THIS HOST
		0 PACKET FORWARDED
		33571 PACKETS NOT FORWARDABLE
		0 REDIRECT SENT
		33514 MULTICAST PACKETS WHICH WE DON'T JOIN
		0 PACKET WHOSE HEADERS ARE NOT CONTINUOUS
		0 TUNNELING PACKET THAT CAN'T FIND GIF
		0 PACKET DISCARDED DUE TO TOO MAY HEADERS
		0 FORWARD CACHE HIT
		0 FORWARD CACHE MISS
		0 PACKET DROPPED DUE TO NO BUFS FOR CONTROL DATA
	343303 PACKETS SENT FROM THIS HOST
		0 PACKET SENT WITH FABRICATED IP HEADER
		0 OUTPUT PACKET DROPPED DUE TO NO BUFS, ETC.
		2291 OUTPUT PACKETS DISCARDED DUE TO NO ROUTE
		0 OUTPUT DATAGRAM FRAGMENTED
		0 FRAGMENT CREATED
		0 DATAGRAM THAT CAN'T BE FRAGMENTED
		0 PACKET THAT VIOLATED SCOPE RULES
		0 PACKET DROPPED DUE TO NECP POLICY
	INPUT HISTOGRAM:
		HOP BY HOP: 5719
		TCP: 423511
		UDP: 283765
		FRAGMENT: 8
		ICMP6: 41875
		PIM: 969
	MBUF STATISTICS:
		1787 ONE MBUF
		TWO OR MORE MBUF:
			LO0= 10540
			UTUN1= 12
		743676 ONE EXT MBUF
		0 TWO OR MORE EXT MBUF
		0 FAILURE OF SOURCE ADDRESS SELECTION
		SOURCE ADDRESSES ON AN OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES ON A NON-OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF SAME SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF A DIFFERENT SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		DEPRECATED SOURCE ADDRESSES
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESS SELECTION
			18411 RULES DEFAULT
			0 RULE PREFER SAME ADDRESS
			5051 RULES PREFER APPROPRIATE SCOPE
			0 RULE AVOID DEPRECATED ADDRESSES
			0 RULE PREFER HOME ADDRESSES
			0 RULE PREFER OUTGOING INTERFACE
			10 RULES PREFER MATCHING LABEL
			47351 RULES PREFER TEMPORARY ADDRESSES
			0 RULE PREFER ADDRESSES ON ALIVE INTERFACES
			0 RULE USE LONGEST MATCHING PREFIX
		0 DUPLICATE ADDRESS DETECTION COLLISION
		0 DUPLICATE ADDRESS DETECTION NS LOOP
		0 TIME IGNORED SOURCE ON SECONDARY EXPENSIVE I/F
ICMP6:
	1726 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED BECAUSE OLD MESSAGE WAS ICMP ERROR OR SO
	0 ERROR NOT GENERATED BECAUSE RATE LIMITATION
	OUTPUT HISTOGRAM:
		UNREACH: 1726
		MLDV1 LISTENER REPORT: 77
		MLDV1 LISTENER DONE: 11
		ROUTER SOLICITATION: 123
		NEIGHBOR SOLICITATION: 5230
		NEIGHBOR ADVERTISEMENT: 4406
		MLDV2 LISTENER REPORT: 1188
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	0 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	INPUT HISTOGRAM:
		UNREACH: 150
		MULTICAST LISTENER QUERY: 2080
		ROUTER ADVERTISEMENT: 30077
		NEIGHBOR SOLICITATION: 4406
		NEIGHBOR ADVERTISEMENT: 4377
	HISTOGRAM OF ERROR MESSAGES TO BE GENERATED:
		0 NO ROUTE
		0 ADMINISTRATIVELY PROHIBITED
		0 BEYOND SCOPE
		150 ADDRESS UNREACHABLE
		1576 PORT UNREACHABLE
		0 PACKET TOO BIG
		0 TIME EXCEED TRANSIT
		0 TIME EXCEED REASSEMBLY
		0 ERRONEOUS HEADER FIELD
		0 UNRECOGNIZED NEXT HEADER
		0 UNRECOGNIZED OPTION
		0 REDIRECT
		0 UNKNOWN
	0 MESSAGE RESPONSE GENERATED
	0 MESSAGE WITH TOO MANY ND OPTIONS
	0 MESSAGE WITH BAD ND OPTIONS
	0 BAD NEIGHBOR SOLICITATION MESSAGE
	0 BAD NEIGHBOR ADVERTISEMENT MESSAGE
	0 BAD ROUTER SOLICITATION MESSAGE
	0 BAD ROUTER ADVERTISEMENT MESSAGE
	0 BAD REDIRECT MESSAGE
	0 PATH MTU CHANGE
	0 DROPPED FRAGMENTED NDP MESSAGE
IPSEC6:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
RIP6:
	0 MESSAGE RECEIVED
	0 CHECKSUM CALCULATION ON INBOUND
	0 MESSAGE WITH BAD CHECKSUM
	0 MESSAGE DROPPED DUE TO NO SOCKET
	0 MULTICAST MESSAGE DROPPED DUE TO NO SOCKET
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	0 DELIVERED
	0 DATAGRAM OUTPUT
PFKEY:
	0 REQUEST SENT TO USERLAND
	0 BYTE SENT TO USERLAND
	0 MESSAGE WITH INVALID LENGTH FIELD
	0 MESSAGE WITH INVALID VERSION FIELD
	0 MESSAGE WITH INVALID MESSAGE TYPE FIELD
	0 MESSAGE TOO SHORT
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
	0 MESSAGE WITH DUPLICATE EXTENSION
	0 MESSAGE WITH INVALID EXTENSION TYPE
	0 MESSAGE WITH INVALID SA TYPE
	0 MESSAGE WITH INVALID ADDRESS EXTENSION
	0 REQUEST SENT FROM USERLAND
	0 BYTE SENT FROM USERLAND
	0 MESSAGE TOWARD SINGLE SOCKET
	0 MESSAGE TOWARD ALL SOCKETS
	0 MESSAGE TOWARD REGISTERED SOCKETS
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
KEVT:
	24 CURRENT KERNEL CONTROL SOCKETS
	18940 KERNEL CONTROL GENERATION COUNT
	0 BAD VENDOR FAILURE
	7345 MESSAGE TOO BIG FAILURES
	0 OUT OF MEMORY FAILURE
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	273989 MESSAGES POSTED
KCTL:
	0 TOTAL KERNEL CONTROL MODULE REGISTERED
	12 CURRENT KERNEL CONTROL MODULES REGISTERED
	55 CURRENT KERNEL CONTROL SOCKETS
	1117 KERNEL CONTROL GENERATION COUNT
	580 CONNECTION ATTEMPTS
	0 CONNECTION FAILURE
	35 SEND FAILURES
	0 SEND LIST FAILURE
	0 ENQUEUE FAILURE
	0 PACKET DROPPED DUE TO FULL SOCKET BUFFERS
XBKIDLE:
	1 MAX PER PROCESS
	600 MAXIMUM TIME (SECONDS)
	131072 HIGH WATER MARK
	0 SOCKET OPTION NOT SUPPORTED FAILURE
	0 TOO MANY SOCKETS FAILURE
	0 TOTAL SOCKET REQUESTED OK
	0 EXTENDED BK IDLE SOCKET
	0 NO CELLULAR FAILURE
	0 NO TIME FAILURES
	0 FORCED DEFUNCT SOCKET
	0 RESUMED SOCKET
	0 TIMEOUT EXPIRED FAILURE
	0 TIMER RESCHEDULED
	0 NO DELEGATED FAILURE
NET_API:
	2 INTERFACE FILTERS CURRENTLY ATTACHED
	2 INTERFACE FILTERS ATTACHED SINCE BOOT
	2 INTERFACE FILTERS ATTACHED SINCE BOOT BY OS
	0 IP FILTER CURRENTLY ATTACHED
	0 IP FILTER ATTACHED SINCE BOOT
	0 IP FILTER ATTACHED SINCE BOOT BY OS
	4 SOCKET FILTERS CURRENTLY ATTACHED
	4 SOCKET FILTERS ATTACHED SINCE BOOT
	4 SOCKET FILTERS ATTACHED SINCE BOOT BY OS
	326289 SOCKETS ALLOCATED SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL BY OS
	2472 SOCKETS WITH NECP CLIENT UUID SINCE BOOT
	104318 LOCAL DOMAIN SOCKETS ALLOCATED SINCE BOOT
	1199 ROUTE DOMAIN SOCKETS ALLOCATED SINCE BOOT
	124419 INET DOMAIN SOCKETS ALLOCATED SINCE BOOT
	59905 INET6 DOMAIN SOCKETS ALLOCATED SINCE BOOT
	10062 SYSTEM DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 MULTIPATH DOMAIN SOCKET ALLOCATED SINCE BOOT
	0 KEY DOMAIN SOCKET ALLOCATED SINCE BOOT
	5 NDRV DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 OTHER DOMAINS SOCKET ALLOCATED SINCE BOOT
	15555 IPV4 STREAM SOCKETS CREATED SINCE BOOT
	108864 IPV4 DATAGRAM SOCKETS CREATED SINCE BOOT
	10299 IPV4 DATAGRAM SOCKETS CONNECTED
	38101 IPV4 DNS SOCKETS
	102165 IPV4 DATAGRAM SOCKETS WITHOUT DATA
	7566 IPV6 STREAM SOCKETS CREATED SINCE BOOT
	52339 IPV6 DATAGRAM SOCKETS CREATED SINCE BOOT
	34877 IPV6 DATAGRAM SOCKETS CONNECTED
	0 IPV6 DNS SOCKET
	28267 IPV6 DATAGRAM SOCKETS WITHOUT DATA
	1115 SOCKET MULTICAST JOINS SINCE BOOT
	1115 SOCKET MULTICAST JOINS SINCE BOOT BY OS
	0 IPV4 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV4 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED
	12 INTERFACES ALLOCATED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED BY OS
	12 EXTENDED INTERFACES ALLOCATED SINCE BOOT BY OS
	2 PF ADDRULE OPERATIONS SINCE BOOT
	0 PF ADDRULE OPERATION SINCE BOOT BY OS
	0 VMNET START SINCE BOOT

raymond

/Users/raymond/a.txt

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
TCP:
	0 PACKET SENT
		0 DATA PACKET (0 BYTE)
		0 DATA PACKET (0 BYTE) RETRANSMITTED
		0 RESEND INITIATED BY MTU DISCOVERY
		0 ACK-ONLY PACKET (0 DELAYED)
		0 URG ONLY PACKET
		0 WINDOW PROBE PACKET
		0 WINDOW UPDATE PACKET
		0 CONTROL PACKET
		0 DATA PACKET SENT AFTER FLOW CONTROL
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
	0 PACKET RECEIVED
		0 ACK (FOR 0 BYTE)
		0 DUPLICATE ACK
		0 ACK FOR UNSENT DATA
		0 PACKET (0 BYTE) RECEIVED IN-SEQUENCE
		0 COMPLETELY DUPLICATE PACKET (0 BYTE)
		0 OLD DUPLICATE PACKET
		0 RECEIVED PACKET DROPPED DUE TO LOW MEMORY
		0 PACKET WITH SOME DUP. DATA (0 BYTE DUPED)
		0 OUT-OF-ORDER PACKET (0 BYTE)
		0 PACKET (0 BYTE) OF DATA AFTER WINDOW
		0 WINDOW PROBE
		0 WINDOW UPDATE PACKET
		0 PACKET RECEIVED AFTER CLOSE
		0 BAD RESET
		0 DISCARDED FOR BAD CHECKSUM
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
		0 DISCARDED FOR BAD HEADER OFFSET FIELD
		0 DISCARDED BECAUSE PACKET TOO SHORT
	0 CONNECTION REQUEST
	0 CONNECTION ACCEPT
	0 BAD CONNECTION ATTEMPT
	0 LISTEN QUEUE OVERFLOW
	0 CONNECTION ESTABLISHED (INCLUDING ACCEPTS)
	0 CONNECTION CLOSED (INCLUDING 0 DROP)
		0 CONNECTION UPDATED CACHED RTT ON CLOSE
		0 CONNECTION UPDATED CACHED RTT VARIANCE ON CLOSE
		0 CONNECTION UPDATED CACHED SSTHRESH ON CLOSE
	0 EMBRYONIC CONNECTION DROPPED
	0 SEGMENT UPDATED RTT (OF 0 ATTEMPT)
	0 RETRANSMIT TIMEOUT
		0 CONNECTION DROPPED BY REXMIT TIMEOUT
		0 CONNECTION DROPPED AFTER RETRANSMITTING FIN
	0 PERSIST TIMEOUT
		0 CONNECTION DROPPED BY PERSIST TIMEOUT
	0 KEEPALIVE TIMEOUT
		0 KEEPALIVE PROBE SENT
		0 CONNECTION DROPPED BY KEEPALIVE
	0 CORRECT ACK HEADER PREDICTION
	0 CORRECT DATA PACKET HEADER PREDICTION
	0 SACK RECOVERY EPISODE
	0 SEGMENT REXMIT IN SACK RECOVERY EPISODES
	0 BYTE REXMIT IN SACK RECOVERY EPISODES
	0 SACK OPTION (SACK BLOCKS) RECEIVED
	0 SACK OPTION (SACK BLOCKS) SENT
	0 SACK SCOREBOARD OVERFLOW
	0 LRO COALESCED PACKET
		0 TIME LRO FLOW TABLE WAS FULL
		0 COLLISION IN LRO FLOW TABLE
		0 TIME LRO COALESCED 2 PACKETS
		0 TIME LRO COALESCED 3 OR 4 PACKETS
		0 TIME LRO COALESCED 5 OR MORE PACKETS
	0 LIMITED TRANSMIT DONE
	0 EARLY RETRANSMIT DONE
	0 TIME CUMULATIVE ACK ADVANCED ALONG WITH SACK
	0 PROBE TIMEOUT
		0 TIME RETRANSMIT TIMEOUT TRIGGERED AFTER PROBE
		0 TIME PROBE PACKETS WERE SENT FOR AN INTERFACE
		0 TIME COULDN'T SEND PROBE PACKETS FOR AN INTERFACE
		0 TIME FAST RECOVERY AFTER TAIL LOSS
		0 TIME RECOVERED LAST PACKET 
		0 SACK BASED RESCUE RETRANSMIT
	0 CLIENT CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 CLIENT CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME GRACEFUL FALLBACK TO NON-ECN CONNECTION
		0 TIME LOST ECN NEGOTIATING SYN, FOLLOWED BY RETRANSMISSION
		0 SERVER CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 SERVER CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME LOST ECN NEGOTIATING SYN-ACK, FOLLOWED BY RETRANSMISSION
		0 TIME RECEIVED CONGESTION EXPERIENCED (CE) NOTIFICATION
		0 TIME CWR WAS SENT IN RESPONSE TO ECE
		0 TIME SENT ECE NOTIFICATION
		0 CONNECTION RECEIVED CE ATLEAST ONCE
		0 CONNECTION RECEIVED ECE ATLEAST ONCE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS BUT NO CE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS AND CE
		0 CONNECTION USING ECN RECEIVED CE BUT NO PACKET LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO SYN-LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO REORDERING
		0 CONNECTION FELL BACK TO NON-ECN DUE TO EXCESSIVE CE-MARKINGS
	0 TIME PACKET REORDERING WAS DETECTED ON A CONNECTION
		0 TIME TRANSMITTED PACKETS WERE REORDERED
		0 TIME FAST RECOVERY WAS DELAYED TO HANDLE REORDERING
		0 TIME RETRANSMISSION WAS AVOIDED BY DELAYING RECOVERY
		0 RETRANSMISSION NOT NEEDED 
	0 TIME DSACK OPTION WAS SENT
		0 TIME DSACK OPTION WAS RECEIVED
		0 TIME DSACK WAS DISABLED ON A CONNECTION
		0 TIME RECOVERED FROM BAD RETRANSMISSION USING DSACK
		0 TIME IGNORED DSACK DUE TO ACK LOSS
		0 TIME IGNORED OLD DSACK OPTIONS
	0 TIME PMTU BLACKHOLE DETECTION, SIZE REVERTED
	0 CONNECTION WERE DROPPED AFTER LONG SLEEP
	0 TIME A TFO-COOKIE HAS BEEN ANNOUNCED
	0 SYN WITH DATA AND A VALID TFO-COOKIE HAVE BEEN RECEIVED
	0 SYN WITH TFO-COOKIE-REQUEST RECEIVED
	0 TIME AN INVALID TFO-COOKIE HAS BEEN RECEIVED
	0 TIME WE REQUESTED A TFO-COOKIE
		0 TIME THE PEER ANNOUNCED A TFO-COOKIE
	0 TIME WE COMBINED SYN WITH DATA AND A TFO-COOKIE
		0 TIME OUR SYN WITH DATA HAS BEEN ACKNOWLEDGED
	0 TIME A CONNECTION-ATTEMPT WITH TFO FELL BACK TO REGULAR TCP
	0 TIME A TFO-CONNECTION BLACKHOLE'D
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO DEFAULT
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO MEDIUM
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO LOW
	0 TIMER DRIFT LESS OR EQUAL TO 1 MS
	0 TIMER DRIFT LESS OR EQUAL TO 10 MS
	0 TIMER DRIFT LESS OR EQUAL TO 20 MS
	0 TIMER DRIFT LESS OR EQUAL TO 50 MS
	0 TIMER DRIFT LESS OR EQUAL TO 100 MS
	0 TIMER DRIFT LESS OR EQUAL TO 200 MS
	0 TIMER DRIFT LESS OR EQUAL TO 500 MS
	0 TIMER DRIFT LESS OR EQUAL TO 1000 MS
	0 TIMER DRIFT GREATER THAN TO 1000 MS
UDP:
	534132 DATAGRAMS RECEIVED
		0 WITH INCOMPLETE HEADER
		0 WITH BAD DATA LENGTH FIELD
		0 WITH BAD CHECKSUM
		54 WITH NO CHECKSUM
		502441 CHECKSUMMED IN SOFTWARE
			253394 DATAGRAMS (80259286 BYTES) OVER IPV4
			249047 DATAGRAMS (109774596 BYTES) OVER IPV6
		5346 DROPPED DUE TO NO SOCKET
		3618 BROADCAST/MULTICAST DATAGRAMS UNDELIVERED
		0 TIME MULTICAST SOURCE FILTER MATCHED
		1 DROPPED DUE TO FULL SOCKET BUFFERS
		0 NOT FOR HASHED PCB
		525167 DELIVERED
	143429 DATAGRAMS OUTPUT
		150640 CHECKSUMMED IN SOFTWARE
			56160 DATAGRAMS (11991557 BYTES) OVER IPV4
			94480 DATAGRAMS (20836786 BYTES) OVER IPV6
ICMP:
	1398 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED 'CUZ OLD MESSAGE WAS ICMP
	OUTPUT HISTOGRAM:
		ECHO REPLY: 38
		DESTINATION UNREACHABLE: 1398
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	1 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	0 MULTICAST ECHO REQUESTS IGNORED
	0 MULTICAST TIMESTAMP REQUESTS IGNORED
	INPUT HISTOGRAM:
		ECHO REPLY: 3
		DESTINATION UNREACHABLE: 2007
		ECHO: 38
		ROUTER ADVERTISEMENT: 147
	38 MESSAGE RESPONSES GENERATED
	ICMP ADDRESS MASK RESPONSES ARE DISABLED
IGMP:
	1637 MESSAGES RECEIVED
	0 MESSAGE RECEIVED WITH TOO FEW BYTES
	0 MESSAGE RECEIVED WITH WRONG TTL
	0 MESSAGE RECEIVED WITH BAD CHECKSUM
	566 V1/V2 MEMBERSHIP QUERIES RECEIVED
	287 V3 MEMBERSHIP QUERIES RECEIVED
	0 MEMBERSHIP QUERIES RECEIVED WITH INVALID FIELD(S)
	835 GENERAL QUERIES RECEIVED
	18 GROUP QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES DROPPED
	784 MEMBERSHIP REPORTS RECEIVED
	0 MEMBERSHIP REPORT RECEIVED WITH INVALID FIELD(S)
	784 MEMBERSHIP REPORTS RECEIVED FOR GROUPS TO WHICH WE BELONG
	0 V3 REPORT RECEIVED WITHOUT ROUTER ALERT
	891 MEMBERSHIP REPORTS SENT
IPSEC:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
ARP:
	1612 BROADAST ARP REQUESTS SENT
	9 UNICAST ARP REQUESTS SENT
	3320 ARP REPLIES SENT
	0 ARP ANNOUNCEMENT SENT
	11630 ARP REQUESTS RECEIVED
	1360 ARP REPLIES RECEIVED
	12992 TOTAL ARP PACKETS RECEIVED
	0 ARP CONFLICT PROBE SENT
	0 INVALID ARP RESOLVE REQUEST
	0 TOTAL PACKET DROPPED DUE TO LACK OF MEMORY
	0 TOTAL PACKET HELD AWAITING ARP REPLY
	43 TOTAL PACKETS DROPPED DUE TO NO ARP ENTRY
	378 TOTAL PACKETS DROPPED DURING ARP ENTRY REMOVAL
	1488 ARP ENTRIES TIMED OUT
	0 DUPLICATE IP SEEN
MPTCP:
	0 DATA PACKET SENT
	0 DATA BYTE SENT
	0 DATA PACKET RECEIVED
	0 DATA BYTE RECEIVED
	0 PACKET WITH AN INVALID MPCAP OPTION
	0 PACKET WITH AN INVALID MPJOIN OPTION
	0 TIME PRIMARY SUBFLOW FELL BACK TO TCP
	0 TIME SECONDARY SUBFLOW FELL BACK TO TCP
	0 DSS OPTION DROP
	0 OTHER INVALID MPTCP OPTION
	0 TIME THE MPTCP SUBFLOW WINDOW WAS REDUCED
	0 BAD DSS CHECKSUM
	0 TIME RECEIVED OUT OF ORDER DATA 
	0 SUBFLOW SWITCH
	0 SUBFLOW SWITCH DUE TO ADVISORY
	0 SUBFLOW SWITCH DUE TO RTT
	0 SUBFLOW SWITCH DUE TO RTO
	0 SUBFLOW SWITCH DUE TO PEER
	0 NUMBER OF SUBFLOW PROBE
IP6:
	757126 TOTAL PACKETS RECEIVED
		0 WITH SIZE SMALLER THAN MINIMUM
		0 WITH DATA SIZE < DATA LENGTH
		0 WITH DATA SIZE > DATA LENGTH
			0 PACKET FORCED TO SOFTWARE CHECKSUM
		0 WITH BAD OPTIONS
		168 WITH INCORRECT VERSION NUMBER
		8 FRAGMENTS RECEIVED
			0 DROPPED (DUP OR OUT OF SPACE)
			0 DROPPED AFTER TIMEOUT
			0 EXCEEDED LIMIT
			4 REASSEMBLED OK
			0 ATOMIC FRAGMENTS RECEIVED
		682259 PACKETS FOR THIS HOST
		0 PACKET FORWARDED
		33636 PACKETS NOT FORWARDABLE
		0 REDIRECT SENT
		33579 MULTICAST PACKETS WHICH WE DON'T JOIN
		0 PACKET WHOSE HEADERS ARE NOT CONTINUOUS
		0 TUNNELING PACKET THAT CAN'T FIND GIF
		0 PACKET DISCARDED DUE TO TOO MAY HEADERS
		0 FORWARD CACHE HIT
		0 FORWARD CACHE MISS
		0 PACKET DROPPED DUE TO NO BUFS FOR CONTROL DATA
	343417 PACKETS SENT FROM THIS HOST
		0 PACKET SENT WITH FABRICATED IP HEADER
		0 OUTPUT PACKET DROPPED DUE TO NO BUFS, ETC.
		2291 OUTPUT PACKETS DISCARDED DUE TO NO ROUTE
		0 OUTPUT DATAGRAM FRAGMENTED
		0 FRAGMENT CREATED
		0 DATAGRAM THAT CAN'T BE FRAGMENTED
		0 PACKET THAT VIOLATED SCOPE RULES
		0 PACKET DROPPED DUE TO NECP POLICY
	INPUT HISTOGRAM:
		HOP BY HOP: 5729
		TCP: 423595
		UDP: 284742
		FRAGMENT: 8
		ICMP6: 41911
		PIM: 973
	MBUF STATISTICS:
		1787 ONE MBUF
		TWO OR MORE MBUF:
			LO0= 10551
			UTUN1= 12
		744776 ONE EXT MBUF
		0 TWO OR MORE EXT MBUF
		0 FAILURE OF SOURCE ADDRESS SELECTION
		SOURCE ADDRESSES ON AN OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES ON A NON-OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF SAME SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF A DIFFERENT SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		DEPRECATED SOURCE ADDRESSES
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESS SELECTION
			18427 RULES DEFAULT
			0 RULE PREFER SAME ADDRESS
			5055 RULES PREFER APPROPRIATE SCOPE
			0 RULE AVOID DEPRECATED ADDRESSES
			0 RULE PREFER HOME ADDRESSES
			0 RULE PREFER OUTGOING INTERFACE
			10 RULES PREFER MATCHING LABEL
			47351 RULES PREFER TEMPORARY ADDRESSES
			0 RULE PREFER ADDRESSES ON ALIVE INTERFACES
			0 RULE USE LONGEST MATCHING PREFIX
		0 DUPLICATE ADDRESS DETECTION COLLISION
		0 DUPLICATE ADDRESS DETECTION NS LOOP
		0 TIME IGNORED SOURCE ON SECONDARY EXPENSIVE I/F
ICMP6:
	1726 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED BECAUSE OLD MESSAGE WAS ICMP ERROR OR SO
	0 ERROR NOT GENERATED BECAUSE RATE LIMITATION
	OUTPUT HISTOGRAM:
		UNREACH: 1726
		MLDV1 LISTENER REPORT: 77
		MLDV1 LISTENER DONE: 11
		ROUTER SOLICITATION: 123
		NEIGHBOR SOLICITATION: 5233
		NEIGHBOR ADVERTISEMENT: 4406
		MLDV2 LISTENER REPORT: 1194
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	0 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	INPUT HISTOGRAM:
		UNREACH: 150
		MULTICAST LISTENER QUERY: 2086
		ROUTER ADVERTISEMENT: 30110
		NEIGHBOR SOLICITATION: 4406
		NEIGHBOR ADVERTISEMENT: 4380
	HISTOGRAM OF ERROR MESSAGES TO BE GENERATED:
		0 NO ROUTE
		0 ADMINISTRATIVELY PROHIBITED
		0 BEYOND SCOPE
		150 ADDRESS UNREACHABLE
		1576 PORT UNREACHABLE
		0 PACKET TOO BIG
		0 TIME EXCEED TRANSIT
		0 TIME EXCEED REASSEMBLY
		0 ERRONEOUS HEADER FIELD
		0 UNRECOGNIZED NEXT HEADER
		0 UNRECOGNIZED OPTION
		0 REDIRECT
		0 UNKNOWN
	0 MESSAGE RESPONSE GENERATED
	0 MESSAGE WITH TOO MANY ND OPTIONS
	0 MESSAGE WITH BAD ND OPTIONS
	0 BAD NEIGHBOR SOLICITATION MESSAGE
	0 BAD NEIGHBOR ADVERTISEMENT MESSAGE
	0 BAD ROUTER SOLICITATION MESSAGE
	0 BAD ROUTER ADVERTISEMENT MESSAGE
	0 BAD REDIRECT MESSAGE
	0 PATH MTU CHANGE
	0 DROPPED FRAGMENTED NDP MESSAGE
IPSEC6:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
RIP6:
	0 MESSAGE RECEIVED
	0 CHECKSUM CALCULATION ON INBOUND
	0 MESSAGE WITH BAD CHECKSUM
	0 MESSAGE DROPPED DUE TO NO SOCKET
	0 MULTICAST MESSAGE DROPPED DUE TO NO SOCKET
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	0 DELIVERED
	0 DATAGRAM OUTPUT
PFKEY:
	0 REQUEST SENT TO USERLAND
	0 BYTE SENT TO USERLAND
	0 MESSAGE WITH INVALID LENGTH FIELD
	0 MESSAGE WITH INVALID VERSION FIELD
	0 MESSAGE WITH INVALID MESSAGE TYPE FIELD
	0 MESSAGE TOO SHORT
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
	0 MESSAGE WITH DUPLICATE EXTENSION
	0 MESSAGE WITH INVALID EXTENSION TYPE
	0 MESSAGE WITH INVALID SA TYPE
	0 MESSAGE WITH INVALID ADDRESS EXTENSION
	0 REQUEST SENT FROM USERLAND
	0 BYTE SENT FROM USERLAND
	0 MESSAGE TOWARD SINGLE SOCKET
	0 MESSAGE TOWARD ALL SOCKETS
	0 MESSAGE TOWARD REGISTERED SOCKETS
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
KEVT:
	24 CURRENT KERNEL CONTROL SOCKETS
	18940 KERNEL CONTROL GENERATION COUNT
	0 BAD VENDOR FAILURE
	7345 MESSAGE TOO BIG FAILURES
	0 OUT OF MEMORY FAILURE
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	274083 MESSAGES POSTED
KCTL:
	0 TOTAL KERNEL CONTROL MODULE REGISTERED
	12 CURRENT KERNEL CONTROL MODULES REGISTERED
	55 CURRENT KERNEL CONTROL SOCKETS
	1117 KERNEL CONTROL GENERATION COUNT
	580 CONNECTION ATTEMPTS
	0 CONNECTION FAILURE
	35 SEND FAILURES
	0 SEND LIST FAILURE
	0 ENQUEUE FAILURE
	0 PACKET DROPPED DUE TO FULL SOCKET BUFFERS
XBKIDLE:
	1 MAX PER PROCESS
	600 MAXIMUM TIME (SECONDS)
	131072 HIGH WATER MARK
	0 SOCKET OPTION NOT SUPPORTED FAILURE
	0 TOO MANY SOCKETS FAILURE
	0 TOTAL SOCKET REQUESTED OK
	0 EXTENDED BK IDLE SOCKET
	0 NO CELLULAR FAILURE
	0 NO TIME FAILURES
	0 FORCED DEFUNCT SOCKET
	0 RESUMED SOCKET
	0 TIMEOUT EXPIRED FAILURE
	0 TIMER RESCHEDULED
	0 NO DELEGATED FAILURE
NET_API:
	2 INTERFACE FILTERS CURRENTLY ATTACHED
	2 INTERFACE FILTERS ATTACHED SINCE BOOT
	2 INTERFACE FILTERS ATTACHED SINCE BOOT BY OS
	0 IP FILTER CURRENTLY ATTACHED
	0 IP FILTER ATTACHED SINCE BOOT
	0 IP FILTER ATTACHED SINCE BOOT BY OS
	4 SOCKET FILTERS CURRENTLY ATTACHED
	4 SOCKET FILTERS ATTACHED SINCE BOOT
	4 SOCKET FILTERS ATTACHED SINCE BOOT BY OS
	326305 SOCKETS ALLOCATED SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL BY OS
	2472 SOCKETS WITH NECP CLIENT UUID SINCE BOOT
	104325 LOCAL DOMAIN SOCKETS ALLOCATED SINCE BOOT
	1199 ROUTE DOMAIN SOCKETS ALLOCATED SINCE BOOT
	124422 INET DOMAIN SOCKETS ALLOCATED SINCE BOOT
	59909 INET6 DOMAIN SOCKETS ALLOCATED SINCE BOOT
	10062 SYSTEM DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 MULTIPATH DOMAIN SOCKET ALLOCATED SINCE BOOT
	0 KEY DOMAIN SOCKET ALLOCATED SINCE BOOT
	5 NDRV DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 OTHER DOMAINS SOCKET ALLOCATED SINCE BOOT
	15556 IPV4 STREAM SOCKETS CREATED SINCE BOOT
	108866 IPV4 DATAGRAM SOCKETS CREATED SINCE BOOT
	10299 IPV4 DATAGRAM SOCKETS CONNECTED
	38105 IPV4 DNS SOCKETS
	102167 IPV4 DATAGRAM SOCKETS WITHOUT DATA
	7566 IPV6 STREAM SOCKETS CREATED SINCE BOOT
	52343 IPV6 DATAGRAM SOCKETS CREATED SINCE BOOT
	34881 IPV6 DATAGRAM SOCKETS CONNECTED
	0 IPV6 DNS SOCKET
	28271 IPV6 DATAGRAM SOCKETS WITHOUT DATA
	1115 SOCKET MULTICAST JOINS SINCE BOOT
	1115 SOCKET MULTICAST JOINS SINCE BOOT BY OS
	0 IPV4 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV4 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED
	12 INTERFACES ALLOCATED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED BY OS
	12 EXTENDED INTERFACES ALLOCATED SINCE BOOT BY OS
	2 PF ADDRULE OPERATIONS SINCE BOOT
	0 PF ADDRULE OPERATION SINCE BOOT BY OS
	0 VMNET START SINCE BOOT

raymond

/Users/raymond/a.txt

PING origin-www.cisco.com (72.163.4.161): 56 data bytes
64 bytes from 72.163.4.161: icmp_seq=0 ttl=243 time=45.290 ms
64 bytes from 72.163.4.161: icmp_seq=1 ttl=243 time=43.472 ms
64 bytes from 72.163.4.161: icmp_seq=2 ttl=243 time=43.733 ms

--- origin-www.cisco.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 43.472/44.165/45.290/0.803 ms

>>> type(s)
<type 'str'>
>>> s.splitlines()
['PING origin-www.cisco.com (72.163.4.161): 56 data bytes', '64 bytes from 72.163.4.161: icmp_seq=0 ttl=243 time=45.290 ms', '64 bytes from 72.163.4.161: icmp_seq=1 ttl=243 time=43.472 ms', '64 bytes from 72.163.4.161: icmp_seq=2 ttl=243 time=43.733 ms', '', '--- origin-www.cisco.com ping statistics ---', '3 packets transmitted, 3 packets received, 0.0% packet loss', 'round-trip min/avg/max/stddev = 43.472/44.165/45.290/0.803 ms']
>>> s.splitlines()[0]
'PING origin-www.cisco.com (72.163.4.161): 56 data bytes'
>>> s.splitlines()[-1]
'round-trip min/avg/max/stddev = 43.472/44.165/45.290/0.803 ms'
>>> s.splitlines()[-2]
'3 packets transmitted, 3 packets received, 0.0% packet loss'
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
TCP:
	0 PACKET SENT
		0 DATA PACKET (0 BYTE)
		0 DATA PACKET (0 BYTE) RETRANSMITTED
		0 RESEND INITIATED BY MTU DISCOVERY
		0 ACK-ONLY PACKET (0 DELAYED)
		0 URG ONLY PACKET
		0 WINDOW PROBE PACKET
		0 WINDOW UPDATE PACKET
		0 CONTROL PACKET
		0 DATA PACKET SENT AFTER FLOW CONTROL
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
	0 PACKET RECEIVED
		0 ACK (FOR 0 BYTE)
		0 DUPLICATE ACK
		0 ACK FOR UNSENT DATA
		0 PACKET (0 BYTE) RECEIVED IN-SEQUENCE
		0 COMPLETELY DUPLICATE PACKET (0 BYTE)
		0 OLD DUPLICATE PACKET
		0 RECEIVED PACKET DROPPED DUE TO LOW MEMORY
		0 PACKET WITH SOME DUP. DATA (0 BYTE DUPED)
		0 OUT-OF-ORDER PACKET (0 BYTE)
		0 PACKET (0 BYTE) OF DATA AFTER WINDOW
		0 WINDOW PROBE
		0 WINDOW UPDATE PACKET
		0 PACKET RECEIVED AFTER CLOSE
		0 BAD RESET
		0 DISCARDED FOR BAD CHECKSUM
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
		0 DISCARDED FOR BAD HEADER OFFSET FIELD
		0 DISCARDED BECAUSE PACKET TOO SHORT
	0 CONNECTION REQUEST
	0 CONNECTION ACCEPT
	0 BAD CONNECTION ATTEMPT
	0 LISTEN QUEUE OVERFLOW
	0 CONNECTION ESTABLISHED (INCLUDING ACCEPTS)
	0 CONNECTION CLOSED (INCLUDING 0 DROP)
		0 CONNECTION UPDATED CACHED RTT ON CLOSE
		0 CONNECTION UPDATED CACHED RTT VARIANCE ON CLOSE
		0 CONNECTION UPDATED CACHED SSTHRESH ON CLOSE
	0 EMBRYONIC CONNECTION DROPPED
	0 SEGMENT UPDATED RTT (OF 0 ATTEMPT)
	0 RETRANSMIT TIMEOUT
		0 CONNECTION DROPPED BY REXMIT TIMEOUT
		0 CONNECTION DROPPED AFTER RETRANSMITTING FIN
	0 PERSIST TIMEOUT
		0 CONNECTION DROPPED BY PERSIST TIMEOUT
	0 KEEPALIVE TIMEOUT
		0 KEEPALIVE PROBE SENT
		0 CONNECTION DROPPED BY KEEPALIVE
	0 CORRECT ACK HEADER PREDICTION
	0 CORRECT DATA PACKET HEADER PREDICTION
	0 SACK RECOVERY EPISODE
	0 SEGMENT REXMIT IN SACK RECOVERY EPISODES
	0 BYTE REXMIT IN SACK RECOVERY EPISODES
	0 SACK OPTION (SACK BLOCKS) RECEIVED
	0 SACK OPTION (SACK BLOCKS) SENT
	0 SACK SCOREBOARD OVERFLOW
	0 LRO COALESCED PACKET
		0 TIME LRO FLOW TABLE WAS FULL
		0 COLLISION IN LRO FLOW TABLE
		0 TIME LRO COALESCED 2 PACKETS
		0 TIME LRO COALESCED 3 OR 4 PACKETS
		0 TIME LRO COALESCED 5 OR MORE PACKETS
	0 LIMITED TRANSMIT DONE
	0 EARLY RETRANSMIT DONE
	0 TIME CUMULATIVE ACK ADVANCED ALONG WITH SACK
	0 PROBE TIMEOUT
		0 TIME RETRANSMIT TIMEOUT TRIGGERED AFTER PROBE
		0 TIME PROBE PACKETS WERE SENT FOR AN INTERFACE
		0 TIME COULDN'T SEND PROBE PACKETS FOR AN INTERFACE
		0 TIME FAST RECOVERY AFTER TAIL LOSS
		0 TIME RECOVERED LAST PACKET 
		0 SACK BASED RESCUE RETRANSMIT
	0 CLIENT CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 CLIENT CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME GRACEFUL FALLBACK TO NON-ECN CONNECTION
		0 TIME LOST ECN NEGOTIATING SYN, FOLLOWED BY RETRANSMISSION
		0 SERVER CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 SERVER CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME LOST ECN NEGOTIATING SYN-ACK, FOLLOWED BY RETRANSMISSION
		0 TIME RECEIVED CONGESTION EXPERIENCED (CE) NOTIFICATION
		0 TIME CWR WAS SENT IN RESPONSE TO ECE
		0 TIME SENT ECE NOTIFICATION
		0 CONNECTION RECEIVED CE ATLEAST ONCE
		0 CONNECTION RECEIVED ECE ATLEAST ONCE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS BUT NO CE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS AND CE
		0 CONNECTION USING ECN RECEIVED CE BUT NO PACKET LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO SYN-LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO REORDERING
		0 CONNECTION FELL BACK TO NON-ECN DUE TO EXCESSIVE CE-MARKINGS
	0 TIME PACKET REORDERING WAS DETECTED ON A CONNECTION
		0 TIME TRANSMITTED PACKETS WERE REORDERED
		0 TIME FAST RECOVERY WAS DELAYED TO HANDLE REORDERING
		0 TIME RETRANSMISSION WAS AVOIDED BY DELAYING RECOVERY
		0 RETRANSMISSION NOT NEEDED 
	0 TIME DSACK OPTION WAS SENT
		0 TIME DSACK OPTION WAS RECEIVED
		0 TIME DSACK WAS DISABLED ON A CONNECTION
		0 TIME RECOVERED FROM BAD RETRANSMISSION USING DSACK
		0 TIME IGNORED DSACK DUE TO ACK LOSS
		0 TIME IGNORED OLD DSACK OPTIONS
	0 TIME PMTU BLACKHOLE DETECTION, SIZE REVERTED
	0 CONNECTION WERE DROPPED AFTER LONG SLEEP
	0 TIME A TFO-COOKIE HAS BEEN ANNOUNCED
	0 SYN WITH DATA AND A VALID TFO-COOKIE HAVE BEEN RECEIVED
	0 SYN WITH TFO-COOKIE-REQUEST RECEIVED
	0 TIME AN INVALID TFO-COOKIE HAS BEEN RECEIVED
	0 TIME WE REQUESTED A TFO-COOKIE
		0 TIME THE PEER ANNOUNCED A TFO-COOKIE
	0 TIME WE COMBINED SYN WITH DATA AND A TFO-COOKIE
		0 TIME OUR SYN WITH DATA HAS BEEN ACKNOWLEDGED
	0 TIME A CONNECTION-ATTEMPT WITH TFO FELL BACK TO REGULAR TCP
	0 TIME A TFO-CONNECTION BLACKHOLE'D
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO DEFAULT
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO MEDIUM
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO LOW
	0 TIMER DRIFT LESS OR EQUAL TO 1 MS
	0 TIMER DRIFT LESS OR EQUAL TO 10 MS
	0 TIMER DRIFT LESS OR EQUAL TO 20 MS
	0 TIMER DRIFT LESS OR EQUAL TO 50 MS
	0 TIMER DRIFT LESS OR EQUAL TO 100 MS
	0 TIMER DRIFT LESS OR EQUAL TO 200 MS
	0 TIMER DRIFT LESS OR EQUAL TO 500 MS
	0 TIMER DRIFT LESS OR EQUAL TO 1000 MS
	0 TIMER DRIFT GREATER THAN TO 1000 MS
UDP:
	537415 DATAGRAMS RECEIVED
		0 WITH INCOMPLETE HEADER
		0 WITH BAD DATA LENGTH FIELD
		0 WITH BAD CHECKSUM
		54 WITH NO CHECKSUM
		505678 CHECKSUMMED IN SOFTWARE
			254947 DATAGRAMS (80699906 BYTES) OVER IPV4
			250731 DATAGRAMS (110195064 BYTES) OVER IPV6
		5683 DROPPED DUE TO NO SOCKET
		3618 BROADCAST/MULTICAST DATAGRAMS UNDELIVERED
		0 TIME MULTICAST SOURCE FILTER MATCHED
		1 DROPPED DUE TO FULL SOCKET BUFFERS
		0 NOT FOR HASHED PCB
		528113 DELIVERED
	143558 DATAGRAMS OUTPUT
		150789 CHECKSUMMED IN SOFTWARE
			56252 DATAGRAMS (12017674 BYTES) OVER IPV4
			94537 DATAGRAMS (20851367 BYTES) OVER IPV6
ICMP:
	1398 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED 'CUZ OLD MESSAGE WAS ICMP
	OUTPUT HISTOGRAM:
		ECHO REPLY: 38
		DESTINATION UNREACHABLE: 1398
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	1 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	0 MULTICAST ECHO REQUESTS IGNORED
	0 MULTICAST TIMESTAMP REQUESTS IGNORED
	INPUT HISTOGRAM:
		ECHO REPLY: 6
		DESTINATION UNREACHABLE: 2007
		ECHO: 38
		ROUTER ADVERTISEMENT: 147
	38 MESSAGE RESPONSES GENERATED
	ICMP ADDRESS MASK RESPONSES ARE DISABLED
IGMP:
	1637 MESSAGES RECEIVED
	0 MESSAGE RECEIVED WITH TOO FEW BYTES
	0 MESSAGE RECEIVED WITH WRONG TTL
	0 MESSAGE RECEIVED WITH BAD CHECKSUM
	566 V1/V2 MEMBERSHIP QUERIES RECEIVED
	287 V3 MEMBERSHIP QUERIES RECEIVED
	0 MEMBERSHIP QUERIES RECEIVED WITH INVALID FIELD(S)
	835 GENERAL QUERIES RECEIVED
	18 GROUP QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES DROPPED
	784 MEMBERSHIP REPORTS RECEIVED
	0 MEMBERSHIP REPORT RECEIVED WITH INVALID FIELD(S)
	784 MEMBERSHIP REPORTS RECEIVED FOR GROUPS TO WHICH WE BELONG
	0 V3 REPORT RECEIVED WITHOUT ROUTER ALERT
	891 MEMBERSHIP REPORTS SENT
IPSEC:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
ARP:
	1625 BROADAST ARP REQUESTS SENT
	9 UNICAST ARP REQUESTS SENT
	3320 ARP REPLIES SENT
	0 ARP ANNOUNCEMENT SENT
	11630 ARP REQUESTS RECEIVED
	1373 ARP REPLIES RECEIVED
	13005 TOTAL ARP PACKETS RECEIVED
	0 ARP CONFLICT PROBE SENT
	0 INVALID ARP RESOLVE REQUEST
	0 TOTAL PACKET DROPPED DUE TO LACK OF MEMORY
	0 TOTAL PACKET HELD AWAITING ARP REPLY
	43 TOTAL PACKETS DROPPED DUE TO NO ARP ENTRY
	378 TOTAL PACKETS DROPPED DURING ARP ENTRY REMOVAL
	1488 ARP ENTRIES TIMED OUT
	0 DUPLICATE IP SEEN
MPTCP:
	0 DATA PACKET SENT
	0 DATA BYTE SENT
	0 DATA PACKET RECEIVED
	0 DATA BYTE RECEIVED
	0 PACKET WITH AN INVALID MPCAP OPTION
	0 PACKET WITH AN INVALID MPJOIN OPTION
	0 TIME PRIMARY SUBFLOW FELL BACK TO TCP
	0 TIME SECONDARY SUBFLOW FELL BACK TO TCP
	0 DSS OPTION DROP
	0 OTHER INVALID MPTCP OPTION
	0 TIME THE MPTCP SUBFLOW WINDOW WAS REDUCED
	0 BAD DSS CHECKSUM
	0 TIME RECEIVED OUT OF ORDER DATA 
	0 SUBFLOW SWITCH
	0 SUBFLOW SWITCH DUE TO ADVISORY
	0 SUBFLOW SWITCH DUE TO RTT
	0 SUBFLOW SWITCH DUE TO RTO
	0 SUBFLOW SWITCH DUE TO PEER
	0 NUMBER OF SUBFLOW PROBE
IP6:
	759085 TOTAL PACKETS RECEIVED
		0 WITH SIZE SMALLER THAN MINIMUM
		0 WITH DATA SIZE < DATA LENGTH
		0 WITH DATA SIZE > DATA LENGTH
			0 PACKET FORCED TO SOFTWARE CHECKSUM
		0 WITH BAD OPTIONS
		168 WITH INCORRECT VERSION NUMBER
		8 FRAGMENTS RECEIVED
			0 DROPPED (DUP OR OUT OF SPACE)
			0 DROPPED AFTER TIMEOUT
			0 EXCEEDED LIMIT
			4 REASSEMBLED OK
			0 ATOMIC FRAGMENTS RECEIVED
		684084 PACKETS FOR THIS HOST
		0 PACKET FORWARDED
		33722 PACKETS NOT FORWARDABLE
		0 REDIRECT SENT
		33665 MULTICAST PACKETS WHICH WE DON'T JOIN
		0 PACKET WHOSE HEADERS ARE NOT CONTINUOUS
		0 TUNNELING PACKET THAT CAN'T FIND GIF
		0 PACKET DISCARDED DUE TO TOO MAY HEADERS
		0 FORWARD CACHE HIT
		0 FORWARD CACHE MISS
		0 PACKET DROPPED DUE TO NO BUFS FOR CONTROL DATA
	343605 PACKETS SENT FROM THIS HOST
		0 PACKET SENT WITH FABRICATED IP HEADER
		0 OUTPUT PACKET DROPPED DUE TO NO BUFS, ETC.
		2291 OUTPUT PACKETS DISCARDED DUE TO NO ROUTE
		0 OUTPUT DATAGRAM FRAGMENTED
		0 FRAGMENT CREATED
		0 DATAGRAM THAT CAN'T BE FRAGMENTED
		0 PACKET THAT VIOLATED SCOPE RULES
		0 PACKET DROPPED DUE TO NECP POLICY
	INPUT HISTOGRAM:
		HOP BY HOP: 5738
		TCP: 423716
		UDP: 286525
		FRAGMENT: 8
		ICMP6: 41950
		PIM: 980
	MBUF STATISTICS:
		1787 ONE MBUF
		TWO OR MORE MBUF:
			LO0= 10571
			UTUN1= 12
		746715 ONE EXT MBUF
		0 TWO OR MORE EXT MBUF
		0 FAILURE OF SOURCE ADDRESS SELECTION
		SOURCE ADDRESSES ON AN OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES ON A NON-OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF SAME SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF A DIFFERENT SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		DEPRECATED SOURCE ADDRESSES
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESS SELECTION
			18460 RULES DEFAULT
			0 RULE PREFER SAME ADDRESS
			5075 RULES PREFER APPROPRIATE SCOPE
			0 RULE AVOID DEPRECATED ADDRESSES
			0 RULE PREFER HOME ADDRESSES
			0 RULE PREFER OUTGOING INTERFACE
			10 RULES PREFER MATCHING LABEL
			47351 RULES PREFER TEMPORARY ADDRESSES
			0 RULE PREFER ADDRESSES ON ALIVE INTERFACES
			0 RULE USE LONGEST MATCHING PREFIX
		0 DUPLICATE ADDRESS DETECTION COLLISION
		0 DUPLICATE ADDRESS DETECTION NS LOOP
		0 TIME IGNORED SOURCE ON SECONDARY EXPENSIVE I/F
ICMP6:
	1726 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED BECAUSE OLD MESSAGE WAS ICMP ERROR OR SO
	0 ERROR NOT GENERATED BECAUSE RATE LIMITATION
	OUTPUT HISTOGRAM:
		UNREACH: 1726
		MLDV1 LISTENER REPORT: 77
		MLDV1 LISTENER DONE: 11
		ROUTER SOLICITATION: 123
		NEIGHBOR SOLICITATION: 5239
		NEIGHBOR ADVERTISEMENT: 4406
		MLDV2 LISTENER REPORT: 1203
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	0 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	INPUT HISTOGRAM:
		UNREACH: 150
		MULTICAST LISTENER QUERY: 2095
		ROUTER ADVERTISEMENT: 30143
		NEIGHBOR SOLICITATION: 4406
		NEIGHBOR ADVERTISEMENT: 4386
	HISTOGRAM OF ERROR MESSAGES TO BE GENERATED:
		0 NO ROUTE
		0 ADMINISTRATIVELY PROHIBITED
		0 BEYOND SCOPE
		150 ADDRESS UNREACHABLE
		1576 PORT UNREACHABLE
		0 PACKET TOO BIG
		0 TIME EXCEED TRANSIT
		0 TIME EXCEED REASSEMBLY
		0 ERRONEOUS HEADER FIELD
		0 UNRECOGNIZED NEXT HEADER
		0 UNRECOGNIZED OPTION
		0 REDIRECT
		0 UNKNOWN
	0 MESSAGE RESPONSE GENERATED
	0 MESSAGE WITH TOO MANY ND OPTIONS
	0 MESSAGE WITH BAD ND OPTIONS
	0 BAD NEIGHBOR SOLICITATION MESSAGE
	0 BAD NEIGHBOR ADVERTISEMENT MESSAGE
	0 BAD ROUTER SOLICITATION MESSAGE
	0 BAD ROUTER ADVERTISEMENT MESSAGE
	0 BAD REDIRECT MESSAGE
	0 PATH MTU CHANGE
	0 DROPPED FRAGMENTED NDP MESSAGE
IPSEC6:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
RIP6:
	0 MESSAGE RECEIVED
	0 CHECKSUM CALCULATION ON INBOUND
	0 MESSAGE WITH BAD CHECKSUM
	0 MESSAGE DROPPED DUE TO NO SOCKET
	0 MULTICAST MESSAGE DROPPED DUE TO NO SOCKET
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	0 DELIVERED
	0 DATAGRAM OUTPUT
PFKEY:
	0 REQUEST SENT TO USERLAND
	0 BYTE SENT TO USERLAND
	0 MESSAGE WITH INVALID LENGTH FIELD
	0 MESSAGE WITH INVALID VERSION FIELD
	0 MESSAGE WITH INVALID MESSAGE TYPE FIELD
	0 MESSAGE TOO SHORT
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
	0 MESSAGE WITH DUPLICATE EXTENSION
	0 MESSAGE WITH INVALID EXTENSION TYPE
	0 MESSAGE WITH INVALID SA TYPE
	0 MESSAGE WITH INVALID ADDRESS EXTENSION
	0 REQUEST SENT FROM USERLAND
	0 BYTE SENT FROM USERLAND
	0 MESSAGE TOWARD SINGLE SOCKET
	0 MESSAGE TOWARD ALL SOCKETS
	0 MESSAGE TOWARD REGISTERED SOCKETS
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
KEVT:
	24 CURRENT KERNEL CONTROL SOCKETS
	18940 KERNEL CONTROL GENERATION COUNT
	0 BAD VENDOR FAILURE
	7352 MESSAGE TOO BIG FAILURES
	0 OUT OF MEMORY FAILURE
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	274149 MESSAGES POSTED
KCTL:
	0 TOTAL KERNEL CONTROL MODULE REGISTERED
	12 CURRENT KERNEL CONTROL MODULES REGISTERED
	55 CURRENT KERNEL CONTROL SOCKETS
	1117 KERNEL CONTROL GENERATION COUNT
	580 CONNECTION ATTEMPTS
	0 CONNECTION FAILURE
	35 SEND FAILURES
	0 SEND LIST FAILURE
	0 ENQUEUE FAILURE
	0 PACKET DROPPED DUE TO FULL SOCKET BUFFERS
XBKIDLE:
	1 MAX PER PROCESS
	600 MAXIMUM TIME (SECONDS)
	131072 HIGH WATER MARK
	0 SOCKET OPTION NOT SUPPORTED FAILURE
	0 TOO MANY SOCKETS FAILURE
	0 TOTAL SOCKET REQUESTED OK
	0 EXTENDED BK IDLE SOCKET
	0 NO CELLULAR FAILURE
	0 NO TIME FAILURES
	0 FORCED DEFUNCT SOCKET
	0 RESUMED SOCKET
	0 TIMEOUT EXPIRED FAILURE
	0 TIMER RESCHEDULED
	0 NO DELEGATED FAILURE
NET_API:
	2 INTERFACE FILTERS CURRENTLY ATTACHED
	2 INTERFACE FILTERS ATTACHED SINCE BOOT
	2 INTERFACE FILTERS ATTACHED SINCE BOOT BY OS
	0 IP FILTER CURRENTLY ATTACHED
	0 IP FILTER ATTACHED SINCE BOOT
	0 IP FILTER ATTACHED SINCE BOOT BY OS
	4 SOCKET FILTERS CURRENTLY ATTACHED
	4 SOCKET FILTERS ATTACHED SINCE BOOT
	4 SOCKET FILTERS ATTACHED SINCE BOOT BY OS
	326357 SOCKETS ALLOCATED SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL BY OS
	2472 SOCKETS WITH NECP CLIENT UUID SINCE BOOT
	104347 LOCAL DOMAIN SOCKETS ALLOCATED SINCE BOOT
	1199 ROUTE DOMAIN SOCKETS ALLOCATED SINCE BOOT
	124433 INET DOMAIN SOCKETS ALLOCATED SINCE BOOT
	59925 INET6 DOMAIN SOCKETS ALLOCATED SINCE BOOT
	10062 SYSTEM DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 MULTIPATH DOMAIN SOCKET ALLOCATED SINCE BOOT
	0 KEY DOMAIN SOCKET ALLOCATED SINCE BOOT
	5 NDRV DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 OTHER DOMAINS SOCKET ALLOCATED SINCE BOOT
	15558 IPV4 STREAM SOCKETS CREATED SINCE BOOT
	108875 IPV4 DATAGRAM SOCKETS CREATED SINCE BOOT
	10299 IPV4 DATAGRAM SOCKETS CONNECTED
	38118 IPV4 DNS SOCKETS
	102174 IPV4 DATAGRAM SOCKETS WITHOUT DATA
	7568 IPV6 STREAM SOCKETS CREATED SINCE BOOT
	52357 IPV6 DATAGRAM SOCKETS CREATED SINCE BOOT
	34887 IPV6 DATAGRAM SOCKETS CONNECTED
	0 IPV6 DNS SOCKET
	28278 IPV6 DATAGRAM SOCKETS WITHOUT DATA
	1115 SOCKET MULTICAST JOINS SINCE BOOT
	1115 SOCKET MULTICAST JOINS SINCE BOOT BY OS
	0 IPV4 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV4 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED
	12 INTERFACES ALLOCATED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED BY OS
	12 EXTENDED INTERFACES ALLOCATED SINCE BOOT BY OS
	2 PF ADDRULE OPERATIONS SINCE BOOT
	0 PF ADDRULE OPERATION SINCE BOOT BY OS
	0 VMNET START SINCE BOOT

raymond

/Users/raymond/a.txt

>>> ping_result
'3 packets transmitted, 3 packets received, 0.0% packet loss'
>>> 'packets' in ping_result
True
>>> 'pack' in ping_result
True
>>> ping_result = '3 packets transmitted, 0 packets received, 100.0% packet loss'
>>> '0.0%' in ping_result
True
>>> ping_result.split()
['3', 'packets', 'transmitted,', '0', 'packets', 'received,', '100.0%', 'packet', 'loss']
>>> '0.0%' in ping_result.split()
False
>>> '100.0%' in ping_result.split()
True
>>> 
>>> 
>>> connection_status = 'Status: connected'
>>> assert 'connected' in connection_status
>>> connection_status = 'Status: disconnected'
>>> assert 'connected' in connection_status
>>> assert 'connected' in connection_status.split()

Traceback (most recent call last):
  File "<pyshell#372>", line 1, in <module>
    assert 'connected' in connection_status.split()
AssertionError
>>> 
>>> 
>>> True and True
True
>>> False and True
False
>>> 0 and True
0
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======


    echo $USER   -->  ['echo', os.environ['USER']]
    echo ~/a.txt 
Learn to communicate with other programs

>>> print __doc__
Learn to communicate with other programs

    echo $USER   -->  ['echo', os.environ['USER']]
    echo ~/a.txt 


>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======


    echo $USER   -->  ['echo', os.environ['USER']]
    echo ~/a.txt 
Learn to communicate with other programs

    ECHO $USER   -->  ['ECHO', OS.ENVIRON['USER']]
    ECHO ~/A.TXT 

>>> err
''
>>> 
>>> # Mac and have homebrew:  brew install graphviz
>>> # graphviz.org  and pick download
>>> # brew update
>>> # brew install graphviz
>>> # port install graphviz
>>> # 2:40
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======

====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======

====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Generated by graphviz version 2.40.1 (20161225.0304)
 -->
<!-- Title: %3 Pages: 1 -->
<svg width="91pt" height="116pt"
 viewBox="0.00 0.00 91.09 116.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 112)">
<title>%3</title>
<polygon fill="#ffffff" stroke="transparent" points="-4,4 -4,-112 87.0852,-112 87.0852,4 -4,4"/>
<!-- raymond -->
<g id="node1" class="node">
<title>raymond</title>
<ellipse fill="none" stroke="#000000" cx="41.5426" cy="-90" rx="41.5852" ry="18"/>
<text text-anchor="middle" x="41.5426" y="-85.8" font-family="Times,serif" font-size="14.00" fill="#000000">raymond</text>
</g>
<!-- matthew -->
<g id="node2" class="node">
<title>matthew</title>
<ellipse fill="none" stroke="#000000" cx="41.5426" cy="-18" rx="40.6162" ry="18"/>
<text text-anchor="middle" x="41.5426" y="-13.8" font-family="Times,serif" font-size="14.00" fill="#000000">matthew</text>
</g>
<!-- raymond&#45;&gt;matthew -->
<g id="edge1" class="edge">
<title>raymond&#45;&gt;matthew</title>
<path fill="none" stroke="#000000" d="M41.5426,-71.8314C41.5426,-64.131 41.5426,-54.9743 41.5426,-46.4166"/>
<polygon fill="#000000" stroke="#000000" points="45.0427,-46.4132 41.5426,-36.4133 38.0427,-46.4133 45.0427,-46.4132"/>
</g>
</g>
</svg>

>>> 
Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 12:01:12) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Generated by graphviz version 2.40.1 (20161225.0304)
 -->
<!-- Title: %3 Pages: 1 -->
<svg width="91pt" height="116pt"
 viewBox="0.00 0.00 91.09 116.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 112)">
<title>%3</title>
<polygon fill="#ffffff" stroke="transparent" points="-4,4 -4,-112 87.0852,-112 87.0852,4 -4,4"/>
<!-- raymond -->
<g id="node1" class="node">
<title>raymond</title>
<ellipse fill="none" stroke="#000000" cx="41.5426" cy="-90" rx="41.5852" ry="18"/>
<text text-anchor="middle" x="41.5426" y="-85.8" font-family="Times,serif" font-size="14.00" fill="#000000">raymond</text>
</g>
<!-- matthew -->
<g id="node2" class="node">
<title>matthew</title>
<ellipse fill="none" stroke="#000000" cx="41.5426" cy="-18" rx="40.6162" ry="18"/>
<text text-anchor="middle" x="41.5426" y="-13.8" font-family="Times,serif" font-size="14.00" fill="#000000">matthew</text>
</g>
<!-- raymond&#45;&gt;matthew -->
<g id="edge1" class="edge">
<title>raymond&#45;&gt;matthew</title>
<path fill="none" stroke="#000000" d="M41.5426,-71.8314C41.5426,-64.131 41.5426,-54.9743 41.5426,-46.4166"/>
<polygon fill="#000000" stroke="#000000" points="45.0427,-46.4132 41.5426,-36.4133 38.0427,-46.4133 45.0427,-46.4132"/>
</g>
</g>
</svg>

>>> # sometimes when you install, existing sessions
>>> # don't about the new path.
>>> # so, restart the terminal session and python itself
>>> #    # python -m idlelib.idle
>>> svg_start = text.index('<svg')
>>> print text[svg_start:]
<svg width="91pt" height="116pt"
 viewBox="0.00 0.00 91.09 116.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 112)">
<title>%3</title>
<polygon fill="#ffffff" stroke="transparent" points="-4,4 -4,-112 87.0852,-112 87.0852,4 -4,4"/>
<!-- raymond -->
<g id="node1" class="node">
<title>raymond</title>
<ellipse fill="none" stroke="#000000" cx="41.5426" cy="-90" rx="41.5852" ry="18"/>
<text text-anchor="middle" x="41.5426" y="-85.8" font-family="Times,serif" font-size="14.00" fill="#000000">raymond</text>
</g>
<!-- matthew -->
<g id="node2" class="node">
<title>matthew</title>
<ellipse fill="none" stroke="#000000" cx="41.5426" cy="-18" rx="40.6162" ry="18"/>
<text text-anchor="middle" x="41.5426" y="-13.8" font-family="Times,serif" font-size="14.00" fill="#000000">matthew</text>
</g>
<!-- raymond&#45;&gt;matthew -->
<g id="edge1" class="edge">
<title>raymond&#45;&gt;matthew</title>
<path fill="none" stroke="#000000" d="M41.5426,-71.8314C41.5426,-64.131 41.5426,-54.9743 41.5426,-46.4166"/>
<polygon fill="#000000" stroke="#000000" points="45.0427,-46.4132 41.5426,-36.4133 38.0427,-46.4133 45.0427,-46.4132"/>
</g>
</g>
</svg>

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
<svg width="91pt" height="116pt"
 viewBox="0.00 0.00 91.09 116.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 112)">
<title>%3</title>
<polygon fill="#ffffff" stroke="transparent" points="-4,4 -4,-112 87.0852,-112 87.0852,4 -4,4"/>
<!-- raymond -->
<g id="node1" class="node">
<title>raymond</title>
<ellipse fill="none" stroke="#000000" cx="41.5426" cy="-90" rx="41.5852" ry="18"/>
<text text-anchor="middle" x="41.5426" y="-85.8" font-family="Times,serif" font-size="14.00" fill="#000000">raymond</text>
</g>
<!-- matthew -->
<g id="node2" class="node">
<title>matthew</title>
<ellipse fill="none" stroke="#000000" cx="41.5426" cy="-18" rx="40.6162" ry="18"/>
<text text-anchor="middle" x="41.5426" y="-13.8" font-family="Times,serif" font-size="14.00" fill="#000000">matthew</text>
</g>
<!-- raymond&#45;&gt;matthew -->
<g id="edge1" class="edge">
<title>raymond&#45;&gt;matthew</title>
<path fill="none" stroke="#000000" d="M41.5426,-71.8314C41.5426,-64.131 41.5426,-54.9743 41.5426,-46.4166"/>
<polygon fill="#000000" stroke="#000000" points="45.0427,-46.4132 41.5426,-36.4133 38.0427,-46.4133 45.0427,-46.4132"/>
</g>
</g>
</svg>

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
>>> print graphviz()
<svg width="91pt" height="116pt"
 viewBox="0.00 0.00 91.09 116.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 112)">
<title>%3</title>
<polygon fill="#ffffff" stroke="transparent" points="-4,4 -4,-112 87.0852,-112 87.0852,4 -4,4"/>
<!-- raymond -->
<g id="node1" class="node">
<title>raymond</title>
<ellipse fill="none" stroke="#000000" cx="41.5426" cy="-90" rx="41.5852" ry="18"/>
<text text-anchor="middle" x="41.5426" y="-85.8" font-family="Times,serif" font-size="14.00" fill="#000000">raymond</text>
</g>
<!-- matthew -->
<g id="node2" class="node">
<title>matthew</title>
<ellipse fill="none" stroke="#000000" cx="41.5426" cy="-18" rx="40.6162" ry="18"/>
<text text-anchor="middle" x="41.5426" y="-13.8" font-family="Times,serif" font-size="14.00" fill="#000000">matthew</text>
</g>
<!-- raymond&#45;&gt;matthew -->
<g id="edge1" class="edge">
<title>raymond&#45;&gt;matthew</title>
<path fill="none" stroke="#000000" d="M41.5426,-71.8314C41.5426,-64.131 41.5426,-54.9743 41.5426,-46.4166"/>
<polygon fill="#000000" stroke="#000000" points="45.0427,-46.4132 41.5426,-36.4133 38.0427,-46.4133 45.0427,-46.4132"/>
</g>
</g>
</svg>

None
>>> 
>>> 
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
>>> t, e = graphviz('digraph {mark;}')
>>> print t
<svg width="65pt" height="44pt"
 viewBox="0.00 0.00 64.55 44.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 40)">
<title>%3</title>
<polygon fill="#ffffff" stroke="transparent" points="-4,4 -4,-40 60.5548,-40 60.5548,4 -4,4"/>
<!-- mark -->
<g id="node1" class="node">
<title>mark</title>
<ellipse fill="none" stroke="#000000" cx="28.2774" cy="-18" rx="28.0565" ry="18"/>
<text text-anchor="middle" x="28.2774" y="-13.8" font-family="Times,serif" font-size="14.00" fill="#000000">mark</text>
</g>
</g>
</svg>

>>> e
''
>>> t, e = graphviz('diagraph {mark;}')

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    t, e = graphviz('diagraph {mark;}')
  File "/Users/raymond/Dropbox/Public/sj178/subprocess_demo.py", line 14, in graphviz
    svg_start = text.index('<svg')
ValueError: substring not found
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
>>> t, e = graphviz('diagraph {mark;}')
>>> t
''
>>> e
"Error: <stdin>: syntax error in line 1 near 'diagraph'\n"
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj178/subprocess_demo.py", line 31, in <module>
    print run_command('netstat -s').upper()
  File "/Users/raymond/Dropbox/Public/sj178/subprocess_demo.py", line 24, in run_command
    raise RuntimeError('Command failed')
RuntimeError: Command failed
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj178/subprocess_demo.py", line 31, in <module>
    print run_command('netstat -s').upper()
  File "/Users/raymond/Dropbox/Public/sj178/subprocess_demo.py", line 24, in run_command
    raise RuntimeError('Command failed')
RuntimeError: Command failed
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj178/subprocess_demo.py", line 31, in <module>
    print run_command('netstat -s').upper()
  File "/Users/raymond/Dropbox/Public/sj178/subprocess_demo.py", line 24, in run_command
    raise RuntimeError('Command failed')
RuntimeError: Command failed
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/subprocess_demo.py ======
TCP:
	0 PACKET SENT
		0 DATA PACKET (0 BYTE)
		0 DATA PACKET (0 BYTE) RETRANSMITTED
		0 RESEND INITIATED BY MTU DISCOVERY
		0 ACK-ONLY PACKET (0 DELAYED)
		0 URG ONLY PACKET
		0 WINDOW PROBE PACKET
		0 WINDOW UPDATE PACKET
		0 CONTROL PACKET
		0 DATA PACKET SENT AFTER FLOW CONTROL
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
	0 PACKET RECEIVED
		0 ACK (FOR 0 BYTE)
		0 DUPLICATE ACK
		0 ACK FOR UNSENT DATA
		0 PACKET (0 BYTE) RECEIVED IN-SEQUENCE
		0 COMPLETELY DUPLICATE PACKET (0 BYTE)
		0 OLD DUPLICATE PACKET
		0 RECEIVED PACKET DROPPED DUE TO LOW MEMORY
		0 PACKET WITH SOME DUP. DATA (0 BYTE DUPED)
		0 OUT-OF-ORDER PACKET (0 BYTE)
		0 PACKET (0 BYTE) OF DATA AFTER WINDOW
		0 WINDOW PROBE
		0 WINDOW UPDATE PACKET
		0 PACKET RECEIVED AFTER CLOSE
		0 BAD RESET
		0 DISCARDED FOR BAD CHECKSUM
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
		0 DISCARDED FOR BAD HEADER OFFSET FIELD
		0 DISCARDED BECAUSE PACKET TOO SHORT
	0 CONNECTION REQUEST
	0 CONNECTION ACCEPT
	0 BAD CONNECTION ATTEMPT
	0 LISTEN QUEUE OVERFLOW
	0 CONNECTION ESTABLISHED (INCLUDING ACCEPTS)
	0 CONNECTION CLOSED (INCLUDING 0 DROP)
		0 CONNECTION UPDATED CACHED RTT ON CLOSE
		0 CONNECTION UPDATED CACHED RTT VARIANCE ON CLOSE
		0 CONNECTION UPDATED CACHED SSTHRESH ON CLOSE
	0 EMBRYONIC CONNECTION DROPPED
	0 SEGMENT UPDATED RTT (OF 0 ATTEMPT)
	0 RETRANSMIT TIMEOUT
		0 CONNECTION DROPPED BY REXMIT TIMEOUT
		0 CONNECTION DROPPED AFTER RETRANSMITTING FIN
	0 PERSIST TIMEOUT
		0 CONNECTION DROPPED BY PERSIST TIMEOUT
	0 KEEPALIVE TIMEOUT
		0 KEEPALIVE PROBE SENT
		0 CONNECTION DROPPED BY KEEPALIVE
	0 CORRECT ACK HEADER PREDICTION
	0 CORRECT DATA PACKET HEADER PREDICTION
	0 SACK RECOVERY EPISODE
	0 SEGMENT REXMIT IN SACK RECOVERY EPISODES
	0 BYTE REXMIT IN SACK RECOVERY EPISODES
	0 SACK OPTION (SACK BLOCKS) RECEIVED
	0 SACK OPTION (SACK BLOCKS) SENT
	0 SACK SCOREBOARD OVERFLOW
	0 LRO COALESCED PACKET
		0 TIME LRO FLOW TABLE WAS FULL
		0 COLLISION IN LRO FLOW TABLE
		0 TIME LRO COALESCED 2 PACKETS
		0 TIME LRO COALESCED 3 OR 4 PACKETS
		0 TIME LRO COALESCED 5 OR MORE PACKETS
	0 LIMITED TRANSMIT DONE
	0 EARLY RETRANSMIT DONE
	0 TIME CUMULATIVE ACK ADVANCED ALONG WITH SACK
	0 PROBE TIMEOUT
		0 TIME RETRANSMIT TIMEOUT TRIGGERED AFTER PROBE
		0 TIME PROBE PACKETS WERE SENT FOR AN INTERFACE
		0 TIME COULDN'T SEND PROBE PACKETS FOR AN INTERFACE
		0 TIME FAST RECOVERY AFTER TAIL LOSS
		0 TIME RECOVERED LAST PACKET 
		0 SACK BASED RESCUE RETRANSMIT
	0 CLIENT CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 CLIENT CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME GRACEFUL FALLBACK TO NON-ECN CONNECTION
		0 TIME LOST ECN NEGOTIATING SYN, FOLLOWED BY RETRANSMISSION
		0 SERVER CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 SERVER CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME LOST ECN NEGOTIATING SYN-ACK, FOLLOWED BY RETRANSMISSION
		0 TIME RECEIVED CONGESTION EXPERIENCED (CE) NOTIFICATION
		0 TIME CWR WAS SENT IN RESPONSE TO ECE
		0 TIME SENT ECE NOTIFICATION
		0 CONNECTION RECEIVED CE ATLEAST ONCE
		0 CONNECTION RECEIVED ECE ATLEAST ONCE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS BUT NO CE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS AND CE
		0 CONNECTION USING ECN RECEIVED CE BUT NO PACKET LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO SYN-LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO REORDERING
		0 CONNECTION FELL BACK TO NON-ECN DUE TO EXCESSIVE CE-MARKINGS
	0 TIME PACKET REORDERING WAS DETECTED ON A CONNECTION
		0 TIME TRANSMITTED PACKETS WERE REORDERED
		0 TIME FAST RECOVERY WAS DELAYED TO HANDLE REORDERING
		0 TIME RETRANSMISSION WAS AVOIDED BY DELAYING RECOVERY
		0 RETRANSMISSION NOT NEEDED 
	0 TIME DSACK OPTION WAS SENT
		0 TIME DSACK OPTION WAS RECEIVED
		0 TIME DSACK WAS DISABLED ON A CONNECTION
		0 TIME RECOVERED FROM BAD RETRANSMISSION USING DSACK
		0 TIME IGNORED DSACK DUE TO ACK LOSS
		0 TIME IGNORED OLD DSACK OPTIONS
	0 TIME PMTU BLACKHOLE DETECTION, SIZE REVERTED
	0 CONNECTION WERE DROPPED AFTER LONG SLEEP
	0 TIME A TFO-COOKIE HAS BEEN ANNOUNCED
	0 SYN WITH DATA AND A VALID TFO-COOKIE HAVE BEEN RECEIVED
	0 SYN WITH TFO-COOKIE-REQUEST RECEIVED
	0 TIME AN INVALID TFO-COOKIE HAS BEEN RECEIVED
	0 TIME WE REQUESTED A TFO-COOKIE
		0 TIME THE PEER ANNOUNCED A TFO-COOKIE
	0 TIME WE COMBINED SYN WITH DATA AND A TFO-COOKIE
		0 TIME OUR SYN WITH DATA HAS BEEN ACKNOWLEDGED
	0 TIME A CONNECTION-ATTEMPT WITH TFO FELL BACK TO REGULAR TCP
	0 TIME A TFO-CONNECTION BLACKHOLE'D
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO DEFAULT
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO MEDIUM
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO LOW
	0 TIMER DRIFT LESS OR EQUAL TO 1 MS
	0 TIMER DRIFT LESS OR EQUAL TO 10 MS
	0 TIMER DRIFT LESS OR EQUAL TO 20 MS
	0 TIMER DRIFT LESS OR EQUAL TO 50 MS
	0 TIMER DRIFT LESS OR EQUAL TO 100 MS
	0 TIMER DRIFT LESS OR EQUAL TO 200 MS
	0 TIMER DRIFT LESS OR EQUAL TO 500 MS
	0 TIMER DRIFT LESS OR EQUAL TO 1000 MS
	0 TIMER DRIFT GREATER THAN TO 1000 MS
UDP:
	621722 DATAGRAMS RECEIVED
		0 WITH INCOMPLETE HEADER
		0 WITH BAD DATA LENGTH FIELD
		0 WITH BAD CHECKSUM
		54 WITH NO CHECKSUM
		588597 CHECKSUMMED IN SOFTWARE
			300857 DATAGRAMS (93253292 BYTES) OVER IPV4
			287740 DATAGRAMS (120899196 BYTES) OVER IPV6
		5693 DROPPED DUE TO NO SOCKET
		3618 BROADCAST/MULTICAST DATAGRAMS UNDELIVERED
		0 TIME MULTICAST SOURCE FILTER MATCHED
		1 DROPPED DUE TO FULL SOCKET BUFFERS
		0 NOT FOR HASHED PCB
		612410 DELIVERED
	147602 DATAGRAMS OUTPUT
		155410 CHECKSUMMED IN SOFTWARE
			58960 DATAGRAMS (12762103 BYTES) OVER IPV4
			96450 DATAGRAMS (21647354 BYTES) OVER IPV6
ICMP:
	1398 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED 'CUZ OLD MESSAGE WAS ICMP
	OUTPUT HISTOGRAM:
		ECHO REPLY: 38
		DESTINATION UNREACHABLE: 1398
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	1 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	0 MULTICAST ECHO REQUESTS IGNORED
	0 MULTICAST TIMESTAMP REQUESTS IGNORED
	INPUT HISTOGRAM:
		ECHO REPLY: 9
		DESTINATION UNREACHABLE: 2007
		ECHO: 38
		ROUTER ADVERTISEMENT: 147
	38 MESSAGE RESPONSES GENERATED
	ICMP ADDRESS MASK RESPONSES ARE DISABLED
IGMP:
	1639 MESSAGES RECEIVED
	0 MESSAGE RECEIVED WITH TOO FEW BYTES
	0 MESSAGE RECEIVED WITH WRONG TTL
	0 MESSAGE RECEIVED WITH BAD CHECKSUM
	568 V1/V2 MEMBERSHIP QUERIES RECEIVED
	287 V3 MEMBERSHIP QUERIES RECEIVED
	0 MEMBERSHIP QUERIES RECEIVED WITH INVALID FIELD(S)
	837 GENERAL QUERIES RECEIVED
	18 GROUP QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES DROPPED
	784 MEMBERSHIP REPORTS RECEIVED
	0 MEMBERSHIP REPORT RECEIVED WITH INVALID FIELD(S)
	784 MEMBERSHIP REPORTS RECEIVED FOR GROUPS TO WHICH WE BELONG
	0 V3 REPORT RECEIVED WITHOUT ROUTER ALERT
	893 MEMBERSHIP REPORTS SENT
IPSEC:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
ARP:
	1872 BROADAST ARP REQUESTS SENT
	9 UNICAST ARP REQUESTS SENT
	3324 ARP REPLIES SENT
	0 ARP ANNOUNCEMENT SENT
	11634 ARP REQUESTS RECEIVED
	1620 ARP REPLIES RECEIVED
	13256 TOTAL ARP PACKETS RECEIVED
	0 ARP CONFLICT PROBE SENT
	0 INVALID ARP RESOLVE REQUEST
	0 TOTAL PACKET DROPPED DUE TO LACK OF MEMORY
	0 TOTAL PACKET HELD AWAITING ARP REPLY
	43 TOTAL PACKETS DROPPED DUE TO NO ARP ENTRY
	378 TOTAL PACKETS DROPPED DURING ARP ENTRY REMOVAL
	1652 ARP ENTRIES TIMED OUT
	0 DUPLICATE IP SEEN
MPTCP:
	0 DATA PACKET SENT
	0 DATA BYTE SENT
	0 DATA PACKET RECEIVED
	0 DATA BYTE RECEIVED
	0 PACKET WITH AN INVALID MPCAP OPTION
	0 PACKET WITH AN INVALID MPJOIN OPTION
	0 TIME PRIMARY SUBFLOW FELL BACK TO TCP
	0 TIME SECONDARY SUBFLOW FELL BACK TO TCP
	0 DSS OPTION DROP
	0 OTHER INVALID MPTCP OPTION
	0 TIME THE MPTCP SUBFLOW WINDOW WAS REDUCED
	0 BAD DSS CHECKSUM
	0 TIME RECEIVED OUT OF ORDER DATA 
	0 SUBFLOW SWITCH
	0 SUBFLOW SWITCH DUE TO ADVISORY
	0 SUBFLOW SWITCH DUE TO RTT
	0 SUBFLOW SWITCH DUE TO RTO
	0 SUBFLOW SWITCH DUE TO PEER
	0 NUMBER OF SUBFLOW PROBE
IP6:
	808506 TOTAL PACKETS RECEIVED
		0 WITH SIZE SMALLER THAN MINIMUM
		0 WITH DATA SIZE < DATA LENGTH
		0 WITH DATA SIZE > DATA LENGTH
			0 PACKET FORCED TO SOFTWARE CHECKSUM
		0 WITH BAD OPTIONS
		168 WITH INCORRECT VERSION NUMBER
		8 FRAGMENTS RECEIVED
			0 DROPPED (DUP OR OUT OF SPACE)
			0 DROPPED AFTER TIMEOUT
			0 EXCEEDED LIMIT
			4 REASSEMBLED OK
			0 ATOMIC FRAGMENTS RECEIVED
		728564 PACKETS FOR THIS HOST
		0 PACKET FORWARDED
		37198 PACKETS NOT FORWARDABLE
		0 REDIRECT SENT
		37141 MULTICAST PACKETS WHICH WE DON'T JOIN
		0 PACKET WHOSE HEADERS ARE NOT CONTINUOUS
		0 TUNNELING PACKET THAT CAN'T FIND GIF
		0 PACKET DISCARDED DUE TO TOO MAY HEADERS
		0 FORWARD CACHE HIT
		0 FORWARD CACHE MISS
		0 PACKET DROPPED DUE TO NO BUFS FOR CONTROL DATA
	352392 PACKETS SENT FROM THIS HOST
		0 PACKET SENT WITH FABRICATED IP HEADER
		0 OUTPUT PACKET DROPPED DUE TO NO BUFS, ETC.
		2291 OUTPUT PACKETS DISCARDED DUE TO NO ROUTE
		0 OUTPUT DATAGRAM FRAGMENTED
		0 FRAGMENT CREATED
		0 DATAGRAM THAT CAN'T BE FRAGMENTED
		0 PACKET THAT VIOLATED SCOPE RULES
		0 PACKET DROPPED DUE TO NECP POLICY
	INPUT HISTOGRAM:
		HOP BY HOP: 6005
		TCP: 430610
		UDP: 327266
		FRAGMENT: 8
		ICMP6: 43255
		PIM: 1194
	MBUF STATISTICS:
		1787 ONE MBUF
		TWO OR MORE MBUF:
			LO0= 11148
			UTUN1= 12
		795559 ONE EXT MBUF
		0 TWO OR MORE EXT MBUF
		0 FAILURE OF SOURCE ADDRESS SELECTION
		SOURCE ADDRESSES ON AN OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES ON A NON-OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF SAME SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF A DIFFERENT SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		DEPRECATED SOURCE ADDRESSES
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESS SELECTION
			19258 RULES DEFAULT
			0 RULE PREFER SAME ADDRESS
			6005 RULES PREFER APPROPRIATE SCOPE
			0 RULE AVOID DEPRECATED ADDRESSES
			0 RULE PREFER HOME ADDRESSES
			0 RULE PREFER OUTGOING INTERFACE
			10 RULES PREFER MATCHING LABEL
			47351 RULES PREFER TEMPORARY ADDRESSES
			0 RULE PREFER ADDRESSES ON ALIVE INTERFACES
			0 RULE USE LONGEST MATCHING PREFIX
		0 DUPLICATE ADDRESS DETECTION COLLISION
		0 DUPLICATE ADDRESS DETECTION NS LOOP
		0 TIME IGNORED SOURCE ON SECONDARY EXPENSIVE I/F
ICMP6:
	1736 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED BECAUSE OLD MESSAGE WAS ICMP ERROR OR SO
	0 ERROR NOT GENERATED BECAUSE RATE LIMITATION
	OUTPUT HISTOGRAM:
		UNREACH: 1736
		MLDV1 LISTENER REPORT: 77
		MLDV1 LISTENER DONE: 11
		ROUTER SOLICITATION: 123
		NEIGHBOR SOLICITATION: 5384
		NEIGHBOR ADVERTISEMENT: 4416
		MLDV2 LISTENER REPORT: 1338
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	0 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	INPUT HISTOGRAM:
		UNREACH: 150
		MULTICAST LISTENER QUERY: 2255
		ROUTER ADVERTISEMENT: 31293
		NEIGHBOR SOLICITATION: 4416
		NEIGHBOR ADVERTISEMENT: 4531
	HISTOGRAM OF ERROR MESSAGES TO BE GENERATED:
		0 NO ROUTE
		0 ADMINISTRATIVELY PROHIBITED
		0 BEYOND SCOPE
		150 ADDRESS UNREACHABLE
		1586 PORT UNREACHABLE
		0 PACKET TOO BIG
		0 TIME EXCEED TRANSIT
		0 TIME EXCEED REASSEMBLY
		0 ERRONEOUS HEADER FIELD
		0 UNRECOGNIZED NEXT HEADER
		0 UNRECOGNIZED OPTION
		0 REDIRECT
		0 UNKNOWN
	0 MESSAGE RESPONSE GENERATED
	0 MESSAGE WITH TOO MANY ND OPTIONS
	0 MESSAGE WITH BAD ND OPTIONS
	0 BAD NEIGHBOR SOLICITATION MESSAGE
	0 BAD NEIGHBOR ADVERTISEMENT MESSAGE
	0 BAD ROUTER SOLICITATION MESSAGE
	0 BAD ROUTER ADVERTISEMENT MESSAGE
	0 BAD REDIRECT MESSAGE
	0 PATH MTU CHANGE
	0 DROPPED FRAGMENTED NDP MESSAGE
IPSEC6:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
RIP6:
	0 MESSAGE RECEIVED
	0 CHECKSUM CALCULATION ON INBOUND
	0 MESSAGE WITH BAD CHECKSUM
	0 MESSAGE DROPPED DUE TO NO SOCKET
	0 MULTICAST MESSAGE DROPPED DUE TO NO SOCKET
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	0 DELIVERED
	0 DATAGRAM OUTPUT
PFKEY:
	0 REQUEST SENT TO USERLAND
	0 BYTE SENT TO USERLAND
	0 MESSAGE WITH INVALID LENGTH FIELD
	0 MESSAGE WITH INVALID VERSION FIELD
	0 MESSAGE WITH INVALID MESSAGE TYPE FIELD
	0 MESSAGE TOO SHORT
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
	0 MESSAGE WITH DUPLICATE EXTENSION
	0 MESSAGE WITH INVALID EXTENSION TYPE
	0 MESSAGE WITH INVALID SA TYPE
	0 MESSAGE WITH INVALID ADDRESS EXTENSION
	0 REQUEST SENT FROM USERLAND
	0 BYTE SENT FROM USERLAND
	0 MESSAGE TOWARD SINGLE SOCKET
	0 MESSAGE TOWARD ALL SOCKETS
	0 MESSAGE TOWARD REGISTERED SOCKETS
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
KEVT:
	24 CURRENT KERNEL CONTROL SOCKETS
	19074 KERNEL CONTROL GENERATION COUNT
	0 BAD VENDOR FAILURE
	7447 MESSAGE TOO BIG FAILURES
	0 OUT OF MEMORY FAILURE
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	278703 MESSAGES POSTED
KCTL:
	0 TOTAL KERNEL CONTROL MODULE REGISTERED
	12 CURRENT KERNEL CONTROL MODULES REGISTERED
	55 CURRENT KERNEL CONTROL SOCKETS
	1119 KERNEL CONTROL GENERATION COUNT
	581 CONNECTION ATTEMPTS
	0 CONNECTION FAILURE
	35 SEND FAILURES
	0 SEND LIST FAILURE
	0 ENQUEUE FAILURE
	0 PACKET DROPPED DUE TO FULL SOCKET BUFFERS
XBKIDLE:
	1 MAX PER PROCESS
	600 MAXIMUM TIME (SECONDS)
	131072 HIGH WATER MARK
	0 SOCKET OPTION NOT SUPPORTED FAILURE
	0 TOO MANY SOCKETS FAILURE
	0 TOTAL SOCKET REQUESTED OK
	0 EXTENDED BK IDLE SOCKET
	0 NO CELLULAR FAILURE
	0 NO TIME FAILURES
	0 FORCED DEFUNCT SOCKET
	0 RESUMED SOCKET
	0 TIMEOUT EXPIRED FAILURE
	0 TIMER RESCHEDULED
	0 NO DELEGATED FAILURE
NET_API:
	2 INTERFACE FILTERS CURRENTLY ATTACHED
	2 INTERFACE FILTERS ATTACHED SINCE BOOT
	2 INTERFACE FILTERS ATTACHED SINCE BOOT BY OS
	0 IP FILTER CURRENTLY ATTACHED
	0 IP FILTER ATTACHED SINCE BOOT
	0 IP FILTER ATTACHED SINCE BOOT BY OS
	4 SOCKET FILTERS CURRENTLY ATTACHED
	4 SOCKET FILTERS ATTACHED SINCE BOOT
	4 SOCKET FILTERS ATTACHED SINCE BOOT BY OS
	328925 SOCKETS ALLOCATED SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL BY OS
	2493 SOCKETS WITH NECP CLIENT UUID SINCE BOOT
	105006 LOCAL DOMAIN SOCKETS ALLOCATED SINCE BOOT
	1199 ROUTE DOMAIN SOCKETS ALLOCATED SINCE BOOT
	124898 INET DOMAIN SOCKETS ALLOCATED SINCE BOOT
	60788 INET6 DOMAIN SOCKETS ALLOCATED SINCE BOOT
	10130 SYSTEM DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 MULTIPATH DOMAIN SOCKET ALLOCATED SINCE BOOT
	0 KEY DOMAIN SOCKET ALLOCATED SINCE BOOT
	5 NDRV DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 OTHER DOMAINS SOCKET ALLOCATED SINCE BOOT
	15625 IPV4 STREAM SOCKETS CREATED SINCE BOOT
	109273 IPV4 DATAGRAM SOCKETS CREATED SINCE BOOT
	10493 IPV4 DATAGRAM SOCKETS CONNECTED
	38717 IPV4 DNS SOCKETS
	102542 IPV4 DATAGRAM SOCKETS WITHOUT DATA
	7671 IPV6 STREAM SOCKETS CREATED SINCE BOOT
	53117 IPV6 DATAGRAM SOCKETS CREATED SINCE BOOT
	35524 IPV6 DATAGRAM SOCKETS CONNECTED
	0 IPV6 DNS SOCKET
	28708 IPV6 DATAGRAM SOCKETS WITHOUT DATA
	1115 SOCKET MULTICAST JOINS SINCE BOOT
	1115 SOCKET MULTICAST JOINS SINCE BOOT BY OS
	0 IPV4 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV4 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED
	12 INTERFACES ALLOCATED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED BY OS
	12 EXTENDED INTERFACES ALLOCATED SINCE BOOT BY OS
	2 PF ADDRULE OPERATIONS SINCE BOOT
	0 PF ADDRULE OPERATION SINCE BOOT BY OS
	0 VMNET START SINCE BOOT

TCP:
	0 PACKET SENT
		0 DATA PACKET (0 BYTE)
		0 DATA PACKET (0 BYTE) RETRANSMITTED
		0 RESEND INITIATED BY MTU DISCOVERY
		0 ACK-ONLY PACKET (0 DELAYED)
		0 URG ONLY PACKET
		0 WINDOW PROBE PACKET
		0 WINDOW UPDATE PACKET
		0 CONTROL PACKET
		0 DATA PACKET SENT AFTER FLOW CONTROL
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
	0 PACKET RECEIVED
		0 ACK (FOR 0 BYTE)
		0 DUPLICATE ACK
		0 ACK FOR UNSENT DATA
		0 PACKET (0 BYTE) RECEIVED IN-SEQUENCE
		0 COMPLETELY DUPLICATE PACKET (0 BYTE)
		0 OLD DUPLICATE PACKET
		0 RECEIVED PACKET DROPPED DUE TO LOW MEMORY
		0 PACKET WITH SOME DUP. DATA (0 BYTE DUPED)
		0 OUT-OF-ORDER PACKET (0 BYTE)
		0 PACKET (0 BYTE) OF DATA AFTER WINDOW
		0 WINDOW PROBE
		0 WINDOW UPDATE PACKET
		0 PACKET RECEIVED AFTER CLOSE
		0 BAD RESET
		0 DISCARDED FOR BAD CHECKSUM
		0 CHECKSUMMED IN SOFTWARE
			0 SEGMENT (0 BYTE) OVER IPV4
			0 SEGMENT (0 BYTE) OVER IPV6
		0 DISCARDED FOR BAD HEADER OFFSET FIELD
		0 DISCARDED BECAUSE PACKET TOO SHORT
	0 CONNECTION REQUEST
	0 CONNECTION ACCEPT
	0 BAD CONNECTION ATTEMPT
	0 LISTEN QUEUE OVERFLOW
	0 CONNECTION ESTABLISHED (INCLUDING ACCEPTS)
	0 CONNECTION CLOSED (INCLUDING 0 DROP)
		0 CONNECTION UPDATED CACHED RTT ON CLOSE
		0 CONNECTION UPDATED CACHED RTT VARIANCE ON CLOSE
		0 CONNECTION UPDATED CACHED SSTHRESH ON CLOSE
	0 EMBRYONIC CONNECTION DROPPED
	0 SEGMENT UPDATED RTT (OF 0 ATTEMPT)
	0 RETRANSMIT TIMEOUT
		0 CONNECTION DROPPED BY REXMIT TIMEOUT
		0 CONNECTION DROPPED AFTER RETRANSMITTING FIN
	0 PERSIST TIMEOUT
		0 CONNECTION DROPPED BY PERSIST TIMEOUT
	0 KEEPALIVE TIMEOUT
		0 KEEPALIVE PROBE SENT
		0 CONNECTION DROPPED BY KEEPALIVE
	0 CORRECT ACK HEADER PREDICTION
	0 CORRECT DATA PACKET HEADER PREDICTION
	0 SACK RECOVERY EPISODE
	0 SEGMENT REXMIT IN SACK RECOVERY EPISODES
	0 BYTE REXMIT IN SACK RECOVERY EPISODES
	0 SACK OPTION (SACK BLOCKS) RECEIVED
	0 SACK OPTION (SACK BLOCKS) SENT
	0 SACK SCOREBOARD OVERFLOW
	0 LRO COALESCED PACKET
		0 TIME LRO FLOW TABLE WAS FULL
		0 COLLISION IN LRO FLOW TABLE
		0 TIME LRO COALESCED 2 PACKETS
		0 TIME LRO COALESCED 3 OR 4 PACKETS
		0 TIME LRO COALESCED 5 OR MORE PACKETS
	0 LIMITED TRANSMIT DONE
	0 EARLY RETRANSMIT DONE
	0 TIME CUMULATIVE ACK ADVANCED ALONG WITH SACK
	0 PROBE TIMEOUT
		0 TIME RETRANSMIT TIMEOUT TRIGGERED AFTER PROBE
		0 TIME PROBE PACKETS WERE SENT FOR AN INTERFACE
		0 TIME COULDN'T SEND PROBE PACKETS FOR AN INTERFACE
		0 TIME FAST RECOVERY AFTER TAIL LOSS
		0 TIME RECOVERED LAST PACKET 
		0 SACK BASED RESCUE RETRANSMIT
	0 CLIENT CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 CLIENT CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME GRACEFUL FALLBACK TO NON-ECN CONNECTION
		0 TIME LOST ECN NEGOTIATING SYN, FOLLOWED BY RETRANSMISSION
		0 SERVER CONNECTION ATTEMPTED TO NEGOTIATE ECN
		0 SERVER CONNECTION SUCCESSFULLY NEGOTIATED ECN
		0 TIME LOST ECN NEGOTIATING SYN-ACK, FOLLOWED BY RETRANSMISSION
		0 TIME RECEIVED CONGESTION EXPERIENCED (CE) NOTIFICATION
		0 TIME CWR WAS SENT IN RESPONSE TO ECE
		0 TIME SENT ECE NOTIFICATION
		0 CONNECTION RECEIVED CE ATLEAST ONCE
		0 CONNECTION RECEIVED ECE ATLEAST ONCE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS BUT NO CE
		0 CONNECTION USING ECN HAVE SEEN PACKET LOSS AND CE
		0 CONNECTION USING ECN RECEIVED CE BUT NO PACKET LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO SYN-LOSS
		0 CONNECTION FELL BACK TO NON-ECN DUE TO REORDERING
		0 CONNECTION FELL BACK TO NON-ECN DUE TO EXCESSIVE CE-MARKINGS
	0 TIME PACKET REORDERING WAS DETECTED ON A CONNECTION
		0 TIME TRANSMITTED PACKETS WERE REORDERED
		0 TIME FAST RECOVERY WAS DELAYED TO HANDLE REORDERING
		0 TIME RETRANSMISSION WAS AVOIDED BY DELAYING RECOVERY
		0 RETRANSMISSION NOT NEEDED 
	0 TIME DSACK OPTION WAS SENT
		0 TIME DSACK OPTION WAS RECEIVED
		0 TIME DSACK WAS DISABLED ON A CONNECTION
		0 TIME RECOVERED FROM BAD RETRANSMISSION USING DSACK
		0 TIME IGNORED DSACK DUE TO ACK LOSS
		0 TIME IGNORED OLD DSACK OPTIONS
	0 TIME PMTU BLACKHOLE DETECTION, SIZE REVERTED
	0 CONNECTION WERE DROPPED AFTER LONG SLEEP
	0 TIME A TFO-COOKIE HAS BEEN ANNOUNCED
	0 SYN WITH DATA AND A VALID TFO-COOKIE HAVE BEEN RECEIVED
	0 SYN WITH TFO-COOKIE-REQUEST RECEIVED
	0 TIME AN INVALID TFO-COOKIE HAS BEEN RECEIVED
	0 TIME WE REQUESTED A TFO-COOKIE
		0 TIME THE PEER ANNOUNCED A TFO-COOKIE
	0 TIME WE COMBINED SYN WITH DATA AND A TFO-COOKIE
		0 TIME OUR SYN WITH DATA HAS BEEN ACKNOWLEDGED
	0 TIME A CONNECTION-ATTEMPT WITH TFO FELL BACK TO REGULAR TCP
	0 TIME A TFO-CONNECTION BLACKHOLE'D
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO DEFAULT
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO MEDIUM
	0 TIME MAXIMUM SEGMENT SIZE WAS CHANGED TO LOW
	0 TIMER DRIFT LESS OR EQUAL TO 1 MS
	0 TIMER DRIFT LESS OR EQUAL TO 10 MS
	0 TIMER DRIFT LESS OR EQUAL TO 20 MS
	0 TIMER DRIFT LESS OR EQUAL TO 50 MS
	0 TIMER DRIFT LESS OR EQUAL TO 100 MS
	0 TIMER DRIFT LESS OR EQUAL TO 200 MS
	0 TIMER DRIFT LESS OR EQUAL TO 500 MS
	0 TIMER DRIFT LESS OR EQUAL TO 1000 MS
	0 TIMER DRIFT GREATER THAN TO 1000 MS
UDP:
	621748 DATAGRAMS RECEIVED
		0 WITH INCOMPLETE HEADER
		0 WITH BAD DATA LENGTH FIELD
		0 WITH BAD CHECKSUM
		54 WITH NO CHECKSUM
		588623 CHECKSUMMED IN SOFTWARE
			300869 DATAGRAMS (93255942 BYTES) OVER IPV4
			287754 DATAGRAMS (120902267 BYTES) OVER IPV6
		5693 DROPPED DUE TO NO SOCKET
		3618 BROADCAST/MULTICAST DATAGRAMS UNDELIVERED
		0 TIME MULTICAST SOURCE FILTER MATCHED
		1 DROPPED DUE TO FULL SOCKET BUFFERS
		0 NOT FOR HASHED PCB
		612436 DELIVERED
	147602 DATAGRAMS OUTPUT
		155410 CHECKSUMMED IN SOFTWARE
			58960 DATAGRAMS (12762103 BYTES) OVER IPV4
			96450 DATAGRAMS (21647354 BYTES) OVER IPV6
ICMP:
	1398 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED 'CUZ OLD MESSAGE WAS ICMP
	OUTPUT HISTOGRAM:
		ECHO REPLY: 38
		DESTINATION UNREACHABLE: 1398
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	1 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	0 MULTICAST ECHO REQUESTS IGNORED
	0 MULTICAST TIMESTAMP REQUESTS IGNORED
	INPUT HISTOGRAM:
		ECHO REPLY: 9
		DESTINATION UNREACHABLE: 2007
		ECHO: 38
		ROUTER ADVERTISEMENT: 147
	38 MESSAGE RESPONSES GENERATED
	ICMP ADDRESS MASK RESPONSES ARE DISABLED
IGMP:
	1639 MESSAGES RECEIVED
	0 MESSAGE RECEIVED WITH TOO FEW BYTES
	0 MESSAGE RECEIVED WITH WRONG TTL
	0 MESSAGE RECEIVED WITH BAD CHECKSUM
	568 V1/V2 MEMBERSHIP QUERIES RECEIVED
	287 V3 MEMBERSHIP QUERIES RECEIVED
	0 MEMBERSHIP QUERIES RECEIVED WITH INVALID FIELD(S)
	837 GENERAL QUERIES RECEIVED
	18 GROUP QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES RECEIVED
	0 GROUP-SOURCE QUERIES DROPPED
	784 MEMBERSHIP REPORTS RECEIVED
	0 MEMBERSHIP REPORT RECEIVED WITH INVALID FIELD(S)
	784 MEMBERSHIP REPORTS RECEIVED FOR GROUPS TO WHICH WE BELONG
	0 V3 REPORT RECEIVED WITHOUT ROUTER ALERT
	893 MEMBERSHIP REPORTS SENT
IPSEC:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
ARP:
	1872 BROADAST ARP REQUESTS SENT
	9 UNICAST ARP REQUESTS SENT
	3324 ARP REPLIES SENT
	0 ARP ANNOUNCEMENT SENT
	11634 ARP REQUESTS RECEIVED
	1620 ARP REPLIES RECEIVED
	13256 TOTAL ARP PACKETS RECEIVED
	0 ARP CONFLICT PROBE SENT
	0 INVALID ARP RESOLVE REQUEST
	0 TOTAL PACKET DROPPED DUE TO LACK OF MEMORY
	0 TOTAL PACKET HELD AWAITING ARP REPLY
	43 TOTAL PACKETS DROPPED DUE TO NO ARP ENTRY
	378 TOTAL PACKETS DROPPED DURING ARP ENTRY REMOVAL
	1652 ARP ENTRIES TIMED OUT
	0 DUPLICATE IP SEEN
MPTCP:
	0 DATA PACKET SENT
	0 DATA BYTE SENT
	0 DATA PACKET RECEIVED
	0 DATA BYTE RECEIVED
	0 PACKET WITH AN INVALID MPCAP OPTION
	0 PACKET WITH AN INVALID MPJOIN OPTION
	0 TIME PRIMARY SUBFLOW FELL BACK TO TCP
	0 TIME SECONDARY SUBFLOW FELL BACK TO TCP
	0 DSS OPTION DROP
	0 OTHER INVALID MPTCP OPTION
	0 TIME THE MPTCP SUBFLOW WINDOW WAS REDUCED
	0 BAD DSS CHECKSUM
	0 TIME RECEIVED OUT OF ORDER DATA 
	0 SUBFLOW SWITCH
	0 SUBFLOW SWITCH DUE TO ADVISORY
	0 SUBFLOW SWITCH DUE TO RTT
	0 SUBFLOW SWITCH DUE TO RTO
	0 SUBFLOW SWITCH DUE TO PEER
	0 NUMBER OF SUBFLOW PROBE
IP6:
	808522 TOTAL PACKETS RECEIVED
		0 WITH SIZE SMALLER THAN MINIMUM
		0 WITH DATA SIZE < DATA LENGTH
		0 WITH DATA SIZE > DATA LENGTH
			0 PACKET FORCED TO SOFTWARE CHECKSUM
		0 WITH BAD OPTIONS
		168 WITH INCORRECT VERSION NUMBER
		8 FRAGMENTS RECEIVED
			0 DROPPED (DUP OR OUT OF SPACE)
			0 DROPPED AFTER TIMEOUT
			0 EXCEEDED LIMIT
			4 REASSEMBLED OK
			0 ATOMIC FRAGMENTS RECEIVED
		728578 PACKETS FOR THIS HOST
		0 PACKET FORWARDED
		37198 PACKETS NOT FORWARDABLE
		0 REDIRECT SENT
		37141 MULTICAST PACKETS WHICH WE DON'T JOIN
		0 PACKET WHOSE HEADERS ARE NOT CONTINUOUS
		0 TUNNELING PACKET THAT CAN'T FIND GIF
		0 PACKET DISCARDED DUE TO TOO MAY HEADERS
		0 FORWARD CACHE HIT
		0 FORWARD CACHE MISS
		0 PACKET DROPPED DUE TO NO BUFS FOR CONTROL DATA
	352392 PACKETS SENT FROM THIS HOST
		0 PACKET SENT WITH FABRICATED IP HEADER
		0 OUTPUT PACKET DROPPED DUE TO NO BUFS, ETC.
		2291 OUTPUT PACKETS DISCARDED DUE TO NO ROUTE
		0 OUTPUT DATAGRAM FRAGMENTED
		0 FRAGMENT CREATED
		0 DATAGRAM THAT CAN'T BE FRAGMENTED
		0 PACKET THAT VIOLATED SCOPE RULES
		0 PACKET DROPPED DUE TO NECP POLICY
	INPUT HISTOGRAM:
		HOP BY HOP: 6005
		TCP: 430610
		UDP: 327280
		FRAGMENT: 8
		ICMP6: 43257
		PIM: 1194
	MBUF STATISTICS:
		1787 ONE MBUF
		TWO OR MORE MBUF:
			LO0= 11148
			UTUN1= 12
		795575 ONE EXT MBUF
		0 TWO OR MORE EXT MBUF
		0 FAILURE OF SOURCE ADDRESS SELECTION
		SOURCE ADDRESSES ON AN OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES ON A NON-OUTGOING I/F
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF SAME SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESSES OF A DIFFERENT SCOPE
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		DEPRECATED SOURCE ADDRESSES
			0 ADDRESSES SCOPE=0
			0 NODE-LOCAL
			0 LINK-LOCAL
			0 ADDRESSES SCOPE=3
			0 ADDRESSES SCOPE=4
			0 SITE-LOCAL
			0 ADDRESSES SCOPE=6
			0 ADDRESSES SCOPE=7
			0 ADDRESSES SCOPE=8
			0 ADDRESSES SCOPE=9
			0 ADDRESSES SCOPE=A
			0 ADDRESSES SCOPE=B
			0 ADDRESSES SCOPE=C
			0 ADDRESSES SCOPE=D
			0 GLOBAL
			0 ADDRESSES SCOPE=F
		SOURCE ADDRESS SELECTION
			19258 RULES DEFAULT
			0 RULE PREFER SAME ADDRESS
			6005 RULES PREFER APPROPRIATE SCOPE
			0 RULE AVOID DEPRECATED ADDRESSES
			0 RULE PREFER HOME ADDRESSES
			0 RULE PREFER OUTGOING INTERFACE
			10 RULES PREFER MATCHING LABEL
			47351 RULES PREFER TEMPORARY ADDRESSES
			0 RULE PREFER ADDRESSES ON ALIVE INTERFACES
			0 RULE USE LONGEST MATCHING PREFIX
		0 DUPLICATE ADDRESS DETECTION COLLISION
		0 DUPLICATE ADDRESS DETECTION NS LOOP
		0 TIME IGNORED SOURCE ON SECONDARY EXPENSIVE I/F
ICMP6:
	1736 CALLS TO ICMP_ERROR
	0 ERROR NOT GENERATED BECAUSE OLD MESSAGE WAS ICMP ERROR OR SO
	0 ERROR NOT GENERATED BECAUSE RATE LIMITATION
	OUTPUT HISTOGRAM:
		UNREACH: 1736
		MLDV1 LISTENER REPORT: 77
		MLDV1 LISTENER DONE: 11
		ROUTER SOLICITATION: 123
		NEIGHBOR SOLICITATION: 5384
		NEIGHBOR ADVERTISEMENT: 4416
		MLDV2 LISTENER REPORT: 1338
	0 MESSAGE WITH BAD CODE FIELDS
	0 MESSAGE < MINIMUM LENGTH
	0 BAD CHECKSUM
	0 MESSAGE WITH BAD LENGTH
	INPUT HISTOGRAM:
		UNREACH: 150
		MULTICAST LISTENER QUERY: 2255
		ROUTER ADVERTISEMENT: 31295
		NEIGHBOR SOLICITATION: 4416
		NEIGHBOR ADVERTISEMENT: 4531
	HISTOGRAM OF ERROR MESSAGES TO BE GENERATED:
		0 NO ROUTE
		0 ADMINISTRATIVELY PROHIBITED
		0 BEYOND SCOPE
		150 ADDRESS UNREACHABLE
		1586 PORT UNREACHABLE
		0 PACKET TOO BIG
		0 TIME EXCEED TRANSIT
		0 TIME EXCEED REASSEMBLY
		0 ERRONEOUS HEADER FIELD
		0 UNRECOGNIZED NEXT HEADER
		0 UNRECOGNIZED OPTION
		0 REDIRECT
		0 UNKNOWN
	0 MESSAGE RESPONSE GENERATED
	0 MESSAGE WITH TOO MANY ND OPTIONS
	0 MESSAGE WITH BAD ND OPTIONS
	0 BAD NEIGHBOR SOLICITATION MESSAGE
	0 BAD NEIGHBOR ADVERTISEMENT MESSAGE
	0 BAD ROUTER SOLICITATION MESSAGE
	0 BAD ROUTER ADVERTISEMENT MESSAGE
	0 BAD REDIRECT MESSAGE
	0 PATH MTU CHANGE
	0 DROPPED FRAGMENTED NDP MESSAGE
IPSEC6:
	0 INBOUND PACKET PROCESSED SUCCESSFULLY
	0 INBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 INBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID INBOUND PACKET
	0 INBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 INBOUND PACKET FAILED GETTING SPI
	0 INBOUND PACKET FAILED ON AH REPLAY CHECK
	0 INBOUND PACKET FAILED ON ESP REPLAY CHECK
	0 INBOUND PACKET CONSIDERED AUTHENTIC
	0 INBOUND PACKET FAILED ON AUTHENTICATION
	0 OUTBOUND PACKET PROCESSED SUCCESSFULLY
	0 OUTBOUND PACKET VIOLATED PROCESS SECURITY POLICY
	0 OUTBOUND PACKET WITH NO SA AVAILABLE
	0 INVALID OUTBOUND PACKET
	0 OUTBOUND PACKET FAILED DUE TO INSUFFICIENT MEMORY
	0 OUTBOUND PACKET WITH NO ROUTE
RIP6:
	0 MESSAGE RECEIVED
	0 CHECKSUM CALCULATION ON INBOUND
	0 MESSAGE WITH BAD CHECKSUM
	0 MESSAGE DROPPED DUE TO NO SOCKET
	0 MULTICAST MESSAGE DROPPED DUE TO NO SOCKET
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	0 DELIVERED
	0 DATAGRAM OUTPUT
PFKEY:
	0 REQUEST SENT TO USERLAND
	0 BYTE SENT TO USERLAND
	0 MESSAGE WITH INVALID LENGTH FIELD
	0 MESSAGE WITH INVALID VERSION FIELD
	0 MESSAGE WITH INVALID MESSAGE TYPE FIELD
	0 MESSAGE TOO SHORT
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
	0 MESSAGE WITH DUPLICATE EXTENSION
	0 MESSAGE WITH INVALID EXTENSION TYPE
	0 MESSAGE WITH INVALID SA TYPE
	0 MESSAGE WITH INVALID ADDRESS EXTENSION
	0 REQUEST SENT FROM USERLAND
	0 BYTE SENT FROM USERLAND
	0 MESSAGE TOWARD SINGLE SOCKET
	0 MESSAGE TOWARD ALL SOCKETS
	0 MESSAGE TOWARD REGISTERED SOCKETS
	0 MESSAGE WITH MEMORY ALLOCATION FAILURE
KEVT:
	24 CURRENT KERNEL CONTROL SOCKETS
	19074 KERNEL CONTROL GENERATION COUNT
	0 BAD VENDOR FAILURE
	7447 MESSAGE TOO BIG FAILURES
	0 OUT OF MEMORY FAILURE
	0 MESSAGE DROPPED DUE TO FULL SOCKET BUFFERS
	278707 MESSAGES POSTED
KCTL:
	0 TOTAL KERNEL CONTROL MODULE REGISTERED
	12 CURRENT KERNEL CONTROL MODULES REGISTERED
	55 CURRENT KERNEL CONTROL SOCKETS
	1119 KERNEL CONTROL GENERATION COUNT
	581 CONNECTION ATTEMPTS
	0 CONNECTION FAILURE
	35 SEND FAILURES
	0 SEND LIST FAILURE
	0 ENQUEUE FAILURE
	0 PACKET DROPPED DUE TO FULL SOCKET BUFFERS
XBKIDLE:
	1 MAX PER PROCESS
	600 MAXIMUM TIME (SECONDS)
	131072 HIGH WATER MARK
	0 SOCKET OPTION NOT SUPPORTED FAILURE
	0 TOO MANY SOCKETS FAILURE
	0 TOTAL SOCKET REQUESTED OK
	0 EXTENDED BK IDLE SOCKET
	0 NO CELLULAR FAILURE
	0 NO TIME FAILURES
	0 FORCED DEFUNCT SOCKET
	0 RESUMED SOCKET
	0 TIMEOUT EXPIRED FAILURE
	0 TIMER RESCHEDULED
	0 NO DELEGATED FAILURE
NET_API:
	2 INTERFACE FILTERS CURRENTLY ATTACHED
	2 INTERFACE FILTERS ATTACHED SINCE BOOT
	2 INTERFACE FILTERS ATTACHED SINCE BOOT BY OS
	0 IP FILTER CURRENTLY ATTACHED
	0 IP FILTER ATTACHED SINCE BOOT
	0 IP FILTER ATTACHED SINCE BOOT BY OS
	4 SOCKET FILTERS CURRENTLY ATTACHED
	4 SOCKET FILTERS ATTACHED SINCE BOOT
	4 SOCKET FILTERS ATTACHED SINCE BOOT BY OS
	328925 SOCKETS ALLOCATED SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL SINCE BOOT
	75 SOCKETS ALLOCATED IN-KERNEL BY OS
	2493 SOCKETS WITH NECP CLIENT UUID SINCE BOOT
	105006 LOCAL DOMAIN SOCKETS ALLOCATED SINCE BOOT
	1199 ROUTE DOMAIN SOCKETS ALLOCATED SINCE BOOT
	124898 INET DOMAIN SOCKETS ALLOCATED SINCE BOOT
	60788 INET6 DOMAIN SOCKETS ALLOCATED SINCE BOOT
	10130 SYSTEM DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 MULTIPATH DOMAIN SOCKET ALLOCATED SINCE BOOT
	0 KEY DOMAIN SOCKET ALLOCATED SINCE BOOT
	5 NDRV DOMAIN SOCKETS ALLOCATED SINCE BOOT
	0 OTHER DOMAINS SOCKET ALLOCATED SINCE BOOT
	15625 IPV4 STREAM SOCKETS CREATED SINCE BOOT
	109273 IPV4 DATAGRAM SOCKETS CREATED SINCE BOOT
	10493 IPV4 DATAGRAM SOCKETS CONNECTED
	38717 IPV4 DNS SOCKETS
	102542 IPV4 DATAGRAM SOCKETS WITHOUT DATA
	7671 IPV6 STREAM SOCKETS CREATED SINCE BOOT
	53117 IPV6 DATAGRAM SOCKETS CREATED SINCE BOOT
	35524 IPV6 DATAGRAM SOCKETS CONNECTED
	0 IPV6 DNS SOCKET
	28708 IPV6 DATAGRAM SOCKETS WITHOUT DATA
	1115 SOCKET MULTICAST JOINS SINCE BOOT
	1115 SOCKET MULTICAST JOINS SINCE BOOT BY OS
	0 IPV4 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV4 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 STREAM NEXUS FLOW ADDED SINCE BOOT
	0 IPV6 DATAGRAM NEXUS FLOW ADDED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED
	12 INTERFACES ALLOCATED SINCE BOOT
	12 INTERFACES CURRENTLY ALLOCATED BY OS
	12 EXTENDED INTERFACES ALLOCATED SINCE BOOT BY OS
	2 PF ADDRULE OPERATIONS SINCE BOOT
	0 PF ADDRULE OPERATION SINCE BOOT BY OS
	0 VMNET START SINCE BOOT

raymond

/Users/raymond/a.txt



    echo $USER   -->  ['echo', os.environ['USER']]
    echo ~/a.txt 
Learn to communicate with other programs

    ECHO $USER   -->  ['ECHO', OS.ENVIRON['USER']]
    ECHO ~/A.TXT 

('<svg width="91pt" height="116pt"\n viewBox="0.00 0.00 91.09 116.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 112)">\n<title>%3</title>\n<polygon fill="#ffffff" stroke="transparent" points="-4,4 -4,-112 87.0852,-112 87.0852,4 -4,4"/>\n<!-- raymond -->\n<g id="node1" class="node">\n<title>raymond</title>\n<ellipse fill="none" stroke="#000000" cx="41.5426" cy="-90" rx="41.5852" ry="18"/>\n<text text-anchor="middle" x="41.5426" y="-85.8" font-family="Times,serif" font-size="14.00" fill="#000000">raymond</text>\n</g>\n<!-- matthew -->\n<g id="node2" class="node">\n<title>matthew</title>\n<ellipse fill="none" stroke="#000000" cx="41.5426" cy="-18" rx="40.6162" ry="18"/>\n<text text-anchor="middle" x="41.5426" y="-13.8" font-family="Times,serif" font-size="14.00" fill="#000000">matthew</text>\n</g>\n<!-- raymond&#45;&gt;matthew -->\n<g id="edge1" class="edge">\n<title>raymond&#45;&gt;matthew</title>\n<path fill="none" stroke="#000000" d="M41.5426,-71.8314C41.5426,-64.131 41.5426,-54.9743 41.5426,-46.4166"/>\n<polygon fill="#000000" stroke="#000000" points="45.0427,-46.4132 41.5426,-36.4133 38.0427,-46.4133 45.0427,-46.4132"/>\n</g>\n</g>\n</svg>\n', '')
>>> s = check_output(['python', 'hello.py'])
>>> s
'Hello World\n'
>>> import hello
Hello World
>>> 
>>> # Graphviz is written in C as standalone application that knows NOTHING about Python.
>>> # There are probably pythongraphviz packages:  they have python functions that call graphviz.exe underneath
>>> 
>>> 
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
>>> from notes2.bottle import template, view
>>> print template('The answer is {{ answer }} today', answer=10)
The answer is 10 today
>>> print template('The answer is {{ answer }} today and its square is {{ answer ** 2 }}', answer=10)
The answer is 10 today and its square is 100
>>> print template('The answer is {{ answer }} today and its square is {{ str(answer ** 2) * 3 }}', answer=10)
The answer is 10 today and its square is 100100100
>>> print template('The villain is {{ v }}', v='Cersei Lannister')
The villain is Cersei Lannister
>>> print template('The villain is {{ v }}', v='Cersei & Jamie Lannister')
The villain is Cersei &amp; Jamie Lannister
>>> print template('The villain is {{! v }}', v='Cersei & Jamie Lannister')
The villain is Cersei & Jamie Lannister
>>> 
>>> # Python statements are on lines where the first non-whitespace character is a %
>>> # Those lines don't print.  They execute.
>>> # To end a block, you need a % end entry.
>>> 
>>> mood_template = '''
I am feeling:
% if hs >= 50:
happy
% else:
sad
% end
today
'''
>>> print template(mood_template, hs=70)

I am feeling:
happy
today

>>> print template(mood_template, hs=40)

I am feeling:
sad
today

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
>>> # Counterpart
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
The lannister Family

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
The Lannister Family

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
The Lannister Family
===========

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
The Lannister Family
====================

>>> 
>>> 
>>> for name in first_names:
	print name

	
tywin
cersei&jamie
tyrion
jeoffrey
tommin
mycella
>>> for i, name in enumerate(first_names):
	print i, name

	
0 tywin
1 cersei&jamie
2 tyrion
3 jeoffrey
4 tommin
5 mycella
>>> for i, name in enumerate(first_names, start=1):
	print i, name

	
1 tywin
2 cersei&jamie
3 tyrion
4 jeoffrey
5 tommin
6 mycella
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
The Lannister Family
====================
name
name
name
name
name
name

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
The Lannister Family
====================
tywin
cersei&amp;jamie
tyrion
jeoffrey
tommin
mycella

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
The Lannister Family
====================
tywin
cersei&jamie
tyrion
jeoffrey
tommin
mycella

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
The Lannister Family
====================
Tywin
Cersei&jamie
Tyrion
Jeoffrey
Tommin
Mycella

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
The Lannister Family
====================
Tywin
Cersei&Jamie
Tyrion
Jeoffrey
Tommin
Mycella

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
The Lannister Family
====================
i. Tywin
i. Cersei&Jamie
i. Tyrion
i. Jeoffrey
i. Tommin
i. Mycella

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
The Lannister Family
====================
1. Tywin
2. Cersei&Jamie
3. Tyrion
4. Jeoffrey
5. Tommin
6. Mycella

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
The Lannister Family
====================
1. Tywin
    ^-- Very important person
2. Cersei&Jamie
3. Tyrion
4. Jeoffrey
5. Tommin
6. Mycella

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
The Lannister Family
====================
1. Tywin
    ^-- Very important person
2. Cersei&Jamie
3. Tyrion
4. Jeoffrey
5. Tommin
6. Mycella

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======

====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======

====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Lannister Family </title>
</head>
<body>
</body>
</html>

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Lannister Family </title>
</head>
<body>
<h1> The <em> Lannister </em> Family </h1>
</body>
</html>

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Lannister Family </title>
</head>
<body>
<h1> The <em> Lannister </em> Family </h1>
<hr>
<ol>
  <li> Tywin </li>
  <li> Cersei&amp;Jamie </li>
  <li> Tyrion </li>
  <li> Jeoffrey </li>
  <li> Tommin </li>
  <li> Mycella </li>
</ol>
</body>
</html>

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Lannister Family </title>
</head>
<body>
<h1> The <em> Lannister </em> Family </h1>
<hr>
<ol>
  <li> Tywin </li>
  <li> Cersei&amp;Jamie </li>
  <li> Tyrion </li>
  <li> Jeoffrey </li>
  <li> Tommin </li>
  <li> Mycella </li>
</ol>
</body>
</html>

stark eddard catelyn robb jonsnow sansa arya bran rickon
targaryen aegon danyeres ameon vasayres
simpsons homer marge bart lisa maggie
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
stark eddard catelyn robb jonsnow sansa arya bran rickon
targaryen aegon danyeres ameon vasayres
simpsons homer marge bart lisa maggie
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
['stark', 'eddard', 'catelyn', 'robb', 'jonsnow', 'sansa', 'arya', 'bran', 'rickon']
['targaryen', 'aegon', 'danyeres', 'ameon', 'vasayres']
['simpsons', 'homer', 'marge', 'bart', 'lisa', 'maggie']
>>> fields[0]
'simpsons'
>>> fields[1:]
['homer', 'marge', 'bart', 'lisa', 'maggie']
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
The Stark Family
================
1. Eddard
    ^-- Very important person
2. Catelyn
3. Robb
4. Jonsnow
5. Sansa
6. Arya
7. Bran
8. Rickon

The Targaryen Family
====================
1. Aegon
    ^-- Very important person
2. Danyeres
3. Ameon
4. Vasayres

The Simpsons Family
===================
1. Homer
    ^-- Very important person
2. Marge
3. Bart
4. Lisa
5. Maggie

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
The Stark Family
================
1. Eddard
    ^-- Very important person
2. Catelyn
3. Robb
4. Jonsnow
5. Sansa
6. Arya
7. Bran
8. Rickon

The Targaryen Family
====================
1. Aegon
    ^-- Very important person
2. Danyeres
3. Ameon
4. Vasayres

The Simpsons Family
===================
1. Homer
    ^-- Very important person
2. Marge
3. Bart
4. Lisa
5. Maggie

>>> line
'simpsons homer marge bart lisa maggie'
>>> get_family
<function get_family at 0x10382bcf8>
>>> get_family(line)

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    get_family(line)
  File "/Users/raymond/Dropbox/Public/sj178/templating_demo.py", line 61, in get_family
    return dict(family_plain_text, lastname=fields[0], first_names=fields[1:])
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
The Stark Family
================
1. Eddard
    ^-- Very important person
2. Catelyn
3. Robb
4. Jonsnow
5. Sansa
6. Arya
7. Bran
8. Rickon

The Targaryen Family
====================
1. Aegon
    ^-- Very important person
2. Danyeres
3. Ameon
4. Vasayres

The Simpsons Family
===================
1. Homer
    ^-- Very important person
2. Marge
3. Bart
4. Lisa
5. Maggie

>>> get_family(line)
{'first_names': ['homer', 'marge', 'bart', 'lisa', 'maggie'], 'lastname': 'simpsons'}
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
The Stark Family
================
1. Eddard
    ^-- Very important person
2. Catelyn
3. Robb
4. Jonsnow
5. Sansa
6. Arya
7. Bran
8. Rickon

The Targaryen Family
====================
1. Aegon
    ^-- Very important person
2. Danyeres
3. Ameon
4. Vasayres

The Simpsons Family
===================
1. Homer
    ^-- Very important person
2. Marge
3. Bart
4. Lisa
5. Maggie

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
The Stark Family
================
1. Eddard
    ^-- Very important person
2. Catelyn
3. Robb
4. Jonsnow
5. Sansa
6. Arya
7. Bran
8. Rickon

The Targaryen Family
====================
1. Aegon
    ^-- Very important person
2. Danyeres
3. Ameon
4. Vasayres

The Simpsons Family
===================
1. Homer
    ^-- Very important person
2. Marge
3. Bart
4. Lisa
5. Maggie

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
The Stark Family
================
1. Eddard
    ^-- Very important person
2. Catelyn
3. Robb
4. Jonsnow
5. Sansa
6. Arya
7. Bran
8. Rickon

The Targaryen Family
====================
1. Aegon
    ^-- Very important person
2. Danyeres
3. Ameon
4. Vasayres

The Simpsons Family
===================
1. Homer
    ^-- Very important person
2. Marge
3. Bart
4. Lisa
5. Maggie

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Stark Family </title>
</head>
<body>
<h1> The <em> Stark </em> Family </h1>
<hr>
<ol>
  <li> Eddard </li>
  <li> Catelyn </li>
  <li> Robb </li>
  <li> Jonsnow </li>
  <li> Sansa </li>
  <li> Arya </li>
  <li> Bran </li>
  <li> Rickon </li>
</ol>
</body>
</html>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Targaryen Family </title>
</head>
<body>
<h1> The <em> Targaryen </em> Family </h1>
<hr>
<ol>
  <li> Aegon </li>
  <li> Danyeres </li>
  <li> Ameon </li>
  <li> Vasayres </li>
</ol>
</body>
</html>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Simpsons Family </title>
</head>
<body>
<h1> The <em> Simpsons </em> Family </h1>
<hr>
<ol>
  <li> Homer </li>
  <li> Marge </li>
  <li> Bart </li>
  <li> Lisa </li>
  <li> Maggie </li>
</ol>
</body>
</html>

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/sj178/templating_demo.py ======
The Stark Family
================
1. Eddard
    ^-- Very important person
2. Catelyn
3. Robb
4. Jonsnow
5. Sansa
6. Arya
7. Bran
8. Rickon

The Targaryen Family
====================
1. Aegon
    ^-- Very important person
2. Danyeres
3. Ameon
4. Vasayres

The Simpsons Family
===================
1. Homer
    ^-- Very important person
2. Marge
3. Bart
4. Lisa
5. Maggie

>>> import sqlite3
>>> conn = sqlite3.connect('example.db')
>>> c = conn.cursor()
>>> c.execute('CREATE TABLE Stocks (date text, trans text, symbol text, qty real, price real)')
<sqlite3.Cursor object at 0x104c32dc0>
>>> c.execute("INSERT INTO Stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100, 35.14);")
<sqlite3.Cursor object at 0x104c32dc0>
>>> conn.commit()
>>> conn.close()
>>> import sqlite3
>>> conn = sqlite3.connect('example.db')
>>> c = conn.cursor()
>>> symbol = 'RHAT'
>>> c.execute('SELECT * FROM Stocks WHERE symbol=?' % symbol)

Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    c.execute('SELECT * FROM Stocks WHERE symbol=?' % symbol)
TypeError: not all arguments converted during string formatting
>>> c.execute('SELECT * FROM Stocks WHERE symbol=%s' % symbol)

Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    c.execute('SELECT * FROM Stocks WHERE symbol=%s' % symbol)
OperationalError: no such column: RHAT
>>> c.execute('SELECT * FROM Stocks WHERE symbol="%s"' % symbol)
<sqlite3.Cursor object at 0x104c32e30>
>>> c.fetchone()
(u'2006-01-05', u'BUY', u'RHAT', 100.0, 35.14)
>>> purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
>>> c.executemany('INSERT INTO Stocks VALUES (?,?,?,?,?)', purchases)
<sqlite3.Cursor object at 0x104c32e30>
>>> for row in c.execute('SELECT * FROM Stocks;'):
	print row

	
(u'2006-01-05', u'BUY', u'RHAT', 100.0, 35.14)
(u'2006-03-28', u'BUY', u'IBM', 1000.0, 45.0)
(u'2006-04-05', u'BUY', u'MSFT', 1000.0, 72.0)
(u'2006-04-06', u'SELL', u'IBM', 500.0, 53.0)
>>> for row in c.execute('SELECT * FROM Stocks ORDER BY price;'):
	print row

	
(u'2006-01-05', u'BUY', u'RHAT', 100.0, 35.14)
(u'2006-03-28', u'BUY', u'IBM', 1000.0, 45.0)
(u'2006-04-06', u'SELL', u'IBM', 500.0, 53.0)
(u'2006-04-05', u'BUY', u'MSFT', 1000.0, 72.0)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/sql_demo.py ==========
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/sql_demo.py ==========
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/sql_demo.py ==========
(4219, u'Advanced Git')
(5103, u'SDN and ACI')
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/sql_demo.py ==========
(5103, u'SDN and ACI')
(4219, u'Advanced Git')
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj178/sql_demo.py ==========
(5103, u'SDN and ACI')
(4219, u'Advanced Git')
(u'Python III',)
>>> 
>>> 
>>> # Build an Amazon or BH Photo Video
>>> import antigravity
>>> import webbrowser
>>> webbrowser.open('file:///Users/raymond/sj/lannisters.html')
True
>>> 
