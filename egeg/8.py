from itertools import *
k=0
##1
##for n in product('01234567',repeat=5):
##    s=''.join(n)
##    if s[0]!='0':
##        l=0
##        for q in range(0,4):
##            if s[q]==s[q+1]:
##                l+=1
##        if l==1:
##            k+=1
##print(k)

##2
##for x in product('0123456789',repeat=6):
##    s=''.join(x)
##    if s[0]!='0' and ('5' in s or '2' in s):
##        k+=1
##print(k)

##3
##for x in permutations('ОЛЬГА'):
##    s=''.join(x)
##    if s[0]!='Ь' and 'ОЬ' not in s and 'АЬ' not in s:
##        k+=1
##print(k)

##4
##ans=[]
##for x in product('МАШИНА', repeat=6):
##    s=''.join(x)
##    if s[0]<=s[2]<=s[4] and s[1]<=s[3]<=s[5]:
##        ans.append(s)
##print(len(set(ans)))

##5
##for x in product('УСПЕХ',repeat=5):
##    s =''.join(x)
##    if s==s[::-1] and s[2] in 'УЕ':
##        k+=1
##print(k)

##6
##for n in product('КОНФЕТА', repeat=5):
##    s=''.join(n)
##    if s.count('О')+ s.count('Е')+ s.count('А')>=2:
##        k+=1
##print(k)

##8
##for n in product('0123456789',repeat=6):
##    s=''.join(n)
##    if s[0]!='0' and s[0]<s[1]<s[2]<s[3]<s[4]<s[5]:
##        k+=1
##        
##print(k)

##9
##for n in product('0123456789',repeat=6):
##    s=''.join(n)
##    b=bin(int(s))[2:]
##    l=0
##    for q in range(0,len(b)-1):
##        if b[q]==b[q+1]:
##            l+=1
##    if l==0:
##        k+=1
##        print(l,k,b,s)
##print(k)

##12
##for n in permutations('qwertyuiopasdfgh',r=6):
##    s=''.join(n)
##    k+=1
##print(k)
    
##13
##for x in permutations('ABCD',r=3):
##    s=''.join(x)
##    k+=1
##print(k)

##14
##for x in product('СОТКА',repeat=3):
##    s=''.join(x)
##    k+=1
##for x in product('СОТКА',repeat=4):
##    s=''.join(x)
##    k+=1
##for x in product('СОТКА',repeat=5):
##    s=''.join(x)
##    k+=1
##print(k)

##15
##for x in product('НАСТЯ',repeat=15):
##    s=''.join(x)
##    if s[0] in 'АЯ' and s[-1] in 'АЯ':
##        if s.count('Н')<=3 and s.count('А')<=3 and s.count('С')<=3 and s.count('Т')<=3 and s.count('Я')<=3:
##            k+=1
##print(k)

##16
##for x in product('ЦИФРА',repeat=5):
##    s=''.join(x)
##    if s[0] not in "ИА":
##        k+=1
##print(k)

##21
##for x in product('ЕКОФ', repeat=5):
##    s=''.join(x)
##    k+=1
##    if s.count('Ф')==1 and s.count('Е')==0:
##        print(k,s)

##8
##for x in permutations('мирослав',r=5):
##    s = ''.join(x)
##    if s[0] not in 'иоа' and 'ио' not in s and 'ои' not in s and 'иа' not in s and 'аи' not in s and 'ао' not in s and 'оа' not in s:
##        if s.count('м')+s.count('р')+s.count('с')+s.count('л')+s.count('в')>s.count('и')+s.count('о')+s.count('а'):
##            k+=1
##print(k)

##9
##a=set()
##for x in product('КРУЖКА', repeat=7):
##    s = ''.join(x)
##    if s.count('У')+s.count('А')==2:
##        a.add(s)
##print(len(a))

##10
##a=set()
##for x in product('РАСЧЕСКА', repeat=3):
##    s=''.join(x)
##    a.add(s)
##for x in product('РАСЧЕСКА', repeat=4):
##    s=''.join(x)
##    a.add(s)
##for x in product('РАСЧЕСКА', repeat=5):
##    s=''.join(x)
##    a.add(s)
##for x in product('РАСЧЕСКА', repeat=6):
##    s=''.join(x)
##    a.add(s)
##print(len(a))

##11
##for x in permutations('УСЛОВИЕ',r=7):
##    s = ''.join(x)
##    if s[0]!='И' and s[-1]!='О' and 'СЛ' not in s and 'ЛС' not in s and 'СВ' not in s and 'ВС' not in s and 'ВЛ' not in s and 'ЛВ' not in s:
##        k+=1
##print(k)

##12
##for x in product('ВИШНЯ', repeat = 5):
##    s = ''.join(x)
##    if s[0] in 'ВШН' and 'ШН' not in s and 'ШВ' not in s and 'ШШ' not in s:
##        k+=1
##print(k)

