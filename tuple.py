Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple
>>> a=(4,4.5,'pyhton',4+7j,True,False)
>>> aprint()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    aprint()
NameError: name 'aprint' is not defined. Did you mean: 'print'?
>>> print(a)
(4, 4.5, 'pyhton', (4+7j), True, False)
>>> type(a)
<class 'tuple'>
>>> a.index(4+7j)
3
>>> len(a)
6
>>> a.cont(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.cont(a)
AttributeError: 'tuple' object has no attribute 'cont'. Did you mean: 'count'?
>>> a.count(true)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.count(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> a,count(True)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a,count(True)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> a.count(True)
1
