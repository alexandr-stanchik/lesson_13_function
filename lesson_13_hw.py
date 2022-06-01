# Hometask_13_1
# Из полученного списка чисел
# создайте список с суммами
# этих чисел, отсортированными
# по возрастанию
# In: 965 582 023 8 695210
# Out: [5, 8, 15, 20, 23]

def sort_sum_numbers(list_1: list) -> list:
    list_2 = []
    for i in list_1:
        sum_num = 0
        while i != 0:
            sum_num += i % 10
            i //= 10
        list_2.append(sum_num)
    return sorted(list_2)


print(sort_sum_numbers([int(i) for i in input().split()]))


# Hometask_13_2
# Напишите функцию f(x), которая
# возвращает значение следующей
# функции, определённой на всей
# числовой прямой:
# In: 4.5
# Out: 7.25

def function_2(x: float) -> float:
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        return -(x / 2)
    else:
        return (x - 2) ** 2 + 1


print(function_2(float(input())))


# Hometask_13_3
# Напишите функцию которая
# принимает на вход список
# целых чисел, удаляет из него
# все нечётные значения, а
# чётные нацело делит на два.
# In: 852 85 784 58
# Out: [426, 392, 29]

def function_1(list_1: list) -> list:
    """
    Функция_1

    Принимает на вход список
    целых чисел, удаляет из него
    все нечётные значения, а
    чётные нацело делит на два.
    """
    list_2 = []
    for i in list_1:
        if i % 2 == 0:
            list_2.append(i // 2)
    return list_2


print(function_1([int(i) for i in input().split()]))
