import csv

# This gets the data
data = list(csv.DictReader(open('Resources/budget_data.csv', 'r')))
total_months, total_pnl, average_change, greatest_decrease_profits, greatest_increase_profits, current_index = 0, 0, 0, 0, 0, 0
changes = []  # We'll use this to store the change every month
month_greatest_increase, month_greatest_decrease = '', ''

# Finds all values except month of greatest increase and decrease
for item in data:
    total_months += 1
    total_pnl += int(data[current_index]['Profit/Losses'])
    if current_index > 0:
        changes.append(int(data[current_index]['Profit/Losses']) - int(data[current_index - 1]['Profit/Losses']))
    greatest_increase_profits = max(greatest_increase_profits,
                                    int(data[current_index]['Profit/Losses']) - int(
                                        data[current_index - 1]['Profit/Losses']))
    greatest_decrease_profits = min(greatest_decrease_profits,
                                    int(data[current_index]['Profit/Losses']) - int(
                                        data[current_index - 1]['Profit/Losses']))
    current_index += 1

# Resets iterator
current_index = 0

# Finds month of greatest increase and decrease
for item in data:
    if int(data[current_index]['Profit/Losses']) - int(
            data[current_index - 1]['Profit/Losses']) == greatest_decrease_profits:
        month_greatest_decrease = data[current_index]['Date']
    if int(data[current_index]['Profit/Losses']) - int(
            data[current_index - 1]['Profit/Losses']) == greatest_increase_profits:
        month_greatest_increase = data[current_index]['Date']
    current_index += 1

average_change = round(sum(changes) / len(changes), 2)

print('Financial Analysis\n------------------\n')
print(
    'Total Months: {}\nTotal Profit/Loss: ${}\nAverage Change: ${}\nGreatest Increase in Profits: {} (${})\nGreatest Decrease in Profits {} (${})'.format(
        total_months, total_pnl, average_change, month_greatest_increase, greatest_increase_profits,
        month_greatest_decrease, greatest_decrease_profits))

with open('Result.txt', 'w') as WriteFile:
    WriteFile.write(
        'Financial Analysis\n------------------\n' + 'Total Months: {}\nTotal Profit/Loss: ${}\nAverage Change: ${}\nGreatest Increase in Profits: {} (${})\nGreatest Decrease in Profits {} (${})'.format(
            total_months, total_pnl, average_change, month_greatest_increase, greatest_increase_profits,
            month_greatest_decrease, greatest_decrease_profits))
