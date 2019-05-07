'''
Help! - 50 XP
==============================================================

Maybe you already know the name of a Python function, but you still have to figure out how to use it. Ironically, you have to ask for information about a function with another function: help(). In IPython specifically, you can also use ? before the function name.

To get help on the max() function, for example, you can use one of these calls:

help(max)
?max

Use the Shell on the right to open up the documentation on complex(). Which of the following statements is true?



Instructions
==============================================================

Possible Answers
A. complex() takes exactly two arguments: real and [, imag].

B. complex() takes two arguments: real and imag. Both these arguments are required.

C. complex() takes two arguments: real and imag. real is a required argument, imag is an optional argument.

D. complex() takes two arguments: real and imag. If you don't specify imag, it is set to 1 by Python.


Answer - 3

Code
==============================================================
'''
'''
help(complex)
Help on class complex in module builtins:

class complex(object)
 |  complex(real[, imag]) -> complex number
 |  
 |  Create a complex number from a real part and an optional imaginary part.
 |  This is equivalent to (real + imag*1j) where imag defaults to 0.

'''