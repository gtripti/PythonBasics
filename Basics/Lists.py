my_list= [1,2,3]
print(my_list)

my_list =['HELLO' , 100 , 2.3]
print(my_list)
# Check Length 
print(len(my_list))

my_list= ['one' , 'two' , 'three']
# Indexing
print(my_list[0])
# Slicing
print(my_list[1:])

another_list = ['four' , 'five']
print(my_list + another_list)
new_list = my_list + another_list
print(new_list)

# Mutable
new_list[0] = "ONE"
print(new_list)

# Methods
    # 1. Append to list
new_list.append('six')
print(new_list)
    # 2.Remove from end of list
popped_item = new_list.pop()
print(popped_item)
print(new_list)
    # 3.Remove from specific index
print(new_list.pop(0))
print(new_list)

new_list = ['a','e','x','b','c']
num_list = [4,1,8,3]
    # 4.Sort the list -- doesn't return anything
new_list.sort()
print(new_list)
num_list.sort()
print(num_list)
    # Reverse a list
num_list.reverse()
print(num_list)

