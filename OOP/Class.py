class Dog():
    # create class object attributes
    # same for any instance of a class
    species = 'mammal'
    
    # functions inside class are called methonds
    # init is special method in class -- called when we create an instance of the class -- constructor
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
    
    def bark(self,num):
        print("WOOOF! My name is : "+self.name+ " and the number is : "+num)
        
# creating an instance of the class
my_dog = Dog('Lab','Sammy' )
type(my_dog)
my_dog.species
my_dog.breed
my_dog.name
my_dog.bark('10')


class Circle():
    pi = 3.14
    
    def __init__(self,radius=1):
        self.radius = radius
    
    def get_circumference(self):
        return self.radius*Circle.pi*2
    
my_circle = Circle(2)
my_circle.get_circumference()
        