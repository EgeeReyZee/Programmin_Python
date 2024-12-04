'''100% complete'''

import random
import sys

sys.setrecursionlimit(10000)
def sea_battle():
    matrix = [["."]*4 for _ in range(4)]
    ships = []
    def ships_placing():
        for i in range(4):
            ships.append([random.randint(0,3), random.randint(0,3)])
        for i in range(4):
            for j in range(4):
                if ships[i] == ships[j] and i != j:
                    ships_placing()
                else: continue
    ships_placing()
    cnt = 0
    print("Ходите! Введите позицию через пробел")
    while ships != []:
        for row in matrix:
            print(*row)
        x, y = map(int, input().split())
        if [x-1, y-1] in ships:
            print("Есть пробитие")
            matrix[x-1][y-1] = "X"
            ships.remove([x-1, y-1])
        cnt += 1
    else:
        print("Поздравляю, вы победили за ", cnt, "ходов")
    argue = str(input("Желаете сыграть еще раз? y/n ")).lower()
    if argue == "y":
        sea_battle
    else:
        print("Хорошего дня <3")
sea_battle()
