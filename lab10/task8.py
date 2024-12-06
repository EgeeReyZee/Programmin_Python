import sys
n, m = map(int, input("Введите размеры змеи: ").split())
if n >= 50 or m > 50 or n % 2 == 0:
    print("Введены ошибочные данные")
    sys.exit()
chet = 0
for i in range(n):
    if chet % 2 == 0:
        print("#"*m)
        chet += 1
    elif chet % 4 == 1:
        print("."*(m-1) + "#")
        chet += 1
    elif chet % 4 == 3:
        print("#" + "."*(m-1))
        chet += 1