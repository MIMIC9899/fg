##1
##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                f = (not w) and (not (z == y)) and (x or y)
##                if f==1:
##                    print(x,y,z,w)

##2
##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                f = (not w) and ((not y) and x or (not z) and y and (not x)) 
##                if f==1:
##                    print(x,y,z,w)

##3
##print('x y z')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            f = (x and (not z)) or ((not y) and (not z))
##            print(x,y,z,f)

##4
##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                f = w and (z == (y and (not x)))
##                if f==1:
##                    print(x,y,z,w)

##5
##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                f = (x == (not y)) <= (z==(y or w))
##                if f==0:
##                    print(x,y,z,w)

##6
##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                f = (x <= y) and ((not z) <= x) or w
##                if f==0:
##                    print(x,y,z,w)

##7
##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                f = ((not z) == x) <= (y == (x or w))
##                if f==0:
##                    print(x,y,z,w)

##1
##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                f = (not (z == x)) and (not x) and ((not (y <= z)) or (w <= y ))
##                if f==1:
##                    print(x,y,z,w)
    
##2
##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                f = (not (x <= y)) or (w <= z)
##                if f==0:
##                    print(x,y,z,w)

##3
##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                f = (not y) and x and (w <= z)
##                if f==1:
##                    print(x,y,z,w)

##4
##print('x y z')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            f = (x or z) <= (x == y)
##            if f==0:
##                print(x,y,z)

##5
##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                f = ((w or x) <= (w and (not z))) and (not y)
##                if f==1:
##                    print(x,y,z,w)

##6
##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                f = (not (x <= y)) <= ((not (w <= z)) and x)
##                if f==0:
##                    print(x,y,z,w)

##1
##print('x y z')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            f = not(z or ((not x) and y))
##            if f==1: print(x,y,z)

##2
##print('x y z')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            f = not(x and (y <= z))
##            if f==0: print(x,y,z)

##3
##print('x y z')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            f = (x and y) or (x and (not y)) or (y and (not z)) or ((not z) and x)
##            if f==0: print(x,y,z)

##4
##print('x y z')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            f = ((not y) <= (x <= (y <= z))) and ((not x) or z)
##            if f==0: print(x,y,z)

##5
##print('x y z')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            f = x and (y == ((not y) <= z))
##            if f==1: print(x,y,z)

##6
##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                f = (x and y) or (y == z) or w
##                if f==0: print(x,y,z,w)

##7
##print('x y z')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            f = (x<=y) and (x or y or (not z)) and ((not x) or z)
##            if f==1: print(x,y,z)

##8
##print('x y z')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            f = not((z or y) <= (z and x))
##            if f==0: print(x,y,z)

##9
##print('x y z')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            f = (z==x) or ((z or y) <= x)
##            if f==0: print(x,y,z)

##10
##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                f = (not z) or (y==w) or ((not w) and x)
##                if f==0: print(x,y,z,w)

##11
##print('x y z')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            f = ((y or z) <= x) or (x == y)
##            if f==0: print(x,y,z)

##12
##print('x y z')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            f = (y == (not x)) <= ((z or x) == y)
##            if f==0: print(x,y,z)

##13
##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                f = (not x) and ((not y) and (not z) or z and w)
##                if f==1: print(x,y,z,w)

##14
##print('x y z w')
##for x in range(2):
##    for y in range(2):
##        for z in range(2):
##            for w in range(2):
##                f = x and (z and w or (not z) and (y==w))
##                if f==1: print(x,y,z,w)









