Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}
a={"name":"srinadh"}
a={"name":"srinadh","age":24,"month":07}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
a={"name":"srinadh","age":24,"month":7}
print(a)
{'name': 'srinadh', 'age': 24, 'month': 7}
type(a)
<class 'dict'>
a.keys()
dict_keys(['name', 'age', 'month'])
a.values()
dict_values(['srinadh', 24, 7])
a.items()
dict_items([('name', 'srinadh'), ('age', 24), ('month', 7)])
a={"year":2026,"month":"july","date":}
SyntaxError: expression expected after dictionary key and ':'
a={"year":2026,"month":"july","date":14}
a.update({"time":2})
a
{'year': 2026, 'month': 'july', 'date': 14, 'time': 2}
a.update({"time":2},{"day":"tuesday"})
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.update({"time":2},{"day":"tuesday"})
TypeError: update expected at most 1 argument, got 2
a.update({"time":2,"day":"tuesday"})
a
{'year': 2026, 'month': 'july', 'date': 14, 'time': 2, 'day': 'tuesday'}
a={"name":"srinadh":"age":24}
SyntaxError: invalid syntax
a={"name":"srinadh","age":24}
a.setdefault("mail","meghasrinadh@gmail.com")
'meghasrinadh@gmail.com'
a
{'name': 'srinadh', 'age': 24, 'mail': 'meghasrinadh@gmail.com'}
a={"state":"ts","country":"india"}
a.pop()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("country")
'india'
a
{'state': 'ts'}
a.popitem()
('state', 'ts')
a
{}
a={"name":"srinadh","food":"biryani"}
a.copy()
{'name': 'srinadh', 'food': 'biryani'}
b=a.copy()
b
{'name': 'srinadh', 'food': 'biryani'}
a
{'name': 'srinadh', 'food': 'biryani'}
len(a)
2
#there is no count and index in dictonary and sets
a={"name":"srinadh","city":"ts","name":"srinadh"}
a
{'name': 'srinadh', 'city': 'ts'}
#the dict doesnot tale duplicate values
#but we can change the key values and take duplicate values
a={"name1":"srinadh","city":"ts","name2":"srinadh"}
>>> a
{'name1': 'srinadh', 'city': 'ts', 'name2': 'srinadh'}
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.count()
AttributeError: 'dict' object has no attribute 'count'
>>> a.index()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a.index()
AttributeError: 'dict' object has no attribute 'index'
>>> a.clear()
>>> a
{}
>>> a={}
>>> a.update({"name":"sriandh"})
>>> a
{'name': 'sriandh'}
>>> a={"idnos":[10,20,30],"names":["srinadh","kumar","kavith"],"marks":[60,70,80]}
>>> print(a)
{'idnos': [10, 20, 30], 'names': ['srinadh', 'kumar', 'kavith'], 'marks': [60, 70, 80]}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['idnos', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['srinadh', 'kumar', 'kavith'], [60, 70, 80]])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['srinadh', 'kumar', 'kavith']), ('marks', [60, 70, 80])])
>>> #only from keys remain
