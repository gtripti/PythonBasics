def square(num):
    return num ** 2
my_nums = [1,2,3,4,5]
# Method 1
for i in map(square,my_nums):
    print(i)
    
# Method 2
list(map(square,my_nums))

def splicer (myString):
    if len(myString)%2 == 0:
        return 'EVEN'
    else:
        return myString[0]

names = ['Ambika', 'Sally','Ambika']
list(map(splicer,names))

def check_even(num):
    return num % 2 == 0
myList = [1,2,3,4,5,6]
list(filter(check_even,myList))

