x,y,z=map(int,input().split())
ttime=z*24*60
timeneeded=x*y
if timeneeded<=ttime:
    print("YES")
else:
    print("NO")
