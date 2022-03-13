import re


class Apple:
    def __init__(self, color,flavour):
        self.color = color 
        self.flavour = flavour
    def __str__(self):
        return "This is a {} colored apple and its has a very {} taste".format(self.color,self.flavour)

object = Apple("red","sweet")
print(object)