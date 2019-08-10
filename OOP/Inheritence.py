# Base animal
class Animal():
    def __init__(self):
        print('Animal Created')
    
    def who_am_i(self):
        print('I am an animal')
    
    def eat(self):
        print('I am eating')
    
my_animal = Animal()
my_animal.eat()
my_animal.who_am_i()

# Child class --- inheritance from animal class
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')
    # overwrite the method
    def eat(self):
        print('I am a dog eating')
    
    def bark(self):
        print('WOOF')

my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()
my_dog.bark()
