class Sobes:
  def __init__(self, name, surname, age, birthdate, exp):
    self.name = name
    self.surname = surname
    self.age = age
    self.birthdate = birthdate
    self.exp = exp

  def printout(self):
    return print(f"Ваше имя: {self.name}. Ваша фамилия: {self.surname}. Ваш возвраст: {self.age}. Дата рождения: {self.birthdate}. Опыт: {self.exp}")

n = input("Как вас зовут?: ")
s = input("Ваша фамилия?: ")
age = input("Ваш возвраст?: ")
birth = input("Дата вашего рождения?: ")
exp = input("Опыт работы?: ")

a = Sobes(n, s, age, birth, exp)
a.printout()

