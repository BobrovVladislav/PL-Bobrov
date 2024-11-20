# Дана прямоугольная матрица A[N, N]. Переставить первый и
# последний столбцы местами и вывести на экран.

def swap_columns(matrix):
    n = len(matrix)
    for i in range(n):
        matrix[i][0], matrix[i][-1] = matrix[i][-1], matrix[i][0]
    return matrix

input_filename = "10/БобровВладиславВладимирович_У244_vvod.txt"
output_filename = "10/БобровВладиславВладимирович_У244_vivod.txt"

# Читаем матрицу из файла
with open(input_filename, 'r', encoding='utf-8') as file:
    matrix = [list(map(int, line.strip().split())) for line in file]

print("Исходная матрица:")
for row in matrix:
    print(row)
swap_columns(matrix)

    # Записываем результаты в файл
with open(output_filename, 'w', encoding='utf-8') as file:
    file.write("Матрица после перестановки первого и последнего столбцов:\n")
    for row in matrix:
        file.write(' '.join(map(str, row)) + '\n')
print(f"Результат записан в файл: {output_filename}")