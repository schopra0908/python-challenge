# Import the necessary dependencies for os.path.join()
import os
import csv

# Read in a .csv file
PyBank_file = os.path.join("PyBank", "budget_data.csv")

# Create lists for variables
variance = []
month = []

# Define variables
month_count = 0
prior_month_variance = 0
current_month_variance = 0
total_variance = 0

# Open the PyBank file
with open(PyBank_file, newline = '') as csvFile:
    csv_reader = csv.reader(csvFile, delimiter=',')
    #Read header Row
    header = next(csv_reader)
    #print(header)

    # Metrics on all rows after header
    for row in csv_reader:
        #month counts
        month_count = month_count + 1

        #total amount of variance over entire period
        current_month_variance = int(row[1])
        total_variance += current_month_variance

        if (month_count == 1):
            #prior month = current month
            prior_month_variance = current_month_variance
            continue
        else:
            #variance
            total_variance = current_month_variance - prior_month_variance
            
            #append month to month
            month.append(row[0])
            variance.append(total_variance)

            #prior month = current month
            prior_month_variance = current_month_variance

        #define new variables
        sum_variance = sum(variance)
        #print (variance)
        average_variance = round(sum_variance/(month_count -1),2)
        max_variance = max(variance)
        min_variance = min(variance)

        #what were the highest and lowest months?
        #locate the index or position of them
        highest_month = variance.index(max_variance)
        lowest_month = variance.index(min_variance)
        #define them
        best_month = month[highest_month]
        worst_month = month[lowest_month]


# Print analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {month_count}")
print(f"Total:  ${total_variance}")
print(f"Average Change:  ${average_variance}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_month})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_month})")


# Export text file with the results
budget_file = os.path.join("PyBank", "budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {month_count}\n")
    outfile.write(f"Total:  ${total_variance}\n")
    outfile.write(f"Average Change:  ${average_variance}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_month})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_month})\n")
    

