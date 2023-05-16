##def f(x,a):
##    return ((x%a==0) and (x%36!=0)) <= (x%12!=0)
##
##for a in range(1,1000):
##    if all(f(x,a)==1 for x in range(1,10001)):
##        print(a)
    
##def f(x,a):
##    return (x&56!=0)<=((x&48==0)<=(x&a!=0))
##for a in range(1,100):
##    if all(f(x,a) for x in range(1,10001)):
##        print(a)

##def f(x,y,a):
##    return (x<a) and (y<a) and (x*y>1200)
##
##for a in range(1,100):
##    if all(f(x,y,a)==0 for x in range(1,100) for y in range(1,100)):
##        print(a)

##p={1,3,5,7,9,11}
##q={3,6,9,12}
##a=set()
##def f(x):
##    return ((x in p) <= (x not in q)) or (x in a)
##for x in range(1,1000):
##    if f(x)==0:
##        a.add(x)
##print(a)

##p={2,4,6,8,10,12,14,16,18,20}
##q={5,10,15,20,25,30,35,40,45,50}
##a=set(range(1,1000))
##def f(x):
##    return ((x in a) <= (x in p)) and ((x in q) <= (x not in a))
##for x in range(1,1000):
##    if f(x)==0:
##        a.remove(x)
##print(a)

####def p(x): return 430<=x<=490
####def q(x): return 440<=x<=530
##def f(x,a1,a2):
##    return ((a1<=x<=a2) <= (430<=x<=490)) or (440<=x<=530)
##m=0
##for a1 in range(400,600):
##    for a2 in range(a1+1,600):
##        if all(f(x,a1,a2)==1 for x in range(400,600)):
##            m = max(m, a2-a1)
##print(m/10)

##def p(x): return 150<=x<=390
##def q(x): return 440<=x<=570
##def f(x,a1,a2):
##    return (p(x) <= (a1<=x<=a2)) and (q(x) <= (a1<=x<=a2))
##m=10**8
##for a1 in range(100,600):
##    for a2 in range(a1+1,600):
##        if all(f(x,a1,a2)==1 for x in range(100,600)):
##            m = min(m, a2-a1)
##print(m/10)

##for a in range(1,1000):
##    f=1
##    for x in range(1,10000):
##        s = (a%9==0) and ((280%x==0)<=((a%x!=0)<=(730%x!=0)))
##        if s==0:
##            f=0
##            break
##    if f ==1:
##        print(a)

##for a in range(1,100):
##    for x in range(1,10000):
##        s = ((x%34==0) and (x%51!=0)) <= ((x%a!=0) or (x%51==0))
##        if s==0:
##            break
##    else:
##        print(a)

##def f(x): return ((x%a==0) and (x%24==0) and (x%16!=0)) <= (x%a!=0)
##
##for a in range(1,100):
##    if all(f(x)==1 for x in range(1,10000)):
##        print(a)

##def f(x): return ((x%84!=0) or (x%90!=0)) <= (x%a!=0)
##
##for a in range(1,10000):
##    if all(f(x)==1 for x in range(1,1000000)):
##        print(a)
##        break

##def f(x): return ((x%15==0) and (x%21!=0)) <= ((x%a!=0) or (x%15!=0))
##
##for a in range(1,100):
##    if all(f(x)==1 for x in range(1,10000)):
##        print(a)

##def f(x): return ((x%4!=3) or (x%6!=1)) <= (x%36!=a)
##
##for a in range(1,100):
##    if all(f(x)==1 for x in range(1,10000)):
##        print(a)

##def f(x): return (a%7==0) and ((240%x==0) <= ((a%x!=0) <= (780%x!=0)))
##
##for a in range(1,1000):
##    if all(f(x)==1 for x in range(1,100000)):
##        print(a)

##def f(x): return (x&41==0) <= ((x&119!=0) <= (x&a!=0))
##
##for a in range(1,100):
##    if all(f(x) for x in range(1,10000)):
##        print(a)

##def f(x): return (((x&13!=0) or (x&a!=0)) <= (x&13!=0)) or ((x&a!=0) and (x&39==0))
##
##for a in range(1,1000):
##    if all(f(x) for x in range(1,100000)):
##        print(a) 

