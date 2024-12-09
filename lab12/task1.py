n = int(input('Введите количество людей на корабле: '))
peoples = []
order = {
    'woman/child': [],
    'man': [],
    'captain': []
}
print('Введите пассажиров корабля')
for i in range(n):
    peoples.append(input().split())
for i in range(n):
    if peoples[i][1] == 'woman' or peoples[i][1] == 'child':
        order['woman/child'].append(peoples[i][0])
    if peoples[i][1] == 'man':
        order['man'].append(peoples[i][0])
    if peoples[i][1] == 'captain':
        order['captain'].append(peoples[i][0])
for i in order['woman/child']:
    print(i)
for i in order['man']:
    print(i)
for i in order['captain']:
    print(i)