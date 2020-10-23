"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""
with open("fifth_task_file.txt", "w") as my_file:
    my_file.write(input("Enter numbers: "))
with open("fifth_task_file.txt", "r") as my_file:
    number_list = my_file.readline().split()
    for i in range(len(number_list)):
        number_list[i] = int(number_list[i])
    print(sum(number_list))