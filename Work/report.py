# report.py
# Exercise 2.16
# Formatted table using zip()
# 2 Aug 2023

# Load libraries
import csv

# Define function to read portfolio
def read_portfolio(filename):
    '''
    Read a csv file with name, shares, price data into a dictionary
    '''
    portfolio = []
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            name = record['name']
            shares = int(record['shares'])
            price = float(record['price'])
            holding = {'name':name, 'shares':shares, 'price':price}
            portfolio.append(holding)
    return portfolio

# Define function to read prices
def read_prices(filename):
    '''
    Read a csv file with names and prices data into a dictionary
    '''
    prices = {}
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        for n, row in enumerate(rows):
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print(f'Row {n}: Empty row, therefore skipped.')
    return prices

# Define function to generate report
def make_report(portfolio, prices):
    '''
    Takes a list of stocks and dictionary of prices as input 
    and returns a list of tuples containing the name of the stock, 
    the number of stocks, the new stock price and the change in 
    stock price since the time of purchase.
    '''
    report = []
    for s in portfolio:
        newPrice = prices[s['name']]
        priceChange = newPrice - s['price']
        newRow = (s['name'], s['shares'], newPrice, priceChange)
        report.append(newRow)
    return report

# Making report
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

# Printing formatted report
headers = ('Name', 'Shares', 'Price', 'Change')
print('\n')
print('%10s %10s %10s %10s' % headers)
print('---------- ---------- ---------- -----------')
for r in report:
    print('%10s %10d %10.2f %10.2f' % r)

# Alternative printing format
print('\n')
print('%10s %10s %10s %10s' % headers)
print('---------- ---------- ---------- -----------')
for name, shares, price, change in report:
    price_dollars = "${:.2f}".format(price)
    print(f'{name:>10s} {shares:>10d} {price_dollars:>10} {change:>10.2f}')

""" ## From Ex. 2.7
# Open files
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

# Calculate original portfolio value
totalOriginal = 0.0
for s in portfolio:
    totalOriginal += s['shares']*s['price']
print('Original Value: ', totalOriginal)

# Calculate new portfolio value
totalNew = 0.0
for s in portfolio:
    newPrice = prices[s['name']]
    totalNew += s['shares']*newPrice
print('New Value: ', totalNew)

# Calculate gain/loss
difference = ((totalNew - totalOriginal)/totalOriginal) * 100
print('The gain/loss is (in percent): ', difference) """


