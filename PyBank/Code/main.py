import os
import csv

budget_csv = os.path.join('..','Resources','budget_data.csv')




with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile , delimiter=",")
    header = next(csvreader)

    print("Finanacial Analysis")
    print("------------------------")
    for row in csvreader:
        Date = row[0]
        Amount = int(row[1])
    #print("Finanacial Analysis")
    #print("----------------------------------")
        Total_months = len(row[0])
    print(f"Total months: {Total_months} ")
    total = sum(Amount)
    #print(f"Total: {sum(Amount)}")
    #print(f"Average change: {sum(Amount)/len(Amount)}")



