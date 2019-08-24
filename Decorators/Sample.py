def func():
    return 1
func()

def hello():
    return 'Hello!!!'
hello()
greet = hello
greet()



def hello1(name = 'Jose'):
    print('The hello1() function is executed')
    def greet():
        return '\t This is the greet function inside hello'
    print(greet())
    
hello1()


