Python 3.8.2 (default, Jul 16 2020, 14:00:26) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruit = 'banana'
>>> letter = fruit[1]
>>> print (letter)
a
>>> letter =fruit[0]
>>> print(letter)
b
>>> len(fruit)
6
>>> length = len(fruit)
>>> last = fruit[lenght]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    last = fruit[lenght]
NameError: name 'lenght' is not defined
>>> last = fruit[lenght-1]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    last = fruit[lenght-1]
NameError: name 'lenght' is not defined
>>> length = len(fruit)
>>> last = fruit[lenght-1]
SyntaxError: multiple statements found while compiling a single statement
>>> last = fruit[length-1]
>>> print(last)
SyntaxError: multiple statements found while compiling a single statement
>>> length = len(fruit)
>>> last = fruit[length-1]
>>> print(last)
a
>>> fruit = 'abcdef'
>>> fruit
'abcdef'
>>> len(fruit)
6
>>> fruit[len(fruit) -1 ]
'f'
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
a
b
c
d
e
f
>>> index = 5
>>> while index >=0:
	letter = fruit[index]
	print(letter)
	index = index - 1

	
f
e
d
c
b
a
>>> for char in fruit:
	print(char)

	
a
b
c
d
e
f
>>> fruit = 'banana'
>>> fruit[:3]
'ban'
>>> fruit[3:]
'ana'
>>> fruit
'banana'
>>> fruit[3:3]
''
>>> 