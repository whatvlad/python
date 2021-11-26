# def greet_user():
#   print("Hello")

# greet_user()



# def summa(a, b):
#   global c
#   c = a + b

# n = int(input("chislo: "))
# m = int(input("chislo2: "))
# summa(n, m)
# print(c)




# def digit(p):
#     print ("1"*p)

# n = int(input("введите число сколько вы хотите получить символов --> "))
# x = int(input("введите число сколько вы хотите получить символов --> "))

# digit(n)
# digit(x)





# def digit(p, w):
#   print(p*w)
  

# n = int(input("skok simvolov: "))
# r = str(input("vvedite simvol: "))
# x = int(input("skok simvolov2: "))
# f = str(input("vvedite simvol2: "))

# digit(r,n)
# digit(f,x)




# def greet_user(username, userlast):
#   print(f"Hello, {username.title()} {userlast.title()}")

# name = input("Name: ")
# lastname = input("Lastname: ")
# greet_user(name, lastname)

# def greet_user(username, userlast):
#   print(f"Hello, {username.title()} {userlast.title()}")

# name = input("Name: ")
# lastname = input("Lastname: ")
# greet_user(name, lastname)

# name_2 = input("Name: ")
# lastname_2 = input("Lastname: ")
# greet_user(name_2, lastname_2)




# def describe_pet(animal_type, pet_name):
#   print(f"\nУ меня есть {animal_type}.")
#   print(f"Мой {animal_type} и его зовут {pet_name.title()}.")
 
# describe_pet("хомяк", "гарри")



# def summa(a,b):
#   c = a+b
#   return c

# s = summa(2, 3)
# print(s)


# def max2(a, b):      
#     if a > b : m = a
#     else:      m = b
#     return m         


# q = max2(5, 2) 
# print("max =", q)



# def get_formatted_name(first_name, last_name):
#   full_name = f"{first_name} {last_name}"
#   return full_name.title()

# name = input("Name --> " )
# l_name = input("Last name --> ")
# musician = get_formatted_name(name, l_name)
# print(musician)



# def get_formatted_name(first_name, last_name):
#   full_name = f"{first_name} {last_name}"
#   return full_name.title()

# while True:
#   print("\nPlease tell me your name:")
#   print("(enter 'q' at any time to quit)")
 
#   f_name = input("First name: ")
#   if f_name == 'q':break
 
#   l_name = input("Last name: ")
#   if l_name == 'q':break
 
#   formatted_name = get_formatted_name(f_name, l_name)
#   print(f"\nHello, {formatted_name}!")