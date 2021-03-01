# Python version 3.8+

>>> a = 6, 9
>>> a
(6, 9)

>>> (a := 6, 9)
(6, 9)
>>> a
6

>>> a, b = 6, 9 # Typical unpacking
>>> a, b
(6, 9)
>>> (a, b = 16, 19) # Oops
  File "<stdin>", line 1
    (a, b = 6, 9)
          ^
SyntaxError: invalid syntax

>>> (a, b := 16, 19) # This prints out a weird 3-tuple
(6, 16, 19)

>>> a # a is still unchanged?
6

>>> b
16
