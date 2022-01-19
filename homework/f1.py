# class Rectangle():
#   def __init__(self, a, b, s):
#     self.a = a
#     self.b = b
#     self.s = s
#     self.s = self.a*self.b
    
#   def printing(self):
#     print(f"Площадь: {self.s}")

# length = int(input("Длина: "))
# width = int(input("Ширина: "))
# a = Rectangle(length, width, 0)
# a.printing()



# class Processing():
#   def __init__(self, input_, output):
#     self.input = input_
#     self.output = output

#   def printing(self, i):
#     print(i.upper())

# i = input("Строка: ")
# a = Processing("","")
# a.printing(i)





# class Shop():
#   def __init__(self, shop_name, store_type):
#     self.shop_name = shop_name
#     self.store_type = store_type
#     self.number_of_units = 0

#   def openshop(self):
#     print("Shop is open!")

#   def describe_shop(self):
#     print(f"Name: {self.shop_name}, type: {self.store_type}")

  
#   def set_number_of_units(self):
#     print(f"Units: {self.number_of_units}")

#   def increment_number_of_units(self, i):
#     self.number_of_units += i

# i = int(input("Set number of units: "))
# a = Shop("Store", "products")
# a.increment_number_of_units(i)
# a.set_number_of_units()
# a.openshop()
# a.describe_shop()


# class Discount(Shop):
#   def __init__(self, discount_products):
#     self.discount_products = discount_products

#   def get_discount_products(self):
#     print(f"Discount products: {self.discount_products}")

# store_discount = Discount("sdsd, sdsd")
# store_discount.get_discount_products()



class Bank():
  def __init__(self, deposit, withdraw):
    self.__balance = 0
    self.deposit = deposit
    self.withdraw = withdraw

  def balance(self):
    print(f"На балансе: {self.__balance}")

  def deposit_in_bank(self):
    self.__balance += d

  def withdraw_from_bank(self):
    w = int(input("Сколько вы хотите вывести денег: "))
    if self.__balance >= w:
      self.__balance -= w
    else:
      print("Не хватает денег!")     

print("Я открыл счет в банке")
d = int(input("Сколько вы хотите внести денег в банк: "))
b = Bank(d, 0)
b.deposit_in_bank()
b.balance()
b.withdraw_from_bank()
b.balance()
