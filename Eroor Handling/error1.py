def add(n1,n2):
    print(n1+n2)

add(10,20)
# error one is number and other is string
number1 = 10
number2 = input("please enter number 2 :")
# add(number1,number2)

try:
    # Want to attempt this code but it can have error1
    result = 10 + 10
except:
    # what will happen if there is an error
    print('Hey it looks like u r not adding correctly')
else:
    print('Sum is = ')
    print(result)
    
    
# Example 2
try:
    f = open('testfile','w')
    f.write('Write a test line')
except TypeError:
    print('There was a type error')
except OSError:
    print('Hey u have OS Error')
finally:
    print('i always run')
    
# Example 3
def ask_for_int():
    while True:
        try:
            int(input('Please provide number : '))
        except:
            print('Whoopsss')
        else:
            print('Yes thanku')
            break
        finally:
            print('End of try except')
            
ask_for_int()
