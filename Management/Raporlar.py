import pandas as pd
import matplotlib.pyplot as plt


def yillik_gelir(year):
    data = pd.read_csv("database/gelir.txt", sep=' ', header=None, names=['Year', 'Month', 'Price'])

    data = data[data['Year'] == year]

    data['Date'] = pd.to_datetime(data[['Year', 'Month']].assign(day=1))

    aggregated_data = data.groupby('Date')['Price'].sum().reset_index()

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(aggregated_data['Date'], aggregated_data['Price'], marker='o')
    ax.set_xlabel('Tarih')
    ax.set_ylabel('Gelir')
    ax.set_title(f'{year} Yılının Gelir Tablosu')
    for label in ax.get_xticklabels():
        label.set_rotation(45)
    ax.grid(True)

    return fig


def yillik_gider(year):
    data = pd.read_csv("database/gider.txt", sep=' ', header=None, names=['Year', 'Month', 'Price'])

    data = data[data['Year'] == year]

    data['Date'] = pd.to_datetime(data[['Year', 'Month']].assign(day=1))

    aggregated_data = data.groupby('Date')['Price'].sum().reset_index()

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(aggregated_data['Date'], aggregated_data['Price'], marker='o')
    ax.set_xlabel('Tarih')
    ax.set_ylabel('Gider')
    ax.set_title(f'{year} Yılının Gider Tablosu')
    for label in ax.get_xticklabels():
        label.set_rotation(45)
    ax.grid(True)

    return fig


def yillik_gelir_gider(year):

    income_data = pd.read_csv("database/gelir.txt", sep=' ', header=None, names=['Year', 'Month', 'Income'])
    outcome_data = pd.read_csv("database/gider.txt", sep=' ', header=None, names=['Year', 'Month', 'Outcome'])

    income_data = income_data.groupby(['Year', 'Month']).sum().reset_index()
    outcome_data = outcome_data.groupby(['Year', 'Month']).sum().reset_index()

    merged_data = pd.merge(income_data, outcome_data, on=['Year', 'Month'], how='outer').fillna(0)

    merged_data['Difference'] = merged_data['Income'] - merged_data['Outcome']

    merged_data['Date'] = pd.to_datetime(merged_data[['Year', 'Month']].assign(day=1))

    merged_data = merged_data[merged_data['Year'] == year]

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(merged_data['Date'], merged_data['Difference'], marker='o', color="red")
    ax.set_xlabel('Tarih')
    ax.set_ylabel('Gelir - Gider')
    ax.set_title(f'{year} Yılı Gelir Gider Tablosu')
    for label in ax.get_xticklabels():
        label.set_rotation(45)

    ax.grid(True)

    return fig

def aylik_gelir(year, month):
    # Read income data
    income_data = pd.read_csv("database/gelir.txt", sep=' ', header=None, names=['Year', 'Month', 'Income'])

    # Filter income data for the specified year and month
    income_data_month = income_data[(income_data['Year'] == year) & (income_data['Month'] == month)].copy()

    # If there's no data for the specified month, return early
    if income_data_month.empty:
        print(f"No data found for year {year} and month {month}.")
        return

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Plot the income data
    ax.plot(range(1, len(income_data_month) + 1), income_data_month['Income'], marker='o')
    ax.set_xlabel('Data Point')
    ax.set_ylabel('Income')
    ax.set_title(f'Income for Year {year} and Month {month}')
    ax.grid(True)

    return fig


def aylik_gider(year, month):
    # Read outcome data
    outcome_data = pd.read_csv("database/gider.txt", sep=' ', header=None, names=['Year', 'Month', 'Outcome'])

    # Filter outcome data for the specified year and month
    outcome_data_month = outcome_data[(outcome_data['Year'] == year) & (outcome_data['Month'] == month)].copy()

    # If there's no data for the specified month, return early
    if outcome_data_month.empty:
        print(f"No data found for year {year} and month {month}.")
        return

    # Plot the outcome data
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Plot the income data
    ax.plot(range(1, len(outcome_data_month) + 1), outcome_data_month['Outcome'], marker='o')
    ax.set_xlabel('Data Point')
    ax.set_ylabel('Outcome')
    ax.set_title(f'Outcome for Year {year} and Month {month}')
    ax.grid(True)

    return fig

