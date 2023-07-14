'''
The piece of code below demostrate a class inheritance, 
Where class Dog and Snake are taking on properties of class Animal.
The class Dog and Snake are not related to one another, though they are both related/belong to class Animal.
'''
class Animal:
    name = ""
    family = ""
    gender = ""
    
class Dog(Animal): #Here we have inheritated the class Animal so the class Dog should take on all attributes form that class Animal.(Accessing the properties of a class Animal)
    sound = "Bark"
    
    def investigate(self):
        print(f"{self.name} sniffs to investigate")

class Snake(Dog): #Here the Class Snake inherits from a class Dog
    
    # sound = "hiss"
    moving = "crwal"
    # snakeSound = sound 
    def detects(self):
        print(f"{self.name} detects by hissing")
        
#Let's instantiate/create objects of a class Dog
gsp = Dog()
gsp.name = "fredy"
gsp.family = "dog"
gsp.gender = 'male'
print(f"{gsp.sound}")


#Let's instantiate/create objects of a class Snake
snake1 = Snake()
snake1.name = "python"
snake1.family = "reptile"
snake1.gender = "not sure"
print(f"{snake1.sound}  for the snake")
print(f"{snake1.moving}  for the snake")