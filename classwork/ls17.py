# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# empty = [a**2 for a in list]
# # for i in list:
# #   empty.append(i)
# print(list)
# print(empty)




# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# empty = [a for a in list if a>5]
# # for i in list:
# #   if i > 5:
# #     empty.append(i)
# print(empty)





# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# empty = [i for i in list if i>5 and i%2==0]

# # for i in list:
# #   if i > 5 and i%2==0:
# #     empty.append(i)
# print(empty)





# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# empty = [i if i > 5 else "Error" for i in list]
# # for i in list:
# #   if i > 5:
# #     empty.append(i)
# #   else:
# #     empty.append("Error")
# print(empty)



# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# empty = ["True_2" if i%2==0 else "True_3" if i%3==0 else "False" for i in list]

# # for i in list:
# #   if i%2==0:
# #     empty.append("True_2")
# #   elif i%3==0:
# #     empty.append("True_3")
# #   else:
# #     empty.append("False")
# print(empty)





# list = [1, 2, 3]
# list_2 = [4, 5, 6]
# empty = [(i,y) for i in list for y in list_2 ]
# # for i in list:
# #   for y in list_2:
# #     empty.append((i, y))
# print(empty)
# for f in empty:
#   print(f)



# list = [5 for i in range(10)]
# print(list)


# a = "refregerator"
# list = [i*5 for i in a ]
# print(list)

# import random
# list = [random.randint(5, 10) for i in range(11)]
# print(list)
