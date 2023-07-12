# num1 = 50
# num2 = 100
# num3 = num1 + num2
# print(num3)


#function definition
def sum():
    num1, num2 = 20,40  #this only used in python
    num3 = num1 + num2
    print(num3)
sum()               #function call/invoking the function above.

def sub():
    num1, num2 = 60,10
    num3 = num1 - num2
    print(num3)
sub()

def modu():
    num1, num2 = 87, 10
    num3 = num1 % num2
    print(num3)
modu()

def myList():
    list1 = [1,2,3,4,10]
    print(list1)
myList()


#ASSIGNMENT making the lists into functions.


'''
This function print out the keys for varible zebra.
And it deletes the item called color in zebra variable values.
'''
def diction():
    #dictionary(dict)
    #It mutable
    zebra = {"name": "tongs", "legs": 4, "color":"black & white", "gender": "male"}
    print(zebra.keys())
    zebra.__delitem__("color")
    print(zebra)
diction()

'''
This function prints out the list of item under fruits variable.
then it proceeds to pop out/delete the last item that was addeded into the set then it prints out the last out put
'''
def fruitList():
    fruits = ["orange", "mangoes","apples"]
    fruits.append("pineapple")
    print(fruits)
    fruits.pop()
    print(fruits)
fruitList()

'''
This function calls a list called osmanlist 
This list explains how mutable they are and how they operate
'''
def osmanList():
    osman = [100,[200]]
    print(osman[1][0])

    osman2 =[1000,[[2000,3000]]]
    print(osman2[1][0][1])

    #example of mutable list
    osman.append(1000)
    osman.pop()
    print(osman)
osmanList()

'''
This function list calls a list known as myList and show the value postions
'''
def list():
    myList = [0,1,2,3,4,5,6,7,8,9]
    print(myList[7])
    myList2 = [10,20,30,40,50,60,62,43,16,27,48,69]
    print(myList2[-1])
list()

'''
This function defines a variable myTurples
and prints out the myTuples values
'''
def tupleTry():
    myTuples = (10,20,30,40,50)
    print(myTuples)
tupleTry()