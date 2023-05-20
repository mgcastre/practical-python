# report.py
# Exercise 2.9
# May 20th, 2023

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
            name = row[0]
            shares = int(row[1])
            price = float(row[2])
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
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print("Empty row, therefore skipped.")
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

# Testing new function
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)
for r in report:
    print(r)


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


