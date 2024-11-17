x,y=map(str,input().split())
arr=["R","P","S"]
if x in arr:
    if x=="R" and y=="P" or x=="P" and y=="S" or x=="S" and y=="R":
        print("Charan")
    elif x=="R" and y=="S" or x=="P" and y=="R" or x=="S" and y=="P":
        print("Vignesh")
    else:
        print("NULL")
else:
    print("NULL")
