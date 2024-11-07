# Дан одномерный массив, состоящий из N целочисленных элементов.
# Ввести массив с клавиатуры. Найти минимальный элемент. Вывести индекс
# минимального элемента на экран.
length = int(input('Введите длину массива: '))
arr = []
for i in range(length):
    print('Введите ', i, ' элемент')
    arr.append(int(input()))
min = arr[0]
for i in range(length):
    if arr[i] < min:
        min = arr[i]
        
print(arr)
print('Индекс минимального элемента массива: ', arr.index(min))
