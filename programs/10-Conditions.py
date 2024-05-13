"""
Conditional Statements
if <condition>
action
else
action
"""
age = int(input("enter your age"))
if (age>=18):
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

runs = int(input("enter runs scored by a player"))
if (runs < 50):
    print("Below 50")
elif(runs >=50 and runs<100):
    print("Fifty")
elif(runs >=100 and runs<200):
    print("Century")
else:
    print("above century")
