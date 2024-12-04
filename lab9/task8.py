'''100% complete'''

row, col = map(int, input("Введите размер матрицы: ").split())
matrix = [[1]*col for _ in range(row)]
for i in range(1, row):
    for j in range(1, col):
        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
for i in range(row):
    for j in range(col):
        matrix[i][j] = str(matrix[i][j]) + " "*(6-len(str(matrix[i][j])))
for col in matrix:
    print(*col)