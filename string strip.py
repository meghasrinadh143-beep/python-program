Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #strip
>>> 
>>> #lstrip(),rstrip()
>>> a="          srinadh"
>>> a.strip()
'srinadh'
>>> a.lstrip()
'srinadh'
>>> a.rstrip()
'          srinadh'
>>> a.lstrip()
'srinadh'
>>> #split()
>>> a="python java c c++"
>>> a.split()
['python', 'java', 'c', 'c++']
>>> b="cd flat cn dbms"
>>> b.split()
['cd', 'flat', 'cn', 'dbms']
>>> #join
>>> c="html","css","js","bs"
>>> "".join(c)
'htmlcssjsbs'
>>> " ".join(c)
'html css js bs'
>>> #concatination
>>> fname="megha"
>>> lname="srinadh"
>>> print(a+b)
python java c c++cd flat cn dbms
a="code"
b="gnan"
print(a+b)
codegnan
print(a+" "+b)
code gnan
fname="megha"
lname="srinadh"
print(fname+" "+lname)
megha srinadh
print(fname.title()+" "+lname.title())
Megha Srinadh
print((fnmae+" "+lname).title())
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print((fnmae+" "+lname).title())
NameError: name 'fnmae' is not defined. Did you mean: 'fname'?
print((fname+" "+lname).title())
Megha Srinadh
#formating
a=5
b=6
print(a+b)
11
print("the sum is",a+b)
the sum is 11
city="hyderabad"
print("city is ",city)
city is  hyderabad
#format()
a="srinadh"
b="lokanadh"

print("hello {}{}".format(a,b))
hello srinadhlokanadh
print("hello {} {}".format(a,b))
hello srinadh lokanadh
print("hello {} hello{}".format(a,b))
hello srinadh hellolokanadh
print("hello {} hello {}".format(a,b))
hello srinadh hello lokanadh
print("hello {}\nhello {}".format(a,b))
hello srinadh
hello lokanadh
#formating string(fstring)
a="sitha"
b="ram"
print(f"hello {a}{b}\")
      
SyntaxError: unterminated f-string literal (detected at line 1)
print(f"hello{a}{b}")
      
hellositharam
print(f"hello {a} {b}")
      
hello sitha ram
print(f"hello {a} hello {b}")
      
hello sitha hello ram
print(f"hello {a}\nhello {b}")
      
hello sitha
hello ram
