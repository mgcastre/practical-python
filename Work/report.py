# report.py
# Exercise 2.5
# Read portfolio of holdings

import csv

# Define function
def read_portfolio(filename):
    '''
    Read a csv file with name, date, shares, price data into a list
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

# Test function
portfolio = read_portfolio('Data/portfolio.csv')
print(portfolio)
