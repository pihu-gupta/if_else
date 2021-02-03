classes_h=int(input("enter the classes held"))
classes_a=int(input("enter the attended class"))
atten=classes_a/classes_h*100
if atten>=75:
    print("sit in exam")
else:
    print("not sit in exam")