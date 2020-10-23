"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""
income_list = []
with open("third_task_file.txt", "r") as my_file:
    lines = my_file.readlines()
    for line in lines:
        surname, income = line.split(": ")
        income = int(income)
        if income < 20000:
            print(surname)
        income_list.append(income)
    print(sum(income_list)/len(income_list))