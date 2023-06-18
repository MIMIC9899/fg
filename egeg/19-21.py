##1-3
##def f(s,m):
##    if s>=38: return m%2==0
##    if m==0: return 0
##    h = [f(s+2,m-1),f(s*2,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,38) if f(s,2)])
##print([s for s in range(1,38) if not f(s,1) and f(s,3)])
##print([s for s in range(1,38) if not f(s,2) and f(s,4)])

##4-6
##def f(s,m):
##    if s>=47: return m%2==0
##    if m==0: return 0
##    h = [f(s+2,m-1),f(s*3,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,47) if f(s,2)])
##print([s for s in range(1,47) if not f(s,1) and f(s,3)])
##print([s for s in range(1,47) if not f(s,2) and f(s,4)])

##7-9
##def f(s,m):
##    if s>=55: return m%2==0
##    if m==0: return 0
##    h = [f(s+4,m-1),f(s*2,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,55) if f(s,2)])
##print([s for s in range(1,55) if not f(s,1) and f(s,3)])
##print([s for s in range(1,55) if not f(s,2) and f(s,4)])

##10-12
##def f(s,m):
##    if s>=29: return m%2==0
##    if m==0: return 0
##    h = [f(s+1,m-1),f(s+2,m-1),f(s*2,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,55) if f(s,2)])
##print([s for s in range(1,55) if not f(s,1) and f(s,3)])
##print([s for s in range(1,55) if not f(s,2) and f(s,4)])

##13-15
##def f(s,m):
##    if s>=61: return m%2==0
##    if m==0: return 0
##    h = [f(s+3,m-1),f(s+5,m-1),f(s*3,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,61) if f(s,2)])
##print([s for s in range(1,61) if not f(s,1) and f(s,3)])
##print([s for s in range(1,61) if not f(s,2) and f(s,4)])

##1-3
##def f(a,b,m):
##    if a+b>=73 : return m%2==0
##    if m==0: return 0
##    h = [f(a+1,b,m-1),f(a,b+1,m-1),f(a*2,b,m-1),f(a,b*2,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,62) if f(11,s,2)])
##print([s for s in range(1,62) if not f(11,s,1) and f(11,s,3)])
##print([s for s in range(1,62) if not f(11,s,2) and f(11,s,4)])

##4-6
##def f(a,b,m):
##    if a+b>=105:return m%2==0
##    if m==0: return 0
##    h = [f(a+1,b,m-1),f(a,b+1,m-1),f(a*4,b,m-1),f(a,b*4,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,101) if f(4,s,2)])
##print([s for s in range(1,101) if not f(4,s,1) and f(4,s,3)])
##print([s for s in range(1,101) if not f(4,s,2) and f(4,s,4)])

##7-9
##def f(a,b,m):
##    if a+b>=108:return m%2==0
##    if m==0: return 0
##    h = [f(a+1,b,m-1),f(a,b+1,m-1),f(a*4,b,m-1),f(a,b*4,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,102) if f(6,s,2)])
##print([s for s in range(1,102) if not f(6,s,1) and f(6,s,3)])
##print([s for s in range(1,102) if not f(6,s,2) and f(6,s,4)])

##10-12
##def f(a,b,m):
##    if a+b>=78:return m%2==0
##    if m==0: return 0
##    h = [f(a+3,b,m-1),f(a,b+3,m-1),f(a*2,b,m-1),f(a,b*2,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,71) if f(7,s,2)])
##print([s for s in range(1,71) if not f(7,s,1) and f(7,s,3)])
##print([s for s in range(1,71) if not f(7,s,2) and f(7,s,4)])

##13-15
##def f(s,m):
##    if s>=46: return m%2==0
##    if m==0: return 0
##    h = [f(s+3,m-1),f(s*2,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,46) if f(s,2)])
##print([s for s in range(1,46) if not f(s,1) and f(s,3)])
##print([s for s in range(1,46) if not f(s,2) and f(s,4)])

##1-3
##def f(s,m):
##    if s>=71: return m%2==0
##    if m==0: return 0
##    h = [f(s+1,m-1),f(s*3,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,71) if f(s,2)])
##print([s for s in range(1,71) if not f(s,1) and f(s,3)])
##print([s for s in range(1,71) if not f(s,2) and f(s,4)])

