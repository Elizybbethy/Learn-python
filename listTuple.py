#List, Tuple and Dictionary in details.
#list are Mutable datatypes
myList = [0,1,2,3,4,5,6,7,8,9]
print(myList[7])
myList2 = [10,20,30,40,50,60,62,43,16,27,48,69]
print(myList2[-1])

osman = [100,[200]]
print(osman[1][0])

osman2 =[1000,[[2000,3000]]]
print(osman2[1][0][1])

#example of mutable list
osman.append(1000)
osman.pop()
print(osman)

fruits = ["orange", "mangoes","apples"]
fruits.append("pineapple")
print(fruits)
fruits.pop()
print(fruits)


#tuples in details
#immutable ie you can't delete/add anything you can only access
myTuples = (10,20,30,40,50)


#dictionary(dict)
#It mutable
zebra = {"name": "tongs", "legs": 4, "color":"black & white", "gender": "male"}
print(zebra.keys())
zebra.__delitem__("color")
print(zebra)