##13
##a = set()
##for x in permutations('ОБОРОНА'):
##    s = ''.join(x)
##    if 'ООО' in s or 'ООА' in s or 'ОАО' in s or 'АОО' in s:
##        a.add(s)
##print(len(a))

##1
##for x in product('ЕКОФ', repeat=5):
##    s = ''.join(x)
##    k+=1
##    if s=='ФЕФКО':
##        print(k)

##2
##for x in product('ГОЭ',repeat=5):
##    s = ''.join(x)
##    k+=1
##    if k==78:
##        print(s)

##3
##for x in product('БОГИНЯ', repeat=6):
##    s = ''.join(x)
##    if s.count('О')==2:
##        k+=1
##print(k)

##4
##for x in product('ГРОЗА', repeat=7):
##    s = ''.join(x)
##    if s.count('З')>=2:
##        k+=1
##print(k)

##5
##for x in product('КАТЕР', repeat=6):
##    s=''.join(x)
##    if s.count('Т')<=1 and s[0]!='Т' and s[1]!='Т' and 'КТ' not in s:
##        k+=1
##print(k)

##6
##for x in product('АПРЕЛ',repeat=6):
##    s = ''.join(x)
##    if s.count('А')+s.count('Е')>s.count('П')+s.count('Р')+s.count('Л'):
##        k+=1
##print(k)

##7
##for x in product('КАМЫШ', repeat=7):
##    s = ''.join(x)
##    if s[0] not in 'АЫ' and 'КК' not in s and 'АА' not in s and 'ММ' not in s and 'ЫЫ' not in s and 'ШШ' not in s:
##        k+=1
##print(k)

##1
##for x in product('МОРС', repeat=5):
##    s = ''.join(x)
##    k+=1
##    if s.count('М')==1 and s.count("Р")==2:
##        print(k,s)

##2
##for x in product('АКЛО', repeat=5):
##    s = ''.join(x)
##    k+=1
##    if k==423:
##        print(s)

##3
##for x in permutations('ПРИКАЗ'):
##    s = ''.join(x)
##    if 'ИА' not in s and 'АИ' not in s:
##        k+=1
##print(k)

##4
##for x in product('ИНФА', repeat=8):
##    s = ''.join(x)
##    if s[0] in 'ИА' and s[-1] in 'ИА' and s.count('Н')<=3:
##        k+=1
##print(k)

##5
##c1=[''.join(i) for i in permutations('02468',r=2)]
##c2=[''.join(i) for i in permutations('13579',r=2)]
##c = c1+c2
##for x in permutations('0123456789', r=8):
##    s = ''.join(x)
##    if int(s)%5==0 and s[0]!='0':
##        f = True
##        for i in c:
##            if i in s:
##                f =False
##        if f==True: k+=1
##print(k)

##6
##for x in permutations('ВЫЧМАТ'):
##    s = ''.join(x)
##    if 'ВВ' not in s and 'ЫЫ' not in s and 'ЧЧ' not in s and 'ММ' not in s and 'АА' not in s and 'ТТ' not in s:
##        k+=1
##print(k)

##7
##for x in product("ПРОГА", repeat=5):
##    s = ''.join(x)
##    if s.count('Г')<=2: k+=1
##print(k)

##8
##for x in product('КВАС', repeat=6):
##    s = ''.join(x)
##    if s.count('А')==1: k+=1
##print(k)

##1
##for x in product('АИНФ',repeat=5):
##    s=''.join(x)
##    k+=1
##    if s=='НФАИА':
##        print(k,s)

##2
##for x in product('АКОР',repeat=5):
##    s=''.join(x)
##    k+=1
##    if k==318:print(s)

##3
##for x in product('СУМКА',repeat=8):
##    s=''.join(x)
##    if s[-1]=='У' and s[0] in 'УА' and s[2] in 'АК' and s[3] in 'СМК':k+=1
##print(k)

##4
##for x in product('ЖАСМИН',repeat=5):
##    s=''.join(x)
##    if s.count('М')>=2:k+=1
##print(k)

##5
##for x in product('ЖЕМЧУГ',repeat=6):
##    s=''.join(x)
##    if s.count('Ч')==2:k+=1
##print(k)

##6
##c1=[]
##for x in permutations('0246',r=2):
##    s = ''.join(x)
##    c1.append(s)
##c2=[]
##for x in permutations('1357',r=2):
##    s = ''.join(x)
##    c2.append(s)
##c = c1+c2
##f=True
##for x in permutations('01234567',r=7):
##    s =''.join(x)
##    if s[0]!='0':
##        f=True
##        for i in c:
##            if i in s:f=False
##        if f ==True:k+=1
##print(k)

##7
##for x in product('ВЕРБЛЮД',repeat=5):
##    s=''.join(x)
##    if s.count('Б')<=1 and s[0]!='Б' and s[-1]!='Б' and 'ЮБ' not in s and 'БЮ' not in s: k+=1
##print(k)









