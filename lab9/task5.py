'''100% complete'''

row, col = map(int, input("Введите количество столбцов и строк: ").split())
matrix = [[0]*col for _ in range(row)]
print("Введите элементы матрицы")
for i in range(row):
    matrix[i] = [int(j) for j in input().strip().split(" ")]
rows_count = len(matrix)
colums_count = len(matrix[0])
new_matrix = [[0] * rows_count for _ in range(colums_count)]
print("Транспонированная матрица: ")
for i in range(rows_count):
    for j in range(colums_count):
        new_matrix[j][i] = matrix[i][j]
for row in new_matrix:
    print(*row)