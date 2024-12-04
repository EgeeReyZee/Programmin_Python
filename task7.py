'''100% complete'''

import random
row, col = map(int, input("Введите размеры зала: ").split())
argue = str(input("Хотите самостоятельно заполнить состояние мест? y/n ")).lower()
matrix = [[0]*row for _ in range(col)]
if argue == "y":
    for i in range(col):
        matrix[i] = [str(j) for j in input().strip().split(" ")]
elif argue == "n":
    for i in range(col):
        for j in range(row):
            matrix[i][j] = str(random.randint(0,1))
company = int(input("Введите количество людей в компании: "))
for i in range(col):
    if "0"*company in "".join(matrix[i]):
        print("Номер ряда с достаточным количество свободных мест: ", i+1)
        break
else:
    print("На вашу компанию нет мест")
print("Состояние зала")
for row in matrix:
    print(*row)