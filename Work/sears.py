bill_thickness = 0.11 * 0.001 # meters (0.11 mm)
sears_height = 442 # height (meters)
nbills = 1
day = 1

while nbills * bill_thickness < sears_height:
    print(day, nbills, nbills * bill_thickness)
    day = day + 1
    nbills = nbills * 2

print('Number of days', day)
print('Number of bills', nbills)
print('Final height', nbills * bill_thickness)
