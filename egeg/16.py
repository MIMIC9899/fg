##1
##from itertools import *
##k=0
##for x in product('НАГКИ', repeat=5):
##    s=''.join(x)
##    k+=1
##    if s=='КНИГА':
##        print(k,s)

##2
##n=int('11',13)
##a=[]
##while n>0:
##    a = [n%4] + a
##    n//=4
##print(a)

##3
##s=12**16+12**22-78
##a=[]
##while s>0:
##    a = [s%12]+a
##    s//=12
##print(a.count(0))

##4
##n = 16**5+8**5-4**2+2**9-535
##b = bin(n)[2:]
##print(b.count('0'))

##5
##n = 5**257+8**837+4**13
##a=[]
##while n>0:
##    a = [n%9]+a
##    n//=9
##print(a.count(8))

##6
##n = 8**2020+4**2017+26-1
##b = bin(n)[2:]
##print(b.count('0'))

##7
##n= (66+6**2019)*6**2019+66+6**6
##a=[]
##while n>0:
##    a = [n%6]+a
##    n//=6
##print(sum(a))

##8
####n=36**8*6**2*35+6**20*6**2*35-12*6**2*35+15
####print(n)
####a=[]
####while n>0:
####    a = [n%6]+a
####    n//=6
####print(a)

##9
##for x in range(0,5):
##    s = int(f'5{x}46',7)+int(f'12{x}1',5)
##    if s%7==0:
##        s1=s
##print(s1/7)

##10
##for x in '0123456789abcdef':
##    s = int(f'1587{x}99',16)+int(f'1{x}048',16)
##    if s%13==0:
##        print(x)

##11
##for x in range(2,30):
##    a=[]
##    n=6561
##    while n>0:
##        a = [n%x]+a
##        n//=x
##    print(x,a)

##12
##for x in range(2,30):
##    n=62
##    a=[]
##    while n>0:
##        a=[n%x]+a
##        n//=x
##    print(a)

##13
##for x in range(200):
##    s = int('11',5) + x == int('323',4)
##    if s==True:
##        print(x)

##14
##for x in range(2,30):
##    try:
##        s = int('246',9) == int('129',x)
##        if s:
##            print(x)
##    except: pass
    
##15
##for x in range(-10000,20000):
##    s = int('30',4)*x**2+int('20',3)*x ==0
##    if s:
##        print(x)

##16
##for x in range(-100,100):
##    for y in range(-100,100):
##        s = int('1000',2)*y+int('100',3)*x == int('112',5)
##        s2 = int('100',4)-x == int('22',3)
##        if s==True and s2==True:
##            print(x,y)

##9
##s = 16**231+4**120-2**50
##b = bin(s)[2:]
##print(b.count('1'))

##10
##s = 81**100-3**200-3**50+2
##a=[]
##while s>0:
##    a = [s%3]+a
##    s//=3
##print(a.count(2))

##11
##n = 2*64**123-8**98+111
##o = oct(n)[2:]
##print(o.count('0'))

##12
##s = 216**900-36**350+6**100-1598
##a = []
##while s>0:
##    a = [s%6] + a
##    s //= 6
##print(a.count(5))

##13
##for x in '0123456789ab':
##    s = int(f'a9{x}64',12) + int(f'1{x}00a',12)
##    if s%11==0:
##        print(s/11)

##14
##for x in '0123456789abcdefghijk':
##    s = int(f'abc1{x}0',21) + int(f'd{x}98',21)
##    if s%65==0:
##        print(s/65)

##15
##for x in '0123456789abcdefg':
##    s = int(f'11{x}586',17) + int(f'5{x}211',17)
##    if s%49==0:
##        print(s/49)

##16
##for x in '0123456789abcdefghijklmno':
##    s = int(f'b0{x}6{x}3',25) + int(f'f0{x}c21',25)
##    if s%44==0:
##        print(s/44)


##17
##def f(n):
##    if n>=670: return n-5
##    if n<670: return 5*n+7+f(5*n+7)
##print(f(600)-f(300))

##18
##def f(n):
##    if n==0: return 6
##    if n>0: return 2*f(n-4)
##    if n<0: return 2*n+5+f(n)
##print(f(12))

##19
##def f(n):
##    if n==0: return 1
##    if n==1: return 2
##    if n>1: return 6*f(n-1)-f(n-2)*n
##print(f(4))

##20
##def f(n):
##    if n<=3: return n
##    if 3<n<=32: return n//4+f(n-3)
##    if n>32: return 2*f(n-5)
##print(f(100))

##21
##def f(n):
##    if n==1: return 3
##    if n==2: return 6
##    if n==3: return 9
##    if n>3: return f(n-3)*n+2
##print(f(12))

##22
##def g(n):
##    if n<=1: return 1
##    if n>1 and n%2==1: return g(n-2)+n**2
##    if n>1 and n%2==0: return g(n-1) + n
##print(g(80))

##1
##k=0
##def f(a,b):
##    global k
##    if a==0:return b
##    if a>0:
##        k+=1
##        return f(a-1,b+1)
##    if a<0:
##        k+=1
##        return f(a+1,b-1)
##print(f(100,200),k)

##2
##def f(n):
##    if n<10: return n
##    return n%10 + f(n//10)
##print(f(10**998+12345))

