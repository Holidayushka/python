"""5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу."""

def summary(arg_string):
    sum_list = arg_string.split()
    global summ
    summ = 0
    for i in range(len((sum_list))):
        sum_list[i] = int(sum_list[i])
        summ += sum_list[i]
    print(summ)
    while True:
        another_list = input("Enter numbers: ")
        another_list = another_list.split()
        if "q" in another_list:
            for i in range(len((another_list))):
                if another_list[i].isdigit():
                    another_list[i] = int(another_list[i])
                    summ += another_list[i]
                else:
                    return summ
        else:
            for i in range(len((another_list))):
                another_list[i] = int(another_list[i])
                summ += another_list[i]
            print(summ)
print(summary(input("Enter numbers: ")))
