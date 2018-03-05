## DAY 1

files involved: __algebra.py__, __subprocess_demo.py__, __templating_demo.py__, __sql_demo.py

-  Understand the __Dunder__ (aka: "double-underscore") notation.
  ```
  __name__ --> automatically generated (generally '__main__')
  __doc__ --> prints the module's documentation or docstring (at the very top of the module)
  ```
  - this is where built-in functions such a dir() come in:
    ```
    $ dir([object])
      --> object (optional) - dir() attempts to return all attributes of this object.
    ```
- What does __import__ do in python?
  ```
    * Scans the current directory and standard library for a py file
    * Runs all the code in its own namespace
    * Wraps it in a module object
    * Makes an assignment to globals
  ```
  - In general, it is advised to run your python modules with a `-m` flag, as mentioned by Raymond on his twitter: "It is better to run "pip" or "venv" with "-m" than with their unqualified command names":
    ```
    $ python3.6 -m pip install hypothesis     # Unequivocal
    $ pip install hypothesis      # Hmm, which python was the install target?
    ```
- Python is a __self documenting language__: functions need to have very clear names, parameters need to have clear names, most importantly every method needs to have a general __Docstring__.
  - Unlike comments, __docstrings__ are stored in memory, a comment is generally explains why the function was written as is, for instance.
  - spell things out, avg should be average, don't abbreviate since people abbreviate in different ways. __UNLESS__: there is an equivocal abbreviation; unless the full word is hard to spell.
-  Even though PEP8 is a common standard it is not always the best thing to follow!

- Another important subject/reminder is understanding that what we see when declaring variables in python is not necessarily how they are stored! Coming from a C/C++ background makes it simple to understand the lower level allocations - and what not - but Python makes things simpler, this doesn't mean we need to ignore it's lower level intricacies. In fact a lot of people have to deal with things like "representation errors", in fact, __when writing a number in decimal floating point, such as a fraction as we know it, it may not be exactly storable in binary floating point. This is why we say that binary floating point intrinsically has "representation error"__:
  ```
  When you type in numbers as decimal fractions, they are stored as binary fractions.
  A little fun on the interpreter makes it very clear:

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

  OR EVEN WITH ARRAYS!:

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

  ```
  __Moral of the story:__
  - The number 2.2 is entered as 22 / 10
  - but stored as 2476979795053773 / 1125899906842624
  - which is slightly off from 22 / 10
  - Instead of s == t, write abs(s-t) < 0.0000001 to get the correct result
  - but stored as 2476979795053773 / 1125899906842624
  - The first number in the fraction is a 53-bits binary  and the second equal to 2 ** 50

  __Reminders / Additional Info__:
  ```
  binary floating point: 101.11
                              ^-- 1/4
                             ^-- 1/2
  101.11 --> 5.75
  You type in numbers as decimal fractions but they are stored as binary functions
  example where it fails: 22/10 --> n / 2 ** m
                                    ^ 53 bits
  x.as_integer_ratio()
  never use == for floating point binary

  the number 2.2 is entered as 22 /10 but stored as huge_number_determined_with_x_as_integer_ratio()/huge_number_determined_with_x_as_integer_ratio() which is slightly off from 22/10

  https://www.ntu.edu.sg/home/ehchua/programming/java/DataRepresentation.html --> for more information on data representation and storage
  ```

- Another built-in function that was explored was __repr()__ and it's usage with __eval__, the below example that used an initial docstring speaks for itself:
  ```
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
  ```  
  - The definition for a __repr()__ being the following:
    - Return a string containing a printable representation of an object. This is the same value yielded by conversions (reverse quotes). It is sometimes useful to be able to access this operation as an ordinary function. For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to eval(), otherwise the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object. A class can control what this function returns for its instances by defining a \__repr__() method.

  - Functions that were also used and that are useful day to day: `lstrip`, `rstrip`, `raw_input`


  - To create colorful documentation, run this:
      ```
      $ python -m pydoc -w algebra
      wrote algebra.html from algebra.py
      ```
  - To create professional documentation, use Sphinx:
      ```
      http://www.sphinx-doc.org/en/master/
      ```
- SHELLSHOCK exploit explanation:
```
>>> # SHELLSHOCK
>>> # Bash runs its start up scripts profile.sh .bashrc
>>> # Inputs: echo ~/.txt
>>> # Parses and translates to: ['/usr/bin/echo', '/Users/raymond/.txt']
>>> # Runs the command
>>> # Capture the output to stdout
```
  - Essentially: "Bash can also be used to run commands passed to it by applications and it is this feature that the vulnerability affects. One type of command that can be sent to Bash allows environment variables to be set. Environment variables are dynamic, named values that affect the way processes are run on a computer. The vulnerability lies in the fact that an attacker can tack-on malicious code to the environment variable, which will run once the variable is received."

- using __splitlines()__ : every new line element/string is put as a new element of an array
- using __split()__: every space between chars in a string is split/marks the split between chars and populates an array.


- using __graphviz__ to represent any types of graphs programmatically.

- Basic templating was also explored using `bottle` which has inspired the likes of django, jinja2..etc:
```
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
```

```
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
```

```
>>> for i, name in enumerate(first_names, start=1):
	print i, name


1 tywin
2 cersei&jamie
3 tyrion
4 jeoffrey
5 tommin
6 mycella
```

- Introduction to bottle templating and logic in __templating_demo.py__.
- SQL demo and creating a db in __sql_demo.py__, also shows the proper way to querying so as to avoid easy sql injections.

## Extras
- Comma at the end of print statement the `print`'s default `\n` and thus doesn't skip a line for every consecutive print in a loop.

- "Write at the level of human thought".
- `python -m` and `-i` (imports) or `-im  -w` creates colourful html documentation.

- sphinx documentation is cool documentation
