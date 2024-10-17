# Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
def smallest_divisor(num):
    if num < 2 :
        return 'Число должно быть не меньше 2'
    else : 
        divisor = 2
        while num % divisor != 0 :
            divisor += 1
        return divisor
    
n = int(input("Введите число: "))
print("Наименьший натуральный делитель равен: " + str(smallest_divisor(n)))  

