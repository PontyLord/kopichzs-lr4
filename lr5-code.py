import random
print("Введите размерность матрицы")
n = int(input("Количество строк: "))
m = int(input("Количество столбцов: "))
matrix = []

for i in range(n):
    mat=[]
    for j in range(m):
        j = random.randint(-1,10)
        mat.append(j)
    matrix.append(mat)

for i in matrix:
  print(i)
zero = []
in_zero = []
sorting = []
symmet = []


import numpy as np

def check_row(row):
    for i in range(len(row) - 1):
        if (row[i] % 2) == (row[i + 1] % 2):
            return False
    if len(row) > 1 and row[0] % 2 == 0 and row[1] % 2 == 1:
        return True
    return False

def count_valid_rows(matrix):
    count = 0
    for row in matrix:
        if check_row(row):
            count += 1
    return count

def generate_random_matrix(rows, cols, min_value=0, max_value=100):
    return np.random.randint(min_value, max_value, size=(rows, cols))

rows1, cols1 = np.random.randint(1, 11), np.random.randint(1, 11)
rows2, cols2 = np.random.randint(1, 11), np.random.randint(1, 11)

matrix1 = generate_random_matrix(rows1, cols1)
matrix2 = generate_random_matrix(rows2, cols2)

count1 = count_valid_rows(matrix1)
count2 = count_valid_rows(matrix2)

print("Первый массив:")
print(matrix1)

if count1 == 0:
    print("В первом массиве нет строк с заданными условиями.")
else:
    print(f"В первом массиве {count1} строк(и) с заданными условиями.")

print("\nВторой массив:")
print(matrix2)

if count2 == 0:
    print("Во втором массиве нет строк с заданными условиями.")
else:
    print(f"Во втором массиве {count2} строк(и) с заданными условиями.")
