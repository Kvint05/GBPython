number = int(input("Введите число больше 0"))
num = (i for i in range(1, number + 1, 2))
for j in num:
    print(j)
