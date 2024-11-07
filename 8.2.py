# Пользователь вводит две стороны трех прямоугольников.
#  Вывести их площади.

def area_of_rectangle(width, height):
    return round(width * height)

arr = []
for i in range(1, 4):
    width = float(input(f"Введите ширину {i}-го прямоугольника: "))
    height = float(input(f"Введите высоту {i}-го прямоугольника: "))
    area = area_of_rectangle(width, height)
    arr.append(area)

print(f'Площади 1, 2, 3 прямоугольников соответственно равны: {arr[0]}, {arr[1]}, {arr[2]}')