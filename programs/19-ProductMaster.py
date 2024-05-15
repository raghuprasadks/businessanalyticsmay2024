"""
ProductMaster
"""
class Product():
    """
    Attributes/Properties
    """
    code:int
    name:str
    supplier:str
    price:int
    """
    method/function
    """
    def information(self):
        print("Code : ",self.code," Name : ",self.name," Price : ",self.price)
"""
Creation of objects
product1,product2
"""
product1 =Product()
product1.code = 1
product1.name ="Smart phone"
product1.supplier = "Nokia"
product1.price = 45000
product1.information()

product2 =Product()
product2.code = 2
product2.name ="Smart watch"
product2.supplier = "Boat"
product2.price = 15000
product2.information()
