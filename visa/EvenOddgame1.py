n=int(input())
s=str(n)
totalsum=0
for i in s:
    totalsum=totalsum+int(i)
if totalsum%2==0:
    print("Vignesh")
else:
    print("Charan")
