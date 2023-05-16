##s ='8'*72
##while '222' in s or '888' in s:
##    if '222' in s:
##        s = s.replace('222','8',1)
##    else:
##        s = s.replace('888','2',1)
##print(s)

##s='8'*70
##while '2222' in s or '8888' in s:
##    if '2222' in s:
##        s = s.replace('2222','88',1)
##    else:
##        s = s.replace('8888','22',1)
##print(s)

##s= '2'+'5'*81
##while '25' in s or '355' in s or '4555' in s:
##    if '25' in s:
##        s = s.replace('25','4',1)
##    if '355' in s:
##        s = s.replace('355','2',1)
##    if '4555' in s:
##        s = s.replace('4555','3',1)
##print(s)

##s = '1' + '0'*33
##while '1' in s or '100' in s:
##    if  '100' in s:
##        s = s.replace('100', '0001',1)
##    else:
##        s = s.replace('1', '00',1)
##print(s.count('0'))

##s = '1'*46 + '2'*31
##while '1111' in s:
##    s = s.replace('1111','2',1)
##    s = s.replace('222','1',1)
##print(s)

##for x in range(1,51):
##    s = '6'*x
##    while '66' in s:
##        s = s.replace('66','1',1)
##        s = s.replace('11','2',1)
##        s = s.replace('22','6',1)
##    if s=='21':
##        print(x)

##s = '25'*12+'2'*7
##while '25' in s:
##    s = s.replace('25','9',1)
##print(sum(int(c) for c in s))

##s= '>'+10*'1'+20*'2'+30*'3'
##while '>1' in s or '>2' in s or '>3' in s:
##    if '>1' in s: s= s.replace('>1','22>',1)
##    if '>2' in s: s= s.replace('>2','2>',1)
##    if '>3' in s: s= s.replace('>3','1>',1)
##print(sum(int(c) for c in s if c!='>'))

##s = '>' + '1'*11 + '2'*12 + '3'*30
##while '>1' in s or '>2' in s or '>3' in s:
##    if '>1' in s: s = s.replace('>1','22>',1)
##    if '>2' in s: s = s.replace('>2','2>',1)
##    if '>3' in s: s = s.replace('>3','1>',1)
##print(sum(int(c) for c in s if c!='>'))

##a = set()
##for i in range(301,400):
##    s=i*'5'
##    while '5555' in s or '888' in s:
##        s = s.replace('5555','88',1)
##        s = s.replace('888','5',1)
##    a.add(s)
##print(len(a))

##s='01'
##while '01' in s or '02' in s or '03' in s:
##    s = s.replace('01','2302',1)
##    s = s.replace('02','10',1)
##    s = s.replace('03','201',1)
##print(s)

##s='01'
##while '01' in s or '02' in s or '03' in s:
##    s = s.replace('01','302',1)
##    s = s.replace('02','3103',1)
##    s = s.replace('03','20',1)
##print(s)

##s='112'*4+'1'*4
##while '11' in s:
##    if '112' in s:
##        s =s.replace('112','7',1)
##    else:
##        s =s.replace('11','3',1)
##print(sum(int(c) for c in s))

##s = '9992'*33+'2'*15+'1'*14
##while '999' in s or '22' in s:
##    if '999' in s:
##        s=s.replace('999','12',1)
##    else:
##        s=s.replace('22','1',1)
##print(s.count('1'))

##a=set()
##for x in range(1,100):
##    s=x*'5'
##    while '555' in s or '888' in s:
##        s = s.replace('555','8',1)
##        s = s.replace('888','55',1)
##    a.add(s)
##print(len(a))























