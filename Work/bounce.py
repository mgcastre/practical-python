# bounce.py
# M. G. Castrellon
# 10/04/2021

# Exercise 1.5: The Bouncing Ball

height = 100

for i in range(10):
	height = (3/5)*height
	# print("Height after %1.0f bounce(s): %0.1f" % (i+1, height))
	print("Height after %1.0f bounce(s):" % (i+1))
	print(round(height, 4))
	print("\n")