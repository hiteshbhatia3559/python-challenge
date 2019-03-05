import csv

# This gets the data
data = list(csv.DictReader(open('Resources/budget_data.csv', 'r')))
total_months = 0
total_pnl = 0
average_change = 0
greatest_increase_profits = 0
greatest_decrease_profits = 0

for item in data:
    total_months += 1
    total_pnl = 

print('Financial Analysis\n------------------')
