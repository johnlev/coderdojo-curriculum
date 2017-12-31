"""
Week 7 - Activity: Aggregation
---------
AUTHOR: Edward Camp
"""

from Week7.Dog import Dog
from Week7.Cat import Cat
from Week7.Collar import Collar

'''
For our classes so far, their variables consist of either strings or numbers. However, it is possible for classes to
have instances of classes as variables as well. If we pass in an object into the constructor of another class for it to
be stored, it is called aggregation. Suppose that an instance of 'Dog' is given a 'Collar' object. Then the relationship
between the two objects would be that "the Dog HAS A Collar."

In this activity, we will be implementing a class called Collar that will store an owner's name, a phone-number, and an 
address. It should also have a 'getInfo' method that should be called within the Dog or Cat's 'getInfo' methods if
there is a collar present. This will require you to revise your Dog and Cat classes. I'd suggest using optional
parameter values.
'''

collar1 = Collar("Alex", "635-474-3383", "2054 Panama Lane")
collar2 = Collar("Bethany", "293-555-0875", "695 Lazuli Road")


dog1 = Dog("gold", 7, ['sit', 'lay', 'rollover'], "golden retriever", "ball", collar1)
dog2 = Dog("black", 4, ['shake', 'speak'], "toy poodle", "sock", collar2)

cat1 = Cat("gray", 9, 8, "russian blue", "chicken", collar1)
cat2 = Cat("brown", 6, 12, "maine coon", "fish")

dog1.getInfo()
cat1.getInfo()
dog2.getInfo()
cat2.getInfo()
