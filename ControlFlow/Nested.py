x = 25
def printer():
    x = 50 
    return x
# local variable
lambda num : num ** 2

#Global
name = 'THIS IS A GLOBAL STRING'
def greet():
    # Enclosing
    # name = 'Sammy'
    def hello():
        # Local
        name = 'THIS IS LOCAL'
        print('Hello ' + name)
    hello()
greet()