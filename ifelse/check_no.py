#Constraint in-order to check the number complex it must have input end with "h"
n=input()
if n.isalpha():
    print("String")
elif n.isdecimal():
    n=int(n)
    if n==0:
        print("Zero")
    else:
        print("Real")
elif n.endswith("h"):
    n=n.replace("h","")
    if n.isalnum():
        print("Complex")
    if "+" in n or "-" in n:
        for i in n:
            if i=="+":
                n=n.replace("+","")
                break
            if i=="-":
                n=n.replace("-","")
                break
        if n.isalnum():
            print("Complex")
else:
    print("Float")