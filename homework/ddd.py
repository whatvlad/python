# class Restaraunt:
#   def __init__(self, restaraunt_name, cuisine_type, number_served):
#     self.restaraunt_name = restaraunt_name
#     self.cuisine_type = cuisine_type
#     self.number_served = 0

#   def describe_restaraunt(self):
#     print(f"Имя ресторана: {self.restaraunt_name}, тип кухни: {self.cuisine_type}")

#   def open_restaraunt(self):
#     print("Ресторан открыт")

#   def increment_number_served(self, n):
#     self.number_served += n

#   def set_number_served(self):
#     print(f"Number served: {self.number_served}")


# n = int(input("Served: "))
# a = Restaraunt("Asdasd", "ukrainian", 0)
# a.increment_number_served(n)
# a.set_number_served()
# a.open_restaraunt()
# a.describe_restaraunt()
# b = Restaraunt("Ffsfsf", "georgian", 0)
# b.open_restaraunt()
# b.describe_restaraunt()
# c = Restaraunt("Zxzxzx", "russian", 0)
# c.open_restaraunt()
# c.describe_restaraunt()


# class IceCreamStand(Restaraunt):
#   def __init__(self, flavor):
#     self.flavor = flavor

#   def show_flavors(self):
#     print(f"Flavors: {self.flavor}")

# i = IceCreamStand("afs")
# i.show_flavors()



class User:
  def __init__(self, first_name, last_name, age, year, login_attempts):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.year = year
    self.login_attempts = 0

  def describe_user(self):
    print(f"Имя пользователя: {self.first_name}. Фамилия пользователя: {self.last_name} Возраст: {self.age}. Год рождения: {self.year}")

  def greet_user(self):
    print(f"Здравствуйте, {self.first_name}")

  def increment_login_attempts(self):
    self.login_attempts += 1
    
  def show_login_attempts(self):
    print(f"Login attempts: {self.login_attempts}")

  def reset_login_attempts(self):
    self.login_attempts = 0
    print(f"Reseted! Login attempts: {self.login_attempts}")


a = User("Vlad", "Tkachenko", 16, 2005, 0)
b = User("Bogdan", "asdasd", 16, 2005, 0)
a.describe_user()
a.greet_user()
b.describe_user()
b.greet_user()
a.increment_login_attempts()
a.show_login_attempts()
a.increment_login_attempts()
a.show_login_attempts()
a.reset_login_attempts()
a.show_login_attempts()
a.increment_login_attempts()
a.show_login_attempts()






class Admin(User):
  def __init__(self, privileges):
    self.privileges = privileges

  # def show_privileges(self):
  #   print(f"Admin privileges: {self.privileges}")



class Privileges(Admin):
  def __init__(self, privileges):
    self.privileges = privileges

  def show_privileges(self):
    print(f"Admin privileges: {self.privileges}")

z = Privileges("разрешено добавлять сообщения, разрешено удалять пользователей, разрешено банить пользователей")
z.show_privileges()