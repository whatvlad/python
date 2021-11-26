# arr = [i if i > 5 else "False" for i in range(1, 11)]
# print(arr)


# a = [1, 2, 3]
# b = [4, 5, 6]
# arr = [(x, y) for x in a for y in b ]
# print(arr)


# dict = {"item": 1, "item2":2, "item3": 3}
# dict2 = {k:v**2 if v>4 else "False" for k,v in dict.items()}
# print(dict2)


import random

# arr = [0 for i in range(7)]
# print(arr)


# arr = [random.randint(0, 1000000) for i in range(100)]
# print(arr)

n = int(input("n = "))
m = int(input("m = "))

matrix = [ [random.randint(1, 9) for i in range(m) ] for j in range(n)]
print("Matrix ----->")
for i in matrix:
  print(f"\t\t{i}")

a = [matrix[j] [i] for i in range(n) for j in range(m) if j == i]
print(f"Главная диагональ - {a}")

b = [matrix[j] [i] for i in range(n) for j in range(m) if j == 1]
print(f"Вторая строка - {b}")

c = [matrix[j] [i] for i in range(n) for j in range(m) if i == 2]
print(f"Третий столбец - {c}")