# Дана прямоугольная матрица A[N, N]. Переставить первый и
# последний столбцы местами и вывести на экран.

def swap_columns(matrix):
    n = len(matrix)
    
    for i in range(n):
        matrix[i][0], matrix[i][-1] = matrix[i][-1], matrix[i][0]

    return matrix

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Исходная матрица:")
for row in A:
    print(row)

swap_columns(A)

print("\nМатрица после замены первого и последнего столбцов:")
for row in A:
    print(row)
