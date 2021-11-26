# import random

# n = int(input("n = "))
# m = int(input("m = "))

# matrix = [[i]*m for i in range(n)]

# for i in matrix:
#     print(i)



# import random

# n = int(input("n = "))
# m = int(input("m = "))

# matrix = [[random.randint(1,9) for j in range(m)] for i in range(n)]

# print("-"*40)
# for i in matrix:
#     print(f"\t|{i}|")








import random

n = int(input("n = "))
m = int(input("m = "))

matrix = [[random.randint(1,9) for j in range(m)] for i in range(n)]

print("-"*40)
for i in matrix:
    print(f"\t|{i}|")

d = [matrix[i][j] for i in range(n) for j in range(m) if i==j]


print("диагональ - ", d)

f = [matrix[i] for i in range(n) if i == 3]
print(f"Третяя строка - {f}")

c = [matrix[j] for j in range(m) if j == 4]
print(f"Третий столбец - {c}")    