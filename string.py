Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#length of string(len())
a="codegnan"
len(a)
8
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
e="i am in vijay"
len(e)
13
e="srinadh is in hyderabad"
len(e)
23
#count()
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("k")
2
a.count("t")
5
a.count(" ")
3
#find a string
a="pyhton"
a.find(y)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.find(y)
NameError: name 'y' is not defined
a.find("y")
1
b="srinadh"
b.find("d")
5
b.find("k")
-1
#escape sequences
#\n->new line
#\t->tab space
a="name\nmailid\tmobile no\ncollege\tbranch"
print(a)
name
mailid	mobile no
college	branch
b="name:srinadh\nmailid:meghasrinadh142@gmail.com\tmobile no:7675817792\ncollege:marri laxman reddy instuite of technology\tbranch:compyter science engineering "
print(b)
name:srinadh
mailid:meghasrinadh142@gmail.com	mobile no:7675817792
college:marri laxman reddy instuite of technology	branch:compyter science engineering 
b="name:srinadh\nmailid:meghasrinadh142@gmail.com\tmobile no:7675817792\ncollege:marri laxman reddy instuite of technology\tbranch:computer science engineering "
print("b")
b
print(b)
name:srinadh
mailid:meghasrinadh142@gmail.com	mobile no:7675817792
college:marri laxman reddy instuite of technology	branch:computer science engineering 
#replace
a="wait until you succeed "
a.replace("wait","work")
'work until you succeed '
b="python java"
b.replace("p","c")
'cython java'
c="wait wait until you succeed "
c.replace("wait","work")
'work work until you succeed '
#upper()
a="code"
a.upper()
'CODE'
b="srinadh"
b="SRINADH"
b.lower()
'srinadh'
c="lokanadh"
c.captlize()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    c.captlize()
AttributeError: 'str' object has no attribute 'captlize'. Did you mean: 'capitalize'?
c.capetilize()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    c.capetilize()
AttributeError: 'str' object has no attribute 'capetilize'. Did you mean: 'capitalize'?
c.capitilize
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    c.capitilize
AttributeError: 'str' object has no attribute 'capitilize'. Did you mean: 'capitalize'?
c.capitilize()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    c.capitilize()
AttributeError: 'str' object has no attribute 'capitilize'. Did you mean: 'capitalize'?
c.capitalize()
'Lokanadh'
d="python course"
d.title()
'Python Course'
e="srinadh is from hyderabad"
e.title()
'Srinadh Is From Hyderabad'
e.capitalize()
'Srinadh is from hyderabad'
a="code"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True
b="code sourse"
b.isalpha()
False
b="codecourse"
b.isalpha()
True
d=1234
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
d="1234"
d.isdigit()
True
>>> e="pooja1234"
>>> e.alnum()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    e.alnum()
AttributeError: 'str' object has no attribute 'alnum'. Did you mean: 'isalnum'?
>>> 
>>> e.isalnum()
True
>>> f="srinadh@20/07/2001"
>>> e.isalnum()
True
>>> a="data science"
>>> a.startswitch("d\")
...               
SyntaxError: unterminated string literal (detected at line 1); perhaps you escaped the end quote?
>>> a.startswitch("d")
...               
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a.startswitch("d")
AttributeError: 'str' object has no attribute 'startswitch'. Did you mean: 'startswith'?
>>> g="data science"
...               
>>> g.startswith("d")
...               
True
>>> g.startswith("e")
...               
False
