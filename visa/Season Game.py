x=int(input())
if x>=1 and x<13:
    if x>=3 and x<=5:
        print("Spring")
    elif x>=6 and x<=8:
        print("Summer")
    elif x>=9 and x<=11:
        print("Autumn")
    elif x<3 or x==12:
        print("Winter")
    else:
        print("Invalid")
else:
    print("Invalid")
