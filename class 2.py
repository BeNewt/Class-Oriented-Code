class Pet:
    """This is the beginning of a class for the humble house dog"""

    def __init__(self, name):
        self.name = name

    def add_breed(self, breed):
        self.breed = breed

    def add_color(self, color):
        self.color = color

    def add_mass(self, mass):
        self.mass = mass

    def add_height(self, height):
        self.height = height

    def add_lifespan(self, min_life, max_life):
        self.min_life = min_life
        self.max_life = max_life

    def add_origin(self, origin):
        self.origin = origin

    def add_hypoallergenic(self, hypoallergenic):
        self.hypoallergenic = hypoallergenic

    def add_temperament(self, temperament):
        self.temperament = temperament

   
class Dog(Pet):
    """Dog inherits from Pet"""

    def speak(self):
        print("bark")
    

class Cat(Pet):
    """Cat inherits from Pet"""

    def speak(self):
        print("meow")

d = Dog("Merritt")

d.add_breed("labrador")

d.add_color("yellow")

d.add_mass(65)

d.add_height(24)

d.add_lifespan(10, 12)

d.add_origin("newfoundland")

d.add_hypoallergenic("no")

d.add_temperament("outgoing")

d.speak()


c = Cat("Seymour")

c.add_breed("bengal")

c.add_color("black and tan")

c.add_mass(10)

c.add_height(3)

c.add_lifespan(10, 16)

c.add_origin("usa")

c.add_hypoallergenic("no")

c.add_temperament("talkative")

c.speak()


print(c.name)
print(c.breed)
print(c.color)
print(c.mass)
print(c.height)
print(c.min_life)
print(c.max_life)
print(c.origin)
print(c.hypoallergenic)
print(c.temperament)

print(d.name)
print(d.breed)
print(d.color)
print(d.mass)
print(d.height)
print(d.min_life)
print(d.max_life)
print(d.origin)
print(d.hypoallergenic)
print(d.temperament)


