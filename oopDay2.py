'''
below is a defined class called girl with
characteristics
propeties
attributes
and all objescts under this class must fulfill them.
'''
class Girl:
    name = "elizy"
    age = 25
    gender = "female"
    body_size = "medium"
    family = "Heavenly"
    bra_size = 30
    def dance():
        return"she likes callipuso"
    def eat():
        print("four times a day")
    def greet():
        print("hello guys")
        return ""
print(Girl.greet())
print(Girl.name)

# if the funtion is just returning and has no print function it has to be evoked with a print fuction.
print(Girl.dance())

# if the function doesnot have a rutuen and has a print you don't have to call it in a print method
Girl.eat()

# all objects in the same class have the same method

girl2 = Girl()
girl2.name = "bbethy"
girl2.age = 24
girl2.gender = "female"
print(girl2.name)
print(f"{girl2.name} is {girl2.age} years old!")
#f is for format

girl3 = Girl()
girl3.name = "Pretty"
girl3.age = 20

