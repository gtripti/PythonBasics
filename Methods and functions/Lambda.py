def square(num):
    return num ** 2

# Converting above function into lambda function
square = lambda num : num ** 2
square(2)

myList= [1,2,3,4]
list(map(lambda num: num ** 2, myList))
list(filter(lambda num : num%2 == 0, myList))