"""
functions
"""
def greet():
    print("Welcome")
greet()
greet()
def add(n1,n2):
    res = n1+n2
    print("result of addition is ",res)
add(100,200)
add(50,100)
print("simple interest")
def simpleinterest(p,r,t):
    si = (p*r*t)/100
    print(" simple interest is ",si)
#simpleinterest(10000,6,1)
p=float(input("Enter principal amount"))
r=float(input("Enter rate of interest"))
t=int(input("Enter time in years"))
simpleinterest(p,r,t)




