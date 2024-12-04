'''100% complete'''

def func(x):
    return x**2/(10+x**3)
a = int(input("Введите левую границу: "))
b = int(input("Введите правую границу: "))
h = [10, 100, 1000]
for i in range(len(h)):
    n = (b-a)/h[i]
    p = a
    sum = n/2*(func(a)+func(b))
    while p < b:
        sum += func(p)*n
        p += n
    print(f"Неопределенный интеграл от {a} до {b} с шагом {h[i]} = {sum}")
