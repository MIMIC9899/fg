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

##13
##n=5**2020-5**1019+100
##a=[]
##while n>0:
##    a= [n%5]+a
##    n//=5
##print(a.count(4))

##14
##n=125**21-4*25**17-2*5**15-3*5**5
##a=[]
##while n>0:
##    a = [n%5]+a
##    n//=5
##print(a.count(0))

##15
##n=4**2023+4**115-3*4**523-2378
##a=[]
##while n>0:
##    a=[n%4]+a
##    n//=4
##print(a.count(3))

##17
##for x in '0123456789abcdefghijk':
##    s = int(f'12{x}ac',21)+int(f'90f{x}e',21)
##    if s%53==0: print(s//53)

##6
##n=16**23*4**11-4**7+132
##a=[]
##while n>0:
##    a = [n%4]+a
##    n//=4
##print(a.count(3))

##7
##n=81**17*9**9+9**5-88
##a=[]
##while n>0:
##    a=[n%9]+a
##    n//=9
##print(a.count(8))

##8
##n=8**1222+4**320-2**16+76
##b=bin(n)[2:]
##print(b.count('1'))

##9
##for x in '0123456789abcd':
##    s = int(f'2{x}745',14)+int(f'53{x}65',14)
##    if s%26==0: print(s//26)

##10
##for x in '0123456789abc':
##    for y in '0123456789abc':
##        s = int(f'1{x}41{y}',13)+int(f'67{x}32{y}',17)
##        if s%81==0: print(s//81)













