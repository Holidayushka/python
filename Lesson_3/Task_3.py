"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов."""

def summary(arg1, arg2, arg3):
    if arg1 == min(arg1, arg2, arg3):
        arg1 = 0
    elif arg2 == min(arg1, arg2, arg3):
        arg2 = 0
    else:
        arg3 = 0
    return arg1 + arg2 + arg3

print(summary(int(input("arg1 = ")), int(input("arg2 = ")), int(input("arg3 = "))))
