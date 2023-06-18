from itertools import *
##1
##def f(x,y,a):
##    return (2*x+3*y<a) or (x>y) or (y>24)
##for a in range(100,121):
##    if all(f(x,y,a)==1 for x in range(4000) for y in range(4000)):
##        print(a)

##2
##from itertools import *
##def f(x):
##    p = 25<=x<=30
##    q = 13<=x<=22
##    a = a1<=x<=a2
##    return (a <= p) or q
##Ox = [i/4 for i in range(12*4,31*4)]
##m = []
##for a1,a2 in combinations(Ox,2):
##    if all(f(x)==1 for x in Ox):
##        m.append(a2-a1)
##print(max(m))

##3
##def f(x,y):
##    return ((y*y<=a) <= (y<=10)) and ((x<=9) <= (x*x<a))
##for a in range(-100,1000):
##    if all(f(x,y)==1 for x in range(1000) for y in range(1000)):
##        print(a)

##4
##from itertools import *
##def f(x):
##    p = 15<=x<=39
##    q = 44<=x<=57
##    a = a1<=x<=a2
##    return (a <= p) or q
##Ox = [i/4 for i in range(14*4,58*4)]
##m = []
##for a1,a2 in combinations(Ox,2):
##    if all(f(x) for x in Ox):
##        m.append(a2-a1)
##print(max(m))

##5
##a = set()
##p = {2,4,6,8,10,12,14,16,18,20}
##q = {3,6,9,12,15,18,21,24,27,30}
##def f(x):
##    P = x in p
##    Q = x in q
##    A = x in a
##    return (P<=A) or ((not A) <= (not Q))
##for x in range(1000):
##    if f(x)==0:
##        a.add(x)
##print(len(a))

##6
##def f(x,y):
##    return ((x-20<a) and (10-y<a)) or ((x+4)*y>45)
##for a in range(21,23):
##    if all(f(x,y) for x in range(1,4000) for y in range(1,4000)):
##        print(a)

##7
##from itertools import *
##def f(x):
##    p = 10<=x<=32
##    q = 18<=x<=45
##    a = a1<=x<=a2
##    return (p and (not a)) <= (not q)
##Ox = [i/4 for i in range(9*4,46*4)]
##m = []
##for a1,a2 in combinations(Ox,2):
##    if all(f(x) for x in Ox):
##        m.append(a2-a1)
##print(min(m))

##8
####from itertools import *
####def f(x,y):
####    ax = a1<=x<=a2
####    ay = a1<=y<=a2
####    return (ax <= (x**2<=144)) and ((y**2 <=100) <= ay)
####Ox = [i/4 for i in range(-200,200)]
####m = []
####for a1,a2 in combinations(Ox,2):
####    if all(f(x/4,y/4) for x in range(-10,10) for y in range(-10,10)):
####        m.append(a2-a1)
####print(max(m))

##9
##a = set(range(1000))
##p = {2,4,6,8,10,12,14,16,18,20}
##q = {3,6,9,12,15,21,24,27,30}
##def f(x):
##    P = x in p
##    Q = x in q
##    A = x in a
##    return (A <= P) or ((not Q) <= (not A))
##for x in range(1000):
##    if f(x)==0:
##        a.remove(x)
##print(len(a))

##10
####a = set()
####def f(x):
####    P = x in {2,4,6,8,10,12,14,16,18,20}
####    Q = x in {3,6,9,12,15,21,24,27,30}
####    A = x in a
####    return (A <= P) or (Q <= (not A))
####for x in range(100000):
####    if f(x)==0:
####        a.add(x)
####print(a)

##1
##def f(x):
##    P = 25<=x<=36
##    Q = 28<=x<=55
##    A = a1<=x<=a2
##    return A or Q or (not P)
##Ox = [i/4 for i in range(24*4,56*4)]
##m = []
##for a1,a2 in combinations(Ox,2):
##    if all(f(x) for x in Ox):
##        m.append(a2-a1)
##print(min(m))

