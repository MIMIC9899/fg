##11
##def div(x):
##    d = set()
##    for i in range(1,int(x**0.5)+1):
##        if x%i==0:
##            d |= {i,x//i}
##    return sorted(d)
##m=0
##for x in range(64032,64131):
##    d = div(x)
##    m = max(m,len(d))
##for x in range(64032,64131):
##    d = div(x)
##    if len(d)==m: print(x,m)

##12
##def div(x):
##    d = set()
##    for i in range(1,int(x**0.5)+1):
##        if x%i==0: d |= {i,x//i}
##    return sorted(d)
##for x in range(2410000,2410101):
##    d = div(x)
##    if len(d)==2: print(x,end=' ')

##14
##def div(x):
##    d = set()
##    for i in range(2,int(x**0.5)+1):
##        if x%i==0: d|= {i,x//i}
##    return sorted(d)
##for x in range(500001,1000000):
##    d = div(x)
##    for i in d:
##        if i%10==8 and i!=8:
##            print(x,i)
##            break

##15
####def div(x):
####    d = set()
####    for i in range(1,int(x**0.5)+1,2):
####        if x%i==0: d|= {i,x//i if (x//i)%2==1 else 1}
####    return sorted(d)
####for x in range(50000000,60000001):
####    d = div(x)
####    if len(d)==5: print(x,d)

##16
##def div(x):
##    d = set()
##    for i in range(2,int(x**0.5)+1):
##        if x%i==0: d|= {i,x//i}
##    return sorted(d)
##for x in range(110000,250001):
##    d =div(x)
##    if len(d)==3: print(d[2], end=' ')

##17
##def div(x):
##    d = set()
##    for i in range(2,int(x**0.5)+1):
##        if x%i==0: d |= {i,x//i}
##    return sorted(d)
##for x in range(14327,30123):
##    d = div(x)
##    if len(d)==3: print(d[2],end=' ')

##18
##def div(x):
##    d = set()
##    for i in range(2,int(x**0.5)+1):
##        if x%i==0: d |= {i,x//i}
##    return sorted(d)
##for x in range(21514,30102):
##    d =div(x)
##    if len(d)==3: print(d[0],d[2])

##19
from fnmatch import *
##for x in range(0,10**6,61):
##    if fnmatch(str(x),'31*2?9*'):
##        print(x)

##20
##for x in range(0,10**7,387):
##    if fnmatch(str(x),'*16*9?0?'): print(x)

##1
##def div(x):
##    d = set()
##    for i in range(2,int(x**0.5)+1):
##        if x%i==0: d|={i,x//i}
##    return sorted(d)
##c=0
##for x in range(100010,321342):
##    if len(div(x))==3:c+=1
##print(c)

##2
##def div(x):
##    d = set()
##    for i in range(1,int(x**0.5)+1):
##        if x%i==0: d|={i,x//i}
##    return sorted(d)
##m=0
##for x in range(101010112,101000000,-16):
##    if len(div(x))==128:
##        m=max(m,x)
##print(m)
##q = div(m)
##print(*[i for i in q if i%2==1])

##3
##def div(x):
##    d =set()
##    for i in range(1,int(x**0.5)+1):
##        if x%i==0: d|={i,x//i}
##    return sorted(d)
##pr = [i for i in range(400000) if len(div(i))<=3]
##print('1')
##for x in range(156239,400000):
##    q=div(x)
##    if len(q)==60:
##        c=0
##        for i in q:
##            if i in pr:
##                c+=1
##        if c==4: print(q)

##1
##for x in range(0,10000):
##    x=str(x)
##    if fnmatch(x,'123?') and (int(x[0])+int(x[1])+int(x[2])+int(x[3]))%3==0:
##        x=int(x)
##        print(x,x//3)

##2
##for x in range(0,10**8,434343):
##    if fnmatch(str(x),'???1??1?'):
##        print(x,x//434343)

##3
##c=0
####for x in range(10**9):
####    if fnmatch(str(x),'1*23?34'):
####        if sum(int(i) for i in str(x))%9==0:
####            c+=1
####            print('0')
####print(c)
##for c1 in '0123456789':
##    a=int(f'123{c1}34')
##    if sum(int(i) for i in str(a))%9==0: c+=1
##for c1 in '0123456789':
##    for c2 in '0123456789':
##        a=int(f'1{c2}23{c1}34')
##        if sum(int(i) for i in str(a))%9==0: c+=1
##for c1 in '0123456789':
##    for c2 in '0123456789':
##        for c3 in '0123456789':
##            a=int(f'1{c2}{c3}23{c1}34')
##            if sum(int(i) for i in str(a))%9==0: c+=1
##for c1 in '0123456789':
##    for c2 in '0123456789':
##        for c3 in '0123456789':
##            for c4 in '0123456789':
##                a=int(f'1{c2}{c3}{c4}23{c1}34')
##                if sum(int(i) for i in str(a))%9==0: c+=1
##print(c)

##4
c=0
def div(x):
    d =set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0: d|={i,x//i}
    return sorted(d)
####for x in range(10**8):
####    if fnmatch(str(x),'123?654?'):
####        s = sum(div(x))
####        su = sum(int(i) for i in str(s))
####        s1= sum(int(i) for i in str(s)[1::2])
####        s2= sum(int(i) for i in str(s)[::2])
####        if abs(s1-s2)%11==0 and su%9==0: c+=1
####print(c)
##for c1 in '0123456789':
##    for c2 in '0123456789':
##        a = int(f'123{c1}654{c2}')
##        s = sum(div(a))
##        su = sum(int(i) for i in str(s))
##        s1= sum(int(i) for i in str(s)[1::2])
##        s2= sum(int(i) for i in str(s)[::2])
##        if abs(s1-s2)%11==0 and su%9==0: c+=1
##print(c)

##5
####c=0
####for x in range(10110,10**6):
####    if fnmatch(str(x),'?????'):
####        try:
####            if x%(int(str(x)[2:4]))==0:
####                c+=1
####        except:pass
####print(c)

##6
##for x in range(0,10**9,21):
##    if fnmatch(str(x),'12345?7?8'):print(x,x//21)


