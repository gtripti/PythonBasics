my_list = [1,2,3,4,5,6,7,8,9,10]
for i in my_list:
    print(i)
for num in my_list:
    # Check for even number
    if num % 2 == 0 :
        print(num)
    else:
        print(f'Odd Number : {num}')
        
my_list = [1,2,3,4,5,6,7,8,9,10]
list_sum = 0
for num in my_list:
    list_sum = list_sum + num
print(list_sum)

my_string = 'Hello World'
for letter in my_string:
    print(letter)
    
tup = (1,2,3)
for i in tup:
    print(i)

mylist = [(1,2),(3,4),(5,6),(7,8)]
for (a,b) in mylist :
    print(a)
    print(b)

# iterate through keys
d = {'k1':1, 'k2':2, 'k3':3}
for i in d:
    print(i)
# iterate through items
d = {'k1':1, 'k2':2, 'k3':3}
for (key, value) in d.items():
    print(key)
    print(value)

x = [1,2,3]
for i in x :
    # do nothing at all
    pass
print('End of the script')

myString = 'Sammy'
for letter in myString :
    if letter == 'a':
        continue
    print(letter)
    
myString = 'Sammy'
for letter in myString :
    if letter == 'a':
        break
    print(letter)

# using range keyword
myList = [1,2,3]
# from 0 upto 10 and not including 10
for num in range(10) :
    print(num)
    
# from 3 upto 10 and not including 10
for num in range(3,10) :
    print(num)

# in steps of 2
for num in range (0,10,2) :
    print(num)

# Enumerate
index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1

# instead of above we use enumerate function
word = 'abcde'
for item in enumerate(word):
    print(item)
for index,letter in enumerate(word):
    print(letter)
    
# Zip
list1 = [1,2,3]
list2 = ['a','b','c']
for item in zip(list1,list2) :
    print(item)
    
# in operator 
'x' in [1,2,3]
d = {'k1' : 345}
345 in d.values()