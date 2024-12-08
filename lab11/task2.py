points = {
    1: ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u'],
    2: ['d', 'g'],
    3: ['b', 'c', 'm', 'p'],
    4: ['f', 'h', 'v', 'w', 'y'],
    5: ['k'],
    8: ['j', 'x'],
    10: ['q', 'z']
}
word = str(input("Введите слово: ")).lower()
total_points = 0
for letter in word:
    for key, value in points.items():
        if letter in value:
            total_points += key
            break
print(total_points)