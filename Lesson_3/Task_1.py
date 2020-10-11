# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(arg1, arg2):
    if arg2 == 0:
        return
    else:
        res = arg1 / arg2
        return res
print(division(int(input("Enter the first argument")), int(input("Enter the second argument"))))