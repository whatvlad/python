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




class Admin(User):
  def __init__(self):
    self.privileges = []

  # def show_privileges(self):
  #   print(f"Admin privileges: {self.privileges}")



class Privileges(Admin):
  def show_privileges(self):
    for i in p:
      self.privileges.append(p)
      print(f"Admin privileges: {i}")

p = ["Allowed to add messages", "Allowed to delete users", "Allowed to ban users"]
z = Privileges()
z.show_privileges()