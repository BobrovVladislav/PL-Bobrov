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

input_filename = "10/БобровВладиславВладимирович_У244_vvod.txt"
output_filename = "10/БобровВладиславВладимирович_У244_vivod.txt"

# Читаем матрицу из файла
matrix = []
with open(input_filename, 'r', encoding='utf-8') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            matrix.append(row)

if is_magic_square(matrix):
    magic_square_result = "Матрица является магическим квадратом."
else:
    magic_square_result = "Матрица не является магическим квадратом."

# Записываем результаты в файл
with open(output_filename, 'w', encoding='utf-8') as file:
    file.write("Результат проверки на магический квадрат:\n")
    file.write(magic_square_result + '\n\n')
print(f"Результат записан в файл: {output_filename}")
