# Даны два целых числа A и В. Выведите все числа от A до B включительно, в
# порядке возрастания, если A < B, или в порядке убывания в противном случае.
a = int(input("Введите число А: "))
b = int(input("Введите число B: "))

nums = [a, b]

if a>b:
    nums.sort()
    print("Сортировка в порядке возрастания: ", nums)
else:
    nums.sort(reverse=True)
    print("Сортировка в порядке убывания: ", nums)