##4-6
##def f(a,b,m):
##    if a+b>=48:return m%2==0
##    if m==0: return 0
##    h = [f(a+1,b,m-1),f(a,b+1,m-1),f(a*2,b,m-1),f(a,b*2,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,44) if f(4,s,2)])
##print([s for s in range(1,44) if not f(4,s,1) and f(4,s,3)])
##print([s for s in range(1,44) if not f(4,s,2) and f(4,s,4)])

##1-3
##def f(s,m):
##    if 64<=s<=84: return m%2==0
##    if s>84: return m%2!=0
##    if m==0: return 0
##    h = [f(s+2,m-1),f(s*3,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,64) if f(s,2)])
##print([s for s in range(1,64) if not f(s,1) and f(s,3)])
##print([s for s in range(1,64) if not f(s,2) and f(s,4)])

##4-6
##def f(a,b,m):
##    if a+b>=63:return m%2==0
##    if m==0: return 0
##    h = [f(a+2,b,m-1),f(a,b+2,m-1),f(a*3,b,m-1),f(a,b*3,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,56) if f(7,s,2)])
##print([s for s in range(1,56) if not f(7,s,1) and f(7,s,3)])
##print([s for s in range(1,56) if not f(7,s,2) and f(7,s,4)])

##def f(a,b,m):
##    if a==b: return m%2==0
##    if m==0: return 0
##    if a<b: h = [f(a+1,b,m-1),f(a+3,b,m-1)]
##    else: h = [f(a,b+1,m-1),f(a,b+3,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)

##1-3
##def f(s,m):
##    if s>=50: return m%2==0
##    if m==0: return 0
##    h = [f(s+1,m-1),f(s+2,m-1),f(s*3,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,50) if f(s,2)])
##print([s for s in range(1,50) if not f(s,1) and f(s,3)])
##print([s for s in range(1,50) if not f(s,2) and f(s,4)])

##4-6
##def f(a,b,m):
##    if a+b>=42:return m%2==0
##    if m==0: return 0
##    h = [f(a+1,b,m-1),f(a,b+1,m-1),f(a*2,b,m-1),f(a,b*2,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,35) if f(7,s,2)])
##print([s for s in range(1,35) if not f(7,s,1) and f(7,s,3)])
##print([s for s in range(1,35) if not f(7,s,2) and f(7,s,4)])

##1-3
##def f(s,m):
##    if s>=78: return m%2==0
##    if m==0: return 0
##    h = [f(s+1,m-1),f(s+5,m-1),f(s*3,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,78) if f(s,2)])
##print([s for s in range(1,78) if not f(s,1) and f(s,3)])
##print([s for s in range(1,78) if not f(s,2) and f(s,4)])

##4-6
##def f(a,b,m):
##    if a+b>=42: return m%2==0
##    if m==0: return 0
##    h = [f(a+1,b,m-1),f(a,b+1,m-1),f(a*2,b,m-1),f(a,b*2,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,35) if f(7,s,2)])
##print([s for s in range(1,35) if not f(7,s,1) and f(7,s,3)])
##print([s for s in range(1,35) if not f(7,s,2) and f(7,s,4)])

##7-9
##def f(a,b,m):
##    if a*b>=1250: return m%2==0
##    if m==0: return 0
##    h = [f(a+1,b,m-1),f(a,b+1,m-1),f(a*5,b,m-1),f(a,b*5,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,313) if f(4,s,2)])
##print([s for s in range(1,313) if not f(4,s,1) and f(4,s,3)])
##print([s for s in range(1,313) if not f(4,s,2) and f(4,s,4)])

##10-12
##def f(s,m):
##    if s<=11: return m%2==0
##    if m==0: return 0
##    h = [f(s-1,m-1),f(s-3,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(12,100) if f(s,2)])
##print([s for s in range(12,100) if not f(s,1) and f(s,3)])
##print([s for s in range(12,100) if not f(s,2) and f(s,4)])

##13-15
##def f(a,b,m):
##    if a+b<=34: return m%2==0
##    if m==0: return 0
##    h = [f(a-1,b,m-1),f(a,b-1,m-1),f(a//2,b,m-1),f(a,b//2,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(13,313) if f(22,s,2)])
##print([s for s in range(13,313) if not f(22,s,1) and f(22,s,3)])
##print([s for s in range(13,313) if not f(22,s,2) and f(22,s,4)])

