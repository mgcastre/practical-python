# pcost.py
# Exercise 2.15
# Practive enumerate()
# M. G. Castrellon
# 2 Aug 2023

import csv, sys
import numpy as np

def portfolio_cost(filename):
	file = open(filename)
	rows = csv.reader(file)
	list_share_cost = []
	next(rows)
	for rowno, row in enumerate(rows, start=1):
		try:
			number_of_shares = int(row[1])
			single_share_cost = float(row[2])
		except ValueError:
			print(f'Row {rowno}: Bad row: {row}')
		else:
			p = number_of_shares*single_share_cost
			list_share_cost.append(p)
	file.close()
	cost = np.sum(list_share_cost)
	return cost

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'
	print('Using '+filename+' as default')

cost = portfolio_cost(filename)
print('\nTotal Cost:', cost)

