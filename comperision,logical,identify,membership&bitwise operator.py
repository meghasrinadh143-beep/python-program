Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=4
>>> b=5
>>> b+=a
>>> b
9
>>> b-=3
>>> b
6
>>> b*=4
>>> b
24
>>> b//=4
>>> b
6
>>> b/=4
>>> b
1.5
>>> b**=4
>>> b
5.0625
>>> b%=4
>>> b
1.0625
>>> #comparision
>>> a=5
>>> b=6
>>> a<b
True
>>> a>b
False
b>a
True
a<=b
True
a>=b
False
a!=b
True
a==b
False
#logical
a=4
b=5
a<b and b>a
True
a<=b andb>=a
SyntaxError: invalid syntax
a<=b and b>=a
True
a!=b and b==a
False
a!= or b==a
SyntaxError: invalid syntax
a!=b or b==a
True
not true
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
not True
False
not False
True
#identify
a=6
type(a) is int
True
type(a)is float
False
b=4.66
type(b) is float
True
a="srinadh"
type(a) is str
True
type(a) is int
False
a=a+7j
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a=a+7j
TypeError: can only concatenate str (not "complex") to str
a=5+7j
type(a) is complex
True
type(a) is str
False
a=True
type(a) is bool
True
type(a) is not str
True
type(a) is bool or complex
True
#membership
a=3,4,5,6,7,8,9
9 in a
True
10 in a
False
10 not in a
True
3 in a
True
3 not in a
False
23 in a
False
23 not in a
True
5 in a
True
5 not in a
False
6 in a
True
6 not in a
False
8in a
True
8not in a
False
00 in a
False
00 not in a
True
#you can take any data type in every operator
#bit wise
#bit wise
#bitwise
a=7
b=9
a&b
1
a=3
b=8
a|b
11
a=2
b=6
a|b
6
~b
-7
#xor bitwise
2<<4
32
a=4
a<<3
32
a=6
a>>4
0
a=3
a^4
7
