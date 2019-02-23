"""
0.
Продолжаем задачу на фигруры.
Параметры каждой фигуры должны быть дескрипторами.
Дескриптор должен валидировать переданное значение.
Используя дескрипторы, проверьте правильность введённых данных (a, b, c, r > 0).
square и perimeter -  теперь тоже дескрипторы. Обратите внимание, что при каждом обращении к square/perimeter
значения будут вычисляться заново. Подумайте, как это можно обойти,
т.е. значение должно вычисляться только при первом обращении к дескриптору.
Если меняется один из атрибутов фигуры ( например r), то необходимо заново пересчитать square или perimeter
"""


"""
1.
Напишите менеджер контекста MultiFileOpen, который позволяет работать с несколькими файлами:
MultiFileOpen(('file1.txt', 'r'), ('file2.txt', 'w'), ..., ('fileN.txt', 'rb'))
"""

"""
2.
Напишите менеджер контекста Timer, который позволяет получать текущее время выполнения кода (отсчет начинается с конструкции with):
with Timer("Time: {}") as timer:
    do_some_logic()
    print(timer.now())  # Time: 3.4123 sec
    do_some_other_logic()
    print(timer.now())  # Time: 5.71 sec
"""


"""
3.
Напишите генератор fibonacci(n), который генерирует числа Фибоначчи до n включительно.
"""



"""
4.
Напишите класс, объектом которого будет итератор производящий только чётные числа до n включительно.
"""


"""
5.
Напишите генератор factorials(n), генерирующий последовательность факториалов натуральных чисел.
"""


"""
6.*
Напишите генератор BinomialCoefficients(n), генерирующий последовательность биномиальных коэффициентов C0n,C1n,…,Cnn
Запрещается использовать факториалы.
"""


"""
7.*
Напишите метакласс, который возводит имена всех аттрибутов класса в верхний регистр.
"""