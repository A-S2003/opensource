n,m=map(int,input().split())
arr=list(map(int,input().split()))
sum1=0
sum2=0
for i in range(n):
    if arr[i]%m==0:
        sum1+=arr[i]
    else:
        sum2+=arr[i]
print(sum1-sum2)
