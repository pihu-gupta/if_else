age =int(input("enter a age"))
sex =str(input("enter a sex"))
if sex=="f":
    print("urban area")
elif sex=="m" and age>=20 and age<=40:
    print("anywhere")
elif sex=="m" and age>=40 and age<=60:
    print("only urben area")
else:
    print("error")
    