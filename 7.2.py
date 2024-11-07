# Дан массив целых чисел. Переписать все положительные элементы во
# второй массив, а остальные - в третий.
length = int(input('Введите длину массива: '))
arr = []
for i in range(length):
    print('Введите ', i, ' элемент')
    arr.append(int(input()))
min = arr[0]
for i in range(length):
    if arr[i] < min:
        min = arr[i]
        
arr_positive = []
arr_other = []
for i in range(length):
    if arr[i] > 0:
        arr_positive.append(arr[i])
    else:
        arr_other.append(arr[i])
print('Выделенные положительные числа в массиве: ', arr_positive)
print('Остальные числа в массиве: ', arr_other)