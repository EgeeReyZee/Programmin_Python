'''100% complete'''

treasureCount = int(input("Введите количество сокровищ: "))
print("Введите коориданты сокровищ:")
treasureMap = []
for i in range(treasureCount):
    treasureMap.append([])
    a, b = map(int, input().split())
    treasureMap[i].append(a)
    treasureMap[i].append(b)
print("Введите коориданты Александра:")
a, b = map(int, input().split())
AlexGeo = [a, b]
min_distance = float('inf')  
min_index = -1

for i in range(treasureCount):    
    distance = abs(treasureMap[i][0] - AlexGeo[0]) + abs(treasureMap[i][1] - AlexGeo[1])
    if distance == 0:
        min_index = i
        break
    if distance < min_distance:
        min_distance = distance
        min_index = i
print("Ближайший клад на координатах: ", treasureMap[min_index])