##2
##def f(x):
##    P = 15<=x<=39
##    Q = 19<=x<=57
##    A = a1<=x<=a2
##    return (not A) <= (P <= (not Q))
##Ox = [i/4 for i in range(14*4,58*4)]
##m = []
##for a1,a2 in combinations(Ox,2):
##    if all(f(x) for x in Ox):
##        m.append(a2-a1)
##print(min(m))

##3
##def f(x):
##    P = 3<=x<=18
##    Q = 12<=x<=32
##    A = a1<=x<=a2
##    return (P == Q) <= (not A)
##Ox = [i/4 for i in range(2*4,33*4)]
##m = []
##for a1,a2 in combinations(Ox,2):
##    if all(f(x) for x in Ox):
##        m.append(a2-a1)
##print(max(m))

##4
##a=set()
##def f(x):
##    P = x in {1,2,3,4,5,6}
##    Q = x in {3,5,15}
##    A = x in a
##    return (not A) <= (((not P) and Q) or (not Q))
##for x in range(1000):
##    if f(x)==0: a.add(x)
##print(len(a))

##5
##a = set()
##def f(x):
##    P = x in {1,3,5,7,9,11,13,15,17,19,21}
##    Q = x in {3,6,9,12,15,21,24,27,30}
##    A = x in a
##    return (A <= P) or ((not Q) <= (not A))
##for x in range(1000):
##    if f(x)==0: a.add(x)
##print(len(a))

##6
##a = set()
##def f(x):
##    P = x in {2,4,6,8,10,12}
##    Q = x in {3,6,9,12,15}
##    A = x in a
##    return (not P) <= ((Q and (not A)) <= P)
##for x in range(1000):
##    if f(x)==0: a.add(x)
##print(len(a))

##7
##def f(x,y): return (x>16) or (y>25) or (a>x+y)
##for a in range(100):
##    if all(f(x,y) for x in range(1000) for y in range(1000)):
##        print(a)

##8
##def f(x): return (x&85==0) <= ((x&54!=0) <= (x&a!=0))
##for a in range(100):
##    if all(f(x) for x in range(10000)):
##        print(a)

##9
##def f(x): return (x&a==0) and (x&58!=0) and (x&22==0)
##for a in range(1,100):
##    if all(f(x)==0 for x in range(1,10000)):
##        print(a)

##10
##def f(x): return ((x&35!=0) or (x&23!=0)) <= ((x&26!=0) or (x&a==0))
##for a in range(1,100):
##    if all(f(x) for x in range(10000)):
##        print(a)

##11
##def f(x): return (x%a!=0) <= ((x%6==0) <= (x%9!=0))
##for a in range(1,100):
##    if all(f(x) for x in range(1,10000)):
##        print(a)

##12
##def f(x): return (70%a==0) and ((x%a!=0) <= ((x%18==0) <= (x%42!=0)))
##for a in range(1,1000):
##    if all(f(x) for x in range(1,10000)):
##        print(a)

##13
##def f(x): return (70%a==0) and ((x%a!=0) <= ((x%18==0) <= (x%42!=0)))
##for a in range(1,1000):
##    if all(f(x) for x in range(10000)):
##        print(a)

##1
##def t(a,b,c):
##    a,b,c=sorted([a,b,c])
##    return a+b>c
##def f(x): return t(x,20,45) or t(x,15,50) or t(max(x,16),36,a) or (x>75)
##for a in range(1,1000):
##    if all(f(x) for x in range(1,10000)):
##        print(a)

##5
##def f(x,y): return (6*x+8*y != 128) or (x<y) or (3*y<a)
##for a in range(-100,100):
##    if all(f(x,y) for x in range(2000) for y in range(2000)):
##        print(a)

##6
##def f(x,y): return (x*y>a) or (27>y) or (y-20>=a) or (x<8)
##for a in range(1000,1,-1):
##    if all(f(x,y) for x in range(2000) for y in range(2000)):
##        print(a)

##7
##def f(x):
##    P = 2<=x<=95
##    Q = 20<=x<=44
##    A = a1<=x<=a2
##    return Q <= (((not P) and Q) <= A)
##Ox = [i/4 for i in range(4,96*4)]
##m =[]
##for a1,a2 in combinations(Ox,2):
##    if all(f(x) for x in Ox):
##        m.append(a2-a1)
##print(min(m))

