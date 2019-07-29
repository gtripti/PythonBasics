print("Hello")
print('Hello')
print('Hello World')
print("'Hello'")
# Print in next line
print("Hello \nWorld")

# Tab between words
print("Hello \tWorld") 

# Length of String
print(len("Hello"))
print(len("Hello World"))

# Indexing
my_string = "Hello World"
print(my_string)
print(my_string[0])
print(my_string[8])

# Reverse Indexing
print(my_string[-2])
print(my_string[-3])

# Last letter of the string
print(my_string[-1])

# Slicing
my_string="Hello World"
    # 1. from starting index till end
print(my_string[2:])
    # 2. Grap from starting upto a particular index
print(my_string[:3])
    # 3. From styarting to end section
print(my_string[3:7])
    # 4. From beginning to end
print(my_string[::])
    # 5. From start to end with steps
print(my_string[::2])
    # 6. Startinf and ending and steps
print(my_string[2:8:2])
    # 7. Reverse the String
print(my_string[::-1])


# String Proprties
    # Immutability
name = "Sam"
# name[0] = "P"  ERROR -- bcoz strings are immutable
last_letters= name[1:]
print(last_letters)
    # Concatenate the strings
print('P' + last_letters)
    # Multiple times
print('z' * 10)
    # will concatenate numbers that are sring
print('2' + '3')
    # Built in Methods --- doesn't affect the original string
x = "Hello World"
x.upper()
x.lower()
x.split()
x.split('l')

# String Formating --- known as string interpolation
    # 1.  .format()
print('This is a String {} ' . format('INSERTED'))
print('The {} {} {} .'.format('fox' , 'brown','quick'))
print('The {2} {1} {0} .'.format('fox' , 'brown','quick'))
print('The {q} {b} {f} .'.format(f = 'fox' , b = 'brown', q = 'quick'))
        # float formating with  .format method
result = 100/777
print(result)
print('Result = {}'.format(result))
print('Result = {r}'.format(r= result))
print('Result = {r:1.3f}'.format(r= result))
    # 2. f_string()
name = "Jose"
age = 20
print('Hello , his name is {}' .format(name))
print(f'Hello , his name is {name}')
print(f'Hello , my name is {name} and age is {age}')

