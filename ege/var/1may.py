##2
##print('x y w z')
##for x in range(2):
##    for y in range(2):
##        for w in range(2):
##            for z in range(2):
##                t =(x==(w or y)) or ((w<=z)and(y<=w))
##                if t ==0:
##                    print(x,y,w,z)

#5
##for n in range(1,100):
##    b = bin(n)[2:]
##    if int(b)%2==0: b = '1' + b + '0'
##    else: b = '11' + b + '11'
##    r = int(b,2)
##    if r>52:
##        print(n)

#8
##from itertools import *
##s = 'ИВАН'
##c=0
##for x in product(s,repeat=5):
##    if x.count('И')>=1:
##        c+=1
##print(c)

#12
##s='1'*84
##while '11111' in s:
##    s = s.replace('222','1',1)
##    s = s.replace('111','2',1)
##print(s)

#14
##s = 125+25**3+5**9
##a=[]
##while s>0:
##    a = [s%5] + a
##    s//=5
##print(a.count(0))

#15
def f(x,y): return ((x<=9)<=(x*x<=a)) and ((y*y<=a)<=(y<=9))

for a in range(110):
    if all(f(x,y) for x in range(1000) for y in range(1000)):
           print(a)









































