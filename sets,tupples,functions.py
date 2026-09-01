fruits = ["apple","banana","orange","coconut"]
print(fruits)
print(fruits[0])
print(fruits[0:3])
for fruit in fruits:
    print(fruit)

print(dir(fruits))
print(len(fruits))
print("apple" in fruits)
fruits[0]="pineapple"
for fruit in fruits:
    print(fruit)
fruits.append("apple")
print(fruits)
fruits.remove("apple")
print(fruits)
fruits.insert(0,"pineapple")
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
fruits.clear()
print(fruits)
fruits.append("apple")
print(fruits.index("apple"))
print(fruits.count("pineapple"))
