with open('C:/Users/619/Desktop/СибГУТИ/Информатика/lab10/file3.txt', 'r') as f6:
    lines = f6.readlines()
encrypted = []
for i in lines:
    k = i.split()
    for j in k:
        encrypted.append(j[::-1])
print(*encrypted)