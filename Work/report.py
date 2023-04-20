# report.py
# Exercise 2.6
# Read portfolio of holdings
# Read prices to dictionary

import csv

# Define function
def read_portfolio(filename):
    '''
    Read a csv file with name, shares, price data into a dictionary
    '''
    portfolio = []
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            name = row[0]
            shares = int(row[1])
            price = float(row[2])
            holding = {'name':name, 'shares':shares, 'price':price}
            portfolio.append(holding)
    return portfolio

# Define another function
def read_prices(filename):
    '''
    Read a csv file with names and prices data into a dictionary
    '''
    prices = {}
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(file)
        for row in rows:
            prices[row[0]] = float(row[1])

# Test function
portfolio = read_portfolio('Data/portfolio.csv')
print(portfolio)
