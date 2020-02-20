#create a program to calculate the full cost of financing a car
import os

from amortization.amount import calculate_amortization_amount
from amortization.schedule import amortization_schedule
from tabulate import tabulate

tr = .07
title = 71.5
reg = 60
fees = title + reg

def precalc(term):

    amount = calculate_amortization_amount(price, ir, term)
    total = dp
    i = 0

    for number, amount, interest, principal, balance in amortization_schedule(price, ir, term):
        total = total + amount
        i = i + interest

    print()
    print('Term length: ', term, 'mo')
    print('Monthly Payment: ', "%.2f" % amount)
    print('interest Paid:  '  "%.2f" % i)
    print('Total Cost:  ', "%.2f" % total)
    print('Annual Cost: ', "%.2f" % (total/12))

    table = (x for x in amortization_schedule(price, ir, term))
    print(
        tabulate(
            table,
            headers=["Number", "Amount", "Interest", "Principal", "Balance"],
            floatfmt=",.2f",
            numalign="right"
        )    
    )

start = "Y"
while start == 'Y':
    os.system("clear")
    sticker = float(input('Enter the price of the vehicle:  ') or 0)
    dp = float(input('Enter downpayment amount:  ') or 0)
    ir = float(input('Enter interest rate:  ') or .18)
    tax = sticker * tr
    price = tax + sticker + title + reg - dp

    print()
    print('Down Payment: ', "%.2f" % dp)
    print('Tax:  ', "%.2f" % tax)
    print('Fees:  ', "%.2f" % fees)
    print('Total Borrowed:  ', "%.2f" % price)
    print('Interest Rate: ', "%.2f" % ir)
    
    for t in range(1, 6):
        term = t * 12
        precalc(term)
        print()
    try:
        start = str.upper(input('Do you wish to try another vehicle? (Y/N)' or "N"))
    except ValueError:
        print('Invalid entry.  Please enter "Y" or "N"')

exit()