##3
##def f(n):
##    if n==1: return True
##    if n%2==1: return False
##    return f(n//2)
##k=0
##for n in range(2,10001):
##    if f(n)==True:
##        k+=1
##print(k)

##4
####from functools import *
####from sys import *
####setrecursionlimit(1000000)
####@lru_cache(None)
####def f(n):
####    if n==0: return 0
####    return f(n//10)+(n%10)
####k=0
####for n in range(555555555,1555555555):
####    if f(n)>f(n+1):
####        k+=1
####print(k)

####5
####6

##7
####from functools import *
####from sys import *
####setrecursionlimit(10000)
####@lru_cache(None)
####def f(a,b):
####    if a==0 and b==0: return 0
####    if a>b: return f(a-1,b)+b
####    if a<=b and b>0: return f(a,b-1)+a
####for a in range(1000):
####    for b in range(1000):
####        if f(a,b)==5555555555555:
####            print(a,b)

##8
##from sys import *
##setrecursionlimit(10000)
##def f(n):
##    if n==0 or n==1: return 1
##    return f(n-1)*n
##print(f(2023)//f(2022))

##9
##def f(k,n):
##    if k==0 or k==n: return 1
##    return f(k-1,n-1)+f(k,n-1)
##print(f(10,20))

##1
##def f(n):
##    if n==1 or n==2: return n
##    return f(n-1)+3*f(n-2)
##print(f(6))

##2
##def f(n):
##    if n==0: return 1
##    if n==1 or n==2: return 3
##    return f(1)*f(n-1)**f(n-3)+f(n-2)
##print(f(4))

##3
##c=0
##def f(n):
##    global c
##    if n<9:
##        f(n+5)
##        f(n+2)
##        print(n)
##        c+=n
##print(f(1),c)

##4
##def f(n):
##    if n<3: return 2*n*n+2
##    if n>2 and n%5==0: return 2*f(n-2)+f(n//2)+n
##    return 2*n*n+f(n-2)+1+f(n//3)
##print(s:=str(f(100)))
##print(s.count('0')+s.count('2')+s.count('4')+s.count('6')+s.count('8'))

##5
##def f(n):
##    if n>32: return n**3
##    return f(n*2)+f(n+1)*n
##k=0
##for n in range(1,1001):
##    s = str(f(n))
##    if s[-1]=='3':
##        k+=1
##print(k)

##6
##def f(n):
##    if n<6: return 2*n+1
##    if n>5 and n%3==0: return 3*f(n-1)+f(n//2)+n
##    return 5*n*n+f(n-1)+f(n//2)
##for n in range(1,1001):
##    if f(n)%10==8:
##        print(n)

##7
##def f(n):
##    if n>25: return 2*n*n*n+n*n
##    return f(n+1)+5*f(n+3)
##s = str(f(2))
##print(sum(int(i) for i in s))

##8
##def f(n):
##    if n<32: return n*n+15
##    return f(n//2)+15+f(n-1)
##k=0
##for n in range(1,101):
##    s = hex(int(f(n)))[2:]
##    print(f(n),s)
##    if s[-1]=='f':
##        k+=1
##print(k)
    
##9
##def f(n):
##    if n<=1: return 3*n
##    return f(n-2)+2*g(n-1)
##def g(n):
##    if n<=2: return n
##    return g(n-2)+2*f(n-2)*f(n-2)
##print(f(5)+g(6))

##10
##def f(n):
##    if n==1 or n==2: return '***'
##    return '***' + g(n-1)
##def g(n):
##    if n==1 or n==2: return '**'
##    return f(n-2) + '**'
##print(f(13).count('*'))

##11
##def g(n):
##    if n<2: return 1
##    return f(n-1)+2*g(n-1)
##def f(n):
##    if n<2: return 1
##    if n>1 and n%2==1: return f(n-1)+g(n-1)
##    return f(n-2)+g(n-2)
##print(f(25)-g(25))

##12
##def f(n):
##    if n<20: return n**2
##    if n>19 and n%2==0: return g(n//2)*3-f(n-2)
##    return g(n-2)
##def g(n):
##    if n<20 and n%5!=0: return 3*n+f(n-2)
##    if n<20 and n%5==0: return g(n-2)+f(n//5)
##    return n**3
##for n in range(1,481):
##    s = str(abs(f(n)))
##    su = sum(int(i) for i in s)
##    if su==48:
##        print(n)

##1
##def f(n):
##    if n>1000: return n
##    return 7*n*n+3+f(n+1)
##print(f(6)-f(12))

##2
##def f(n):
##    if n==2: return 2
##    return f(n-1)*(n+4)
##print(f(11)//f(7))

##3
##def f(n):
##    if n<=1: return 0
##    if n>1 and n%2==0: return f(n-1)+n//4
##    return f(n-1)*(n+1)//2+5
##print(f(11))

##4
##def f(n):
##    if n<=9: return n
##    if 9<n<=30: return f(n-7)+2*n**2
##    return f(n-9)*n+15
##print(f(31))

##5
##def f(n):
##    if n<=15: return n
##    if 15<n<=25: return f(n-15)+n//3
##    return f(n-6)
##print(f(20))

##6
##def f(n):
##    if n>=256: return n
##    return 2*f(n+3)-f(n+4)+3*n
##print(f(8800)/f(250))

##7
##def f(n):
##    if n<100: return 5+ n+f(n+2)
##    return n+2
##print(f(90)-f(101))





