##16-18
##def f(a,b,m):
##    if a+b>=199: return m%2==0
##    if m==0: return 0
##    h = [f(a,b*2,m-1),f(b,a,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,100) if f(99,s,2)])
##print([s for s in range(1,100) if not f(99,s,1) and f(99,s,3)])
##print([s for s in range(1,100) if not f(99,s,2) and f(99,s,4)])

##19-21
##def f(s,m):
##    if 45<=s<=112: return m%2==0
##    if s>112: return m%2!=0
##    if m==0: return 0
##    h = [f(s+2,m-1),f(s*3,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,45) if f(s,2)])
##print([s for s in range(1,45) if not f(s,1) and f(s,3)])
##print([s for s in range(1,45) if not f(s,2) and f(s,4)])

##22-24
##def f(s,m):
##    if s>=42: return m%2==0
##    if m==0: return 0
##    h = [f(s+2,m-1),f(s*3,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,42) if f(s,2)])
##print([s for s in range(1,42) if not f(s,1) and f(s,3)])
##print([s for s in range(1,42) if not f(s,2) and f(s,4)])

##1-3
##def f(s,m):
##    if s>=58: return m%2==0
##    if m==0: return 0
##    h = [f(s+1,m-1),f(s*2,m-1),f(s*4,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,58) if f(s,2)])
##print([s for s in range(1,58) if not f(s,1) and f(s,3)])
##print([s for s in range(1,58) if not f(s,2) and f(s,4)])

##4-6
##def f(a,b,m):
##    if a+b>=51: return m%2==0
##    if m==0: return 0
##    h = [f(a+2,b,m-1),f(a,b+2,m-1),f(a+3,b,m-1),f(a,b+3,m-1),f(a*2,b,m-1),f(a,b*2,m-1),]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,46) if f(5,s,2)])
##print([s for s in range(1,46) if not f(5,s,1) and f(5,s,3)])
##print([s for s in range(1,46) if not f(5,s,2) and f(5,s,4)])

##7-9
##def f(a,b,m):
##    if a*b>=1000: return m%2==0
##    if m==0: return 0
##    h = [f(a+1,b,m-1),f(a,b+1,m-1),f(a*3,b,m-1),f(a,b*3,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,84) if f(12,s,2)])
##print([s for s in range(1,84) if not f(12,s,1) and f(12,s,3)])
##print([s for s in range(1,84) if not f(12,s,2) and f(12,s,4)])

##10-12
##def f(s,m):
##    if s<=7: return m%2==0
##    if m==0: return 0
##    h = [f(s-1,m-1),f(s-3,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(8,58) if f(s,2)])
##print([s for s in range(8,58) if not f(s,1) and f(s,3)])
##print([s for s in range(8,58) if not f(s,2) and f(s,4)])

##13-15
##def f(a,b,m):
##    if a+b<=32: return m%2==0
##    if m==0: return 0
##    h = [f(a-1,b,m-1),f(a,b-1,m-1),f((a+1)//2,b,m-1),f(a,(b+1)//2,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(23,840) if f(10,s,2)])
##print([s for s in range(23,840) if not f(10,s,1) and f(10,s,3)])
##print([s for s in range(23,840) if not f(10,s,2) and f(10,s,4)])

##16-18
##def f(s,m):
##    if s>=43: return m%2==0
##    if m==0: return 0
##    h = [f(s+1,m-1),f(s+2,m-1),f(s*3,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,43) if f(s,2)])
##print([s for s in range(1,43) if not f(s,1) and f(s,3)])
##print([s for s in range(1,43) if not f(s,2) and f(s,4)])

##19-21
##def f(s,m):
##    if 45<=s<=112: return m%2==0
##    if s>112: return m%2!=0
##    if m==0: return 0
##    h = [f(s+2,m-1),f(s*3,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,45) if f(s,2)])
##print([s for s in range(1,45) if not f(s,1) and f(s,3)])
##print([s for s in range(1,45) if not f(s,2) and f(s,4)])

##22-24
##def f(a,b,m):
##    if a+b>=100: return m%2==0
##    if m==0: return 0
##    h = [f(a+1,b,m-1),f(a,b+1,m-1),f(a*3,b,m-1),f(a,b*3,m-1)]
##    return any(h) if (m-1)%2==0 else all(h)
##print([s for s in range(1,93) if f(7,s,2)])
##print([s for s in range(1,93) if not f(7,s,1) and f(7,s,3)])
##print([s for s in range(1,93) if not f(7,s,2) and f(7,s,4)])





















