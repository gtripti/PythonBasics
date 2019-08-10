class Animal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
    
class Dog(Animal):
    # def __init__(self,name):
    #     Animal.__init__(self)
    #     self.name = name
    def speak(self):
        return self.name + ' says woof'


class Cat(Animal):
    # def __init__(self,name):
    #     self.name = name
    def speak(self):
        return self.name + ' says meoww'

dog = Dog('dog')
cat = Cat('cat')
print(dog.speak())
print(cat.speak())

for pet in [dog,cat]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

pet_speak(dog)
pet_speak(cat)

