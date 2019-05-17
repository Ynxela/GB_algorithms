# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4
# квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья
# прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего.

# Ремарка - я понял задание как нахождение средней прибыли за год для каждого в отдельности, а потом средннее
# среди средних. Если интерпретировать задание, как получение среднего значения от годовых доходов всех предприятий,
# то решение задачи становится еще проще...

from collections import namedtuple

Enterprise = namedtuple('Enterprise', ['name', 'avg_'])

all_enterprises = set()

quantity = int(input('Сколько будет предприятий? '))

for e in range(quantity):
    data = input('Введите через запятую название и прибыли за 4 квартала (4 числа): ').split(' ')
    avg_ = (int(data[1]) + int(data[2]) + int(data[3]) + int(data[4])) / 4
    enterprise = Enterprise(data[0], avg_)
    all_enterprises.add(enterprise)

# Получаем среднее значение средних прибылей предприятий
total_avg = 0
for e in all_enterprises:
    total_avg += e.avg_
total_avg = total_avg / len(all_enterprises)

print('Предприятия с прибылями выше среднего: {}:'.format(total_avg))
for e in all_enterprises:
    if e.avg_ > total_avg:
        print('Предприятие "{}" со средней прибылью: {}.'.format(e.name, e.avg_))

print('\n')

print('Предприятия с прибылями ниже среднего: {}:'.format(total_avg))
for e in all_enterprises:
    if e.avg_ < total_avg:
        print('Предприятие "{}" со средней прибылью: {}.'.format(e.name, e.avg_))
