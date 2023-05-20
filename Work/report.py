# report.py
# Exercise 2.7
# Compute the current value of the portfolio along with the gain/loss
# May 20th, 2023

# Load libraries
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
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print("Empty row, therefore skipped.")
    return prices

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
print('The gain/loss is (in percent): ', difference)