##def f(x): return ((x&17!=0) <= ((x&a!=0) <= (x&58!=0))) <= ((x&8==0) and (x&a!=0) and (x&58==0))
##
##for a in range(1,1000):
##    if all(f(x)==0 for x in range(1,100000)):
##        print(a) 

##def f(x,y): return (y+3*x<a)or(x>20)or(y>40)
##
##for a in range(1,200):
##    if all(f(x,y) for x in range(1,100) for y in range(1,100)):
##        print(a)

##def f(x,y): return (2*y+3*x<a) or (x+y>40)
##
##for a in range(1,200):
##    if all(f(x,y) for x in range(0,100) for y in range(0,100)):
##        print(a)

##def f(x,y,z): return (220!=y+2*x+z) or (a < 6*x) or (a <y) or (a < 2*z)
##
##for a in range(100,200):
##    if all(f(x,y,z) for x in range(150) for y in range(150) for z in range(150)):
##        print(a)

##k=0
##for x in range(100):
##    for y in range(100):
##        f = not(((x>6) and ((x+y)>=5)) or (y>=5))
##        if f:
##            k+=1
##print(k)

##def f(x): return ((x&26!=0) or (x&13!=0)) <= ((x&29==0) <= (x&a!=0))
##
##for a in range(1,100):
##    if all(f(x) for x in range(1,10000)):
##        print(a)

##def f(x): return (((x&13!=0) or (x&a!=0)) <= (x&13!=0)) or ((x&a!=0) and (x&39==0))
##
##for a in range(1,100):
##    if all(f(x) for x in range(1,10000)):
##        print(a)

##def f(x): return (x&107 ==0) <= ((x&55!=0) <= (x&a!=0))
##
##for a in range(1,100):
##    if all(f(x) for x in range(1,10000)):
##        print(a)

##def f(x,y): return (x*y>a) and (x>y) and(x<8)
##
##for a in range(1,100):
##    if all(f(x,y)==0 for x in range(1,1000) for y in range(1,1000)):
##        print(a)

##def f(x,y): return (x>39) or (y>26) or (2*x+4*y<a)
##
##for a in range(1,1000):
##    if all(f(x,y)==1 for x in range(1,1000) for y in range(1,1000)):
##        print(a)

##def f(x,y): return (2*x+y!=70) or (x<y) or(a<x)
##
##for a in range(1,10000):
##    if all(f(x,y)==1 for x in range(1000) for y in range(1000)):
##        print(a)

##def f(x,y): return (x**2 - 10*x + 16 >0) or (y**2-10*y+21>0) or (x*y<2*a)
##
##for a in range(1,1000):
##    if all(f(x,y)==1 for x in range(1,1000) for y in range(1,1000)):
##        print(a)

##a = set()
##b = {2,4,6,8,10,12}
##c = {3,6,9,12,15}
##
##def f(x):
##    A=x in a
##    B=x in b
##    C=x in c
##    return B <= ((C and (not A)) <= (not B))
##
##for x in range(1000):
##    if f(x)==0:
##        a.add(x)
##print(a)

##a = set()
##
##def f(x):
##    A=x in a
##    B=x in {2,4,6,8,10,12}
##    C=x in {3,6,9,12,15}
##    return (not B) or ((not C) <= A)
##
##for x in range(1000):
##    if f(x)==0:
##        a.add(x)
##print(a)

##a = set(range(1000))
##
##def f(x):
##    A= x in a
##    P=x in {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
##    Q=x in {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
##    return (A<=P) and (Q<=(not A))
##
##for x in range(1000):
##    if f(x)==0:
##        a.remove(x)
##print(len(a))

##from itertools import *
##b=[''.join(i) for i in product('01', repeat=8)]
##
##a = set()
##p = {i for i in b if i[0]+i[1]=='11'}
##q = {i for i in b if i[-1]=='0'}
##
##def f(x):
##    A = x in a
##    P = x in p
##    Q = x in q
##    return (not A) <= (P or (not Q))
##
##for x in b:
##    if f(x)==0:
##        a.add(x)
##print(len(a))

