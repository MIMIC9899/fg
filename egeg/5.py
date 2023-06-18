##1
##for x in range(1000):
##    b = bin(x)[2:]
##    if int(b)%2==0: b+='11'
##    else: b+='01'
##    r = int(b,2)
##    if r<128:
##        print(r)

##2
##for x in range(1000):
##    b = bin(x)[2:]
##    s = b.count('1')
##    b+=str(s%2)
##    s = b.count('1')
##    b+=str(s%2)
##    r = int(b,2)
##    if r>103:
##        print(r)

##3
##for n in range(2,1000):
##    b = bin(n)[2:]
##    sl1 = int(b[-1])
##    sl2 = int(b[-2])
##    b+= str(sl1*sl2)
##    sl1 = int(b[0])
##    sl2 = int(b[1])
##    b+= str(sl1*sl2)
##    r = int(b,2)
##    if r>55:
##        print(n)

##4
##for n in range(1,256):
##    b = bin(n)[2:].zfill(8)
##    b = b[:-1]
##    b = b[::-1]
##    r = int(b,2)
##    if r<100:
##        if r==n:
##            print(n)

##5
##for n in range(100,1000):
##    n = str(n)
##    s1 = int(n[0])+int(n[1])
##    s2 = int(n[1])+int(n[2])
##    mi = str(min(s1,s2))
##    ma = str(max(s1,s2))
##    r = ma + mi
##    if r == '1511':
##        print(n,r)

##6
##for n in range(100,1000):
##    n =str(n)
##    s1 = int(n[0]) * int(n[1])
##    s2 = int(n[1]) * int(n[2])
##    mi=str(min(s1,s2))
##    ma=str(max(s1,s2))
##    r = ma + mi
##    if r == '153':
##        print(n)

##7
##for x in range(10000,100000):
##    x = str(x)
##    s1 = int(x[0])**2+int(x[2])**2+int(x[4])**2
##    s2 = int(x[1])**2+int(x[3])**2
##    mi = str(min(s1,s2))
##    ma = str(max(s1,s2))
##    r = mi + ma
##    if r == '7590':
##        print(x)

##8
##for k in range(-1000,100):
##    m=k
##    if k<-9 or k>9:
##        kd = str(k)[-2]
##    else: kd =0 
##    ke = str(k)[-1]
##    m *= int(kd)
##    m += int(ke)
##    if m==860:
##        print(k)
    
##9
####for x in range(1000,10000):
####    q = x
####    if str(x)[-1] != '9':
####        x += 1
####    else: pass
####    last=str(x)[-1]
####    x = str(x)[:-1]
####    x = last + x
####    for n in range(6):
####        if str(x)[-1] != '9':
####            x = int(x)
####            x += 1
####        else: pass
####        last=str(x)[-1]
####        x = str(x)[:-1]
####        x = last + x
####    su =0 
####    for s in x:
####        su+=int(s)
####    if su==31 and x[2]=='8':
####        print(q)
    
##10
##from itertools import *
##k=0
##for x in range(500,701):
##    a=[]
##    mi,ma=10000,-10000
##    x=str(x)
##    for s in x:
##        a.append(int(s))
##    for q in permutations(x,r=2):
##        s = ''.join(q)
##        if s[0]!='0':
##            mi = min(mi,int(s))
##            ma = max(ma,int(s))
##    if (ma-mi)==50:
##        k+=1
##print(k)

##11
##for x in range(10000,100000):
##    n = str(x)
##    s1 = int(n[0]) + int(n[1])
##    s2 = int(n[2]) + int(n[3])
##    s3 = int(n[0]) + int(n[4])
##    ma = max(s1,s2,s3)
##    mi = min(s1,s2,s3)
##    m = s1+s2+s3-ma-mi
##    k = str(mi)+str(m)
##    if k=='311':
##        print(x)

##12
##for x in range(100,1000):
##    for y in range(100,1000):
##        n1,n2 = str(x),str(y)
##        s1n1,s1n2 = n1[0],n2[0]
##        s2n1,s2n2 = n1[1],n2[1]
##        s3n1,s3n2 = n1[2],n2[2]
##        s1 = int(s1n1) + int(s1n2)
##        s2 = int(s2n1) + int(s2n2)
##        s3 = int(s3n1) + int(s3n2)
##        ma = max(s1,s2,s3)
##        mi = min(s1,s2,s3)
##        m = s1+s2+s3-ma-mi
##        r = str(ma)+str(m)+str(mi)
##        if r=='16118' and (x==307 or y==307):
##            print(x,y)

##13
##ручной

##14
####

