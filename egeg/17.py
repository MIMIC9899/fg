##k=0
##m=-100000000
##
##for x in range(12345,67891):
##    if x%17==0 and x%13!=0 and x%22!=0:
##        k+=1
##        m=max(m,x)
##print(k,m)

##1
##k=0
##m=1000000000
##for x in range(5352,20464):
##    if x%12==0 and x%11!=0 and x%66!=0:
##        k+=1
##        m=min(m,x)
##print(k,m)

##2
##s,k=0,0
##for x in range(3172,9732):
##    if x%3==1 and x%8==5:
##        k+=1
##        s+=x
##print(k,s)

##3
##k=0
##m=100000000
##for x in range(94252,144569):
##    q = x//100%10
##    if x//10%10<=4 and 2<=q<=5:
##        k+=1
##        m = min(m,x)
##print(k,m)

##4
##s,k=0,0
##for x in range(113480,992403):
##    if x%8==6 and x%3!=0:
##        k+=1
##        s+=x
##print(k,s)

##5
##k=0
##m=-10000
##for x in range(5629,130453):
##    if x//10%10<=8 and 7<=x//100%10<=9:
##        k+=1
##        m=max(m,x)
##print(k,m)

##6
##f = open('dz17-13__tcco.txt')
##n = 10000
##s=100000000
##k=0
##a=[]
##for x in range(n):
##    a.append(int(f.readline()))
##for i in range(n-1):
##    if a[i]<60 and a[i+1]<60 and (a[i]%5==0 or a[i]%8==0 or a[i+1]%5==0 or a[i+1]%8==0):
##        k+=1
##        s1=a[i]+a[i+1]
##        s=min(s,s1)
##print(k,s)
        
##7
##f = open('2__w42q.txt')
##n=10000
##mi=1000000
##ma=-100000000
##a=[]
##k=0
##for x in range(n):
##    a.append(int(f.readline()))
##for i in range(n-1):
##    if (a[i]*a[i+1])%(a[i]+a[i+1])==0:
##        k+=1
##        mi=min(mi,a[i],a[i+1])
##        ma=max(ma,a[i],a[i+1])
##print(k,ma+mi)

##8
##f = open('dz17-20__tcd8.txt')
##n=100000
##a=[]
##a1=[]
##k=0
##for x in range(n):
##    a.append(int(f.readline()))
##sr=sum(a)/n
##for i in range(n-1):
##    if a[i]>sr or a[i+1]>sr:
##        k+=1
##        if a[i]>a[i+1]:
##            a1.append(a[i])
##        else:
##            a1.append(a[i+1])
##print(k,sum(a1))

##9
##f = open('dz17-23__tcdd.txt')
##n=100000
##k=0
##m=0
##a=[]
##for x in range(n):
##    a.append(int(f.readline()))
##sr=sum(a)/n
##for i in range(n-1):
##    if (a[i]>sr or a[i+1]>sr) and (a[i]%17==0 or a[i+1]%17==0):
##        k+=1
##        m=max(m,a[i]+a[i+1])
##print(k,m)

##10
##f = open('dz17-18__tcd3.txt')
##n=10000
##m,k=[],0
##a=[]
##for x in range(n):
##    a.append(int(f.readline()))
##for i in range(n-2):
##    q = max(a[i],a[i+1],a[i+2])
##    if q**2<a[i]**2+a[i+1]**2+a[i+2]**2-q**2:
##        k+=1
##        m.append(q)
##print(k,sum(m))

##11

##1
##k=0
##for x in range(22578,124287211):
##    if x%2023==0:
##        k+=1
##print(k)

##2
##k,m=0,-1000
##for x in range(15228,84256):
##    if x%2==0 and x%3!=0 and x%4!=0 and x%5!=0 and x%6!=0:
##        k+=1
##        m=max(m,x)
##print(k,m)

##3
##s,k=0,0
##for x in range(34740,43880):
##    if x%8==6 and x%3!=0:
##        k+=1
##        s+=x
##print(k,s)

##4
##k,m=0,100000
##for x in range(51354,82395):
##    if x//10%10<=4 and 2<= x//100%10<=5:
##        k+=1
##        m=min(m,x)
##print(k,m)

##5
##k,m=0,10000
##for x in range(3712,8433):
##    if x%2==x%4 and (x%13==0 or x%14==0 or x%15==0):
##        k+=1
##        m=min(m,x)
##print(k,m)

