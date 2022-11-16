# pcost.py
# Exercise 1.30
# Turning script into a function
# M. G. Castrellon
# 16 Nov 2022

import numpy as np

def portfolio_cost(filename):
	file = open(filename, 'rt')
	headers = next(file).split(',')
	share_cost = []
	for line in file:
		row = line.split(',')
		number_of_shares = float(row[1])
		single_share_cost = float(row[2])
		p = number_of_shares*single_share_cost
		share_cost.append(p)
	file.close()
	return np.sum(share_cost)

total_cost = portfolio_cost('Data/portfolio.csv')
print('Total cost: ', total_cost)
