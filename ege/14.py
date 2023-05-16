##x = 7**103+6*7**104-3*7**57+98
##a = []
##while x>0:
##    a = [x%7] + a
##    x//=7
##print(sum(a))

##x = 6**203+5*6**405-3*6**144+76
##a=[]
##while x>0:
##    a = [x%6] + a
##    x//=6
##print(a.count(0)-a.count(5))

##x = 17**5+85**8-10
##a=[]
##while x>0:
##    a = [x%17]+a
##    x//=17
##print(a.count(16))

##x = 7**2+49**4-21
##a=[]
##while x>0:
##    a = [x%14]+a
##    x//=14
##print(a.count(10)+a.count(0))

##for x in range(1,100):
##    t = 81**20-9**x+50
##    a=[]
##    while t>0:
##        a = [t%9]+a
##        t//=9
##    if sum(a)==138:
##        print(x)
##
##for x in range(1,1000):
##    t = oct(64**12-8**14+x)[2:]
##    if t.count('7')==12 and t.count('1')==1:
##        print(x)
##        break

##x = 64**30+2**300-4
##a=[]
##while x>0:
##    a = [x%8]+a
##    x//=8
##print(a.count(7))

##x = 51*7**12-7**3-22
##a=[]
##while x>0:
##    a = [x%7]+a
##    x//=7
##print(sum(a))

##for y in range(1,10000):
##    x=125**200-5**y+74
##    a=[]
##    while x>0:
##        a = [x%5]+a
##        x//=5
##    if a.count(4)==100:
##        print(y)

##for y in range(1,10000):
##    x=bin(4**2015+2**y-2**2015+15)
##    if x.count('1')==500:
##        print(y)

##for x in range(1,10000):
##    t = bin(4**1014-2**x+12)[2:]
##    if t.count('0')==2000:
##        print(x)

##for x in range(1,10000):
##    t = 36**17-6**x+71
##    a=[]
##    while t>0:
##        a= [t%6]+a
##        t//=6
##    if sum(a)==61:
##        print(x)

##x=6*144**26+11*12**75-48
##a =[]
##while x>0:
##    a = [x%12]+a
##    x//=12
##print(a.count(11))

##x=5*216**1156-4*36**1147+6**1153-875
##a =[]
##while x>0:
##    a = [x%6]+a
##    x//=6
##print(a.count(5)-a.count(0))

##for x in '0123456789abcdefgh':
##    a = int(f'9009{x}', 18) + int(f'2257{x}',18)
##    if a%15==0:
##        print(x, a/15)

##for x in range(18):
##    a = 11*18**4+2*18**3+5*18**2+16*18+2*x
##    if a%15==0:
##        print(x)

##for x in '123456789abcdefghijkl':
##    for y in '0123456789abc':
##        a = int(f'{x}23{x}5',22) - int(f'67{y}9{y}',13)
##        if a%57==0:
##            print(x,y,int(x,22)+int(y,13),a/57)

##for x in '0123456789abcde':
##    y = int(f'123{x}5',15) + int(f'1{x}233',15)
##    if y%14==0:
##        print(x,y/14)

##for x in '0123456789abcdefg':
##    y = int(f'9759{x}',17) + int(f'3{x}108',17)
##    if y%11==0:
##        print(x,y/11)

##for x in range(11):
##    if 3*11**4+3*11**3+6*11**2+4*11+x+x*12**4+7*12**3+9*12**2+4*12+6 == 5*14**4+5*14**3+x*14**2+8*14+7:
##        print(5*14**4+5*14**3+x*14**2+8*14+7)

##for x in '0123456789abcde':
##    for y in '0123456789abcdefg':
##        t = int(f'123{x}5',15)+int(f'67{y}9',17)
##        if t%131==0:
##            print(x,y,t/131)

##for x in '0123456789abcdefghijk':
##    for y in '0123456789abcdefghijk':
##        t = int(f'12{y}{x}9',21)+int(f'36{y}99',21)
##        if t%18==0:
##            print(x,y,t/18)

##for n in range(2,40):
##    try:
##        if int('103',n)==int('97',n+2):
##            print(n)
##    except:
##        pass

##for n in range(2,40):
##    try:
##        if int('132',n)+int('13',8)==int('124',n+1):
##            print(n)
##    except:
##        pass

##for n in range(1,100):
##    if int('33',n+4)-int('33',4) == 33:
##        print(n)

##for n in range(2,100):
##    try:
##        if int('21',n)*int('13',n)==int('313',n):
##            print(n)
##    except:
##        pass

##for x in range(21,30):
##    if x%3==1 and x//3%3==1:
##        print(x)

##for x in range(3,40):
##    a = bin(x)[2:]
##    if a[-4:] == '1011':
##        print(x)

##for n in range(2,100):
##    if 68%n==2 and n**3<=68<n**4:
##        print(n)

##for n in range(1,100):
##    if 25<=n<=36 and n%11==1:
##        print(n)

##for n in range(1,100):
##    if 36<=n<49 and n%13==3:
##        print(n)

k=0
for x in range(1,1000):
    if x<5**4 and x>=2**4 and x%16==12:
        k+=1
print(k)




































