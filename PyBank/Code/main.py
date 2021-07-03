# PyBank

import os
import csv

budget_csv = os.path.join('..','Resources','budget_data.csv')

months = 0
total_amount = 0
greatest_increase = 0
greatest_decrease = 0
bm = ''
wm = ''
change = []
dates = []


with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile , delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        months += 1
        total_amount += int(row[1])
        change.append(int(row[1]))
        dates.append(row[0])

monthly_change = []
for i in range(len(change)-1):
    changes = change[i+1] - change[i]
    monthly_change.append(changes)

avg_change = sum(monthly_change)/len(monthly_change)

greatest_inc = max(monthly_change)
greatest_index = monthly_change.index(greatest_inc)
greatest_date = dates[greatest_index + 1]


greatest_dec = min(monthly_change)
worst_index = monthly_change.index(greatest_dec)
worst_date = dates[worst_index + 1]

print("Financial Analysis")
print("_______________________________________")

print(f"Total Months: {months}")
print(f"Total: $ {total_amount}")
print(f"Average Change: $ {round(avg_change,2)}")
print(f"Greatest Increase in Profits: {greatest_date} ($ {greatest_inc})")
print(f"Greatest Decrease in Profits:  {worst_date} ($ {greatest_dec})")

filename = '../Analysis/Financial_analysis.txt'
f = open(filename, "w")
f.write("Financial Analysis \n")
f.write("_______________________________________ \n")

f.write(f"Total Months: {months} \n")
f.write(f"Total: $ {total_amount} \n")
f.write(f"Average Change: $ {round(avg_change,2)} \n")
f.write(f"Greatest Increase in Profits: {greatest_date} ($ {greatest_inc}) \n")
f.write(f"Greatest Decrease in Profits:  {worst_date} ($ {greatest_dec}) \n")


