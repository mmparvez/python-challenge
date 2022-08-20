# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#-----------------------------------------------------
# Set working directory to where this Python file is
os.chdir(os.path.dirname(__file__))

# Optional: print the current working directory
print("This program is running from: " + os.getcwd())
#-----------------------------------------------------
csvpath = os.path.join('Resources', 'budget_data.csv')

def Average(lst):
    return sum(lst) / len(lst)
# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    month_count = 0
    ttl_value = 0
    month=[]
    value=[]
    changes=[]

        # Read each row of data after the header
    for row in csvreader:
        month_count = month_count + 1
        month.append(row[0])
        ttl_value = ttl_value + int(row[1])
        value.append(int(row[1]))
    
    for i in range(1,len(value)):
        changes.append(value[i] - value[i-1])
    Average_change = Average(changes)
    Average_change = round(Average_change,2)
    Max_change = max(changes)
    Min_change = min(changes)
    Max_month = month[changes.index(Max_change) + 1]
    Min_month = month[changes.index(Min_change) + 1]

# Specify the file to write to
output_path = os.path.join("Analysis", "Result.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    filewriter = txtfile.write("Financial Analysis\n")
    filewriter = txtfile.write("----------------------------\n")
    filewriter = txtfile.write(f"Total Months: {month_count}\n")
    filewriter = txtfile.write(f"Total: ${ttl_value}\n")
    filewriter = txtfile.write(f"Average Change: ${Average_change}\n")
    filewriter = txtfile.write(f"Greatest Increase in Profits: {Max_month} (${Max_change})\n")
    filewriter = txtfile.write(f"Greatest Decrease in Profits: {Min_month} (${Min_change})\n")


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${ttl_value}")
print(f"Average Change: ${Average_change}")
print(f"Greatest Increase in Profits: {Max_month} (${Max_change})")
print(f"Greatest Decrease in Profits: {Min_month} (${Min_change})")

