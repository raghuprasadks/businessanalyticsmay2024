"""
Object oriented
class and object
class is collection of attributes and functions
"""
class SimpleCalculator():
    # function or method
    def add(self,n1,n2):
        print(n1," + ",n2," = ",(n1+n2))
    def subtract(self,n1,n2):
        print(n1," - ",n2," = ",(n1-n2))
#mycalculator is an object
mycalculator = SimpleCalculator()
mycalculator.add(100,40)
mycalculator.subtract(100,40)

"""
numlist = [20,30,35,40]
numlst =list([20,30,35,40])
numlist.append(45)
"""