import os
import csv

budget_csv = os.path.join('..','Resources','budget_data.csv')

months = 0
total_amount = 0
greatest_increase = 0
greatest_decrease = 0
bm = ''
wm = ''


with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile , delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        months += 1
        total_amount += int(row[1])
        if int(row[1]) > greatest_increase:
            bm = row[0]
            greatest_increase = int(row[1])
        elif int(row[1]) < greatest_decrease:    
            wm = row[0]
            greatest_decrease = int(row[1])

print("Financial Analysis")
print("___________________________________")

print(f"Total Months: {months}")
print(f"Total: $ {total_amount}")
print(f"Average Change: $ {round(total_amount/months,2)}")
print(f"Greatest Increase in Profits: {bm} ($ {greatest_increase})")
print(f"Greatest Decrease in Profits:  {wm} ($ {greatest_decrease})")




