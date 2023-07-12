#Numeric datatype, string, sequence, mapping, boolean, set,
#Numeric(intergers - int, float, complex)
num1 = 1000
num2 = 1000.0
num3 = 1+5j
print(type (num1))
print(type(num2))
print(type(num3))

#string (str)
num4 ="1000"
name = "elizy"
print(type(num4))
print(type(name))

#sequence (list, tuple, range)
#list
myList = [0,2,4,6]
myList2 = [0,2,4,6,"elizy"]
print(type(myList))
print(type(myList2))

#Tuple
myTuple = (0,2,4,6)
print(type(myTuple))

#mapping
myDict = {"uganda": "kampala", "italy": "rome", "france": "paris", "kenya": "nairobi"}
print(type(myDict))

#set
mySet = {5,10,15,20}
mySet2 = {10,10, 5,5,15,20,15,20}
print(mySet)
print(mySet2)
print(set(myDict))