n=int(input())
Pos=str(input())
d,s=0,0
for i in range(len(Pos)):
    if Pos[i]=='X':
        s=s+1
    else:
        d=d+1
if s==d:
    print(0)
    print(Pos)
elif s>d:
    z=(s-d)/2
    o=z
    for i in range(len(Pos)):
        if i==o:
            break
        Pos.replace('X','x')
    print(o)
    print(Pos)
elif d>s:
    z=(d-s)/2
    o = z
    for i in range(len(Pos)):
        if i==o+1:
            break

        Pos[i].upper()
    print(int(o))
    print(Pos)