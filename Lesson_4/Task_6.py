"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного
б) итератор, повторяющий элементы некоторого списка, определенного заранее."""
from itertools import count
from itertools import cycle
first_elem = int(input("Enter start number: "))
last_elem = int(input("Enter last number: "))
for el in count(first_elem):
    if el > last_elem:
        break
    else:
        print(el)


last_count = int(input("Enter last count: "))
count = 1
for elem in cycle(input("Enter cycle: ")):
    if count > last_count:
        break
    print(elem)
    count += 1