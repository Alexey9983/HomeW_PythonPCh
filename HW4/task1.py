# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = (int(input("Введите число n : ")))
list_1 = []
for i in range(n):
    numb = int(input("Введите numb "))
    list_1.append(numb)
print(list_1)
m = (int(input("Введите число m элементов: ")))
list_2 = []
for i in range(m):
    numb = int(input("Введите numb "))
    list_2.append(numb)
print(list_2)
list3 = list_1 + list_2
print(list3)
final_list = []
for i in list3:
    if list3.count(i) > 1 and i not in final_list:
        final_list.append(i)
print(sorted(final_list))
