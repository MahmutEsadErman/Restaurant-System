import pandas as pd
import matplotlib.pyplot as plt


def yillik_gelir(year):
    data = pd.read_csv("../database/gelir.txt", sep=' ', header=None, names=['Year', 'Month', 'Price'])

    data = data[data['Year'] == year]

    data['Date'] = pd.to_datetime(data[['Year', 'Month']].assign(day=1))

    aggregated_data = data.groupby('Date')['Price'].sum().reset_index()

    plt.plot(aggregated_data['Date'], aggregated_data['Price'], marker='o')
    plt.xlabel('Tarih')
    plt.ylabel('Gelir')
    plt.title(f'{year} Yılının Gelir Tablosu')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()


def yillik_gider(year):
    data = pd.read_csv("../database/gider.txt", sep=' ', header=None, names=['Year', 'Month', 'Price'])

    data = data[data['Year'] == year]

    data['Date'] = pd.to_datetime(data[['Year', 'Month']].assign(day=1))

    aggregated_data = data.groupby('Date')['Price'].sum().reset_index()

    plt.plot(aggregated_data['Date'], aggregated_data['Price'], marker='o')
    plt.xlabel('Tarih')
    plt.ylabel('Gider')
    plt.title(f'{year} Yılının Gider Tablosu')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()


def yillik_gelir_gider(year):

    income_data = pd.read_csv("../database/gelir.txt", sep=' ', header=None, names=['Year', 'Month', 'Income'])
    outcome_data = pd.read_csv("../database/gider.txt", sep=' ', header=None, names=['Year', 'Month', 'Outcome'])

    income_data = income_data[income_data['Year'] == year]
    outcome_data = outcome_data[outcome_data['Year'] == year]

    merged_data = pd.merge(income_data, outcome_data, on=['Year', 'Month'], how='outer').fillna(0)

    merged_data['Difference'] = merged_data['Income'] - merged_data['Outcome']

    merged_data['Date'] = pd.to_datetime(merged_data[['Year', 'Month']].assign(day=1))

    merged_data = merged_data.groupby('Date')['Difference'].sum().reset_index()

    plt.plot(merged_data['Date'], merged_data['Difference'], marker='o')
    plt.xlabel('Tarih')
    plt.ylabel('Gelir - Gider')
    plt.title(f'{year} Gelir Gider Farkı')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()


yillik_gelir_gider(2024)

