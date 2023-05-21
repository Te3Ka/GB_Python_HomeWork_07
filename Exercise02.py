'''
Напишите функцию
print_operation_table(operation, num_rows = 6, num_columns = 6),
которая принимает в качестве аргумента функцию,
вычисляющую элемент по номеру строки и столбца.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны.
Нумерация строк и столбцов идёт с единицы.
Примечание: бинарной операцией называется любая операция,
у которой ровно два аргумента, как, например, у операции умножения.

Ввод:
print_operation_table(lambda x, y: x * y)

Вывод:
 1  2  3  4  5  6
 2  4  6  8 10 12
 3  6  9 12 15 18
 4  8 12 16 20 24
 5 10 15 20 25 30
 6 12 18 24 30 36
'''

# Функция вывода автора программы
def author():
    print('****************************')
    print('Программа создана:')
    print('Илья "Te3K@_PaynE" Новичихин')
    print('79811131773@yandex.ru')
    print('****************************')

def print_operation_table(operation, num_rows = 6, num_columns = 6):
    funct = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in funct:
        print(*[f'{x:>5}' for x in i])


print("Программа выводит таблицу множения со всеми элементами от 1 * 1 до введённого количество строк и столбцов.")
rows = int(input("Введите количество строк: "))
columns = int(input("Введите количество столбцов: "))
print_operation_table(lambda rows, columns: rows * columns, rows, columns)
author()