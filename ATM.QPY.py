num1= input(("walcame"))
if num1=="bank":
    print("walcame to central bank")
    num2= input(("chus tha language"))
    if num2=="english":
        print("next")
        num3= int(input("enter tha pin"))
        if num3==1234:
            print("next")              
            num4= int(input("enter tha account number"))
            if num4==252525:
                print("next")
                num5= input(("enter tha saveing or crrant"))
                if num5=="saveing":
                    print("it is saveing account")
                    num6= int(input("enter tha amount"))
                    if num6<=100000:
                        print("take a money")
                    else:
                        print("not bal")
                else:
                    print("carrnte account")
            else:
                print("invelde account number")
        else:
            print("inveld pin")
    else:
        print("not language")
else:
    print("this is not bank")