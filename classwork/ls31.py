class Restaraunt:
  def __init__(self, restaraunt_name, cuisine_type, number_served):
    self.restaraunt_name = restaraunt_name
    self.cuisine_type = cuisine_type
    self.number_served = 0

  def describe_restaraunt(self):
    print(f"Имя ресторана: {self.restaraunt_name}, тип кухни: {self.cuisine_type}")

  def open_restaraunt(self):
    print("Ресторан открыт")

  def increment_number_served(self, n):
    self.number_served += n

  def set_number_served(self):
    print(f"Number served: {self.number_served}")


n = int(input("Served: "))
a = Restaraunt("Asdasd", "ukrainian", 0)
a.increment_number_served(n)
a.set_number_served()
a.open_restaraunt()
a.describe_restaraunt()
b = Restaraunt("Ffsfsf", "georgian", 0)
b.open_restaraunt()
b.describe_restaraunt()
c = Restaraunt("Zxzxzx", "russian", 0)
c.open_restaraunt()
c.describe_restaraunt()


class User:
  def __init__(self, first_name, last_name, login_attempts):
    self.first_name = first_name
    self.last_name = last_name
    self.login_attempts = 0

  def describe_user(self):
    print(f"Имя пользователя: {self.first_name}. Фамилия пользователя: {self.last_name}")

  def greet_user(self):
    print(f"Здравствуйте, {self.first_name}")

  def increment_login_attempts(self):
    self.login_attempts += 1
    
  def show_login_attempts(self):
    print(f"Login attempts: {self.login_attempts}")

  def reset_login_attempts(self):
    self.login_attempts = 0
    print(f"Reseted! Login attempts: {self.login_attempts}")


a = User("Vlad", "Tkachenko", 0)
b = User("Bogdan", "asdasd", 0)
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



class IceCreamStand(Restaraunt):
  def __init__(self, flavor):
    self.flavor = flavor

  def show_flavors(self):
    print(f"Flavors: {self.flavor}")

i = IceCreamStand("afs")
i.show_flavors()



class Admin(User):
  def __init__(self):
    self.privileges = []

  # def show_privileges_(self):
  #   print(f"Admin privileges: {self.privileges}")



class Privileges(Admin):
  def show_privileges(self):
    for i in p:
      self.privileges.append(p)
      print(f"Admin privileges: {i}")

z = Privileges()
p = ["Allowed to add messages", "Allowed to delete users", "Allowed to ban users"]
z.show_privileges()
