mans = []
with open('C:/Users/619/Desktop/СибГУТИ/Информатика/lab10/file8.txt', 'r') as list:
    for string in list:
        mans.append([int(string.split()[1]), string.split()[0]])
mans.sort()
womans = []
with open('C:/Users/619/Desktop/СибГУТИ/Информатика/lab10/file7.txt', 'r') as list2:
    for string in list2:
        womans.append([int(string.split()[1]), string.split()[0]])
womans.sort()
n = int(input("Введите нужное количество имён: "))
sex = str(input("Введите пол: ")).lower()
if sex == "ж":
    for i in range(1, n+1):
        print(womans[-i][1])
elif sex == "м":
    for i in range(1, n+1):
        print(mans[-i][1])