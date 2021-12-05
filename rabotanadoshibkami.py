#1

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i < 5:
#         print(i)
# print(a[-1])



#2

# import random
# n = int(input("Кол-во элементов списка: "))
# a = 1
# arr = [random.randint(1, 15) for i in range(n)]
# print(arr)
# for i in arr:
#     a*=i
# print(a)


#3

# numbers = [5,6,7,6, 106, 161, 101, 91, 51, 54,237, 241]
# for i in numbers:
#     if i % 2 == 0:
#         print(i)
#     elif i == 237:
#         break



#4

# registered = ["User1", "User2", "User3"]
# checked = []
# for i in registered:
#     print(f"{i} not checked")
# print(checked)
# while registered:
#     f = registered.pop(0)
#     checked.append(f)
#     for i in checked:
#         print(f"user {i} is checked")
# print(checked)




#6
# a = ["burger", "pizza", "poure"]
# b = a[:]
# print(a)
# print(b)
# n = input("Какие блюда: ")
# a.append(n)
# print(a)
# print(b)




#7
# s = 0
# lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
# a = []
# for i in lst:
#     if i < 30 and i % 3 == 0:
#         a.append(i)
#         print(a)
#     else:
#         s+=i
#         print(s)




#8 
# a = {'a': 2, 'b': 4, 'c': 6, 'd': 8} 
# for i in a.values():
#     if i > 2:
#         print(i)





#9
# a = ["k1", "k2", "k3"]
# b = ["k4", "k5", "k6"]
# dict = {i:j for i,j in zip(a,b)}
# print(dict)





#10
# d = {"gorod1": 15, "gorod2": 5, "gorod3": 4}
# del d["gorod1"]
# print(d)




#11
# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# b = {i:["even" if j % 2 == 0 else "odd"] for i, j in d.items()}
# print(b)



#12
# import random

# n = int(input("n = "))
# m = int(input("m = "))

# matrix = [[random.randint(1,9) for i in range(n)] for j in range(m)]

# print("-"*40) 

# for i in matrix:
#   print(i)

# print("-"*40) 

# b = int(input("stroka = "))
# c = [matrix[b-1][j] for j in range(m)]
# print(c)

# f = int(input("stolbec = "))
# g = [matrix[i][f-1] for i in range(n)]
# print(g)

