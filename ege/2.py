from itertools import *
##print('x y z')
##for x in 0,1:
##    for y in 0,1:
##        for z in 0,1:
##            t = ((y or z) <= x) or (x == z)
##            if t==0:
##                print(x,y,z)
##print('x y z w')
##for x in 0,1:
##    for y in 0,1:
##        for z in 0,1:
##            for w in 0,1:
##                t = (x== (not z)) <= ((x or w) == y)
##                if t==0:
##                    print(x,y,z,w)
##print('x y z w')
##for x in 0,1:
##    for y in 0,1:
##        for z in 0,1:
##            for w in 0,1:
##                t = ((y<=x) or ((not z) and w)) == (w==x)
##                if t==1:
##                    print(x,y,z,w)
##print('x y z w')
##for x in 0,1:
##    for y in 0,1:
##        for z in 0,1:
##            for w in 0,1:
##                t = ((x or (not y)) and ((not z)==w)) <= (y and z)
##                if t==0:
##                    print(x,y,z,w)
##print('x y z w')
##for x in 0,1:
##    for y in 0,1:
##        for z in 0,1:
##            for w in 0,1:
##                t = ((x<=y) or (y==w)) and ((x or z) == w)
##                if t==1:
##                    print(x,y,z,w)

##print('x y z w')
##for x in 0,1:
##    for y in 0,1:
##        for z in 0,1:
##            for w in 0,1:
##                t = (x or (not y)) and (not (y==z)) and w
##                if t==1:
##                    print(x,y,z,w)

##print('x y z')
##for x in 0,1:
##    for y in 0,1:
##        for z in 0,1:
##            t = ((not x) and y and z) or ((not x) and (not y) and z) or ((not x) and (not y) and (not z))
##            if t==1:
##                print(x,y,z)

##print('x y z w')
##for x in 0,1:
##    for y in 0,1:
##        for z in 0,1:
##            for w in 0,1:
##                t = (((not x) and y) == z) and w
##                if t==1:
##                    print(x,y,z,w)

##print('x y z w')
##for x in 0,1:
##    for y in 0,1:
##        for z in 0,1:
##            for w in 0,1:
##                t = (x <= (y and (not z))) or w
##                if t==0:
##                    print(x,y,z,w)

##print('x y z w')
##for x in 0,1:
##    for y in 0,1:
##        for z in 0,1:
##            for w in 0,1:
##                t = (x and (not y)) or (x==z) or w
##                if t==0:
##                    print(x,y,z,w)

##print('x y z')
##for x in 0,1:
##    for y in 0,1:
##        for z in 0,1:
##            t = ((not x) and y and z) or ((not x) and (not z))
##            if t==1:
##                print(x,y,z)

##print('x y z w')
##for x in 0,1:
##    for y in 0,1:
##        for z in 0,1:
##            for w in 0,1:
##                t = (not y) and x and ((not z) or w)
##                if t==1:
##                    print(x,y,z,w)

##print('x y z w')
##for x in 0,1:
##    for y in 0,1:
##        for z in 0,1:
##            for w in 0,1:
##                t = (y <= (x or z)) and (z <=y)
##                if t==0:
##                    print(x,y,z,w)

##print('x y z')
##for x in 0,1:
##    for y in 0,1:
##        for z in 0,1:
##            t = not(x == (y <=z))
##            print(x,y,z, t==1)

##def f(x,y,z):
##    return (x<=y) and (y<=z)
##
##table = [(1,0,0),(1,0,1)]
##
##for p in permutations('xyz'):
##    if [f(**dict(zip(p,row))) for row in table] == [0,1]:
##        print(p)
##def f(x,y,z):
##    return ((not x) and y and z) or ((not x) and (not z))
##
##table = [(0,0,0),(1,0,0),(1,1,0)]
##
##for p in permutations('xyz'):
##    if [f(**dict(zip(p,r))) for r in table] == [1,1,1]:
##        print(p)
##def f(x,y,z,w):
##    return (not y) or x or ((not z) and w)
##
##table = [(0,0,0,1),(0,0,1,1),(1,0,1,1)]
##
##for p in permutations('xyzw'):
##    if [f(**dict(zip(p,r))) for r in table] == [0,0,0]:
##        print(p)
##def f(a,b,c,d):
##    return (a <= d) and (not (b <= c))
##
##table = [(1,0,1,0),(1,1,1,0),(0,0,1,0)]
##
##for p in permutations('abcd'):
##    if [f(**dict(zip(p,r))) for r in table] == [1,1,1]:
##        print(p)
##def f(x,y,z,w):
##    return ((y <= x) or ((not z) and w)) == (w==x)
##
##for a in product([0,1], repeat=3):
##    table = [(a[0],1,0,0),(0,0,0,1),(0,1,a[1],a[2])]
##    if len(table) == len(set(table)):
##        for p in permutations('xyzw'):
##            if [f(**dict(zip(p,r))) for r in table] == [1,1,1]:
##                print(p)

##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                t = (y<=x) or (not ((x<=z) and (z<=x))) and (not w)
##                if t==0:
##                    print(x,y,z,w)

##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                t = (not w) and ((y or z) <= ((not x) and y))
##                if t==1:
##                    print(x,y,z,w)

##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                t = ((w <=y) or (not (y<=z))) and (not x) and (not(x == z))
##                if t==1:
##                    print(x,y,z,w)

##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                t = (x <= y) or (not (w <=z))
##                if t==0:
##                    print(x,y,z,w)

##print('a b c d')
##for a in range(2):
##    for b in range(2):
##        for c in range(2):
##            for d in range(2):
##                t = ((a and b) == (not c)) and  (b<=d)
##                if t==1:
##                    print(a,b,c,d)

##def f(a,b,c,d):
##    return ((a and b) == (not c)) and (b <= d)
##table = [(1,0,0,0),(1,0,1,0),(1,0,1,1),(1,1,0,0)]
##
##for p in permutations('abcd'):
##    if [f(**dict(zip(p,r))) for r in table] == [1,1,1,1]:
##        print(p)

##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                t = (not (z and (not w))) or ((z<=w) == (x<=y))
##                if t==0:
##                    print(x,y,z,w)

##print('a b c d')
##for a in range(2):
##    for b in range(2):
##        for c in range(2):
##            for d in range(2):
##                t = ((not a) and (not b)) or (b==c) or d
##                if t==0:
##                    print(a,b,c,d)

##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                t = ((z <= x) and (x <= w)) or (y == (z or x))
##                if t==0:
##                    print(x,y,z,w)

##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                t = (x and z) or ((w<=x)==(z<=y))
##                if t==0:
##                    print(x,y,z,w)

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                t = (x == (not z)) <= ((x or w) == y)
                if t==0:
                    print(x,y,z,w)


































