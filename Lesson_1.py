
#Task №1

elem_1 = 12
elem_2 = 15.8
elem_3 = "some string"
elem_4 = True
print(elem_1, elem_2, elem_3, elem_4)
elem_5 = input('Введите число')
elem_6 = input('Введите строку')
print(elem_5, elem_6)

#Task №2

sec = int(input("Введите время"))
min = sec // 60
hour = min // 60
sec = sec % 60
min = min % 60
print(f"%02d:%02d:%02d" % (hour, min, sec))

#Task №3

number = int(input("Введите число"))
result = number + number*10 + number + number * 100 + number * 10 + number
print(result)

#Task №4

number_1 = int(input("Введите число"))
maxdig = 0
while number_1 > 10:
    dig1 = number_1 % 10
    if dig1 > maxdig:
        maxdig = dig1
    number_1 = number_1 // 10
if number_1 > maxdig:
    maxdig = number_1
print(maxdig)

#Task №5

profits = int(input("Введите выручку"))
costs = int(input("Введите издержки"))
if profits > costs:
    print(f"Ваша прибыль больше издержек на {profits - costs}")
    staff = int(input("Введите численность сотрудников"))
    print(f"Ваша прибыль в расчете на 1 сотрудника равна {(profits - costs)/staff}")
elif profits < costs:
    print(f"Ваши издержки больше прибыли на {costs - profits}")
else:
    print("Вы работаете в нуль")

#Task №6

current_day = int(input("Введите результат первого дня"))
last_day = int(input("Введите желаемый результат"))
count = 1
while current_day < last_day:
    current_day = current_day * 1.1
    count = count + 1
print(count)
