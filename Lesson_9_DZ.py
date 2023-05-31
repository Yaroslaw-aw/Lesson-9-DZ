import numpy as np

#Задача 1. Дан список элементов. Используя библиотеку NumPy,
#  подсчитайте количество уникальных элементов в нём.
def dz_task1():
    size = np.random.randint(10, 20)
    spisok_elementov = np.random.randint(1, 10, size)
    print(spisok_elementov)
    unique_list, unique_counts = np.unique(spisok_elementov, return_counts=True)
    print(f'Уникальные элементы: {unique_list}')
    print(f'Их количество:       {unique_counts}')

# Задача 2. Создайте двумерный массив, размером 5х5. 
# Определите, есть ли в нём одинаковые строки.

def dz_task2():
    size = (5,5)
    matrix = np.random.randint(0, 2, size)
    print(matrix)
    result = np.corrcoef(matrix)
    print(result)
    for i in range(5 - 1):
        for j in range(i + 1, 5):
            answer = np.array_equal(matrix[i], matrix[j], equal_nan=False)
            if answer == True:
                print(f'Одинаковые строки есть, это {i+1}-я и {j+1}-я')
                return
    print('Одинаковых строк нет')

# Задача 3. Создайте двумерный массив случайного размера.
# Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива

def dz_task3():
    x = np.random.randint(3, 10)
    y = np.random.randint(3, 10)
    size = (x, y)
    matrix = np.random.randint(1, 20, size)
    print(matrix)
    max_index = np.argmax(matrix)
    print(f'Индекс максимального элемента: {max_index}')
    min_index = np.argmin(matrix)
    print(f'Индекс минимального элемента: {min_index}')
    main_diag = np.diag(matrix)
    print(f'Элементы главной диагонали матрицы:\n{main_diag}')
