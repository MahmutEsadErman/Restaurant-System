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

    income_data = income_data.groupby(['Year', 'Month']).sum().reset_index()
    outcome_data = outcome_data.groupby(['Year', 'Month']).sum().reset_index()

    merged_data = pd.merge(income_data, outcome_data, on=['Year', 'Month'], how='outer').fillna(0)

    merged_data['Difference'] = merged_data['Income'] - merged_data['Outcome']

    merged_data['Date'] = pd.to_datetime(merged_data[['Year', 'Month']].assign(day=1))

    merged_data = merged_data[merged_data['Year'] == year]

    plt.plot(merged_data['Date'], merged_data['Difference'], marker='o', color="red")
    plt.xlabel('Tarih')
    plt.ylabel('Gelir - Gider')
    plt.title(f'{year} Yılı Gelir Gider Tablosu')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()


def aylik_gelir(year, month):
    # Read income data
    income_data = pd.read_csv("../database/gelir.txt", sep=' ', header=None, names=['Year', 'Month', 'Income'])

    # Filter income data for the specified year and month
    income_data_month = income_data[(income_data['Year'] == year) & (income_data['Month'] == month)].copy()

    # If there's no data for the specified month, return early
    if income_data_month.empty:
        print(f"No data found for year {year} and month {month}.")
        return

    # Plot the income data
    plt.plot(range(1, len(income_data_month) + 1), income_data_month['Income'], marker='o')
    plt.xlabel('Data Point')
    plt.ylabel('Income')
    plt.title(f'Income for Year {year} and Month {month}')
    plt.xticks(range(1, len(income_data_month) + 1))
    plt.tight_layout()
    plt.grid(True)
    plt.show()

def aylik_gider(year, month):
    # Read outcome data
    outcome_data = pd.read_csv("../database/gider.txt", sep=' ', header=None, names=['Year', 'Month', 'Outcome'])

    # Filter outcome data for the specified year and month
    outcome_data_month = outcome_data[(outcome_data['Year'] == year) & (outcome_data['Month'] == month)].copy()

    # If there's no data for the specified month, return early
    if outcome_data_month.empty:
        print(f"No data found for year {year} and month {month}.")
        return

    # Plot the outcome data
    plt.plot(range(1, len(outcome_data_month) + 1), outcome_data_month['Outcome'], marker='o', color='red')
    plt.xlabel('Data Point')
    plt.ylabel('Outcome')
    plt.title(f'Outcome for Year {year} and Month {month}')
    plt.xticks(range(1, len(outcome_data_month) + 1))
    plt.tight_layout()
    plt.grid(True)
    plt.show()

#yillik_gelir_gider(2024)
aylik_gider(2024, 5)
