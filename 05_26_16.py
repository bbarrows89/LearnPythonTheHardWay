Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 00:54:21) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
9 -2
7
>>> def convert_to_celsius(fahrenheit):
	return (fahrenheit - 32) * 5 / 9
help(convert_to_celsius)
SyntaxError: invalid syntax
>>> def  convert_to_celsius(fahrenheit):
	return (fahrenheit - 32) * 5 / 9
convert_to_celsius(28)
SyntaxError: invalid syntax
>>> 
>>> convert_to_celsius(28)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    convert_to_celsius(28)
NameError: name 'convert_to_celsius' is not defined
>>> def convert_to_celsius(fahrenheit):
	return (fahrenheit - 32) * 5 / 9

>>> help(convert_to_celsius)
Help on function convert_to_celsius in module __main__:

convert_to_celsius(fahrenheit)

>>> convert_to_celsius(75)
23.88888888888889
>>> convert_to_celsius(100)
37.77777777777778
>>> def quadratic(a, b, c, x):
	first = a * x ** 2
	second = b * x
	third = c
	return first + second + third

>>> quadratic(2, 3, 4, 0.5)
6.0
>>> quadratic(2, 3, 4, 1.5)
13.0
>>> quadratic(4)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    quadratic(4)
TypeError: quadratic() missing 3 required positional arguments: 'b', 'c', and 'x'
>>> quadratic(4,1,6,10
	  )
416
>>> quadratic(5, 6, 10, -2)
18
>>> help(quadratic)
Help on function quadratic in module __main__:

quadratic(a, b, c, x)

>>> quadratic(1,4,52,2
	  )
64
>>> 
