import pandas as pd
from matplotlib import pyplot as plt
"""
Поля в данных: CARGO - авиакомпания, PRICE - стоимость груза на борту, WEIGHT - масса груза на борту.
Задача: посчитайте, сколько рейсов выполнила каждая авиакомпания, полную стоимость и полную массу перевезённых ей грузов.
Постройте график уместного вида с результатами.
"""
flights = pd.read_csv("flights.csv", index_col=0, sep=',')
companies = flights.CARGO.unique()
num_flights = pd.Series(dtype=int)
prices = pd.Series(dtype=int)
weights = pd.Series(dtype=int)

for company in companies:
    num_flights[company] = (flights['CARGO'] == company).sum()
    prices[company] = flights.loc[flights['CARGO'] == company, 'PRICE'].sum()
    weights[company] = flights.loc[flights['CARGO'] == company, 'WEIGHT'].sum()

print("Num of flights for each company:")
print(num_flights.to_string())
print("\nFull price of cargo for each company:")
print(prices.to_string())
print("\nFull weight of cargo for each company:")
print(weights.to_string())

fig, ax = plt.subplots(1, 3)
plt.subplots_adjust(wspace=0.8)
fig.set_figwidth(12)

ax[0].bar(companies, weights, color='violet')
ax[0].set_title('Weight')
ax[0].set_xlabel('Company')

ax[1].bar(companies, prices, color='blue')
ax[1].set_title('Price')
ax[1].set_xlabel('Company')

ax[2].bar(companies, num_flights, color='gray')
ax[2].set_title('Flights')
ax[2].set_xlabel('Company')

#plt.show()
plt.savefig('second_task.png')