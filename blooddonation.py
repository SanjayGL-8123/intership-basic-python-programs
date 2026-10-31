age=int(input("enter age:"))
weight=int(input("enter weight"))
if age>=18:
    if weight>=50:
        print("you are eligible to donate blood")
    else:
        print("you are not eligible to donate blood, you are under weight")
else:
    print("you are not eligible to donate blood, you are under age")