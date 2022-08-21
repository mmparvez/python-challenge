# create file paths across operating systems
import os

# Module for reading CSV files
import csv

#-----------------------------------------------------
# Set working directory to where this Python file is
os.chdir(os.path.dirname(__file__))

#Set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

#Define function for average change in profit/loss
def Average(lst):
    return sum(lst) / len(lst)

#Defining variables and lists for calculations
month_count = 0
ttl_value = 0
month=[]
value=[]
changes=[]

#Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        month.append(row[0]) #add each month to month list
        value.append(int(row[1])) #add each value to value list
    
    month_count = len(month) #set month_count to length of month list
    ttl_value = sum(value) #set ttl_value to sum of value list

    #loop through value list
    for i in range(1,len(value)): 
        changes.append(value[i] - value[i-1]) #add each change to changes list
    
    Average_change = Average(changes) #calling average function to set Average_change
    Average_change = round(Average_change,2) #round to 2 decimal places
    Max_change = max(changes) #set Max_change to max of changes list
    Min_change = min(changes) #set Min_change to min of changes list
    #set month for the max and min change
    #first month's changes on profit/loss was 0, so add 1 to index
    Max_month = month[changes.index(Max_change) + 1] 
    Min_month = month[changes.index(Min_change) + 1]

# Specify the file to write to
output_path = os.path.join("Analysis", "Result.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
    # Writing in the file
    filewriter = txtfile.write("Financial Analysis\n")
    filewriter = txtfile.write("----------------------------\n")
    filewriter = txtfile.write(f"Total Months: {month_count}\n")
    filewriter = txtfile.write(f"Total: ${ttl_value}\n")
    filewriter = txtfile.write(f"Average Change: ${Average_change}\n")
    filewriter = txtfile.write(f"Greatest Increase in Profits: {Max_month} (${Max_change})\n")
    filewriter = txtfile.write(f"Greatest Decrease in Profits: {Min_month} (${Min_change})\n")

# Printing in the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${ttl_value}")
print(f"Average Change: ${Average_change}")
print(f"Greatest Increase in Profits: {Max_month} (${Max_change})")
print(f"Greatest Decrease in Profits: {Min_month} (${Min_change})")

