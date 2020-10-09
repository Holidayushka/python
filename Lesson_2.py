# #Task 1

samplelist = [1, 1.5, 'adsas', True, [1,3]]
for item in range(len(samplelist)):
    print(type(samplelist[item]))

#Task 2

somelist = input("Enter something ").split()
j = 0
for item in range(int(len(somelist)/2)):
    somelist[j], somelist[j+1] = somelist[j+1], somelist[j]
    j += 2
print(somelist)

#Task 3

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
month = int(input("Enter the number of month "))
if month in winter:
    print('Winter')
elif month in spring:
    print('Spring')
elif month in summer:
    print("Summer")
else:
    print("Autumn")

month = int(input("Enter the number of month "))
seasons = {
    12 : "Winter",
    1 : "Winter",
    2 : "Winter",
    3 : "Spring",
    4 : "Spring",
    5 : "Spring",
    6 : "Summer",
    7 : "Summer",
    8 : "Summer",
    9 : "Autumn",
    10 : "Autumn",
    11 : "Autumn"
}
for k in seasons.keys():
    if month == k:
        print(seasons[k])

#Task 5

my_list = [7, 5, 3, 3, 2]
new_element = int(input("Enter new element: "))
for i in range(len(my_list)):
    if new_element >= my_list[0]:
        my_list.insert(0, new_element)
        break
    elif new_element < my_list[i] and new_element >= my_list[i+1]:
        my_list.insert(i+1, new_element)
        break
    else:
        my_list.append(new_element)
        break
print(my_list)

#Task 6

product = []
number = 1
while True:
    if input("exit?") != "exit":
        i = 0
        dict_sample = {}
        while i < 4:
            dict_sample[input("Enter name of the position")] = input("Enter position")
            i += 1
        i = 0
        new_product = (number, dict_sample)
        product.append(new_product)
        number += 1
        print(product)
    else:
        break

analis_dict = {}
analis_dict = dict.fromkeys(product[0][1])
for key in analis_dict.keys():
    current_set = set()
    for i in range(len((product))):
        current_set.add(product[i][1][key])
    analis_dict[key] = current_set
print(analis_dict)

#end