# Задача 2(18)
# Требуется найти в массиве A[1. N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
import random
MyArray = []
count = 0
N = int(input('Введите длину массива: '))
for i in range(N):
    MyArray.append(random.randint(1, N))
X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
if N < X:
    input('Искомое число не входит в диапазон массива')
else:
    minim = abs(X - MyArray[0])
    index = 0
    for i in range(1, N):
        count = abs(X - MyArray[i])
        if count < minim:
            minim = count
            index = i
    print(MyArray)
    print(f'Число {X} наиболее близко по величине к числу {MyArray[index]}, их разница {abs(X - MyArray[index])}')
