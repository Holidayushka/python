"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран."""
my_dict = {}
with open("sixth_task_file.txt", "r") as my_file:
    lines = my_file.readlines()
    for line in lines:
        new_arg_string = ""
        for i in line:
            if i in "1234567890":
                new_arg_string += i
            else:
                new_arg_string += " "
            new_arg_list = new_arg_string.split()
        for i in range(len(new_arg_list)):
            new_arg_list[i] = int(new_arg_list[i])
        print(f"{line.split()[0]} {sum(new_arg_list)}")