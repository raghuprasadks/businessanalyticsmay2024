"""
15-Functionswithreturn.py
"""
def multiply(n1,n2):
    res = n1*n2
    print("result ",res)
multiply(10,20)
def multiplylatest(n1,n2):
    res = n1*n2
    return res
result = multiplylatest(10,15)
print("result with return value is ",result)