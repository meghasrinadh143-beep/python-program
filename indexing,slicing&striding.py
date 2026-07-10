Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="i am in class"
a[8,9,0,11,12]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a[8,9,0,11,12]
TypeError: string indices must be integers, not 'tuple'
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[2]+a[3]
'am'
a[5]+a[6]
'in'
a[1]
' '
a[1]+a[4]+a[7]
'   '
b="I am learning pyhton"
a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
IndexError: string index out of range
a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
IndexError: string index out of range
b[15]+b[16]+b[17]+b[18]+b[19]+b[20]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b[15]+b[16]+b[17]+b[18]+b[19]+b[20]
IndexError: string index out of range
b="i am learning python"
b[15]+b[16]+b[17]+b[18]+b[19]+b[20]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    b[15]+b[16]+b[17]+b[18]+b[19]+b[20]
IndexError: string index out of range
b[14]+b[15]+b[16]+b[17]+b[18]+b[19]
'python'
b[5]+b[6]+b[7]+b[8]
'lear'
b[5]+b[6]+b[7]+b[8]+b[9]
'learn'
c="i love codegnan"
c[7]+c[8]+c[9]+c[10]
'code'
c[11]+c[12]+c[13]+c[14]
'gnan'
c[2]+c[3]+c[4]c[5]
SyntaxError: invalid syntax
c[2]+c[3]+c[4]+c[5]
'love'
d="vijayawada is a royal city"
d[-6]+d[-7]+d[-8]+d[-9]+d[-10]
'layor'
d[-10]+d[-9]+d[-8]+d[-7]+d[-6]
'royal'
d[-1]+d[-2]+d[-3]+d[-4]
'ytic'
KeyboardInterrupt
d[-4]+d[-3]+d[-2]+d[-1]
'city'
d[-14]+d[-13]
's '
d[-15]+d[-14]
'is'
e="vizag is a city of destiny"
e[-7]+e[-6]+e[-5]+e[-4]+e[-3]+e[-2]+e[-1]
'destiny'
e[-15]+e[-14]+e[-13]+e[-12]
'city'
e[-26]+e[-25]+e[-24]+e[-23]+e[-22]
'vizag'
#sliccing
f="codegnan"
a[0:4]
'i am'
f="codegnan"
f[0:4]
'code'
f[4:8]
'gnan'
f[:4]
'code'
f[4:]
'gnan'
g="work util you succeed"
g[:4]
'work'
g[5:11]
'util y'
g[5:10]
'util '
g="work until you succeed"
g[:4]
'work'
g[6:10]
'ntil'
g[5:10]
'until'
g[14:]
' succeed'
g[15:]
'succeed'
g[11:15]
'you '
g[11:14]
'you'
h="time is very precious"
h[13:20]
'preciou'
h[13:21]
'precious'
h[8:12]
'very'
b[:4]
'i am'
h[:4]
'time'
i="simple is better then complex"
i[19:13]
''
i[19:13]
''
i[19:12]
''
h="simple is better than complex"
h[20:13]
''
h[:-7]
'simple is better than '
h[-20:-13]
' better'
h[-19:-13]
'better'
h[:-23]
'simple'
h[-7:]
'complex'
k="codegnan it solutions"
k[:-13]
'codegnan'
k[-9:]
'solutions'
#strading
#
=
#+ve strading
>>> l="Data science"
>>> l[::]
'Data science'
>>> l[::1]
'Data science'
>>> l[::2]
'Dt cec'
>>> m="machine learning"
>>> m[::4]
'miln'
>>> m[::7]
'm n'
>>> m[::2]
'mcielann'
>>> m[2:8]
'chine '
>>> m[:9]
'machine l'
>>> m[7:]
' learning'
>>> n="cloud computhin"
>>> n[1:12:3]
'ldou'
>>> n[-4:-14:-4]
'tou'
>>> n[-6:-10:-1]
'pmoc'
>>> n[-2:-13:-5]
'imu'
>>> n[4:14:4]
'dmh'
