"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""
with open("first_task_file.txt", "w") as first_file:
    while True:
        new_line = input("Enter new line: ")
        if new_line == "q":
            break
        else:
            first_file.write(f"{new_line}\n")