# mortgage.py
# M. G. Castrellon
# 10/04/2021

# Exercise 1.7: Dave's Mortgage

amount = 500000 #dollars
time = 30 #years
rate = 0.05
payment = 2684.11 #dollars
extra_payment = 1000 #dollars
ep_start_month = 61
ep_end_month = 108
total_paid = 0
x = 0

print('Month','\tTotal Paid','\tRemaining')
print('----\t----------\t---------')
while amount > 0:
    x += 1
    if (ep_start_month <= x <= ep_end_month) and (payment < amount):
        amount = amount * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
    elif payment < amount:
        amount = amount * (1+rate/12) - payment
        total_paid = total_paid + payment
    else:
        last_payment = amount
        amount = amount - last_payment
        total_paid = total_paid - last_payment
    print('%1.0f,\t%0.2f,\t%0.2f' % (x, total_paid, amount))

print('\nTotal paid %0.1f' % total_paid)
print('Number of months', x)
