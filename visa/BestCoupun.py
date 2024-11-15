amt=int(input())
d=amt//10
if d>100:
    bill=amt-d
else:
    bill=amt-100
print(bill)
