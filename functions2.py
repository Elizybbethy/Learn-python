def sum():
    num1 = 200
    num2 = 500
    num3 = num1 + num2
    print(num3)
sum() # these are called static functions.

#dynamic function
def dynamic(num1, num2):
    num3 = num1 + num2
    print(num3)
dynamic(200,500)
dynamic(10, 40)
dynamic(4,5)

def modulus(num1 , num2):
    num3 = num1 % num2
    print(num3)
modulus(7,2)

def division(num1 , num2):
    num3 = num1 / num2
    print(num3)
division(500,200)

def multipulation(num1 , num2):
    num3 = num1 * num2
    print(num3)
multipulation(2,4)

'''
Functions are self contained
They can't be accesible inside the other
They are independent of each other unless they are assgned to access each other.
'''