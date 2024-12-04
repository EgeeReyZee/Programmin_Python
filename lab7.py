#1
# a = str(input())
# b = ""
# a1 = a.split()
# for i in range(len(a1)-1):
#     if a1[i] != a1[i+1]:
#         b = b + a1[i] + " "
# if a1[-1] != a1[-2]:
#     b = b + a1[-1]
# print(b)

#2 V1
# a = str(input())
# b = ""
# a1 = a.split()
# for i in range(1, len(a1)+1):
#     b = b + a1[-i] + " "
# print(b)
#2 V2
# a = str(input())
# a1 = a.split()
# b = ""
# if len(a1) == 2:
#     b = a1[1] + " " + a1[0]
#     print(b)
# else: print(" Ошибка! Некорректное количество слов")

#3
# a = str(input())
# b = ""
# for i in range(len(a)):
#     b = b + a[i] + "."
# print(b[:-1:])

#4
# a = str(input())
# a = a.replace("не плохо", "хорошо")
# a = a.replace("не плохой", "хороший")
# a = a.replace("не плоха", "хороша")
# print(a)

#5
# a1 = str(input())
# a2 = str(input())
# a3 = str(input())
# if a1 == "" or a2 == "" or a3 == "":
#     print("Не хайку. Должно быть 3 строки.")
# else:
#     glas = "ёуеаоэяию"
#     cnt = 0
#     for i in range(len(a1)):
#         if a1[i] in glas:
#             cnt += 1
#     if cnt == 5:
#         cnt = 0
#         for i in range(len(a2)):
#             if a2[i] in glas:
#                 cnt += 1
#     if cnt == 7:
#         cnt = 0
#         for i in range(len(a3)):
#             if a3[i] in glas:
#                 cnt += 1
#     if cnt == 5:
#         print("Хайку!")
#     else: print("Не хайку.")

#6
# a = str(input())
# nach = ""
# if a[-1] == "#":
#     a1 = a[:-1:]
#     for i in range(len(a1)):
#         if i % 2 == 0:
#             nach = nach + a1[i]
#     kon = ""
#     for i in range(len(a1)):
#         if i % 2 != 0:
#             kon = a1[i] + kon
#     print(nach+kon)
# else:
#     print("Ошибка! Отсутствует символ #")

#7
# import random
# dlina = int(input("Введите желаемую длину пароля: "))
# big = str(input("нужны ли заглавные буквы (да/нет) ")).lower() == "да"
# small = str(input("нужны ли строчные буквы (да/нет) ")).lower() == "да"
# nums = str(input("нужны ли цифры (да/нет) ")).lower() == "да"
# spec = str(input("нужны ли специальные символы (да/нет) ")).lower() == "да"

# symbs = ""
# if big: symbs += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# if small: symbs += "abcdefghijklmnopqrstuvwxyz"
# if nums: symbs += "1234567890"
# if spec: symbs += '!@#$%^&*()_+-={}[]|;\':"<>,.?/~'

# if symbs == "" or dlina < 0:
#     print("Ошибка!")
# else:
#     parol = ''.join(random.choice(symbs) for i in range(dlina))
# print(parol)

#8
# a = str(input("Введите данные матча: "))
# n1 = ""
# for i in range(len(a)):
#     if a[i] != "-":
#         n1 += a[i]
#     else:
#         a = a[i+1::]
#         break
# n2 = ""
# nums = "1234567890"
# for i in range(len(a)):
#     if a[i] not in nums:
#         n2 += a[i]
#     else:
#         a = a[i::]
#         break
# r1 = ""
# r2 = ""
# chet = 0
# for i in range(len(a)):
#     if a[i] != ":" and chet == 0:
#         r1 += a[i]
#     elif a[i] == ":":
#         chet += 1
#         a = a[i+1::]
#         r2 = a
#         break
# if int(r1) > int(r2):
#     print(n1)
# elif int(r1) < int(r2):
#     print(n2)
# else: print("Ничья")