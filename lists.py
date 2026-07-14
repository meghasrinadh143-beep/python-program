Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,4.5,"pyhton",6+7j,True,False]
print(a)
[2, 4.5, 'pyhton', (6+7j), True, False]
type(a)
<class 'list'>
b=8.9
type(b)
<class 'float'>
c=[8.9]
type(c)
<class 'list'>
#append
a=["python","c","c++"]
a.append("java")
a
['python', 'c', 'c++', 'java']
a.append(html,css)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.append(html,css)
NameError: name 'html' is not defined. Did you forget to import 'html'?
a.append("html","css")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.append("html","css")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["html","css"])
a
['python', 'c', 'c++', 'java', ['html', 'css']]
#extend
a=["vij",'hyd','viz']
a.extend(['pochampally','secbad'])
a
['vij', 'hyd', 'viz', 'pochampally', 'secbad']
#insert
b=['srinadh','lokanadh','kavitha']
b.insert(1,'kumar')
b
['srinadh', 'kumar', 'lokanadh', 'kavitha']
#indexin list
a=['apple'.'banana','graps']
SyntaxError: invalid syntax
a=['apple','banana','graps']
a.indexing
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.indexing
AttributeError: 'list' object has no attribute 'indexing'
a.index('graps ')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.index('graps ')
ValueError: list.index(x): x not in list
a.index('graps')
2
a.copy()
['apple', 'banana', 'graps']
b=a.copy
b
<built-in method copy of list object at 0x000002505E2C57C0>
b=a.copy()
b
['apple', 'banana', 'graps']
#count
a.count('apple')
1
#length
len(a)
3
d='apple'
len(d)
5
e=['apple']
len(e)
1
2
2
#sort
a=['kiwi','mango','apple','banana','dragon']
a.sort()
a
['apple', 'banana', 'dragon', 'kiwi', 'mango']
b=[9,7,6,5,4,3,2]
a.sort()
b.sort()
b
[2, 3, 4, 5, 6, 7, 9]
a
['apple', 'banana', 'dragon', 'kiwi', 'mango']
#reverse
a=['flat','cd','cn']
a.reverse()
a
['cn', 'cd', 'flat']
b=[0,9,7,6,5,4,3,3,4,5]
b.reverse()
b
[5, 4, 3, 3, 4, 5, 6, 7, 9, 0]
>>> #pop
>>> a=['srinadh','vyshnavi','vennela','kumar','kavitha','lokanadh',]
>>> a.pop(1,2)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a.pop(1,2)
TypeError: pop expected at most 1 argument, got 2
>>> a.pop(1)
'vyshnavi'
>>> a
['srinadh', 'vennela', 'kumar', 'kavitha', 'lokanadh']
>>> a.pop(1)
'vennela'
>>> a
['srinadh', 'kumar', 'kavitha', 'lokanadh']
>>> a.pop('srinadh')
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a.pop('srinadh')
TypeError: 'str' object cannot be interpreted as an integer
>>> a.remove('lokanadh')
>>> a
['srinadh', 'kumar', 'kavitha']
>>> #clear
>>> a=['ke','ka','ap','up']
>>> a.clear()
>>> a
[]
>>> a.append('srinadh')
>>> a
['srinadh']
