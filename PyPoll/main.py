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
csvpath = os.path.join('Resources', 'election_data.csv')

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

    vote_count = 0
    candidate={}
    


        # Read each row of data after the header
    for row in csvreader:
        vote_count = vote_count + 1
        if row[2] in candidate:
            candidate[row[2]] = candidate[row[2]] + 1
        else:
            candidate[row[2]] = 1
   
# Specify the file to write to
output_path = os.path.join("Analysis", "Result.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    filewriter = txtfile.write("Election Results\n")
    filewriter = txtfile.write("----------------------------\n")
    filewriter = txtfile.write(f"Total votes: {vote_count}\n")
    filewriter = txtfile.write("----------------------------\n")
    for key in candidate:
        vote_percentage = (candidate[key]/vote_count)*100
        filewriter = txtfile.write(f"{key}: {vote_percentage:.3f}% ({candidate[key]})\n")
    
    winner = max(candidate, key=candidate.get)
    filewriter = txtfile.write("----------------------------\n")
    filewriter = txtfile.write(f"Winner: {winner}\n")
    filewriter = txtfile.write("----------------------------\n")