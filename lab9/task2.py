'''any% complete'''

import random
import sys

sys.setrecursionlimit(1000000)

matrix = [[0]*3 for _ in range(3)]
def fulling():
    nums = [x for x in range(1, 3**2+1)]
    summa = sum(nums) / 3

    for i in range(3):
        for j in range(3):
            matrix[i][j] = random.choice(nums)
            nums.remove(matrix[i][j])

    diag1, diag2, col, row = 0, 0, 0, 0
    for i in range(3):
        diag1 += matrix[i][i]
        diag2 += matrix[3-1-i][i]
        if sum(matrix[i]) == summa:
            row += 1
        col_sum = 0
        for j in range(3):
            col_sum += matrix[j][i]
        if col_sum == summa:
            col += 1
    if row == col and row == 3 and diag1 == diag2 and diag1 == summa:
        for row in matrix:
            print(*row)
    else:
        fulling()
fulling()
