def check(un, pw):
    print("this is my function")
    if un == "admin" and pw == "password":
        print("login success")
    else:
        print("login failed")

s1 = input("enter user name \n")
s2 = input("enter password \n")

check(s1, s2)