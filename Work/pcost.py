# pcost.py
# Exercise 1.27
# Reading a data file
# M. G. Castrellon
# 16 Nov 2022

import numpy as np

file = open('Data/portfolio.csv', 'rt')
headers = next(file).split(',')
share_cost = []
for line in file:
	row = line.split(',')
	number_of_shares = float(row[1])
	single_share_cost = float(row[2])
	p = number_of_shares*single_share_cost
	share_cost.append(p)
file.close()
total_cost = np.sum(share_cost)
print('Total cost: ', total_cost)
