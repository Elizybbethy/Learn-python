'''
This function has various inputs functions where the user is required to enter student details and the parent details.
'''
def student():
    name = input("Please insert Student Fistname and lastname: ")
    age = input("Insert the Student Age: ")
    location = input("Add your location: ")
    parentName = input("Please Insert Parent's Name here: ")
    print("Parent's Name: ", name)
    print("Summary Details: " "Name:", name + " " + "Age:", age +" " + "Located:",location + " " + "Student's Parent: ", parentName)
student()
print(".....................................")
print("Choose the Student's class below.")
print("                              ")


'''
This function shows the available classes
Its prompts the user to input the student's class
Then print out the school fees for that student basing on the input class
'''
def schoolFees():
    # studentclass = "Baby Class " + "Middle Class " + "Top class"
    studentclass = ["Baby", "Middle", "Top", "P.1"]

    print("                              ")
    print(studentclass)
    registeringClass = input("Enter the student class: ")
    # print("Class: ", registeringClass)
    babyclass = 900000
    middleclass = 800000
    topclass = 600000
    # print(babyclass, middleclass, topclass)
    if registeringClass == "Baby":
        print("Baby class fees: ", babyclass)
    elif registeringClass == "Middle":
        print("Middle Class fees: ", middleclass)
    elif registeringClass == "Top":
        print("Top class fees: ", topclass)
    else:
        print("Please enter the student's class or check the spelling")
        print("Please re-enter the student class")
        registeringClass = input("Enter the student class: ")
        if registeringClass == "Baby Class":
            print("Baby class fees: ", babyclass)
        elif registeringClass == "Middle Class":
            print("Middle Class fees: ", middleclass)
        elif registeringClass == "Top Class":
            print("Top class fees: ", topclass)
    
    print("                               ")
schoolFees()

'''
This function requires the user to input the payment status, i.e whether he/she has paid or not
'''
def payments():
    payment = input("Enter student current payment status (Yes/No): ")
    if payment == "yes":
        print("Thank you for the payement")
    elif payment == "no":
        print("Please go we argue to make the payment:")
    else:
        print("Please Insert your payment status")
    print(".............................")
payments()