#2
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((y==z) or (not(w)) or ((not(x)) and z)) == 0:
#                     print(x,y,z,w)

#5
# for i in range(10000,100000):
#     i = str(i)
#     s1 = int(i[0]) + int(i[2]) + int(i[4])
#     s2 = int(i[1]) + int(i[3])
#     s = str(min(s1,s2)) + str(max(s1,s2))
#     if s == '723':
#         print(i)
#         break


#6
# from turtle import *
# color('black', 'red')
# m = 100
# begin_fill()
# left(90)
# for i in range(3):
#     forward(111*m)
#     right(120)
# end_fill()
# canvas = getcanvas()
# c = 0
# for y in range(-120*m,120*m,m):
#     for x in range(-120*m,120*m,m):
#         item = canvas.find_overlapping(x,y,x,y)
#         if len(item) == 1 and item[0] == 5:
#             c+=1  
# print(c)
# done()
# exit()

#8
# import itertools
# s = 'АОУ'
# s1='МТР'
# s2 = 'ЕО'
# c =1
# for x in itertools.product(s, repeat=5):
#     a = ''.join(x)
#     print(c, a)
#     c+=1
# print(c)

#12
# s = '1'*101
# while '111' in s:
#     if '111' in s:
#         s = s.replace('111', '22',1)
#         s = s.replace('222', '11',1)
# print(s)

# def k(s):
#     while '111' in s:
#         s = s.replace('111','2',1)
#         s = s.replace('222','1',1)
#     return s
# for x in range(1000):
#     s = '1'*80 + '1'*x
#     if k(s) == '21':
#         print(x)

#14
# for n in range(2,100):
#     m=86
#     a=[]
#     while m>0:
#         a = [m%n] +a
#         m//=n
#     if a[:2] == [2,2]:
#         print(n, a)

# for x in range(2,100):
#     if (x+2)*(x+3) == (2*x**2+x+1):
#         print(x)

# for n in range(2,100):
#     a=int(f'123{n}5',13) + int(f'1{n}233',13)
#     if a%12==0:
#         print(a//12)

# b = 49**7+7**21-7
# a=[]
# while b>0:
#     a = [b%7]+a
#     b//=7
# print(a)
# print(a.count(6))

#19
# def f(s,m):
#     if 45<=s<=112: return m%2==0
#     if s>112: return m%2!=0
#     if m==0: return 0
#     h = [f(s+2, m-1), f(s*3,m-1)]
#     return any(h) if (m-1)%2 == 0 else all(h)
# print('19)',[s for s in range(1,45) if f(s,2)])
# print('20)',[s for s in range(1,45) if not f(s,1) and f(s,3)])
# print('21)',[s for s in range(1,45) if not f(s,2) and f(s,4)])

# def f(a,b,m):
#     if a+b>=45: return m%2==0
#     if m==0: return 0
#     h = [f(a+1, b, m-1),f(a*3, b, m-1),f(a, b+1, m-1),f(a, b*3, m-1)]
#     return any(h) if (m-1)%2==0 else all(h)
# print('19)', [s for s in range(1,41) if f(4,s,2)]) #all -> any
# print('20)', [s for s in range(1,41) if not f(4,s,1) and f(4,s,3)]) 
# print('21)', [s for s in range(1,41) if not f(4,s,2) and f(4,s,4)]) 

# def f(a,b,m):
#     if a+b<=20: return m%2==0
#     if m==0: return 0
#     h = [f(a-1, b, m-1),f((a+1)//2, b, m-1),f(a, b-1, m-1),f(a, (b+1)//2, m-1)]
#     return any(h) if (m-1)%2==0 else all(h)
# print('19)', [s for s in range(11,1000) if f(10,s,2)]) #all -> any
# print('20)', [s for s in range(11,1000) if not f(10,s,1) and f(10,s,3)]) 
# print('21)', [s for s in range(11,1000) if not f(10,s,2) and f(10,s,4)]) 