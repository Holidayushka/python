"""4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор."""

origin_list = [1, 1, 212, 3, 123, 43, 3, 4, 5, 6, 6, 4]
new_list = []
for i in range(len(origin_list)):
    if origin_list[i] not in new_list:
        new_list.append(origin_list[i])
print(new_list)

#new_list_2 = [origin_list[i] for i in range(len(origin_list)) if origin_list[i] not in new_list_2]