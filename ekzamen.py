
####1

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i < 5:
#         print(i)




##2

# import random
# n = int(input("Количество элементов: "))
# a = 1
# arr = [random.randint(0,15) for i in range(n)]
# print(arr)
# print(arr[0], arr[-1])
# for i in arr:
#     a*=i
# print(a)



#3
# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217]

# for i in numbers:
#     if i % 2 == 0:
#         print(i)
#     elif i == 237:
#         break



#4
# age = int(input("Ваш возраст: "))
# if age < 2:
#     print("Вы младенец.")
# elif age >= 2 and age < 4:
#     print("Вы малыш.")
# elif age >= 4 and age < 13:
#     print("Вы ребенок.")
# elif age >= 13 and age < 20:
#     print("Вы подросток.")
# elif age >= 20 and age < 65:
#     print("Вы взрослый.")
# elif age >= 65:
#     print("Вы пожилой человек.")
# else:
#     print("undefined")



#5 

# registered = ["a", "b", "c", "d"]
# checked = []
# while registered:
#     a = registered.pop(0)
#     checked.append(a)
#     for i in checked:
#         print(f"Пользователь {i} верифицирован")
# print(registered)
# print(checked)



#6 
# arr = ['pizza', 'falafel', 'carrot cake']
# arr2 = []
# arr2.append(arr)
# print(arr2)
# n = input("Добавить блюда: ")
# arr2.append(n)
# print(arr2)




#7 ne yveren
# a = 0
# lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
# for i in lst:
#     if i < 30 and i % 3 == 0:
#         print(i)
# for b in lst:
#     a+=b
#     print(b)




#8
# d = {'a': 2, 'b': 4, 'c': 6, 'd': 8}
# for k, v in d.items():
#     if v > 2:
#         print(v)





#9 
# a = ["k1", "k2", "k3", "k4", "k5", "k6"]
# b = [7, 8, 9, 10, 11, 12]
# n = int(input("Степень: "))
# d = {i:j**n for i, j in zip(a, b)}

# print(d)
# print(f"Я знаю твой ключ: {a}, его значением является: {b}")



#10
# dct = {"Gorod1": 200, "Gorod2": 150, "gorod3": 15}
# for k,v in dct.items():
#     i = k
# print(dct[input("Gorod: ")])





# #11

# dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# for k,v in dic.items():
#     if v % 2 == 0:
#         print(f"{v} even")
#     else:
#         print(f"{v} odd")





# #12 
# import random

# n = int(input("n = "))
# m = int(input("m = "))

# matrix = [[random.randint(1,9) for j in range(m)] for i in range(n)]

# print("-"*40) 
# for i in matrix:
#     print(f"{i}")

# d = [matrix[i][j] for i in range(n) for j in range(m) if i==j]


# print("диагональ - ", d)
# print("-"*40)

# b = int(input("stroka = "))
# c = [matrix[b-1][j] for j in range(m) ]
# print(c)

# f = int(input("stolbec = "))
# g = [matrix[i][f-1] for i in range(n) ]
# print(g)