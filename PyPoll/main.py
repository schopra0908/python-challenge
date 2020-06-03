# Import the necessary dependencies for os.path.join()
import os
import csv
import collections
from collections import Counter

# Read in a .csv file
PyPoll_file = os.path.join("PyPoll", "election_data.csv")

# Create lists for variables
voters = []
unique_candidates = []

# Open the PyPoll file
with open(PyPoll_file, newline = '') as csvFile:
    csv_reader = csv.reader(csvFile, delimiter=',')
    #Read header Row
    header = next(csv_reader)
    #print(header)

# Metrics on all rows after header
    for row in csv_reader:
        #voters in the row
        voters.append(row[2])
        #sort them in ascending order - low to high
        ascending_list = sorted(voters)
        count = Counter(ascending_list)
        unique_candidates.append(ascending_list)

# ranking of candidates
    for value in unique_candidates:
        first_place = format((value[0][1])*100/sum(count.values()))
        second_place = format((value[1][1])*100/sum(count.values()))
        third_place = format((value[2][1])*100/sum(count.values()))
        fourth_place = format((value[2][1])*100/sum(count.values()))


# Print analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(count.values())}")
print("-------------------------")
print(f"{unique_candidates[0][0][0]}: {first_place}% ({unique_candidates[0][0][1]})")
print(f"{unique_candidates[0][1][0]}: {second_place}% ({unique_candidates[0][1][1]})")
print(f"{unique_candidates[0][2][0]}: {third_place}% ({unique_candidates[0][2][1]})")
print(f"{unique_candidates[0][3][0]}: {fourth_place}% ({unique_candidates[0][3][1]})")
print("-------------------------")
print(f"Winner:  {unique_candidates[0][0][0]}")
print("-------------------------")


# Export text file with the results
election_file = os.path.join("PyPoll", "election_data.txt")
with open(election_file, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes:  {sum(count.values())}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"{unique_candidates[0][0][0]}: {first_place}% ({unique_candidates[0][0][1]})\n")
    outfile.write(f"{unique_candidates[0][1][0]}: {second_place}% ({unique_candidates[0][1][1]})\n")
    outfile.write(f"{unique_candidates[0][2][0]}: {third_place}% ({unique_candidates[0][2][1]})\n")
    outfile.write(f"{unique_candidates[0][3][0]}: {fourth_place}% ({unique_candidates[0][3][1]})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner:  {unique_candidates[0][0][0]}\n")
    outfile.write("-------------------------\n")    