class Animal:
  def __init__(self, species):
    self.species = species

  def animal_info(self):
    print(f"Im an - {self.species}")


class Dog(Animal):
  def __init__(self):
    self.species = "Dog"

  def animal_sound(self):
    print(f"Woof! Woof!")


class Cat(Animal):
  def __init__(self):
    self.species = "Cat"

  def animal_sound(self):
    print(f"Meow!")

arr = ["dog", "cat"]


def show_animal_info(name):
  if name not in arr:
    print(f"{name} is not an animal!")
  elif name == "dog":
    name = Dog()
    name.animal_info()
    name.animal_sound()
  elif name == "cat":
    name = Cat()
    name.animal_info()
    name.animal_sound()

show_animal_info("dog")
show_animal_info("cat")
show_animal_info("book")

