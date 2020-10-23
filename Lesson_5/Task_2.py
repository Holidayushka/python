"""2. Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""
with open("second_task_file.txt") as my_file:
    count = 0
    for line in my_file:
        count += 1
        print(f"There are {len(line)} signs in {count} string")
    print(f"There are {count} strings in this file")