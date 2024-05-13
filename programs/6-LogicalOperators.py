"""
Logical Operators - and,or,not
"""
num1 = 100
num2 = 150
num3 = 75
print("Logical operator - and")
res = (num2 > num1) and (num1 > num3)
print (" (num2 > num1) and (num1 > num3) ",res)
print("Logical operator - or")
res = (num2 < num1) or (num1 > num3)
print (" (num2 > num1) or (num1 > num3) ",res)
print("Logical operator - not")
res = not ((num2 < num1) or (num1 > num3))
print (" not ((num2 > num1) or (num1 > num3)) ",res)

