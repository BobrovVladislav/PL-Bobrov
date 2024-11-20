# Дана целая квадратная матрица n-го порядка.
#  Определить,является ли она магическим квадратом,
#  т. е. такой матрицей, в которой суммы элементов во всех строках и столбцах одинаковы.

def is_magic_square(matrix):
    n = len(matrix)
    # Проверяем, что это квадратная матрица
    for row in matrix:
        if len(row) != n:
            return False
        
    # Считаем сумму первой строки как эталон
    magic_sum = sum(matrix[0])

    # Проверяем суммы строк
    for row in matrix:
        if sum(row) != magic_sum:
            return False
    # Проверяем суммы столбцов
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != magic_sum:
            return False
    # Проверяем сумму главной диагонали
    if sum(matrix[i][i] for i in range(n)) != magic_sum:
        return False
    # Проверяем сумму побочной диагонали
    if sum(matrix[i][n - i - 1] for i in range(n)) != magic_sum:
        return False

    return True

matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(matrix):
    print("Матрица является магическим квадратом.")
else:
    print("Матрица не является магическим квадратом.")
