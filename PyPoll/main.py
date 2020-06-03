# Import the necessary dependencies for os.path.join()
import os
import csv

# Read in a .csv file
PyPoll_file = os.path.join("PyPoll", "election_data.csv")

# Create lists for variables
voters = []
voters_percent = []
candidates = []
unique_candidates = []

# Define Variables
count = 0


# Open the PyPoll file
with open(PyPoll_file, newline = '') as csvFile:
    csv_reader = csv.reader(csvFile, delimiter=',')
    #Read header Row
    header = next(csv_reader)
    #print(header)

# Metrics on all rows after header
    for row in csv_reader:
        #voters in the row
        count = count + 1
        candidates.append(row[2])

# unique candidates count and totals
    for all in set(candidates):
        total_candidates = candidates.count(all)
        voters.append(total_candidates)
        total_percent = (total_candidates/count)*100
        voters_percent.append(total_percent)
        
# winners
winning_count = max(voters)

print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
print