#operators in python
#what are operators
#operators tells a computer what to do with an operand.
#Operand it's what an operator acts upon

#operators are categorised
#Arithmetic operators(+, -, * , / , // , % , **)

#example
num1 = 10
num2 = 20
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2) #floor division
print(num1 % num2)  #modulus
print(num1 ** num2) #exponetial

#assigment operators (= , +=, -=, *=, /=, %=, **=)
num3 = 50
num4 = 100
num3 += num4 #same as num3 = num3 + num4
print(num3)

num3 -= num4
print(num3)

#comparision operators
print(num1 == num2)
print(num1 != num2)
print(num1 <= num2)
print(num1 >= num2)

#logical operators(and , or , not)
print(True and True)
print(True and False)
print(True or False)
print(not True)

#Identity operators (is , is not)
name = "elizy"
print(num3 is num4)
print(num3 is not num4)

#membership operators (in , not in)
print("a" in name)
print("e" in name)
print("E" in name)
print("a" not in name)