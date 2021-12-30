# def den():
#     b = 2
#     a = b*b
#     yield a
#     print("privet")
#     yield b

# t = den()
# print(next(t))
# print(next(t))





# def gen():
#     x = 2
#     print("Perviy perebor")
#     yield x
#     x*=2
#     print("Vtoroy perebor")
#     yield x
#     x /= 2
#     print("Tretiy perebor")
#     yield x

# t = gen()
# # print(next(t))
# # print(next(t))
# # print(next(t))

# for i in gen():
#     print(i)




# def gen():
#     n = int(input("кол-во чисел фибоначи: "))
#     a, b = 1, 1
#     for i in range(n):
#         yield a
#         a,b = b, a+b

# t = list(gen())
# for i in t:
#     print(i)
    



# def gen():
#     a = 1
#     while True:
#         if a > 1:
#             for i in range(2, a):
#                 if a % i == 0:
#                     break
#                 else:
#                     yield a
#         a+=1

# for i in gen():
#     print(i)



