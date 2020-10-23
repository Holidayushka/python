"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со
средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста."""
import json

with open("seventh_task_file.json", "w") as my_json:
    with open("seventh_task_file.txt", "r") as my_file:
        company_dict = {}
        medium_profit_dict = {}
        total_profit, count = 0, 0
        lines = my_file.readlines()
        for line in lines:
            company_info = line.split()
            profit = int(company_info[2]) - int(company_info[3])
            company_dict[company_info[0]] = profit
            if profit > 0:
                total_profit += profit
                count += 1
                medium_profit_dict["average_profit"] = total_profit / count
            company_list = [company_dict, medium_profit_dict]
        json.dump(company_list, my_json)