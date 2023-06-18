##1
##from functools import *
##@lru_cache(None)
##def f(s,e):
##    if s>e: return 0
##    if s==e: return 1
##    if s<e: return f(s+1,e) + f(s+4,e)
##print(f(1,128))

##2
##def f(s,e):
##    if s>e: return 0
##    if s==e: return 1
##    if s<e: return f(s+2,e)+f(s*4,e)+f(s+1,e)
##print(f(2,25))

##3
##def f(s,e):
##    if s>e: return 0
##    if s==e: return 1
##    if s<e: return f(s+2,e)+f(s+3,e)+f(s+s-1,e)
##print(f(2,11))

##4
##def f(s,e):
##    if s<e: return 0
##    if s==e: return 1
##    if s>e and s>4: return f(s-1,e)+f(s-3,e)+f(s%4,e)
##    else: return f(s-1,e)+f(s-3,e)
##print(f(22,2))

##5
##def f(s,e):
##    if s<e: return 0
##    if s==e: return 1
##    if s>e and s%3==0 and s%2==0: return f(s-3,e)+f(s//3,e)+f(s//2,e)
##    if s>e and s%3==0 and s%2!=0: return f(s-3,e)+f(s//3,e)
##    if s>e and s%3!=0 and s%2==0: return f(s-3,e)+f(s//2,e)
##    if s>e: return f(s-3,e)
##print(f(30,3))

##6
##def f(s,e):
##    if s<e: return 0
##    if s==e: return 1
##    if s>e and s>4: return f(s-1,e)+f(s-3,e)+f(s%4,e)
##    return f(s-1,e)+f(s-3,e)
##print(f(22,2))

##7
##def f(s,e):
##    if s>e: return 0
##    if s==e: return 1
##    if s<e: return f(s+3,e)+f(s*2,e)
##print(f(12,30)*f(30,96))

##8
##def f(s,e):
##    if s>e: return 0
##    if s==e: return 1
##    if s<e: return f(s+1,e)+f(s+2,e)+f(s*3,e)
##print(f(2,10)*f(10,13))

##9
##def f(s,e):
##    if s>e: return 0
##    if s==e: return 1
##    if s<e: return f(s+1,e)+f(s+4,e)+f(s*4,e)
##print(f(3,11)*f(11,27))

##10
##def f(s,e):
##    if s>e or s==14: return 0
##    if s==e: return 1
##    if s<e: return f(s+1,e)+f(s*2,e)
##print(f(1,19))

##11
##def f(s,e):
##    if s>e or s==26: return 0
##    if s==e: return 1
##    if s<e: return f(s+1,e)+f(2*s+1,e)
##print(f(1,27))

##12
##def f(s,e):
##    if s>e or s==13: return 0
##    if s==e: return 1
##    if s<e: return f(s+2,e)+f(s*3,e)+f(s+s%2+2,e)
##print(f(1,15))

##13
##def f(s,e,k):
##    if s<e: return 0
##    if s==e and k==9: return 1
##    if s==e and k!=9: return 0
##    if s>e and s%2==0: return f(s-3,e,k+1)+f(s-1,e,k+1)+f(s//2,e,k+1)
##    return f(s-3,e,k+1)+f(s-1,e,k+1)
##print(f(33,12,0))

##14
##def f(s,e):
##    if s>e: return 0
##    if s==e: return 1
##    if s<e and s%2==0 and s%3==0: return f(s//2,e,k+1)+f(s+1,e,k+1)+f(s+s//3,e,k+1)
##    if s<e and s%2==0 and s%3!=0: return f(s//2,e,k+1)+f(s+1,e,k+1)
##    if s<e and s%2!=0 and s%3==0: return f(s+1,e,k+1)+f(s+s//3,e,k+1)
##    if s<e: return f(s+1,e,k+1)
##print(f(1,60,0))

##8
##def f(s,e):
##    if s<e: return 0
##    if s==e: return 1
##    if s>e: return f(s-5,e)+f(s-7,e)
##print(f(101,37)*f(37,20))

##9
##def f(s,e):
##    if s>e: return 0
##    if s==e: return 1
##    if s<e: return f(s+1,e)+f(s+4,e)+f(s*2,e)
##print(f(10,18)*f(18,36))

##10
##def f(s,e):
##    if s>e or s==40: return 0
##    if s==e: return 1
##    if s<e: return f(s+1,e)+f(s*3,e)
##print(f(1,16)*f(16,60))

##11
##def f(s,e):
##    if s>e or s==10 or s==20: return 0
##    if s==e: return 1
##    if s<e: return f(s+1,e)+f(s+2,e)+f(s*3,e)
##print(f(3,15)*f(15,30))

##12
##def f(s,e):
##    if s>e or s==13: return 0
##    if s==e: return 1
##    if s<e: return f(s+1,e)+f(s*2,e)+f(s+2,e)
##print(f(3,8)*f(8,23))
##def f(s,e):
##    if s>e or s==8: return 0
##    if s==e: return 1
##    if s<e: return f(s+1,e)+f(s*2,e)+f(s+2,e)
##print(f(3,13)*f(13,23))

##13
##def f(s,e):
##    if s>e or s==14: return 0
##    if s==e: return 1
##    if s<e: return f(s+1,e)+f(s*2,e)+f(s+3,e)
##print(f(1,9)*f(9,20))

##14
##def f(s,e):
##    if s>e: return 0
##    if s==e: return 1
##    if s<e: return f(s+1,e)+f(s+2,e)+f(s*2,e)
##print(f(3,9)*f(9,11)*f(11,13))

##15
##def f(s,e):
##    if s<e: return 0
##    if s==e: return 1
##    if s>e: return f(s-2,e)+f(s-3,e)+f(s**0.5,e)
##print(f(25,3))

##16
##def f(s,e):
##    if s>e or s==8 or s==15: return 0
##    if s==e: return 1
##    if s<e: return f(s+1,e)+f(s+2,e)+f(s*3,e)
##print(f(3,10)*f(10,22))

##17
##def f(s,e):
##    if s>e: return 0
##    if s==e: return 1
##    if s<e: return f(s+3,e)+f(s*2,e)
##print(f(12,96))











