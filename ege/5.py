##for n in range(1,100):
##    b=bin(n)[2:]
##    b+= '0' if b.count('1')%2==0 else '1'
##    b+= '0' if b.count('1')%2==0 else '1'
##    r = int(b,2)
##    if r>130:
##        print(r)

##for n in range(1,100):
##    b=bin(n)[2:]
##    b+=b[-1]
##    b+= '0' if b.count('1')%2==0 else '1'
##    b+= '0' if b.count('1')%2==0 else '1'
##    r = int(b,2)
##    if r>97:
##        print(n)

##for n in range(1,100):
##    s=0
##    b = bin(n)[2:]
##    for i in b:
##        s+=int(i)
##    b+=str(s%2)
##    s=0
##    for i in b:
##        s+=int(i)
##    b+=str(s%2)
##    r = int(b,2)
##    if r>80:
##        print(r)
    
##for n in range(1,100):
##    b = bin(n)[2:]
##    b+= '01' if n%2==0 else '10'
##    r=int(b,2)
##    if r>81:
##        print(r)

##for n in range(1,100):
##    b = bin(n)[2:]
##    b+=b[-1]
##    b+= '0' if b.count('1')%2==0 else '1'
##    b+= '0' if b.count('1')%2==0 else '1'
##    r = int(b,2)
##    if r>130:
##        print(n)
##        break

##for n in range(1,100):
##    b = bin(n)[2:]
##    b+=b[-1]
##    b+= '0' if b.count('1')%2==0 else '1'
##    b+= '0' if b.count('1')%2==0 else '1'
##    r=int(b,2)
##    if r>144:
##        print(r)

##for n in range(1,100):
##    b=bin(n)[2:]
##    b = b[::-1]
##    b=int(b,2)
##    if b==13:
##        print(n)

##k=0
##for n in range(1,100):
##    b = bin(n)[2:]
##    s=0
##    for i in b:
##        s+=int(i)
##    b+=str(s%2)
##    for i in b:
##        s+=int(i)
##    b+=str(s%2)
##    r=int(b,2)
##    if r<80:
##        k+=1
##        print(k)

##for n in range(1,1000):
##    b = bin(n)[2:]
##    s=0
##    for i in b:
##        s+=int(i)
##    b+=str(s%2)
##    s=0
##    for i in b:
##        s+=int(i)
##    b+=str(s%2)
##    r = int(b,2)
##    if r>1017:
##        print(n)
##        break

##m=1000000
##for n in range(1,100):
##    b=bin(n)[2:]
##    if n%2==0:
##        b+='0'
##        b = '1' +b
##    else:
##        b+='11'
##        b = '11' +b
##    r=int(b,2)
##    if r>52:
##        m = min(m,r)
##print(m)

##for n in range(1,100):
##    b=bin(n)[2:]
##    if b.count('1')%2==0:
##        b+='1'
##        b=b[2:]
##        b='10'+b
##    else:
##        b+='1'
##        b=b[2:]
##        b='11'+b
##    r=int(b,2)
##    if r<35:
##        print(n)

##for n in range(1,128):
##    b = bin(n)[2:].zfill(8)
##    b = b.replace('1','2').replace('0','1').replace('2','0')
##    r=int(b,2)
##    r+=1
##    if r==153:
##        print(n)

##for n in range(1,100):
##    q=n
##    a=''
##    while n>0:
##        a= str(n%3) + a
##        n//=3
##    a += str(q%3)
##    r = int(a,3)
##    if r>99:
##        print(q,r)
##        break















































