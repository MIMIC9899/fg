##8
##f = open('1__1vf5v.txt').readline()
##f = f.replace('C',' ').replace('D',' ')
##print(max(len(c) for c in f.split()))

##9
##f = open('2__1vf5w.txt').readline()
##f1,f2 = f,f
##for c in '0123456789':
##    f1 = f1.replace(c,' ')
##for c in 'qwertyuiopasdfghjklzxcvbnm':
##    f2 = f2.replace(c,' ')
##print(max(len(c) for c in f1.split()))
##print(max(len(c) for c in f2.split()))

##10
##f = open('3__1vf5x.txt').readline()
##for i in range(len(f)):
##    if f[i]=='B':
##        if f[i+1]=='B':
##            if f[i+2]=='D' and f[i+3]=='E' and f[i+4]=='C': print(i)

##11
##f = open('4__1vf5y.txt').readline()
##for c in 'BCDE':
##    f = f.replace(c,' ')
##print(max(len(c) for c in f.split()))

##12
##f = open('5__1vf5z.txt').readline()
##f = f.replace('C', ' ')
##print(max(len(c) for c in f.split()))

##1
##f = open('1__h1li__t9im.txt').readline()
##print(f.count('P'))

##2
##f = open('Задача_6__uhdi.txt').readline()
##print(f.count('V'))

##3
##f = open('Задание_24__t2n9.txt').readline()
##c=0
##for i in range(len(f)-4):
##    if f[i]+f[i+4]=='MM':c+=1
##print(c)

##4
##f = open('Задача_7__uhdq.txt').readline()
##f = f.replace('D',' ').replace('V',' ')
##print(max(len(c) for c in f.split()))

##5
##f = open('24__14izr.txt').readline()
##f = f.replace('+','')
##print(sum(int(i) for i in f))

##6
##f = open('Задание_2_ДЗ__tceu.txt').readline()
##print(f.count('BA'))

##7
##f = open('Задание_4_ДЗ__tcex.txt').readline()
##c=m=0
##for i in range(1,len(f)):
##    if f[i]==f[i-1]:
##        c+=1
##        m=max(m,c)
##    else:c=0
##print(m)

##8
##f = open('Задача_3__fz2n__tads.txt').readline()
##c=0
##for i in range(len(f)):
##    if f[i]==f[i-1]:
##        c+=int(str(f[i])*2)
##print(c)

##9
##f = open('24__1crre.txt').readline()
##print(f.count('A')+f.count('E')+f.count('I')+f.count('O')+f.count('Y')+f.count('U'))

##10
##f = open('Задание_7_ДЗ__tcf7.txt').readline()
##f2=f
##f = f.replace('B',' ').replace('C',' ').replace('D',' ').replace('E',' ')
##m1 = max(len(c) for c in f.split())
##f2 = f2.replace('A',' ').replace('C',' ').replace('D',' ').replace('E',' ')
##m2 = max(len(c) for c in f2.split())
##print(m1,m2)
##print(abs(m1-m2))

##1
##f = open('Задача_10__uhdy.txt').readline()
##f = f.replace('VV','*').replace('DD','*').replace('MM','*').replace('V',' ').replace('D',' ').replace('M',' ')
##print(max(len(c) for c in f.split()))

##2
##f = open('string__swps.txt').readline()
##m=[]
##for i in range(1,len(f)-1):
##    if f[i-1]>=f[i]<=f[i+1]:
##        m.append(i)
##ma=0
##for i in range(len(m)-1):
##    ma=max(ma,m[i+1]-m[i])
##print(ma)

##3
##f = open('Задание_40_ДЗ__tcnc.txt').readline()
##c=m=0
##for i in range(1,len(f)):
##    if ord(f[i-1])==ord(f[i])-1:
##        c+=1
##        m=max(m,c)
##    else: c=0
##print(m)

##4
##f = open('Задание_33_ДЗ__tcmp.txt').readline()
##su=0
##for x in '0123456789':
##    c = f.count(f'-{x}')
##    su-=c*int(x)
##for x in '0123456789':
##    c = f.count(f'+{x}')
##    su+=c*int(x)
##print(su,f[0:5])

##5
##f = open('Задание_27_ДЗ__tcmd.txt').readline()
##c=m=0
##a=[]
##for x in 'QWERTYUIOPASDFGHJKLZXCVBNM':
##    c = f.count(x)
##    if c>m:
##        a.append(x+str(c))
##print(a)

##7
##f = open('Задание_24__iob7__t2rw.txt').readline()
##c=m=0
##a=[]
##for i in range(1,len(f)):
##    if f[i]==f[i-1]:
##        c+=1
##        if c>m:
##            m=c
##            a.append(str(f[i])+str(m))
##    else:c=0
##print(a)

##8
####f = open('Задание_49_ДЗ__tctq.txt')
####c,m=0,0
####s=''
####for x in f:
####    c=0
####    for i in range(len(x)-1):
####        if ord(x[i])+1==ord(x[i+1]):c+=1
####    if c>m:
####        m=c
####        s=x
####a=[0]*26
####al=sorted(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
####for i in range(len(al)):
####    a[i]=s.count(al[i])
####print(m)
####print(al[a.index(max(a))])

##9
##f = open('Задание_24__cke9__rko6.txt').readline()
##c=0
##for i in range(len(f)//2):
##    if f[i]==f[len(f)-i-1]:c+=1
##print(c)

##1
##f = open('1-3__1vq2c.txt')
##n,k=1000,0
##a=[]
##for _ in range(n): a.append(f.readline())
##for i in a:
##    if i.count('B')>i.count('N'):k+=1
##print(k)

