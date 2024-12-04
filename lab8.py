#1
# a = str(input("Введите список: "))
# a1 = a.split()
# letters = []
# nums = []
# print(len(a1))
# for i in range(len(a1)):
#     if a1[i].isalpha(): letters.append(a1[i])
#     elif a1[i].isdigit(): nums.append(a1[i])
# a1.clear()
# print(letters, "\n", nums)

#2
# import random
# ticket = []
# for i in range(6):
#     ticket.append((random.randint(1, 50)))
# print(ticket)

#3
# a = str(input("Введите ряд чисел: "))
# a1 = a.split()
# ans = []
# for i in range(len(a1)-1):
#     if int(a1[i]) < int(a1[i+1]):
#         ans.append(int(a1[i+1]))
# print(ans)

#4
# print("Начните вводить числа: ")
# spisok = []
# while "" not in spisok:
#     a = input()
#     if a != "":
#         spisok.append(int(a))
#     else: spisok.append(a)
# spisok = spisok[:-1:]
# avg = 0
# for i in spisok:
#     avg += i
# avg = avg/len(spisok)
# low = []
# eq = []
# high = []
# for i in spisok:
#     if i < avg:
#         low.append(i)
#     elif i > avg:
#         high.append(i)
#     else:
#         eq.append(i)
# print(avg, "\n", low, "\n", eq, "\n", high)

#5
# a = str(input("Введите ряд: "))
# b = int(input("Введите рост Андрея: "))
# a1 = a.split()
# for i in range(len(a1)):
#     if int(a1[-1]) < b:
#         if int(a1[i]) < b:
#             print(i+1)
#             break
#         elif int(a1[i]) == b:
#             print(i+2)
#             break
#     else: 
#         print(len(a1)+1)
#         break

#6
# import random
# a = []
# atts = 3
# for i in range(3):
#     num = random.randint(0, 1)
#     if num == 0:
#         a.append("O")
#     else: 
#         a.append("P")
# while not(a[-1] == a[-2] and a[-1] == a[-3]):
#     num = random.randint(0, 1)
#     if num == 0:
#         a.append("O")
#     else: 
#         a.append("P")
#     atts += 1
# print(a, "Количество попыток:", atts)

#7
# a = str(input("Введите номер карты: "))
# sum = 0
# if len(a) == 16:
#     for i in range(1, len(a), 2):
#         sum += int(a[i])
#     for i in range(0, len(a), 2):
#         if int(a[i]) * 2 < 9:
#             sum += int(a[i]) * 2
#         else:
#             sum += int(a[i]) * 2 - 9
#     if sum % 10 == 0:
#         print("Корректный номер")
#     else: print("Некорректный номер")
# else: print("Некорректный номер")

#8
# a = int(input())
# spisok = []
# for i in range(a):
#     b = str(input())
#     short = ""
#     if len(b) > 10:
#         short = b[0] + str(len(b) - 2) + b[-1]
#         spisok.append(short)
#     else:
#         spisok.append(b)
# for i in spisok:
#     print(i)

#9
# rooms = int(input("Введите количество комнат: "))
# cnt = 0
# for i in range(rooms):
#     room = str(input())
#     room = room.split()
#     if int(room[0]) + 2 <= int(room[1]):
#         cnt += 1
# print(cnt)