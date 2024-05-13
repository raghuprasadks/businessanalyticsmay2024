"""
Simple interest with user inputs
"""
print("Simple interest calculator")
p = int(input("enter principal amount"))
roi = float(input("enter rate of interest"))
t = int(input("enter time in year "))
si=(p*roi*t)/100
print(" simple interest is ",si)

