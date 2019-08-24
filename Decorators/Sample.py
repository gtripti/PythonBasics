def func():
    return 1
func()

def hello():
    return 'Hello!!!'
hello()
greet = hello
greet()

# Return Functions
def hello1(name = 'Jose'):
    print('The hello1() function is executed')
    def greet():
        return '\t This is the greet function inside hello'
    def welcome():
        return '\t this is welcome function inside hello'
    # print(greet())
    # print(welcome())
    # print('This is the end of hello function')
    
    print('I am going to return a function')
    if name == 'Jose':
        return greet
    else:
        return welcome
new_funct = hello1('Jose')
new_funct()

def cool():
    def supercool():
        return 'I am very cool'
    return supercool
some_funct = cool()
some_funct
some_funct()

# Pass function as argument
def hello2():
    return 'Hi Jose'
def other(some_def_funct):
    print('Other code')
    print(some_def_funct)
other(hello2)
