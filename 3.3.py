# Шоколадка имеет вид прямоугольника, разделенного на n×m долек.
# Шоколадку можно один раз разломить по прямой на две части.
# Определите, можно ли таким образом отломить от шоколадки часть, состоящую ровно из k долек.
# Программа получает на вход три числа: n, m, k и должна вывести "Да" или "Нет".

def can_break_chocolate(n, m, k):
    # чтобы отломить целое количество долек k должно быть кратно либо n либо m
    if (k % n == 0 or k % m == 0) and k <= n * m:
        print("Да")
    else:
        print("Нет")

n = int(input("Введите количество долек по вертикали (n): "))
m = int(input("Введите количество долек по горизонтали (m): "))
k = int(input("Введите количество долек, которое хотите отломить (k): "))

can_break_chocolate(n, m, k)