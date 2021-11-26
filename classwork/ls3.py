# arr = ["a", "b", "c", "d", "e", "f"]
# print(arr)
# print(arr[0])
# print(arr[3].title())
# print(arr[0].title())
# print(arr[-1].title())
# arrs = f"Буква: {arr[0].title()}"
# print(arrs)



# arr = []
# print(arr)
# arr.append("a")
# arr.append("b")
# arr.append("c")
# arr.append("d")
# arr.append("e")
# arr.append("f")
# print(arr)
# arr[0] = "g"
# print(arr)
# arr.insert(1, "p")
# print(arr)
# del arr[2]
# print(arr)
# del_item = arr.pop()
# print(del_item)
# print(arr)

# arr = ["lambo", "zhigul", "bmw", "mers"]
# print("Машины: ", arr)
# arrshow = f"Мне нужна машина: ", {arr[0].title()}
# print(arrshow)
# del arr[0]
# print("Машины: ", arr)



# arr = ["s", "f", "c", "g", "q", "h"]
# arr.sort(reverse=True)
# print(arr)

# arr = ["s", "f", "c", "g", "q", "h"]
# a = len(arr)
# print(arr)
# print(a)

# a = 5000
# b = 20
# c = int(input("Скок дней: "))

# if c >= 365:
#     s = a + a * b/100
#     print(s)
# else:
#     print("Нет")

# a = int(input("сторона а = "))
# r = int(input("радиус = "))
# pol = a/2
# if pol == r:
#     print("Да")
# else:
#     print("Нет")


win = int(input("Какая команда победила?: "))
if win == 1:
    print("Победила команда a")
elif win == 2:
    print("Победила команда b")
elif win == 3:
    print("Победила команда c")
elif win == 4:
    print("Победила команда d")
elif win == 5:
    print("Победила команда e")
elif win == 6:
    print("Победила команда f")
else:
    print("Никто не победил")
