#Pypoll

import os
import csv

election_csv = os.path.join("Resources","election_data.csv")

Total_votes = 0
Candidates = []
Candidate_votes = []
Percent_votes = []

with open(election_csv , 'r') as csvfile:
    csvreader = csv.reader(csvfile , delimiter = ',')
    csvheader = next(csvreader)
    for row in csvreader:
        Total_votes += 1

        if row[2] not in Candidates:
            Candidates.append(row[2])
            index = Candidates.index(row[2])
            Candidate_votes.append(1)
        else:
            index = Candidates.index(row[2])
            Candidate_votes[index] += 1

    for votes in Candidate_votes:
        percentage = round(((votes/Total_votes)*100),3)
        Percent_votes.append(percentage)

    maxvotes = max(Candidate_votes)
    index = Candidate_votes.index(maxvotes)
    winner = Candidates[index]

print("Election Results") 
print("----------------------------")
print(f"Total Votes : {Total_votes}")
print("----------------------------")
for i in range(len(Candidates)):
    print(f"{Candidates[i]}: {Percent_votes[i]}% ({Candidate_votes[i]}) ")  
print("----------------------------")
print(f"Winner : {winner}")
print("----------------------------")

filename = "Analysis/Poll_analysis.txt"
f = open(filename,'w')
f.write("Election Results \n")
f.write("----------------------------\n")
f.write(f"Total Votes : {Total_votes}\n")
f.write("----------------------------\n")
for i in range(len(Candidates)):
    f.write(f"{Candidates[i]}: {Percent_votes[i]}% ({Candidate_votes[i]}) \n")  
f.write("----------------------------\n")
f.write(f"Winner : {winner}\n")
f.write("----------------------------\n")






