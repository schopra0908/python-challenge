# Import the necessary dependencies for os.path.join()
import os
import csv
from collections import Counter

# Read in a .csv file
PyPoll_file = os.path.join( "election_data.csv")

# Create lists for variables
voters = []
voters_percent = []
candidates = []
unique_candidates = []

#after multiple failed attempts with the list
# or dictionary method, i've resorted to if thens 
county = []
khan = []
correy = []
li = []
otooley = []

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
        voters.append(int(row[0]))
        candidates.append(row[2])
        county.append(row[1])
        

# unique candidates count and totals
    #for all in set(candidates):
        #total_candidates = candidates.count(all)
        #vote_count = Counter(candidates)
        #voters.append(total_candidates)
        #total_percent = (total_candidates/count)*100
        #voters_percent.append(total_percent)
        
    #first_place = max(voters)
    #winners = max(vote_count.values())
    #second = max(vote_count.values()) - 1

    # - Note failed attempts in creating lists as arrays :(
    #lst=[i for i in vote_count.keys() if vote_count[i]==winners] 
    #lst2=[i for i in vote_count.keys() if vote_count[i]==second] 

    #for item in voters:
        #first = format((item[0][1]*100))

# winners
#winning_count = max(voters)
#print(f"{voters}")
#print(f"{first_place}: {first_place[0][0][0]}")
#print(sorted(lst2)[0])
#print(f"{first_place}: {first_place[0][0][0]}")
#print(sorted(lst2)[0])

# vote count - attempt #12312 (len = # items in list)
total_votes = (len(voters))

# votes per candidate
for candidate in candidates:
    if candidate == "khan":
        khan.append(candidates)
        khan_total = len(khan)
    elif candidate == "correy":
        correy.append(candidates)
        correy_total = len(correy)
    elif candidate == "li":
        li.append(candidates)
        li_total = len(li)
    else:
        otooley.append(candidates)
        otooley_total = len(otooley)

# calculate percentages
    khan_per = round(((khan_total / total_votes)*100),2)
    correy_per = round(((correy_total / total_votes)*100),2)
    li_per = round(((li_total / total_votes)*100),2)
    otooley_per = round(((otooley_total / total_votes)*100),2)

print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
print(f"Khan: {khan_per}% ({khan_total})")
