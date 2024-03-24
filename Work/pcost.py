# pcost.py
# Exercise 3.14
# M. G. Castrellon
# 24 March 2024

import csv, sys
import numpy as np
import report

def portfolio_cost(filename):
	portfolio = report.read_portfolio(filename)
	n_records = len(portfolio)
	nshares = np.zeros(n_records)
	prices = np.zeros(n_records)
	for i, record in enumerate(portfolio):
		nshares[i] = record['shares']
		prices[i] = record['price']
	cost = nshares*prices
	total_cost = np.sum(cost)
	return total_cost

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    filename = args[1]
    print('Total cost:', portfolio_cost(filename))

if __name__ == '__main__':
    import sys
    main(sys.argv)

