n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    if y>x:
        print("0")
    else:
        print(x-y)
