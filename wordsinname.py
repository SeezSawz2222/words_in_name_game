import random

a=['AMAZING','ANALYTICAL','ASSERTIVE','ASTONISHING','AUTHENTIC']
b=[' BENEFICENT','BLASTING','BELIEVER','BEAUTEOUS','BOMBASTIC']
c=['CAREFUL','CHANGELESS','COLORFUL','CONFIDENT','CONSISTENT']
d=['DESIROUS','DELIGHTFUL','DISCOVERER','DUTIFUL','DYNAMIC']
e=['EMPATHETIC','ENCHANTING','ENTERTAINER','EXPERT','EXPENSIVE']
f=['FORGIVINGLY','FASTEST','FLAVORFUL','FAULTLESS','FLEXIBLE']
g=['GENEROUS','GLORIOUS','GOODHEARTED','GIST','GLEEFULLY']
h=['HARD-WORKING',' HERITRIX',' HOLY SPIRIT','HEROISM','HELPFUL']
i=['ICON','IMPRESSIVE',' INCREDIBLE','INTELLECTUAL','INTERESTING']
j=[' JAMMING','JOYSOME','JUST','JOCULAR','JEEZ']
k=['KAZAAM','KEEN',' KINGLY','KNOWLEDGEABLE','KOOKY']
l=['LEGEND',' LONG-LASTING','LAVISH','LUSTY',' LOYAL']
m='hhjhg'
n='nfsaf'
o='odfhdh'
p='pfdbfbc'
q='qcggfg'
r='rdfsdfds'
s='srt'
t='tdfdsfd'
u='udfgdsg'
v='vgdg'
w='wdsfdsfds'
x='xasfsaf'
y='ydgdsg'
z='zasfs'
print("enter your name")
aa=str(input())
aa=aa.lower()
for i in range(len(aa)):
    if aa[i]=='a':
        print('a= ',random.choice(a))
    elif aa[i]=='b':
        print('b= ',random.choice(b))
    elif aa[i]=='c':
        print('c= ',random.choice(c))
    elif aa[i]=='d':
        print('d= ',random.choice(d))
    elif aa[i]=='e':
        print('e= ',random.choice(e))
    elif aa[i]=='f':
        print('f= ',random.choice(f))
    elif aa[i]=='g':
        print('g= ',random.choice(g))
    elif aa[i]=='h':
        print('h= ',random.choice(h))
    elif aa[i]=='i':
        print('i= ',random.choice(i))
    elif aa[i]=='j':
        print('j= ',random.choice(j))
    elif aa[i]=='k':
        print('k= ',random.choice(k))
    elif aa[i]=='l':
        print('l= ',random.choice(l))
    elif aa[i]=='m':
        print('m= ',random.choice(m))
    elif aa[i]=='n':
        print('n= ',random.choice(n))
    elif aa[i]=='o':
        print('o= ',random.choice(o))
    elif aa[i]=='p':
        print('p= ',random.choice(p))
    elif aa[i]=='q':
        print('q= ',random.choice(q))
    elif aa[i]=='r':
        print('r= ',random.choice(r))
    elif aa[i]=='s':
        print('s= ',random.choice(s))
    elif aa[i]=='t':
        print('t= ',random.choice(t))
    elif aa[i]=='u':
        print('u= ',random.choice(u))
    elif aa[i]=='v':
        print('v= ',random.choice(v))
    elif aa[i]=='w':
        print('w= ',random.choice(w))
    elif aa[i]=='x':
        print('x= ',random.choice(x))
    elif aa[i]=='y':
        print('y= ',random.choice(y))
    elif aa[i]=='z':
        print('z= ',random.choice(z))
    else:
        print("error")
    i+=1

input()