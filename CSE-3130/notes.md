//notes.md

# object-oriented programming 2 notes
## inheritance
Inheritance is the process where one class inherits attributes and methods from another class. While some languages, such as java prohibit it, classes can inheirt from multiple parent classes. However, this process of multiple inheritances is often avoided because of potential naming conflicts. In general, classes only inherit from a single parent class.

Inheritance describes as _Is-A_ relationship, where the interaction between the parent and child classes can be expressed as a sentence using "is a".

* A deck of cards __is a__ group of a cards and a hand of cards __is a__ group of cards, but a deck  _is not a_ Hand. Therefore, a Deck and Hand class can inherit from a Group_of_cards class

__Abstract Classes__ (as opposed to concrete classes) are classes that are never instantiated individually. Instead, they are written soley for the purpose of inheritance. Oftentimes, these classes have __abstract attributes and methods__, which cannot function properly in the abstract class. Instead, they rely on data in their respective sub-classes.


NOTE: inheritance often reveals itself during the design process when multiple classes have similar attributes or methods

```python
class Mammal: # abstract parent class
    def __init__(self, genus, species, common_name):
        self.__genus = genus
        self.__species = species
        self.__common_name = common_name
        self.__cry_sound = object
    
    def setCry(self, sound):
        self.__cry_sound = sound
    def Cry(self):
        return self.__cry_sound
        
class Dog(Mammal): # concrete child class
    def __init__(self, genus, species, name):
        Mammal.__init__(self,genus, species, name)
        self.setCry(Sound("Bark"))

        
class Cat(Mammal):  # concrete child class
    def __init__(self, name):
        Mammal.__init__(self, "Felis", "catis", name)
        self.setCry(Sound("Meow"))
     
        
HUSKY = Dog("Canis", "lupis", "rover")
SIAMESE = Cat("Luna")
    

HUSKY.Cry() # output "Bark"
SIAMESE.Cry() # output "meow"

```

## Public, Private, and Semi-private attributes and methods
Python is an open object-oriented programming language, which means that attributes and methods are public _by default_. Therefore, the rest of the program can access attributes and methods without an interfacing method. (Object in python lack encapsulation by default). Python uses the underscore character to indicate whether an attribute or method is public, private, or semi-private.

* __Public__ properties do not require underscores at the start of the property name. In general, attributes should never be public, and only specific methods that manipulate attributes or retrieve attribute values should be public.
    ```python
    class Main:
        def __init__(self):
            self.__VALUE = "hello world"  # private attribute
  
        def getValue(self):
            return self.__VALUE
  
    # A public method returns the value of a private attribute.
    ```
* __Private__ Properties are not accessible outside the object. To indicate that a property is private, two underscores are used at the beginning of the attribute or method name.
  * NOTE: Private methods or attributes are not the same as magic methods or attributes.
  ```python
    class Main:
        def __init__(self):
            self.public = "hello"
            self.__private = "world"
            
    MAIN = Main()
    print(MAIN.public)  # output "hello"
    print(MAIN.__private)  # error
  ```
* __Semi-private properties are visible to child classes of the class (but not the child of the child class. Only goes one level deep). Semi-private properties are still inaccessible to the rest of the program.
  ```python
    class Main:
        def __init__(self):
            self.public = "hello"
            self.__private = "world"
            self._semi_private = "hi!"
  
    class SubClass(Main):
        def __init__(self):
            Main.__init__(self)
    
        def newMethod(self):
            self._semi_private = "new text"  # Update the attribute from Main
            self.public = "new hello"  # Update the attribute from Main
  
        def newMethod2(self):
            self.__private = "new world"  # Error!
  
        def newMethod3(self):
            self.__semi_private = "even newer text"  # Create a new attribute in SubClass
  ``` 
## Polymorphism
Polymorphism is the ability to have the same methods in different classes that may modify and inherited method to perform a specific tasks for the subclass. Oftentimes, the tasks of each-class are similar.
```python
# Use objects from above
HUSKY.cry() #"Bark"
SIAMESE.cry() # "meow"


```
Note that both objects have the same method, but different outputs