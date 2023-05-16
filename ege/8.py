##from itertools import product
##k=0
##for x in product('01234567', repeat=5):
##    s = ''.join(x)
##    if s[0]!='0' and s.count('6')==1:
##        s = s.replace('3','1').replace('5','1').replace('7','1')
##        if '16' not in s and '61' not in s:
##            k+=1
##print(k)

##from itertools import product
##k=0
##for x in product('ВИШНЯ', repeat=6):
##    s = ''.join(x)
##    if s.count('В')<=1 and s[0]!='Ш' and s[-1] not in 'ИЯ':
##        k+=1
##print(k)

##from itertools import product
##k=0
##for x in product('01234', repeat=6):
##    s = ''.join(x)
##    if s[0]!='0' and s[0]!='1' and s[-1]!='3' and s[-1]!='4':
##        k+=1
##print(k)

##from itertools import *
##
##k=0
##
##for x in product('ЧН', repeat = 11):
##    s = ''.join(x)
##    if s.count('Н')==4 and 'НН' not in s:
##        if s[0]=='Ч': k+= 3*4**10
##        else: k+=4**11
##print(k)

##from itertools import product
##k=0
##for x in product('AB123', repeat=8):
##    s = ''.join(x)
##    s = s.replace('B','A')
##    if s.count('A')==2:
##        k+=1
##print(k)

##from itertools import *
##k=0
##q = ['BA','CB','CA','DA','DB','DC']
##for x in product('ABCD', repeat=4):
##    s = ''.join(x)
##    if any(sub in s for sub in q):
##        continue
##    else:
##        k+=1
##print(k)

##from itertools import *
##k=0
##for x in product('0123456789', repeat=3):
##    s = ''.join(x)
##    if s[0]!='0' and s[0]<=s[1]<=s[2]:
##        k+=1
##print(k)

##from itertools import *
##k=0
##for x in permutations('ВАЙФУ', r=4):
##    s = ''.join(x)
##    if s[0]!='Й' and 'ВФ' not in s and 'ФВ' not in s:
##        k+=1
##print(k)

##from itertools import *
##k=0
##for x in set(permutations('МИМИКРИЯ')):
##    s = ''.join(x)
##    k+=1
##print(k)

##from itertools import *
##k=0
##for x in product('АГИЛМОРТ',repeat=4):
##    s = ''.join(x)
##    k+=1
##    if s[-1]=='М' and s[-2]=='И':
##        print(k,s)

##from itertools import *
##k=0
##for x in product('АИМРЯ',repeat=4):
##    s = ''.join(x)
##    k+=1
##    if k==211:
##        print(k,s)


