##4
##for x in range(-264,44):
##    try:
##        if -264%x==0 and -352%x==0:
##            print(x)
##    except:pass

##5
##s = '383'*10
##while ('38' in s and '83' in s) or '39' in s:
##    s =s.replace('383','9',1)
##    s =s.replace('39','6',1)
##print(s)

##6
##s = '1'*111
##while '111' in s:
##    s = s.replace('111','11',1)
##print(s)

##7
##s = '5'*10+'4'*10+'2'*10+'7'*10
##while '54' in s or '27' in s:
##    if '55' in s:
##        s = s.replace('55','7',1)
##    elif '22' in s:
##        s = s.replace('22','7',1)
##    if '44' in s:
##        s = s.replace('44','4',1)
##    elif '77' in s:
##        s = s.replace('77','7',1)
##print(s.count('7'))

##8
##s='BULLBULLBULL'
##while 'LL' in s:
##    s = s.replace('BU', 'LL',1)
##    print('1')
##    print(s)
##    if 'BULL' not in s:
##        s = s.replace('LLLLLL', 'CAT',1)
##        print('2')
##print(s)

##3
##for x in range(1,35):
##    if 35%x==0 and 42%x==0:
##        print(x)

##4
##for x in range(1,32):
##    if 32%x==0 and 20%x==0:
##        print(x)

##5
##for x in range(1,25):
##    if 168%x==0 and 24%x==0:
##        print(x)

##6
##for x in range(1,41):
##    if 72%x==0 and 40%x==0:
##        print(x)

##7
##s = '4'*44
##while '4444' in s or '333' in s:
##    s = s.replace('444','3',1)
##    if '333' in s:
##        s = s.replace('333','2',1)
##print(s)

##8
##s = '7'*40+'2'*20+'4'*80+'5'*40
##while '45' in s or '72' in s:
##    if '44' in s:
##        s = s.replace('44','2',1)
##    elif '77' in s:
##        s = s.replace('77','2',1)
##    if '55' in s:
##        s = s.replace('55','5',1)
##    elif '22' in s:
##        s = s.replace('22','2',1)
##su = 0
##for x in s:
##    su+=int(x)
##print(su)

##9
##s = '*'+'2'*30+'5'*63+'9'*36
##while '*2' in s or '*5' in s or '*9' in s:
##    if '*2' in s:
##        s = s.replace('*2','*',1)
##    if '*5' in s:
##        s = s.replace('*5','6*',1)
##    if '*9' in s:
##        s = s.replace('*9','7*',1)
##print(sum(int(i) for i in s if i!='*'))

##10
##for x in range(101,5000):
##    s = '4'*x
##    while '4444' in s:
##        s = s.replace('444','333',1)
##        s = s.replace('33','44',1)
##    if s.count('4')==6:
##        print(x,s)

##11
##ручное

##12
##for x in range(1,100):
##    s='1'*44+'5'*x+'3'*12
##    while '15' in s:
##        s = s.replace('15','5',1)
##        s = s.replace('53','3',1)
##    if s.count('5')==30:
##        print(x)

##1
##pro=[]
##for x in range(1,1000):
##    k=0
##    for y in range(1,x):
##        if x%y==0: k+=1
##    if k<2:
##        pro.append(x)
##for n in range(100):
##    s = '>' + '0'*15+'1'*n+'2'*15
##    while '>0' in s or '>1' in s or '>2' in s:
##        if '>0' in s:
##            s = s.replace('>0','22>',1)
##        if '>1' in s:
##            s = s.replace('>1','2>',1)
##        if '>2' in s:
##            s = s.replace('>2','1>',1)
##    su = sum(int(i) for i in s if i!='>')
##    if su in pro:
##        print(n)

##1
##for m in range(100):
##    s = '1'+'3'*m+'2'*m
##    while '12' in s or '13' in s:
##        if '12' in s: s = s.replace('12','48',1)
##        if '13' in s: s = s.replace('13','568',1)
##    su = sum(int(i) for i in s)
##    if su%23==0: print(m)

##2
##for x in range(100):
##    for y in range(100):
##        s = '8' + '3'*x + '4'*y + '8'
##        while '83' in s or '84' in s:
##            s = s.replace('83','33',1)
##            s = s.replace('84','438',1)
##        if s.count('3')==27 and s.count('4')==37:
##            print(y)

##3
##s='7'*209
##while '111' in s or '77' in s:
##    if '111' in s: s = s.replace('111','7',1)
##    else: s = s.replace('77','17',1)
##print(s)

##4
##s = '6'*149 +'1'
##while '14' in s or '661' in s:
##    if '14' in s: s = s.replace('14','61',1)
##    else: s = s.replace('661','14',1)
##print(s)

##5
##for x in range(151,300):
##    s = '2'*x
##    while '2222' in s:
##        s = s.replace('2222','44',1)
##        s = s.replace('444','22',1)
##    if s.count('2')==4: print(x)

##6
##for x in range(44):
##    for y in range(44):
##        for z in range(44):
##            s = '1' + '2'*x + '3'*y + '4'*z + '1'
##            while '11' not in s:
##                s = s.replace('12','41',1)
##                s = s.replace('13','21',1)
##                s = s.replace('14','31',1)
##            if s.count('2')==17 and s.count('3')==31 and s.count('4')==43:
##                print(x+y+z+2)

##7
##for x in range(100):
##    for y in range(100):
##        s = '3' + '1'*x + '4'*y + '3'
##        while '31' in s or '34' in s:
##            s = s.replace('31','443',1)
##            s = s.replace('34','13',1)
##        if s.count('1')==35 and s.count('4')==44:
##            print(x+y)

##6
##def div(x):
##    d = set()
##    for i in range(1,int(x**0.5)+1):
##        if x%i==0: d|= {i,x//i}
##    return sorted(d)
##print(div(54),div(81))
##9
##print(div(56),div(49))
##10
##print(div(18),div(48))






