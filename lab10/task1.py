scores = []
with open('C:/Users/619/Desktop/СибГУТИ/Информатика/lab10/file4.txt', 'r') as list:
    for string in list:
        scores.append([int(string.split()[2]), string.split()[0], string.split()[1]])
scores.sort()
print(scores[-2][1], scores[-2][2], "(Набранное количество баллов: ", scores[-2][0], ")")