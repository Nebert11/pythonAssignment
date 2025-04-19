#First class  called smartphone
class smartphone:
    brand = "Huawei"

    def ring(self):
        print("Ringing......")

my_smartphone = smartphone()
my_smartphone.ring()
print(my_smartphone.brand)

#Constructors
class book:
    def __init__(self, title, publisher):
        self.title = title
        self.publisher = publisher

bookDetails = book("Hosting", "Jason Miles")
print(bookDetails.title)
print(bookDetails.publisher)

#Inheritance
class superhero:
    def __init__(self, name, powers):
        self.name = name
        self.powers = powers

class flash(superhero):
    pass

flash = superhero("Hunter", "Speed")
print("Name:",flash.name, "Powers:",flash.powers)

#Polymorphism in action
class vehicle:
    def move(self):
        return "Driving"

class plane:
    def move(self):
        return "Flying"
    
class ship:
    def move(self):
        return "Sailing"
    
for machine in [vehicle(), plane(), ship()]:
    print(machine.move())
