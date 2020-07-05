# pcost.py
#
# Exercise 1.27
import sys
def portfolio_cost(filename):
    f = open(filename, 'rt')
    headers = next(f)
    total_price = 0
    for line in f:
        row = line.split(',')
        total_price += int(row[1])*float(row[2])
    f.close()
    return total_price

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print ('Tota; cost:' , cost)
