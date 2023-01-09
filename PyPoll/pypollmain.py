import os
import csv

csvpath = os.path.join(".", "Instructions", "PyPoll/Resources", "election_data.csv")

candidates = []
number_of_votes = []
percent_of_votes = []
total_votes = 0


with open(csvpath, "r") as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread, None)

    for row in csvread:

        total_votes = total_votes + 1

        name_candidate = row[2]

        if name_candidate not in candidates:
            candidates.append(name_candidate)
            index = candidates.index(row[2])
            number_of_votes.append(1)
        else: 
            index = candidates.index(row[2])
            number_of_votes[index] += 1

    for votes in number_of_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_of_votes.append(percentage)


    winner = max(number_of_votes)
    index = number_of_votes.index(winner)
    winning_candidate = candidates[index]

print("Election Results")
print("------------------------------------")
print("Total Votes: " + str(total_votes))
print("------------------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_of_votes[i])} ({str(number_of_votes[i])})")
print("------------------------------------")
print(f"Winner: {winning_candidate}")  


results_file = os.path.join(".", "Instructions", "PyPoll/Resources", "election_data_results.txt")

with open(results_file, "w") as txtfile:
   
    txtfile.write("Election Results")
    txtfile.write("------------------------------------")
    txtfile.write("Total Votes:" + str(total_votes))
    txtfile.write("------------------------------------")
    for i in range(len(candidates)):
        txtfile.write(f"{candidates[i]}: {str(percent_of_votes[i])} ({str(number_of_votes[i])})")
    txtfile.write("------------------------------------")
    txtfile.write("Winner:" + str(winning_candidate))