"""
List - []
"""
"""
fruits = ['Apple','Banana','Guava']
print("fruits ",fruits)
fruits.append("Mango")
print("fruits after append ",fruits)
print("change apple to pineapple")
fruits[0]='Pine Apple'
print("fruits after update ",fruits)
print("fruit at 2nd index",fruits[2])
fruits.remove("Banana")
print("after remove ",fruits)

print("sort in ascending order:: ")
fruits.sort()
print(fruits)
print("sort in descending order:: ")
fruits.sort(reverse=True)
print(fruits)
print('search')
fruittosearch = input("Enter fruit to  search")
for fruit in fruits:
    if (fruit ==fruittosearch):
        print(fruittosearch, " is found")
"""
runs=[10,25,35,12,55,3]
print("maximum runs ",max(runs))
print("minimum runs ",min(runs))
print("total runs ",sum(runs))
length = len(runs)
total = sum(runs)
avg = total/length
print("average runs ",avg)

