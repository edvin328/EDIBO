Python 3.8.2 (default, Jul 16 2020, 14:00:26) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=11
>>> a
11
>>> type(a)
<class 'int'>
>>> if type(a) == int:
	print("labi")

	
labi
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
else:
	print("slikti")

	
labi
>>> a=5.5
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
else:
	print("slikti")

	
arī labi
>>> a=djdj
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a=djdj
NameError: name 'djdj' is not defined
>>> 