'''
This is a static appending list function 
'''
students = []
def register(name, room):
    # name = input("please enter your name here: ")
    # room = input("Enter the student's class here: ")
    name1 = name
    room1 = room
    # print(f"{name}{room}")
    print(f"{name1}{room1}")
    students.append(name1)
    students.append(room1)
    print(students)
    
register("elizy", 1)

'''
This is a dynamic apending list function that registers students
'''
students = []
def register():
    name = input("please enter your name here: ")
    room = input("Enter the student's class here: ")
    name1 = name
    room1 = room
    # print(f"{name}{room}")
    print(f"{name1}{room1}")
    students.append(name1)
    students.append(room1)
    print(students)

#Here the function is looped through 3 times using a while loop
r = 0    
while r<3:
    register()
    r+=1

#Here the function is looped through 3 times using a for loop
s = 0
for s in range(0,3):
    #The if function is used to determine the status of the function
    if len(students) >= 1:
        print("we're good to go")
    elif len(students) < 1:
        print("There is no registered students yet")
    register()
