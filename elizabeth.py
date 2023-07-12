#assignment create atleast 10 classes corresponding with their 5 objects and print one property for each class.

'''
This class color having several attributes
And it has different objects
'''
class Color:
    name = "blue"
    type = "primary"
    code = "#0000FF"
    texture = "light"
    shades_example = "powder blue"
print(Color.name)

color2 = Color()
color2.name = "red"
color2.type = "primary"
color2.code = "#FF0000"
color2.texture = "light"
color2.shades_example = "crimson"
print(color2.shades_example)

color3 = Color()
color3.name = "grey"
color3.type = "secondary"
color3.code = "#808080"
color3.texture = "dark"
color3.shades_example = "DarkGray"
print(color3.code)

color4 = Color()
color4.name = "black"
color4.type = "secondary"
color4.code = "#000000"
print(color4.name)

color5 = Color()
color5.name = "purple"
color5.type = "secondary"
color5.code = "#800080"
print(color5.name)

'''
This class shoe having several attributes
And it has different objects
'''

class Shoe:
    brand = "Jordan"
    type = "Snickers"
    size = 7
    color = "black"
print(Shoe.brand)

shoe2 = Shoe()
shoe2.brand = "nick"
shoe2.type = "boot"
shoe2.size = 9
shoe2.color = "brown"
print(shoe2.brand)

shoe3 = Shoe()
shoe3.brand = "adidas"
shoe3.type = "leisure"
shoe3.size = 8
shoe3.color = "white"
print(shoe3.type)

shoe4 = Shoe()
shoe4.brand = "umoja"
shoe4.type = "sandals"
shoe4.size = 5
shoe4.color = "blue"
print(shoe4.brand)

shoe5 = Shoe()
shoe5.brand = "Puma"
shoe5.type = "snickers"
shoe5.size = 41
shoe5.color = "pitch"
print(shoe5.type)

'''
This class house having several attributes
And it has different objects
'''

class House:
    size = "large"
    type = "flat"
    location = "Kampala"
    color = "Grey"
print(House.type)

house2 = House()
house2.size = "small"
house2.type = "single"
house2.location = "Mukono"
house2.color = "none"
print(house2.type)

house3 = House()
house3.size = "medium"
house3.type = "double_roomed"
house3.location = "Wakiso"
house3.color = "brown"
print(house3.type)

house4 = House()
house4.size = "medium"
house4.type = "rental"
house4.location = "kampala"
house4.color = "dark-blue"
print(house4.type)

house5 = House()
house5.size = "large"
house5.type = "Apartment"
house5.location = "Ntida"
house5.color = "grey"
print(house5.type)

'''
This class Furniture having several attributes
And it has different objects
'''
class Furniture:
    Category = "chairs"
    color = "browm"
    type = "single sitter"
    size = "medium"
    texture = "smooth"
print(Furniture.Category)

furniture2 = Furniture()
furniture2.Category = "tables"
furniture2.color = "grey"
furniture2.size = "large"
print(furniture2.Category)

furniture3 = Furniture()
furniture3.Category = "tables"
furniture3.color = "grey"
furniture3.size = "large"
print(furniture3.Category)

furniture4 = Furniture()
furniture4.Category = "doors"
furniture4.color = "mellon"
furniture4.size = "meduim"
print(furniture4.Category)

furniture5 = Furniture()
furniture5.Category = "beds"
furniture5.color = "coffee"
furniture5.size = 6 * 6
print(furniture5.Category)

'''
This class Utesils having several attributes
And it has different objects
'''
class Untesil:
    Category = "plates"
    color = "white"
    brand = "lumunarc"
    size = "medium"
    type = "dinner"
print(Untesil.brand)

untesil2 = Untesil()
untesil2.Category = "spoons"
untesil2.color = "gold"
untesil2.type = "tea spoons"
print(Untesil.brand)

untesil3 = Untesil()
untesil3.Category = "forks"
untesil3.color = "gold"
untesil3.type = "disert"
print(untesil3.brand)

untesil4 = Untesil()
untesil4.Category = "saucepans"
untesil4.color = "sliver"
untesil4.size = "big"
print(untesil4.brand)

