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
  
  # classmethods can be used even without instantiating
  # the class
  # but requires "cls" instead of self, as an argument
  # we can use the cls to instantiate the class
  # classmethod when you do care about the class attrs
  @classmethod
  def adding_things(cls, num1, num2):
    return cls("Teddy", num1 + num2)
    # here we instantiate the class
  
  @staticmethod
  def adding_things_static(num1, num2):
    return num1 + num2
    # staticmethod works the same as classmethod
    # however you do not have access to the class
    # staticmethod when you don't care about the class
    # attributes

player_1 = PlayerCharacter("kyle", 24)
player_2 = PlayerCharacter("bob", 53)
player_2.attack = 50

player_3 = PlayerCharacter.adding_things(2, 3)
print(player_3.age)
# using classmethod we now instantiated a class from
# within the class using the parameters in the function

print(player_1.name)
print(player_2.age)
player_1.run()
print(player_1.attack)
print(player_2.attack)

player_1.shout()
player_2.shout()

# 
