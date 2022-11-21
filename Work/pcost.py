# pcost.py
# Exercise 1.33
# Read from cmd line
# M. G. Castrellon
# 21 Nov 2022

import csv, sys
import numpy as np

def portfolio_cost(filename):
	file = open(filename)
	rows = csv.reader(file)
	list_share_cost = []
	next(rows)
	for row in rows:
		try:
			number_of_shares = int(row[1])
			single_share_cost = float(row[2])
		except ValueError:
			print("Failed to parse, row skipped.")
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