##8
####def f(x):
####    P = 2212598<=x<=7215678
####    Q = 4200000<=x<=10202053
####    A = a1<=x<=a2
####    return (not ((not A) and P)) or Q
####Ox = [i/3 for i in range(2212597*3, 10202054*3)]
####m = []
####for a1,a2 in combinations(Ox,2):
####    if all(f(x) for x in Ox):
####        m.append(a2-a1)
####print(min(m))

##9
##def f(x):
##    P = 12<=x<=56
##    Q = 30<=x<=85
##    A = a1<=x<=a2
##    return (P <= (not Q)) or A
##Ox = [i/3 for i in range(11*3,86*3)]
##m=[]
##for a1,a2 in combinations(Ox,2):
##    if all(f(x) for x in Ox):
##        m.append(a2-a1)
##print(min(m))

##10
##a=set()
##def f(x):
##    P = x in {2,4,8,12,15}
##    Q = x in {3,6,8,15}
##    A = x in a
##    return P <= ((not Q) or A)
##for x in range(1000):
##    if f(x)==0: a.add(x)
##print(len(a))

##11
##a = set()
##def f(x):
##    P = x in {2,4,6,8,10,12}
##    Q = x in {3,6,9,12,15}
##    A = x in a
##    return P <= ((Q and (not A)) <= (not P))
##for x in range(1000):
##    if f(x)==0: a.add(x)
##print(a)

##12
##a = set()
##def f(x):
##    P = x not in {2,4,6,8,10,12}
##    Q = x in {3,6,9,12,15}
##    A = x not in a
##    return P or ((Q and A) <= P)
##for x in range(1000):
##    if f(x)==0: a.add(x)
##print(len(a))

##13
##def f(x): return (((x%a==0) and (x%36==0)) <= (x%324==0)) and (a>100)
##for a in range(1,1000):
##    if all(f(x) for x in range(1,100000)):
##        print(a)

##14
##def f(x): return (45%a==0) and (((x%30==0) and (x%12==0)) <= (x%a==0))
##for a in range(1000,1,-1):
##    if all(f(x) for x in range(1,10000)):
##        print(a)

##15
##def f(x,y): return ((x*y)%a!=0) or (y>4095) or (x>2*y+1) or (y%2!=0) or (x%2==0)
##for a in range(1,10000):
##    if all(f(x,y) for x in range(1,1000) for y in range(1,1000)):
##        print(a)

##16
##def f(x): return (x&38==0) <= ((x&55!=0) <= (x&a!=0))
##for a in range(0,100):
##    if all(f(x) for x in range(10000)):
##        print(a)

##17
##def f(x): return (x&a!=0) <= ((x&25==0) <= (x&17!=0))
##for a in range(10000,1,-1):
##    if all(f(x) for x in range(10000)):
##        print(a)

##18
##def f(x): return (x&a==0) or ((x&74==0) <= (x&65!=0))
##for a in range(10000,1,-1):
##    if all(f(x) for x in range(10000)):
##        print(a)

##1
##def f(x):
##    P = 15<=x<=50
##    Q = 35<=x<=60
##    A = a1<=x<=a2
##    return ((not A) <= P) <= (A <= Q)
##Ox = [i/3 for i in range(14*3,61*3)]
##m=[]
##for a1,a2 in combinations(Ox,2):
##    if all(f(x) for x in Ox):
##        m.append(a2-a1)
##print(max(m))

##2
##def f(x):
##    P = 10<=x<=17
##    Q = 15<=x<=25
##    A = a1<=x<=a2
##    return P <= ((Q and (not A)) <= (not P))
##Ox = [i/3 for i in range(9*3,26*3)]
##m = []
##for a1,a2 in combinations(Ox,2):
##    if all(f(x) for x in Ox):
##        m.append(a2-a1)
##print(min(m))

##3
##def f(x): return ((x%34==0) and (x%51!=0)) <= ((x%a!=0) or (x%51==0))
##for a in range(1,1000):
##    if all(f(x) for x in range(1,10000)):
##        print(a)

