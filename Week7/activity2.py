"""
Week 7 - Activity: Subclasses
---------
AUTHOR: Edward Camp
"""

from Week7.Dog import Dog
from Week7.Cat import Cat

'''
At this point, we've created a very simple class that gives the color and age of an Animal. But suppose we wish to 
further specify that the animal is a Dog. We could either introduce more variables to the current existing Animal class
or create a subclass called 'Dog' that is an extension of 'Animal'. The latter option means that the relationship
between 'Animal' and 'Dog' is that "a Dog IS AN Animal". By making 'Dog' the subclass and 'Animal' the superclass, we
will implement what is called 'inheritance'. Thus, 'Dog' will have the same variables and methods that belong to Animal
pre-defined.

In this activity, we will be creating two subclasses: a 'Dog' and a 'Cat'. We will also introduce a few more variables
to each subclass. The Dog subclass should have a list of tricks it is capable of doing, it's breed, it's favorite toy,
and the noise it makes. The Dog subclass should have two methods defined: a 'makeSound' method that prints out the noise
the Dog makes and a 'getInfo' method that prints out not only it's color and age like before but also it's breed,
favorite toy, and the tricks it is capable of performing. On the other hand, the Cat subclass should have the number
of whiskers it has, it's breed, it's favorite food, and the noise it makes. The Cat will also have a similar 'makeSound'
method like for the 'Dog' subclass and a 'getInfo' method that prints out the Cat's color, age, number of whiskers, 
favorite food, and it's breed.

Note, the getInfo should print out whether the animal is a Dog or Cat rather than printing out it is an "Animal"
'''

dog1 = Dog("gold", 7, ['sit', 'lay', 'rollover'], "golden retriever", "ball")
dog2 = Dog("black", 4, ['shake', 'speak'], "toy poodle", "sock")

cat1 = Cat("gray", 9, 8, "russian blue", "chicken")
cat2 = Cat("brown", 6, 12, "maine coon", "fish")

cat1.makeSound()
dog1.makeSound()
dog2.makeSound()
cat2.makeSound()

cat1.getInfo()
dog2.getInfo()
