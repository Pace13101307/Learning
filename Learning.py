#OOP

"""
classes use CamelCase
we need to create an object

class BigObject:
  pass
  
obj_1 = BigObject()
# instanciate the object of BigObject

you can instantiate a class
and make separate instances of a class

it's the same like making multiple lists, 
giving me access to methods of class list
"""

class PlayerCharacter:
  def __init__(self, name):
    self.name = name
  
  def run(self):
    print("Run")
