user= str(input("enter tha name"))
password=int(input("enter tha password"))
if user=="pihu" and password==2525:
    print("your account")
elif user!="pihu" and password!=2525:
    print("this is not your account ")
elif user!="pihu":
    print("name is rong")
elif password!=2525:
    print("passwoed is rong")
if user=="lovely" and password==0000:
    print("creat a new account")
    