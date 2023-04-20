# report.py
# Exercise 2.4
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
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio

# Test function
portfolio = read_portfolio('Data/portfolio.csv')
print(portfolio)
