import random

with open('C:/Users/619/Desktop/СибГУТИ/Информатика/lab10/file1.txt', 'r') as f7:
    lines = f7.readlines()
# words = lines.split()
words = []
for i in lines:
    k = i.split()
    for j in k:
        j = j.replace(',', '')
        j = j.replace('.', '')
        j = j.replace('!', '')
        j = j.replace('?', '')
        j = j.replace('-', '')
        j = j.replace('"', '')
        j = j[:1:].upper() + j[1::]
        if len(j) >= 3 and len(j) <= 7:
            words.append(j)
def passw():
    password = words[random.randint(0, len(words)-1)] + words[random.randint(0, len(words)-1)]
    if len(password) >= 8 and len(password) <= 10:
        print(password)
    else:
        passw()
passw()