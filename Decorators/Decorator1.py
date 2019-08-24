# create a new decorator
def new_decorator(original_function):
    # represents the extra funtionallity u want to add
    def wrap_funct():
        print('Some extra code before the original function')
        original_function()
        print('Some extra code after the original function')
    return wrap_funct

def funct_needs_decorator():
    print('I want to be decorated')

decorated_funct = new_decorator(funct_needs_decorator)
decorated_funct()

# Special syntax
@new_decorator
def funct_needs_decorator1():
    print('I want to be decorated')
    
funct_needs_decorator1()