##2
##f = open('1-3__1vq2d.txt')
##n,k=1000,0
##a=[]
##for _ in range(n): a.append(f.readline())
##for i in a:
##    if i.count('SY')>2:k+=1
##print(k)

##3
##f = open('1-3__1vq2e.txt')
##n=1000
##k=0
##a=[]
##for _ in range(n): a.append(f.readline())
##for i in a:
##    for j in range(len(i)-3):
##        if i[j] + i[j+3]=='TO':
##            k+=1
##            break
##print(k)

##5
##f = open('5__1vq2g.txt')
##n=1000
##c=0
##aa=set()
##a=[]
##for _ in range(n): a.append(f.readline())
####for i in a:
####    m=0
####    k=1
####    for j in range(1,len(i)):
####        if i[j]==i[j-1]:
####            k+=1
####        else:
####            m=max(m,k)
####            k=1
##s='EFRSESQNJGVLOBYBUEAACHPXVMTTUIMCZCCAJZDZLMINHGEWJTVLYHAEWBWWFRUWGTIIOIALKHFTOZBACYLYRPJMFDIMSHNGHHCXLXGCCQFABFZIJLSSEBAOLUZMJSDFJIMASIRMKADDVLPNNWGGFHNPUGVCZCYUFCXNENWYJWXACLUGKNTVHNWKGHRVFTMUXKTEXWHDRPHFWEQKNQPQEAPWJYQPVISMAWUHVTLYPPFCZOVSWNEYEBAHYSXSPNMYPPTWNOHZVHWEBKNFOJEXHPFEOZETLVXCMTBSCRVHUKUJWWIZFDSHGJFWDELIERAOVEUNDDDKHQNTQMPGXQIVCUUKWSMXLMHGNZSAJMZVIXYFRNIJBCURTBLJRDOIIKFPVGIGBYJTYKMIBUXXUSEFEIHCWVZRXOGROQCWKZTIXDFUMCSJEWZDQBUTDXVLXGKZQBCICCPHCGIFJTKMIFGAIFMQYSNICVDXJKFMAAHQIZTDBEJUXDKVDSSPINLGPCJWXHCUOKWBVBFGBFIZMVBBBBGNXVQBCNJRHSQZKLJOGAKMUNRKUYUAJTSAIVLGEKYVCYHLFEBLKCKTZBRKKKIMPAHBCOCRFEJGKEPXHACPONKKVFHUMOMPGSXXQXMCJZULDJWADQAHBXVKREFDUJZBOVXATYQOSQIKECDAPYWGFUGYKCCHZIYRPTCGOMPCSMNIUJTPEXHCWFGYSIKPZCTGOXFXMEYTESNCILWMHEQENPTFOOHJUYENPFBCYYNDSRUFWVDKXJSQDUIITUXEKWZTPYOECUCKLRLBVZPZOMFEJAGYXMBEVSUMNDAFCGAPHQZDKKNQCZUQTFDAFQELPVNIVTZTQRXLLIUWHMNNXNAQXLMSTOIHDNZPKHKMWOLRNJAHZNVRVZRVAHWURXENXJATPDHDRTVNYZEGNPMACYDFHVCUQPMUBKYFOCXKDMTZQLHSOQXPOYDFOCUCLOPUASKZWEEEVJXCNBKKILKPRDJRXJADU'
##for i in a:
##    c+=i.count('RU')
##print(c)
##7
##f = open('7__1vq2i.txt').readline()
##f = f.replace('A',' ').replace('C',' ').replace('E',' ').replace('F',' ')
##f = f.split()
##for i in f:
##    if 'DBDBDB' in i:
##        print(i)

##8
##f = open('8__1vq2j.txt').readline()
##f = f.replace('AE', 'A E')
##print(max(len(c) for c in f.split()))

##2
##f = open('2__1vv4j.txt').readline()
##f = f.replace('A',' ').replace('B',' ').replace('D',' ').replace('E',' ')
##print(max(len(c) for c in f.split()))

##3
##f = open('3__1vv4k.txt').readline()
##f = f.replace('B',' ').replace('C',' ')
##print(max(len(c) for c in f.split()))

##4
##f = open('4__1vv4m.txt').readline()
##f = f.replace('D',' ')
##print(max(len(c) for c in f.split()))

##5
##f = open('5__1vv4o.txt').readline()
##k=0
##for i in range(1,len(f)-1):
##    if f[i-1]<f[i]>f[i+1]:
##        k+=1
##print(k)

##6
##f = open('6__1vv4p.txt').readline()
##k=1
##m=[]
##for i in range(len(f)):
##    if ord(f[i])<ord(f[i-1]):
##        k+=1
##    else:
##        if k>7:
##            m.append([i,k])
##        k=1
##print(m)

##9
##f = open('9__1vv4s.txt').readline()
##while '00' in f or '11' in f or  '22' in f or  '33' in f or  '44' in f or '55' in f or  '66' in f or  '77' in f or   '88' in f or  '99' in f:
##    f = f.replace('00','0').replace('11','1').replace('22','2').replace('33','3').replace('44','4').replace('55','5').replace('66','6').replace('77','7').replace('88','8').replace('99','9')
##print(sum(int(c) for c in f))

##10
##f = open('10__1vv4t.txt').readline()
##f = f.replace('A',' ').replace('B',' ').replace('C',' ').replace('D',' ')
##f = f.split()
##for i in f:
##    if len(i)>5: print(i)