##a = set()
##
##def f(x):
##    A=x in a
##    B=x in {1,3,5,7,9,11}
##    C=x in {3,6,9,12}
##    return (B <= (not C)) or A
##
##for x in range(1000):
##    if f(x)==0:
##        a.add(x)
##print(a)

##a = set()
##
##def f(x):
##    A=x in a
##    B=x in {3,6,9,12}
##    C=x in {1,2,3,4,5,6}
##    return (not ((not A) and B)) or (not C)
##
##for x in range(1000):
##    if f(x)==0:
##        a.add(x)
##print(len(a))

##a = set(range(1000))
##
##def f(x):
##    A= x in a
##    P= x in {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
##    Q= x in {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
##    return (A <= P) and (Q <= (not A))
##
##for x in range(10000):
##    if f(x)==0:
##        a.remove(x)
##print(a)

##a = set()
##
##def f(x):
##    A= x not in a
##    P= x in {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
##    Q= x in {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
##    R =x in {12, 24, 36, 48, 60}
##    return A <= ((P and Q) <= R)
##
##for x in range(10000):
##    if f(x)==0:
##        a.add(x)
##print(a)

##from itertools import *
##
##def f(x):
##    P = 25<=x<=50
##    Q = 54<=x<=75
##    A = a1<=x<=a2
##    return Q <= ((P == Q) or ((not P) <=A))
##
##Ox = [i/4 for i in range(24*4,76*4)]
##m =[]
##
##for a1,a2 in combinations(Ox,2):
##    if all(f(x)==1 for x in Ox):
##        m.append(a2-a1)
##print(min(m))

##from itertools import *
##
##def f(x):
##    P = 25<=x<=37
##    Q = 32<=x<=50
##    A = a1<=x<=a2
##    return (A and (not Q)) <= (P or Q)
##
##Ox = [i/4 for i in range(24*4,51*4)]
##m =[]
##for a1,a2 in combinations(Ox, 2):
##    if all(f(x)==1 for x in Ox):
##        m.append(a2-a1)
##print(max(m))

##from itertools import *
##
##def f(x):
##    P = 5<=x<=100
##    Q = 15<=x<=25
##    R = 35<=x<=50
##    A = a1<=x<=a2
##    return (P <= Q) or ((not A) <= R)
##
##Ox = [i/4 for i in range(4*4,101*4)]
##m =[]
##for a1,a2 in combinations(Ox, 2):
##    if all(f(x)==1 for x in Ox):
##        m.append(a2-a1)
##print(min(m))

##from itertools import *
##
##def f(x):
##    P = 1<=x<=98
##    Q = 25<=x<=42
##    A = a1<=x<=a2
##    return Q <= (((not P) and Q) <= A)
##
##Ox = [i/3 for i in range(0*3,99*3)]
##m =[]
##for a1,a2 in combinations(Ox, 2):
##    if all(f(x)==1 for x in Ox):
##        m.append(a2-a1)
##print(round(min(m)))

##from itertools import *
##
##def f(x):
##    D = 17<=x<=58
##    C = 29<=x<=80
##    A = a1<=x<=a2
##    return D <= (((not C) and (not A)) <= (not D))
##
##Ox = [i/4 for i in range(16*4,81*4+1)]
##m =[]
##
##for a1,a2 in combinations(Ox, 2):
##    if all(f(x)==1 for x in Ox):
##        m.append(a2-a1)
##print(min(m))

##from itertools import *
##
##def f(x):
##    P = 17<=x<=54
##    Q = 37<=x<=83
##    A = a1<=x<=a2
##    return P <= ((Q and (not A)) <= (not P))
##
##Ox = [i/4 for i in range(16*4,84*4+1)]
##m =[]
##
##for a1,a2 in combinations(Ox, 2):
##    if all(f(x)==1 for x in Ox):
##        m.append(a2-a1)
##print(min(m))

from itertools import *

def f(x):
    B=18<=x<=52
    C=16<=x<=41
    A= a1<=x<=a2
    return (B <= A) and ((not C) or A)

Ox = [i/4 for i in range(15*4,53*4+1)]
m=[]
for a1,a2 in combinations(Ox,2):
    if all(f(x)==1 for x in Ox):
        m.append(a2-a1)
print(min(m))





























