# pcost.py
# Exercise 1.31
# Error handling
# M. G. Castrellon
# 16 Nov 2022

import numpy as np

def portfolio_cost(filename):
	file = open(filename, 'rt')
	headers = next(file).split(',')
	list_share_cost = []
	for line in file:
		row = line.split(',')
		try:
			number_of_shares = int(row[1])
			single_share_cost = float(row[2])
			p = number_of_shares*single_share_cost
		except ValueError:
			print("Failed to parse")
			# pass
			# raise RuntimeError("Failed to parse")
		# single_share_cost = float(row[2])
		# p = number_of_shares*single_share_cost
		list_share_cost.append(p)
	file.close()
	cost = np.sum(list_share_cost)
	return cost, list_share_cost

print()
total_cost, table = portfolio_cost('Data/missing.csv')
print("Total price per share:")
for i in range(len(table)):
	print(table[i])
print('\nTotal cost: ', total_cost)
