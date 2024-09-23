#Мне нужно сделать функцию №1
import math

# x = float(14.26)
# y = float(-1.22)
# z = float(3.5 * 10 ** (-2))

x = float(input('Введите x: '))
y = float(input('Введите y: '))
z = float(input('Введите z: ')) * 10**(-2)

s = (2 * math.cos(x - 2/3))/(1/2 + pow(math.sin(y), 2)) * (1 + (pow(z, 2))/3-pow(z, 2)/5)
print('Результат функции ', s)