##1
##for n in range(172,1000):
##    b = bin(n)[2:]
##    s = sum(int(i) for i in b)
##    b += str(s%2)
##    b += str(s%2)
##    r = int(b,2)
##    if r%2==0:
##        print(n,r)

##2
##for n in range(1000):
##    b = bin(4*n)[2:]
##    s = b.count('1')
##    b += str(s%2)
##    s = b.count('1')
##    b += str(s%2)
##    r = int(b,2)
##    if r>211:
##        print(n)

##3
##for n in range(1000):
##    b = bin(n)[2:]
##    s = b.count('1')
##    b+= str(s%2)
##    s = b.count('1')
##    b+= str(s%2)
##    r = int(b,2)
##    if r>255:
##        print(r)

##4
##for n in range(94,200):
##    b = bin(n)[2:]
##    for _ in range(3):
##        s1 = b.count('1')
##        s0 = b.count('0')
##        if s1==s0:
##            b += b[-1]
##        elif s1>s0:
##            b += '0'
##        else:
##            b+='1'
##    r = int(b,2)
##    if r%6==0:
##        print(n)

##5
##for x in range(1,1000,2):
##    b = bin(x)[2:]
##    s = b[1:]
##    q=''
##    for i in s:
##        if i=='1': q+='0'
##        else: q+='1'
##    b = '1' + q
##    r = int(b,2)
##    r += x
##    if r>85:
##        print(x)

##6
##for n in range(100):
##    b = bin(n)[2:]
##    b += b[-1]
##    b+= str(b.count('1')%2)
##    b+= str(b.count('1')%2)
##    r = int(b,2)
##    if r>204:
##        print(r)
    
##7
##for n in range(1000):
##    b = bin(n)[2:]
##    s = sum(int(i) for i in b)
##    b+= str(s%2)
##    b+= str(s%2)
##    r = int(b,2)
##    if r>57:
##        print(r)

##8
##for n in range(1000):
##    b =bin(n)[2:]
##    s = sum(int(i) for i in b)
##    b += str(s%2)
##    s = sum(int(i) for i in b)
##    b += str(s%2)
##    r = int(b,2)
##    if r>199:
##        print(n)

##1
##for n in range(10000,100000):
##    b=str(n)
##    s1,s2=0,0
##    for i in range(1,5,2):
##        s1 += int(b[i])**2
##    for i in range(0,5,2):
##        s2 += int(b[i])**2
##    s = str(min(s1,s2))+str(max(s1,s2))
##    if s=='1350':print(n)

##2
##for k in range(100):
##    n = k*(k//10)
##    n+= k%10
##    if n==102:print(k)

##3
##for n in range(10000,100000):
##    b=str(n)
##    s1,s2=0,0
##    for i in range(1,5,2):
##        s1+= int(b[i])**2
##    for i in range(0,5,2):
##        s2+= int(b[i])**2
##    s = str(min(s1,s2))+str(max(s1,s2))
##    if s=='2597': print(n)

##4
##for n in range(1,1000):
##    b = bin(n)[2:]
##    s = b.count('1')
##    b+= str(s%2)
##    s = b.count('1')
##    b+= str(s%2)
##    r=int(b,2)
##    if r>73:print(r)

##5
##for n in range(1,1000):
##    b = bin(n)[2:]
##    s = b.count('1')
##    if s%2==1: b+='11'
##    else: b+='00'
##    r=int(b,2)
##    if r>201: print(n)

##1
##for n in range(1,1000):
##    b = bin(n)[2:]
##    s = b.count('1')
##    b += str(s%2)
##    s = b.count('1')
##    b += str(s%2)
##    r = int(b,2)
##    if r>126: print(n)

##2
##for n in range(1,1000):
##    b = bin(n)[2:]
##    if b[-1]=='0': b+='01'
##    else: b+='11'
##    r= int(b,2)
##    if r>206: print(n)

##3
##for n in range(4,1000):
##    b = bin(n)[2:]
##    b = b[:-1]
##    if n%2==1:
##        b+='10'
##    else: b+='01'
##    r=int(b,2)
##    if r==769: print(n)

##4
##for n in range(1000,10000):
##    s1=int(str(n)[0])*int(str(n)[1])
##    s2=int(str(n)[2])*int(str(n)[3])
##    s = str(max(s1,s2)) + str(min(s1,s2))
##    if s=='3612': print(n)

##5
##for n in range(1000,10000):
##    s1=int(str(n)[0])+int(str(n)[1])
##    s2=int(str(n)[1])+int(str(n)[2])
##    s3=int(str(n)[2])+int(str(n)[3])
##    s = str(s1+s2+s3-max(s1,s2,s3)-min(s1,s2,s3)) +str(max(s1,s2,s3))
##    if s=='713': print(n)

















