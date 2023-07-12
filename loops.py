'''
loops
mechanism that instruct a computer to repeatedly perform a specific activity
'''

#For loop
def myCount():
    for item in range(10): #item it can be any word representing a value.
        print(item)
myCount()


#accessing a list element using a for loop
def myExample():
    languages = ["python", "javascript", "java", "c++", "c#"]
    for language in languages:
        print(language)
myExample()


def moreExample(num):
    for number in range(num):
        print(number)
moreExample(3)
moreExample(7)

# working with if condition with list in the function
def myLang():
    languages = ["javascript","python","java", "c++", "c#"]
    for language in languages:
        if language == "python":
            print("You're currently in python class!")
myLang()

def even(num):
    for number in range(num):
        if number % 2 == 0:
            print(number)
even(10)

def odd(num):
    for number in range(num):
        if number % 2 != 0:
            print(number)
odd(10)

# power
def power(energy):
    powerEnergy = energy ** 2
    if powerEnergy % 2 == 0:
        print("The power value is even number")
    else:
        print("The power is an odd number")
power(4)