"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""
my_list = ["Один", "Два", "три", "Четыре"]
with open("fourth_task_file.txt", "r") as first_file:
    with open("fourth_task_file2", "w") as second_file:
        lines = first_file.readlines()
        for line, i in zip(lines, range(len(my_list))):
            number = line.split(" - ")
            second_file.write(f"{my_list[i]} - {number[1]}")