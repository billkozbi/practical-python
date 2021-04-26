# mortgage.py
#
# Exercise 1.7

principal = 50000.0
rate = 0.05
payment = 2684.11
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
total_paid = 0.0
payment_month = 0

month_column = "MONTH"
already_paid_column = "ALREADY_PAID"
principal_left_column = "PRINCIPAL LEFT"
print(f'{month_column:>5}{already_paid_column:>20}{principal_left_column:>20}')
while principal > 0:
    payment_month += 1
    one_month_payment = payment
    if payment_month >= extra_payment_start_month and payment_month <= extra_payment_end_month:
        one_month_payment += extra_payment
    current_principal = principal * (1+rate/12)
    one_month_payment = min(one_month_payment, current_principal)
    principal = current_principal - one_month_payment
    total_paid = total_paid + one_month_payment
    print(f'{payment_month:5}{total_paid:20,.2f}{principal:20,.2f}')

print(f'Total paid {total_paid:,.2f}')
print(f'Months {payment_month}')