##6
##f = open('dz17-26__tcdg.txt')
##n=100000
##k=0
##ms=0
##a=[]
##for x in range(n):
##    a.append(int(f.readline()))
##mp=[]
##for x in a:
##    if x%171==0:
##        mp.append(x)
##m = max(mp)
##for i in range(n-1):
##    if (a[i]<m or a[i+1]<m) and (a[i]%2==1 or a[i+1]%2==1):
##        k+=1
##        ms=max(ms,a[i]+a[i+1])
##print(k,ms)

##7
##f = open('dz17-22__tcdc.txt')
##n = 100000
##k,m=0,-1000
##a =[]
##for x in range(n):
##    a.append(int(f.readline()))
##cr = sum(a)/n
##for i in range(n-1):
##    if a[i]>cr and a[i+1]>cr and str(a[i]+a[i+1])[-2:]=='31':
##        k+=1
##        m=max(m,a[i]+a[i+1])
##print(k,m)

##8
##f = open('dz17-16__tccv.txt')
##n=10000
##k=0
##a=[]
##ms=[]
##for _ in range(n):
##    a.append(int(f.readline()))
##for i in range(n-2):
##    b1 = bin(a[i])[2:]
##    b2 = bin(a[i+1])[2:]
##    b3 = bin(a[i+2])[2:]
##    if b1.count('1')==3 and b2.count('1')==3 and b3.count('1')==3:
##        k+=1
##        ms.append(max(a[i],a[i+1],a[i+2]))
##print(k,sum(ms))

##9
##f = open('3__w42t.txt')
##n=10000
##k=0
##ma=-10000
##mi=100000
##a=[]
##for _ in range(n):
##    a.append(int(f.readline()))
##for i in range(n-2):
##    s = a[i]+a[i+1]+a[i+2]
##    b = bin(abs(s))[2:]
##    if b[-2] == '1' and b[-1] =='1':
##        k+=1
##        ma=max(ma,max(a[i],a[i+1],a[i+2]))
##        mi=min(mi,min(a[i],a[i+1],a[i+2]))
##print(k,ma-mi)

##10
##f = open('17__1sn7o.txt')
##n=100000
##k=0
##m=0
##a=[]
##for _ in range(n):
##    a.append(int(f.readline()))
##s= sum(a)%54321
##for i in range(n-1):
##    h1 = hex(a[i])[2:]
##    h2 = hex(a[i+1])[2:]
##    if a[i]<=s and a[i+1]<=s and (h1[-1]=='b' or h2[-1]=='b'):
##        k+=1
##        m=max(m,a[i]*a[i+1])
##print(k,m)

##11
##f = open('17__1sslb.txt')
##n=10000
##a=[]
##for _ in range(n):
##    a.append(int(f.readline()))
##k=0
##m=0
##for i in range(n):
##    for x in range(i+1,n):
##        if abs(a[i]-a[x])%31==0:
##            k+=1
##            m=max(m,abs(a[i]-a[x]))
##print(k,m)

##12
##f = open('17__1sso1.txt')
##n = int(f.readline())
##k=0
##a=[]
##for _ in range(n):
##    a.append(int(f.readline()))
##for i in range(n):
##    for j in range(i+2,n):
##        if (a[i]+a[j])%2==1 and a[i]>0 and a[j]>0:
##            for c in range(i+1,j):
##                if a[c]==0:
##                    k+=1
##                    break
##print(k)

##13
##f = open('17__1sso9.txt')
##n = int(f.readline())
##k=0
##a=[]
##for _ in range(n):
##    a.append(int(f.readline()))
##for i in range(n):
##    for j in range(i+1,n):
##        if i+3<=j<=n and (a[i]*a[j])%34==0:
##            k+=1
##print(k)

##14
##f = open('17__1ssmj.txt')
##n = 10000
##a=[]
##for _ in range(n):
##    a.append(int(f.readline()))
##k=0
##m=1000000000000
##mi=100000000
##for x in range(n):
##    if len(str(a[x]))==3 and str(a[x])[-1]=='3':
##        mi = min(mi,a[x])
##for i in range(n):
##    for j in range(i+1,n):
##        if (len(str(a[i]))==3 and len(str(a[j]))!=3) or (len(str(a[i]))!=3 and len(str(a[j]))==3):
##            if (a[i]+a[j])%mi==0:
##                k+=1
##                m=min(m,a[i]+a[j])
##print(k,m)

##15
##f = open('17__1ssk3.txt')
##n=10000
##a=[]
##for _ in range(n):
##    a.append(int(f.readline()))
##k=0
##mi=1000000
##for x in range(n):
##    if a[x]%24==0:
##        mi = min(mi,a[x])
##m=0
##for i in range(n):
##    for j in range(i+1,n):
##        if a[i]%mi==0 or a[j]%mi==0:
##            k+=1
##            m=max(m,a[i]+a[j])
##print(k,m)

