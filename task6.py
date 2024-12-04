'''100% complete'''

n = int(input("Введите размер матрицы: "))
matrix = [[0]*n for _ in range(n)]
print("Введите элементы матрицы")
for i in range(n):
    matrix[i] = [int(j) for j in input().strip().split(" ")]
new_matrix = matrix
for i in range(n):
    new_matrix[i][i], new_matrix[n-1-i][i] = matrix[n-1-i][i], matrix[i][i]
print("Новая матрица")
for n in new_matrix:
    print(*n)