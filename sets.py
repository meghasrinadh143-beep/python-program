Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #sets{}
>>> a={a,7.8,'srinadh',5+3j,True,False}
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a={a,7.8,'srinadh',5+3j,True,False}
NameError: name 'a' is not defined
>>> a={4}
>>> a={2,4.6,'srinadh',5+6j,True,False}
>>> print(a)
{False, True, 2, 4.6, 'srinadh', (5+6j)}
>>> type(a)
<class 'set'>
>>> b={9,8,7,6,5,4,3,2}
>>> print(b)
{2, 3, 4, 5, 6, 7, 8, 9}
>>> type(b)
<class 'set'>
>>> #add
>>> a={2,3,4,5,6,7}
>>> a.add(3)
>>> a
{2, 3, 4, 5, 6, 7}
>>> #issubset
>>> a={2,3,4,5,6,7}
>>> b={4,5,6,7}
>>> b.issubset(a)
True
>>> a.issubset(b)
False
>>> #superset
a={3,4,5,6,7,8,9,11,12}
b={3,4,5,6,7}
a.issuperset(b)
True
b.issuperset(a)
False
#union
a={1,2,3,4,5}
b{2,3,4,5,6,7,8}
SyntaxError: invalid syntax
b={2,3,4,5,6,7,8,9}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
#instesectoin()
a={1,2,3,4,5,6,7}
b={2,3,4}
a.intersection(b)
{2, 3, 4}
b.intersetion(a)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    b.intersetion(a)
AttributeError: 'set' object has no attribute 'intersetion'. Did you mean: 'intersection'?
b.intersection(a)
{2, 3, 4}
#difference

a={1,2,3,4,5,6,7,8,9,12,13,14}
b={3,4,5,6,7,8,9,12,15,17}
a.difference(b)
{1, 2, 13, 14}
b.difference(a)
{17, 15}
#update
a={2,3,4,5}
b={5,6,7,8}
a.update(a)
a
{2, 3, 4, 5}
a.update(b)
a
{2, 3, 4, 5, 6, 7, 8}
b.update(a)
b
{2, 3, 4, 5, 6, 7, 8}
a
{2, 3, 4, 5, 6, 7, 8}
b
{2, 3, 4, 5, 6, 7, 8}
#symetric_difference
a={3,4,5,6,7,8,9}
b={1,2,3,4,5,6,7,8,9,0}
a.symetric_difference(b)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.symetric_difference(b)
AttributeError: 'set' object has no attribute 'symetric_difference'. Did you mean: 'symmetric_difference'?
a.symmetric_difference()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.symmetric_difference()
TypeError: set.symmetric_difference() takes exactly one argument (0 given)
a.symmetric_difference(b)
{0, 1, 2}
b.symmetric_difference(a)
{0, 1, 2}
#difference_update
a={2,3,4,5,6,7}
b={2,3,4,5,6,7,8,9}
a.difference_update(b)
a
set()
b.difference_update(a)
b
{2, 3, 4, 5, 6, 7, 8, 9}
#intersection_update
a={1,2,3,4,5,6,7,8}
b={13,24,5,6,2,3}
a.intersection_update()
b
a.intersection_update(b)
a
{2, 3, 5, 6}
b.intersection_update(a)
b
{2, 3, 5, 6}
a={11,12,13,14,15,16}
\
b={13,14,15,16,17}
a.
(b)
SyntaxError: invalid syntax
a.symmetric_update(b)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.symmetric_update(b)
AttributeError: 'set' object has no attribute 'symmetric_update'
a.symmetric_difference_update(b)
a
{17, 11, 12}
b.symmetric_difference_update(a)
b
{16, 11, 12, 13, 14, 15}
#pop i set
a={3,4,5,6}
a.pop()
3
a
{4, 5, 6}
a.pop(2)#we cant detele a specific number with pop function
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    a.pop(2)#we cant detele a specific number with pop function
TypeError: set.pop() takes no arguments (1 given)
a.remove(4)
a
{5, 6}
#copy
a={2,3,4,56}
a.copy(b)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    a.copy(b)
TypeError: set.copy() takes no arguments (1 given)
c.copy()
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    c.copy()
NameError: name 'c' is not defined
a.copy()
{56, 2, 3, 4}
b=a.copy()
b
{56, 2, 3, 4}
#discard
a={2,3,4,5,6}
a.discard(5)
a
{2, 3, 4, 6}
#clear
a={2,3,4,5}
a.clear()
a
set()
#add
a.add(3)
a
{3}
a={2,3,4,5,6}
b={6,7,8,9}
a.isdisjoint(b)
False
c={1,2,3,4}
d={5,6,7,8}
c.isdisjoint(d)
True