##1
##f = open('1__1vf52.txt')
##n = 6367
##m,k=0,0
##mi=1000000
##a=[]
##for _ in range(n): a.append(int(f.readline()))
##for i in range(n):
##    if a[i]%15==0: m = max(m,a[i])
##for i in range(n-1):
##    if a[i]>m or a[i+1]>m:
##        k+=1
##        mi = min(mi,a[i]+a[i+1])
##print(k,mi)
        
##2
##f = open('2__1vf54.txt')
##n = 4418
##ks=[]
##ma,k=0,0
##a = []
##for _ in range(n): a.append(int(f.readline()))
##for i in range(n):
##    if a[i]%6==0: ks.append(a[i])
##sr = sum(ks)/704
##for i in range(n-1):
##    if (a[i]>sr and a[i+1]<sr) or (a[i]<sr and a[i+1]>sr):
##        k+=1
##        ma = max(ma,a[i]+a[i+1])
##print(k,ma)

##3
##f = open('3__1vf57.txt')
##n=5800
##a=[]
##k=0
##mi=10000000
##for _ in range(n): a.append(int(f.readline()))
##for i in range(n-2):
##    if (a[i]%2 + a[i+1]%2 + a[i+2]%2)<=1 and (a[i]+a[i+1]+a[i+2])%3==0:
##        k+=1
##        mi = min(mi,a[i]+a[i+1]+a[i+2])
##print(k,mi)

##4
##f = open('4__1vf58.txt')
##n=5800
##a = []
##k,m=0,0
##for _ in range(n): a.append(int(f.readline()))
##mi,ma = min(a),max(a)
##for i in range(n-2):
##    if (a[i]%10==3 or a[i]%10==7 or a[i+1]%10==3 or a[i+1]%10==7 or a[i+2]%10==3 or a[i+2]%10==7):
##        if a[i]+a[i+1]+a[i+2]<mi+ma:
##            k+=1
##            m = max(m,a[i]+a[i+1]+a[i+2])
##print(k,m)

##5
##f = open('5__1vf59.txt')
##n=8300
##a=[]
##k,ma=0,-1000000
##for _ in range(n): a.append(int(f.readline()))
##sr = sum(a)/n
##for i in range(n-2):
##    if (a[i]%2+a[i+1]%2+a[i+2]%2)==2 and max(a[i],a[i+1],a[i+2])+min(a[i],a[i+1],a[i+2])<sr:
##        k+=1
##        ma = max(ma,a[i]+a[i+1]+a[i+2])
##print(k,ma)

##6
##f = open('6__1vf5a.txt')
##n=7268
##a=[]
##k,m=0,100000
##for _ in range(n): a.append(int(f.readline()))
##for i in range(n-2):
##    if (a[i]%2+a[i+1]%2+a[i+2]%2)==3 and max(a[i],a[i+1],a[i+2])+min(a[i],a[i+1],a[i+2])<0:
##        k+=1
##        m = min(m,a[i]+a[i+1]+a[i+2])
##print(k,m)

##7
##f = open('7__1vf5c.txt')
##n = 5373
##a = []
##for _ in range(n): a.append(int(f.readline()))
##k,m=0,0
##sr = sum(a)/n
##for i in range(n-2):
##    if (a[i]%14==0 or a[i+1]%14==0 or a[i+2]%14==0) and (a[i]<sr or a[i+1]<sr or a[i+2]<sr):
##        k+=1
##        m = max(m,a[i]+a[i+2]+a[i+1])
##print(k,m)

##8
##f = open('8__1vf5e.txt')
##n=10000
##a=[]
##k=0
##m=0
##for _ in range(n): a.append(int(f.readline()))
##for i in range(n-1):
##    if (a[i]%5==0 or a[i+1]%5==0) and (a[i]+a[i+1])%10==0:
##        k+=1
##        m = max(m,a[i]+a[i+1])
##print(k,m)

##9
##f = open('9__1vf5f.txt')
##n=10000
##a=[]
##for _ in range(n): a.append(int(f.readline()))
##k,m=0,0
##for i in range(n):
##    for j in range(i+1,n):
##        if (a[i]+a[j])%134==0:
##            k+=1
##            m = max(m,a[i]+a[j])
##print(k,m)

##10
##f = open('10__1vf5g.txt')
##n=10000
##a=[]
##for _ in range(n): a.append(int(f.readline()))
##k,mi=0,1000000
##for i in range(n):
##    for j in range(i+1,n):
##        if abs(a[i]-a[j])%2==0 and (a[i]%11==0 or a[j]%11==0):
##            k+=1
##            mi = min(mi,a[i]+a[j])
##print(k,mi)
























