Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
a=9
b=10
print(a+b)
19
c=7
print(c)
7
Z=40
print(Z)
40
age=23
print(age)
23
AGE_of_srinadh=25
print(AGE_of_srinadh)
25
city=hyderabad
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    city=hyderabad
NameError: name 'hyderabad' is not defined
city="hyderabad"
print(city)
hyderabad
country="uk"
print(country)
uk
_place="mangalagiri"
print(_place)
mangalagiri
2=30
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a2=30
print(a2)
30
4a=30
SyntaxError: invalid decimal literal
a0123456789
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a0123456789
NameError: name 'a0123456789' is not defined
a0123456789=100
print(a0123456789)
100
#special characters
@=50
SyntaxError: invalid syntax
$=70
SyntaxError: invalid syntax
_=30
print(_)
30
_d=30
print(_d)
30
 f=40
 
SyntaxError: unexpected indent
#keywords
if=89
SyntaxError: invalid syntax
first name="lokanadh"
SyntaxError: invalid syntax
first_name="lokanadh"
print(first_name)
lokanadh
fristname="lokanadh "
print(firstname )
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print(firstname )
NameError: name 'firstname' is not defined. Did you mean: 'first_name'?
print(firstname)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print(firstname)
NameError: name 'firstname' is not defined. Did you mean: 'first_name'?
fristname="lokanadh"
print(firstname)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(firstname)
NameError: name 'firstname' is not defined. Did you mean: 'first_name'?
a=4,b=9
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=5;v=5
print(a,v)
5 5
print(a+v)
10
a,b=5,7
print(a+b)
12
a=2,3,4,5,6,7,8
print(a)
(2, 3, 4, 5, 6, 7, 8)
a,b,c=3,5,7
print(a,b,c)
3 5 7
a,b,c=2,3,4,5,6,7
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a,b,c=2,3,4,5,6,7
ValueError: too many values to unpack (expected 3, got 6)
#unpacking
a,b,c=(6,7,8)
print(a,b,c)
6 7 8
#delete key word
a=6
print(a)
6
del a
print(a)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'a2'?
fname="srinadh"
>>> lanme="lokanadh"
>>> print(fname+lname)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print(fname+lname)
NameError: name 'lname' is not defined. Did you mean: 'fname'?
>>> print(fname+lanme)
srinadhlokanadh
>>> print(fname+" "+lanme)
srinadh lokanadh
>>> print(fname,lanme)
srinadh lokanadh
>>> name="srinadh"
>>> print(name)
srinadh
>>> NAME="srinadh"
>>> print(NAME)
srinadh
>>> Name="srinadh"
>>> print(Name)
srinadh
>>> name="srinadh"
>>> print(Name)
srinadh
>>> print(nAME)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    print(nAME)
NameError: name 'nAME' is not defined. Did you mean: 'NAME'?
