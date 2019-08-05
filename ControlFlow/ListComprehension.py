myString = 'Hello'
myList = []
for letter in myString:
    myList.append(letter)
print(myList)
# Or better method
myList1 = [letter for letter in myString]
print(myList1)

myList2 = [num for num in range(0,11)]
print(myList2)

myList3 = [num ** 2 for num in range(0,11)]
print(myList3)

# print only even numbers
myList = [x for x in range(0,11) if x%2 == 0]
print(myList)

# Mathematical calc
celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp +32) for temp in celcius]
print(fahrenheit)

# Conditional statements
results = [x if x%2 ==0 else 'ODD' for x in range(0,11)]
print(results)

# Nested loop
myList = []
for x in [2,4,6] :
    for y in [100, 200, 300]:
        myList.append(x*y)

# Better method
myList = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(myList)