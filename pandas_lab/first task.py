import pandas as pd
""" 
Судя по всему, поля в данных следует воспринимать предельно просто:
CONTRACTOR - кому платёж, STATUS - статус операции, SUM - сумма операции.

Задача #1: найдите 3 самых крупных платежа из реально проведённых (статус OK).

Задача #2: определите полную сумму реально проведённых платежей в адрес Umbrella, Inc.
"""
actions = pd.read_csv("transactions.csv", index_col=0, sep=',')
print("Task 1: Three largest payments with 'OK' status\n")
done_actions = actions[actions['STATUS']=='OK']
print(done_actions.sort_values(by='SUM', ascending=False).head(3))

#####
print("\n\nTask 1: Sum of payments with 'OK' status for Umbrella, Inc\n")
sum = done_actions.loc[done_actions['CONTRACTOR'] == 'Umbrella, Inc', 'SUM'].sum()
print("Sum: %d" % sum)





