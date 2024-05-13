"""
Simple calculator
"""
n1 = int(input("enter first number"))
n2 = int(input("enter second number"))
oper = input("enter operator (+,-,*,/) ")
if (oper == "+"):
    res = n1+n2
    print(n1,oper,n2," = ",res)
elif (oper == "-"):
    res = n1-n2
    print(n1,oper,n2," = ",res)
else:
    print("invalid operator")