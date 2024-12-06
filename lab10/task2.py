file5 = open('C:/Users/619/Desktop/СибГУТИ/Информатика/lab10/file5.txt', 'r')
f5 = file5.read().split()
file6 = open('C:/Users/619/Desktop/СибГУТИ/Информатика/lab10/file6.txt', 'r')
f6 = file6.read().split()
for word in f5:
    if word == "Academy":
        print("Слово Academy в file5")
        break
else:
    print("Слово Academy в file6")