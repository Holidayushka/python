"""2. Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента."""

origin_list = [3, 2, 5, 12, 7, 234, 67, 1233, 65]
print([origin_list[i] for i in range(1, len(origin_list)) if origin_list[i-1] < origin_list[i]])