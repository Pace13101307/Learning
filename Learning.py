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

1 class will allow for many instances 
which will live in different places in memory
"""

class PlayerCharacter:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def run(self):
    print("Run")
    return "done"

player_1 = PlayerCharacter("kyle", 24)
player_2 = PlayerCharacter("bob", 53)
player_2.attack = 50

print(player_1.name)
print(player_2.age)
player_1.run()
print(player_1.attack)
print(player_2.attack)

# 
