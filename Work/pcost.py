# pcost.py
# Exercise 2.16
# Using zip()
# M. G. Castrellon
# 2 Aug 2023

import csv, sys
import numpy as np

def portfolio_cost(filename):
	file = open(filename)
	rows = csv.reader(file)
	headers = next(rows)
	list_share_cost = []
	for rowno, row in enumerate(rows, start=1):
		record = dict(zip(headers, row))
		try:
			nshares = int(record['shares'])
			price = float(record['price'])
		except ValueError:
			print(f'Row {rowno}: Bad row: {row}')
		else:
			cost = nshares*price
			list_share_cost.append(cost)
	file.close()
	total_cost = np.sum(list_share_cost)
	return total_cost

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'
	print('Using '+filename+' as default')

cost = portfolio_cost(filename)
print('\nTotal Cost:', cost)

