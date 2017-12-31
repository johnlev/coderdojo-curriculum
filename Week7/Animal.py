# This is an example answer. Students will have to code the Animal class as their assignment

class Animal:
    def __init__(self, color, age, animal = "Animal"):
        self.color = color
        self.age = age
        self.animal = animal

    def getInfo(self):
        print("I am a {}-furred {}, and I am {} years old".format(self.color, self.animal, self.age))