##4
##def f(x): return (70%a==0) and ((x%28==0) <= ((x%a!=0) <= (x%21!=0)))
##for a in range(1000,1,-1):
##    if all(f(x) for x in range(1,10000)):
##        print(a)

##5
##a = set(range(1000))
##def f(x):
##    P = x in {2,4,6,8,10,12,14,16,18,20}
##    Q = x in {5,10,15,20,25,30,35,40,45,50}
##    A = x in a
##    return (A <= P) or ((not Q) <= (not A))
##for x in range(1000):
##    if f(x)==0: a.remove(x)
##print(len(a))

##6
##a=set()
##def f(x):
##    P = x in {2,4,6,8,10,12,14,16,18,20}
##    Q = x in {3,6,9,12,15,21,24,27,30}
##    A = x in a
##    return ((not A) <= P) or (Q <= A)
##for x in range(1000):
##    if f(x)==0: a.add(x)
##print(len(a))

##7
##def f(x,y): return (5*x+2*y!=85) or (a<=x) or (x<=y)
##for a in range(1000,1,-1):
##    if all(f(x,y) for x in range(1000) for y in range(1000)):
##        print(a)

##8
##def f(x): return (x<a) or (x<20) or (x>30)
##for a in range(1,1000):
##    if all(f(x) for x in range(10000)):
##        print(a)

##1
##def f(x,y): return (x<a) or (y<a) or ((x*y)%3==0) or (4*x+2*y!=150)
##for a in range(-100,100):
##    if all(f(x,y) for x in range(1000) for y in range(1000)):
##        print(a)

##2
##def f(x): return ((x%5==0) and (x%11==0)) <= ((x&17!=0) or (x&64==0) or (a*x<=190387))
##for a in range(1000,1,-1):
##    if all(f(x) for x in range(-1000,1000)):
##        print(a)

##3
##def f(x):
##    Q = 16<=x<=64
##    P = 48<=x<=96
##    return (x%10==0) or (not Q) or (x&a==0) or (P <= (abs(x-30)>=20))
##for a in range(1,100):
##    if all(f(x) for x in range(-1000,1000)):
##        print(a)

##4
##def f(x):
##    Q = 8<=x<=48
##    S = x in {43,23,76}
##    return ((x%5!=0) and (not S)) <= ((abs(x-40) <= 11) <= Q) or (x&a==0)
##for a in range(1,100):
##    if all(f(x) for x in range(-1000,1000)):
##        print(a)

##9
##def f(x): return (a%12==0) and ((530%x==0) <= ((not (a%x==0)) <= (not (170%x==0))))
##for a in range(1,100):
##    if all(f(x) for x in range(1,10000)):
##        print(a)

##10
##def f(x): return ((not (x%a==0)) and (x%15==0)) <= ((not (x%18==0)) or (not (x%15==0)))
##for a in range(1000,1,-1):
##    if all(f(x) for x in range(1,10000)):
##        print(a)

##11
##def f(x,y): return (x*y>a) and (x>y) and (x<8)
##for a in range(-100,1000):
##    if all(f(x,y)==0 for x in range(1,1000) for y in range(1,1000)):
##        print(a)

##12
##def f(x): return (x&a!=0) <=((x&14==0) <= (x&75!=0))
##for a in range(1000,1,-1):
##    if all(f(x) for x in range(1,10000)):
##        print(a)

##13
##def f(x): return (((x&13!=0) or (x&a!=0)) <= (x &13!=0)) or ((x&a!=0) and (x&39==0))
##for a in range(1000,1,-1):
##    if all(f(x) for x in range(1,10000)):
##        print(a)

##14
##def f(x,y): return (x>=7) or (2*x<y) or (x*y<a)
##for a in range(1000):
##    if all(f(x,y) for x in range(1000) for y in range(1000)):
##        print(a)

##15
##def f(x): return ((x&28!=0) or (x&45!=0)) <= ((x&17==0) <= (x&a!=0))
##for a in range(1,1000):
##    if all(f(x) for x in range(1,10000)):
##        print(a)

##16
##def f(x): return ((x%19!=0) or (x%13!=0)) <= (x%a!=0)
##for a in range(1,1000):
##    if all(f(x) for x in range(1,10000)):
##        print(a)











