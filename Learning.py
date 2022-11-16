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
  
  # class object attribute
  # is not dynamic, is static
  # this will be the same for all instances of the object
  membership = True
  
  def __init__(self, name, age):
    
    # because membership is a class object attribute
    # we can pass the class name instead of self.
    # and still have it work
    # any attributes initialized as self. however
    # will not allow getting the class name instead
    
    if PlayerCharacter.membership:
      # attributes
      self.name = name
      self.age = age
  
  def run(self):
    print("Run")
    return "done"
  
  def shout(self):
    print(f"my name is {self.name}")

player_1 = PlayerCharacter("kyle", 24)
player_2 = PlayerCharacter("bob", 53)
player_2.attack = 50

print(player_1.name)
print(player_2.age)
player_1.run()
print(player_1.attack)
print(player_2.attack)

player_1.shout()
player_2.shout()

# 
