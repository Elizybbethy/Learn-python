'''
The number of paramenter should be the same as the number of properties
'''
class School: #dynamic class
    def __init__(self, name, motto, no_teachers, location, uneb_num ): #(name, motto etc) are paramenters
        self.name = name    #self.name is a property,  name is the property value
        self.motto = motto
        self.no_teachers = no_teachers
        self.location = location
        self.uneb_num = uneb_num  
        
    def register(self):
        print(f"{self.name} is fully registered with UNEB")
school1 = School("agape", "Trust in God's providence", 20, "mukono", "ueb102")  #instantiate an object of a class(giving an example)
school1.register()

school2 = School("groundbreaker", "unlock your full potential", 4, "ntinda", 13434 )
school2.register()
        
class Country:
    def __init__(self, A , B, C):
        self.name = A
        self.city = B
        self.popn = C
        
class Continent:
    def __init__(continent, A, B, C):
        continent.name = A
        continent.lakes = B
        continent.rivers = C