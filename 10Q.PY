costprice =int(input("entar tha cost price"))
tax =int(input("entar tha tax"))
if costprice>100000:
    print("it is tax 15%")
elif costprice>50000 and costprice<=100000:
    print("it is tax 10%")
elif costprice<50000:
    print("it is tax 5%")
else:
    print("it is eqvaly")