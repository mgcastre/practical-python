# report.py
# Exercises 3.12
# M. G. Castrellon
# 24 March 2024

# Load libraries
import csv
from fileparse import parse_csv

# Define function to read portfolio
def read_portfolio(filename):
    '''
    Read a csv file with name, shares, price data into a dictionary
    '''
    with open(filename) as f:
        portfolio = parse_csv(lines=f, select=['name', 'shares', 'price'], 
                              types=[str, int, float])
    return portfolio

# Define function to read prices
def read_prices(filename):
    '''
    Read a csv file with names and prices data into a dictionary
    '''
    with open(filename) as f:
        prices = parse_csv(lines=f, has_headers=False, types=[str, float])
    prices = dict(prices)
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


# Define function(s) to print properly formatted report

def print_table_header():
    '''
    Prints header of report table. This function requires 
    no arguments.
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('\n')
    print('%10s %10s %10s %10s' % headers)
    print('---------- ---------- ---------- -----------')

def print_table_simple(report):
    '''
    Prints a table of the report in a simple format.
    '''
    print_table_header()
    for r in report:
        print('%10s %10d %10.2f %10.2f' % r)

def print_table_dollar(report):
    '''
    Prints a table of the report with tabs and dollar sign.
    '''
    print_table_header()
    for name, shares, price, change in report:
        price_dollars = "${:.2f}".format(price)
        print(f'{name:>10s} {shares:>10d} {price_dollars:>10} {change:>10.2f}')

def print_report(report, print_type=1):
    '''
    Takes a report of portfolio and prices and prints
    it nicely formatted. There are two formats available:
    (1) simple formatting (2) highly formatted with tabs 
    and dollar signs. Type 0 to print both types of report.
    '''
    if print_type == 1:
        print_table_simple(report)
    elif print_type == 2:
        print_table_dollar(report)
    elif print_type == 0:
        print_table_simple(report)
        print('\n')
        print_table_dollar(report)
    else:
        print("The number is out of bounds of the choices.")

# Define function to make and print report
def portfolio_report(portfolio_filename, prices_filename, print_type=2):
    '''
    Takes a portfolio and prices file and prints a report of how the value
    of the portfolio has changed over time.
    '''
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report, print_type)

# Define the main function
def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])

# Execute script if main
if __name__ == '__main__':
    import sys
    main(sys.argv)


