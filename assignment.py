def student():
    name = input("Please insert Student Fistname and lastname: ")
    print("Student Name: ", name)
    age = input("Insert the Student Age: ")
    print("Age: ", age)
    registeringClass = input("Enter the student class: ")
    print("Student class: ", registeringClass)
    location = input("Add your location: ")
    print("Your Located at: ", location)
    # 
    # print("Parent's Name: ", parentsDetails)
    print("Summary Details: " "Name:", name + " " + "Age:", age +" " + "Class:",registeringClass + " "+ "Located:",location)
student()
print(".....................................")

'''
parent's details
payemnt details whether they have paid or not
'''
def parent():
    name = input("Please Insert Parent's Name here: ")
    print("Parent's Name: ", name)
    print("................................")
    print("Payement status:")
    payment = input("Enter your current payment (Yes/No): ")
    if payment == "yes":
        print("Thank you for the payement")
    elif payment == "no":
        print("Please go we argue to make the payment:")
    else:
        print("Please Insert your payment status")
    print(".............................")
parent()

'''
amount of fees to be paid
'''
def schoolFees():
    babyclass = 900000
    middleclass = 800000
    topclass = 600000
    print(babyclass, middleclass, topclass)
schoolFees()