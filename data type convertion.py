Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatype convertion
#int
int(5)
5
int(7.5)
7
int("srinadh")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("srinadh")
ValueError: invalid literal for int() with base 10: 'srinadh'
int(5+8j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(5+8j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(5)
5.0
float(5.7)
5.7
float("srinadh")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("srinadh")
ValueError: could not convert string to float: 'srinadh'
float(5+9j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(5+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#string
str(3)
'3'
str(5.9)
'5.9'
str(""srinadh)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
str("srinadh")
'srinadh'
str(5+8j)
'(5+8j)'
str(True)
'True'
str(False)
'False'
#complex
complex(4)
(4+0j)
>>> complex(4.9)
(4.9+0j)
>>> complex("srinadh")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    complex("srinadh")
ValueError: complex() arg is a malformed string
>>> complex(6+7j)
(6+7j)
>>> comple(True)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    comple(True)
NameError: name 'comple' is not defined. Did you mean: 'compile'?
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #boolean
>>> bool(4)
True
>>> bool(4.9)
True
>>> bool("srinadh")
True
>>> bool(6+7j)
True
>>> bool(True)
True
>>> bool(False)
False
