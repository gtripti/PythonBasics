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

    