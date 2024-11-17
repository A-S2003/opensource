n=int(input())
arr=list(map(int,input().split()))
temp=arr[0]
for i in range(1,n):
    arr[i-1]=arr[i]
arr[-1]=temp
print(" ".join(map(str,arr)))
