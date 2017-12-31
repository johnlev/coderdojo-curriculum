"""
Week 7 - Activity: Classes
---------
AUTHOR: Edward Camp
"""

from Week7.Animal import Animal

'''
Up until now, we've been coding away within either methods or 'activity' python files to accomplish tasks and finish
projects. However, a lot of the based code provided and methods you've tasked to code in have been within classes.
Classes are an easier way of bundling related data into one object rather than multiple variables scattered throughout
the code. In addition, classes contain methods that allow users to access and manipulate existing data in the object.

When it comes to actually coding classes, it better to think of them as 'blueprint' to what you wish to build. Once the
blueprint is completed, it can be used to create multiple copies of such class. Each will contain the same variables and 
methods to access data, but the data stored in such copies may have different values. For example, if I wish to build a
car, I would need to define a 'Car' class, declare variables that describe a car like 'maxSpeed' or an 'engine' object,
and create methods that access or manipulate the data that belongs to the car like 'gasConsumption' or 'emergencyBrake'.

In this activity, we will be defining what makes up an Animal. We could define 'hasFur', 'hasTail', 'weight', etc.
However, we will only require you to define a 'color' and 'age' variable of the Animal (to be passed into the 
constructor), and a 'getInfo' that prints out the 'color' and 'age' of the animal.
Example message: "I am a blue Animal, and I am 7 years old."

If done correctly, 'activity1.py' should print out information about a red, green, and purple animal who are 24, 16, and
35 years old, respectively.
'''

animal1 = Animal('red', 24)
animal2 = Animal('green', 16)
animal3 = Animal('purple', 35)

animal1.getInfo()
animal2.getInfo()
animal3.getInfo()