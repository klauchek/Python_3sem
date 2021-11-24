import pandas as pd

from matplotlib import pyplot as plt
"""
Задача #1: постройте графики среднего количества решённых задач (а) по факультетским группам,
(б) по группам по информатике. Формат графика - любой достаточно наглядный.

Задача #2: определите, из каких факультетских групп пришли и в какие группы по информатике попали люди,
которые смогли пройти более одного теста в хотя бы одной из двух последних задач. (Задачи G и H в таблице, каждый тест даёт 10 баллов.)
Рисовать график не обязательно, можно просто цифры посчитать.
"""

ejudge_data = pd.read_html('students/results_ejudge.html')
dec_data = pd.read_excel('students/students_info.xlsx')

ejudge_data = ejudge_data[0].rename(columns={'User': 'login'})
data = ejudge_data.merge(dec_data, on='login')

by_fac = data.groupby('group_faculty').mean()['Solved']
faculty_groups = list(by_fac.index)
by_fac_list = by_fac.to_list()

by_out = data.groupby('group_out').mean()['Solved']
groups_out = list(by_out.index)
by_out_list = by_out.to_list()

fig, ax = plt.subplots(ncols=2, nrows=1, gridspec_kw={"wspace": 0.3}, figsize=[12, 5])

ax[0].bar(faculty_groups, by_fac_list)
ax[0].set_xlabel('faculty_group')
ax[0].set_ylabel('average mark')

ax[1].bar(groups_out, by_out_list)
ax[1].set_xlabel('group_out')

fig.suptitle('Average marks in faculty and informatics groups')
#plt.show()
plt.savefig('marks.png')

###############################
successful = data[(data['G'] >= 10) | (data['H'] >= 10)]
print('Faculty groups:')
print(sorted(successful['group_faculty'].unique()))
print('Informatics groups:')
print(sorted(successful['group_out'].unique()))

