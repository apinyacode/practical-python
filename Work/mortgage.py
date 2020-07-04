# mortgage.py
#
# Exercise 1.7
principle = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 12*5
extra_payment_end_month = 12*9
extra_payment = 1000
month = 1

while principle > 0:
    
    if month < extra_payment_start_month or month > extra_payment_end_month:
        extra_payment = 0
    else : extra_payment = 1000
    principle = principle * (1+rate/12) - payment - extra_payment
    total_paid = total_paid + payment + extra_payment
    print(month, total_paid, extra_payment)
    month = month + 1

print('Total paid', total_paid)
print('Over', month, 'months')