untesil5 = Untesil()
untesil5.Category = "glasses"
untesil5.color = "color-less"
untesil5.type = "luumunarc"
print(untesil5.brand)

'''
This class Bus having several attributes
And it has different objects
'''
class Bus:
    name = "Gaaga"
    color = "white"
    seats = 60
    tyres = 8
print(Bus.name)

bus2 = Bus()
bus2.name = "link"
bus2.color = "Green"
bus2.seats = 60
bus2.tyres = 8
print(bus2.name)

bus3 = Bus()
bus3.name = "baby-coach"
bus3.color = "yellow"
bus3.seats = 60
bus3.tyres = 8
print(bus3.name)

bus4 = Bus()
bus4.name = "wakula ennume"
bus4.color = "Green"
bus4.seats = 60
bus4.tyres = 6
print(bus4.name)

bus5 = Bus()
bus5.name = "kasumba"
bus5.color = "yellow"
bus5.seats = 60
bus5.tyres = 6
print(bus5.name)

'''
This class cloth having several attributes
And it has different objects
'''
class Cloth:
    type = "dress"
    color = "black"
    size = "small"
print(Cloth.type)

cloth2 = Cloth()
cloth2.type = "top"
cloth2.color = "red"
cloth2.size = "small"
print(cloth2.type)

cloth3 = Cloth()
cloth3.type = "short"
cloth3.color = "blue"
cloth3.size = "medium"
print(cloth3.type)

cloth4 = Cloth()
cloth4.type = "trouser"
cloth4.color = "brown"
cloth4.size = "large"
print(cloth4.type)

cloth5 = Cloth()
cloth5.type = "sweeater"
cloth5.color = "green"
cloth5.size = "fitting"
print(cloth5.type)

'''
This class Device having several attributes
And it has different objects
'''
class Device:
    name = "television"
    color = "black"
    brand = "sam sung"
print(Device.name)

device2 = Device()
device2.name = "phones"
device2.color = "black"
device2.brand = "sam sung"
print(device2.name)

device3 = Device()
device3.name = "computers"
device3.color = "black"
device3.brand = "dell"
print(device3.name)

device4 = Device()
device4.name = "latops"
device4.color = "black"
device4.brand = "lenovo"
print(device4.name)

device5 = Device()
device5.name = "speakers"
device5.color = "black"
device5.brand = "phillps"
print(device5.name)

'''
This class Snack having several attributes
And it has different objects
'''
class Snack:
    name = "cakes"
    flavor = "chocolate"
    size = "small"
print(Snack.name)

snack2 = Snack()
snack2.name = "Buns"
snack2.flavor = "vanilla"
snack2.size = "small"
print(snack2.name)

snack3 = Snack()
snack3.name = "Doughnuts"
snack3.flavor = "vanilla"
snack3.size = "medium"
print(snack3.name)

snack4 = Snack()
snack4.name = "Cup cakes"
snack4.flavor = "Straberry"
snack4.size = "small"
print(snack4.name)

snack5 = Snack()
snack5.name = "bread"
snack5.flavor = "coconut"
snack5.size = "big"
print(snack5.name)

'''
This class foods having several attributes like tribe standing for the tibe that has that type of food as their favorite, and soup standing for the favorite soup that goes well with tha food.
And it has different objects
'''
class Food:
    name = "matooke"
    tribe = "Baganda"
    soup = "Meat"
print(Food.name)

food2 = Food()
food2.name = "Cassava"
food2.tribe = "Banyoro"
food2.soup = "Meat"
print(food2.name)

food3 = Food()
food3.name = "posho"
food3.tribe = "Kenyans"
food3.soup = "Beans"
print(food3.name)

food4 = Food()
food4.name = "Irish"
food4.tribe = "Bakiga"
food4.soup = "Pork"
print(food4.name)

food5 = Food()
food5.name = "Sweet potatoes"
food5.tribe = "Basonga"
food5.soup = "G.nuts"
print(food5.name)

food2 = Food()
food2.name = "matooke"
food2.tribe = "Baganda"
food2.soup = "Meat"
print(food2.name)