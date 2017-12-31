# This is an example answer. Students will have to code the Animal class as their assignment

from Week7.Animal import Animal

class Cat(Animal):
    def __init__(self, color, age, numOfWhiskers, breed, favFood, collar = None):
        Animal.__init__(self, color, age, "Cat")
        self.numOfWhiskers = numOfWhiskers
        self.breed = breed
        self.favFood = favFood
        self.noise = "Meow"

        self.collar = collar

    def makeSound(self):
        print("{}!".format(self.noise))

    def getInfo(self):
        Animal.getInfo(self)
        print("I am a {} and my favorite food is a {}".format(self.breed, self.favFood))
        print("I have about {} whiskers.".format(self.numOfWhiskers))
        if (self.collar):
            print("Oh, there's a collar attached. It says...")
            self.collar.getInfo()
        print()