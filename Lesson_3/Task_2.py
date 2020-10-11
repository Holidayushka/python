"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой."""

def person(name, surname, age, city, email, phone_number):
    return " ".join([name, surname, age, city, email, phone_number])
print(person(input("Enter name"), input("Enter surname"), input("Enter age"), input("Enter city"), input("Enter email"), input("Enter phone_number")))