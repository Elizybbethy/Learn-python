class Color:
    def __init__(color, name, type, code, texture, shades_example):
        color.name = name
        color.type = type
        color.code = code
        color.texture = texture
        color.shades_example = shades_example
    def favorite(color):
        print(f"{color.name} is my favorite color")
color1 = Color("black","Secondary", "#000000", "Dark", "Off white")
color1.favorite()

class Shoe:
    def __init__(shoe, brand, type, size, color):
        shoe.brand = brand
        shoe.type = type
        shoe.size = size
        shoe.color = color
    def betterOne(shoe):
        print(f"{shoe.brand} is the better shoe of all")
shoe1 = Shoe("Jordan", "Snickers", 40, "Black")
shoe1.betterOne()

class House:
    def __init__(house, size, type, location, color):
        house.size = size
        house.type = type
        house.location = location
        house.color = color
    def myHouse(house):
        print(f"{house.type} is my future house")
house1 = House("Large", "Flat", "Mukono", "Black & Grey")
house1.myHouse()

class Furniture:
    def __init__(furniture, category, color, type, size, texture):
        furniture.category = category
        furniture.color = color
        furniture.type = type
        furniture.size = size
        furniture.texture = texture
    def myFurniture(furniture):
        print(f"{furniture.type} will be our house furniture")
furniture1 = Furniture("Dinners", "Black", "Mahgan", "large", "Smooth")
furniture1.myFurniture()

class Untesil:
    def __init__(self, category, color, brand, type):
        self.category = category
        self.color = color
        self.brand = brand
        self.type = type
    def homeUntesils(self):
        print(f"{self.brand} are so classy")
ourUntesils = Untesil("plates", "Grey", "Lumunarc","dinner")
ourUntesils.homeUntesils()
        
class Bus:
    def __init__(self, name, color, seats, tyres):
        self.name = name
        self.color = color
        self.seats = seats
        self.tyres = tyres
    def commonBusses(self):
        print(f"{self.name} are commonly used")
busses = Bus("Gaaga", "white", 60,8)
busses.commonBusses()

class Cloth:
    def __init__(self, type, color,size):
        self.type = type
        self.color = color
        self.size = size
    def bestClothes(self):
        print(f"{self.type} are commonly used for valentine day")
clothes = Cloth("Dress", "red", "small")
clothes.bestClothes()

class Device:
    def __init__(self, name, color, brand,):
        self.name = name
        self.color = color
        self.brand = brand
    def myDevice(self):
        print(f"{self.brand} is my one of the genuine one")
device1 = Device("Laptop", "black", "Lenovo")
device1.myDevice()

class Snack:
    def __init__(self, name, flavor, size):
        self.name = name
        self.flavor = flavor
        self.size = size
    def delicious(self):
        print(f"{self.flavor} snacks are the most delicious ones")
snack1 = Snack("Cake", "Chocolate", "medium")
snack1.delicious()

class Food:
    def __init__(self, name, tribe, soup):
        self.name = name
        self.tribe = tribe
        self.soup = soup
    def favourite(self):
        print(f"{self.name} is the favourite food for {self.tribe}")
food1 = Food("Matooke", "Baganda", "Meat")
food1.favourite()

