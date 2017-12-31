# This is an example answer. Students will have to code the Animal class as their assignment

from Week7.Animal import Animal

class Dog(Animal):
    def __init__(self, color, age, tricks, breed, favToy, collar = None):
        Animal.__init__(self, color, age, "Dog")
        self.tricks = tricks
        self.breed = breed
        self.favToy = favToy
        self.noise = "Bark"

        self.collar = collar

    def makeSound(self):
        print("{}!".format(self.noise))

    def getInfo(self):
        Animal.getInfo(self)
        print("I am a {} and my favorite toy is a {}".format(self.breed, self.favToy))
        print("I can do the following tricks:")
        for trick in self.tricks:
            print(trick)
        if(self.collar):
            print("Oh, there's a collar attached. It says...")
            self.collar.getInfo()
        print()