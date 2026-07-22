#difference b/w break,continue&pass
#break   : is used to terminate the entire loop
#continue: continue is used to skips the current itteration and rest of the code will continue
#pass    : a pass is a nulll statment it does nothing but syntactically we need 

#break
#1
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==6:
        break'''

#2
'''a=20
while a>3:
    a=a-1
    if a==6:
        break
    print(a)'''

#3
'''for i in range(25):
    if i==24:
        break
    print(i)'''

#4
'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''

#continue

#1
'''a=30
while a>1:
    a=a-1
    if a==15:
        continue
    print(a)'''

#2
'''for i in range(15):
    if i==12:
        continue
    print(i)'''

#3
'''a="python"
for i in a:
    if i=="h":
        continue
    print(i)'''


#pass
#1
a=9
while a>2:
    print(a)
    a=a-1
    if a==7:
        pass

#2
for i in range(25)







