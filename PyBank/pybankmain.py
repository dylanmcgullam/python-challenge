import os
import csv



csvpath = os.path.join(".", "Instructions", "PyBank/Resources", "budget_data.csv")


total_months = 0
total_revenue =0
period_changes =[]
date_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0


with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)

    old_profit = int(row[1])
    total_months = total_months + 1
    total_revenue = total_revenue + int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    for row in csvreader:

        total_months= total_months + 1
        total_revenue = total_revenue + int(row[1])

        revenue_changes= int(row[1]) - old_profit
        period_changes.append(revenue_changes)
        old_profit= int(row[1])
        date_count.append(row[0])


        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]


        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]


mean_change = sum(period_changes)/len(period_changes)


high = max(period_changes)
low = min(period_changes)

print("Financial Analysis")
print("Total Months:" + str(total_months))
print("Total Amount:" + str(total_revenue))
print(mean_change)
print(greatest_increase_month, max(period_changes))
print(greatest_decrease_month, min(period_changes))
    