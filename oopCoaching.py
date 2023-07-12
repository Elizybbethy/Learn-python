'''
A function inside of a class is called a method or a behaviour
'''
class Student: #This is a class
    # these  below are called attributes, they describe what a stiudent is
    name = "kapere"
    age = 30
    phoneNumber = 778904657
    address = "Ntinda"
    
    def assignment(): #This ia a method
        num = 5 + 10
        # return num
        # return "Completes Assignment" #Behaviour
        return [num, "Completes Assignment"] #a list helps to excute many returns like two or more
    
print(Student.name, Student.age, Student.phoneNumber, Student.address) # this prints the class attributes
print(Student.assignment()) #This prints the behaviour

items = ["cake", "sweets", "buttercream", "pizza"] #The list is now stored into items
for item in items:
    print(item)

print("........................................")
cars = 1
while cars <= 10:
    print(cars) #the print functions comes first before the additional function because when it comes to the increament it starts with 1 but if print comes after the increament will start from 2
    cars = cars + 1
  
print(".................................")  
    
for i in range(10): #Range is use to run the sequence of the number
    print(i)