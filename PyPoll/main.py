# create file paths across operating systems
import os

# Module for reading CSV files
import csv

os.chdir(os.path.dirname(__file__))

#Setting working directory to where this Python file is
csvpath = os.path.join('Resources', 'election_data.csv')

#Define variables and dictionary{candidate: Vote count} for calculations
vote_count = 0
candidate={}

#Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        vote_count = vote_count + 1 #add 1 to vote_count for each row

          
        if row[2] in candidate: #if candidate is in candidate dictionary add 1 to vote count
            candidate[row[2]] = candidate[row[2]] + 1 
        
        else: #if candidate is not in dictionary, add candidate and 1 to vote count 
            candidate[row[2]] = 1 
   
# Specify the file to write to
output_path = os.path.join("Analysis", "Result.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
#wrining the header and total votes in the file
    filewriter = txtfile.write("Election Results\n")
    filewriter = txtfile.write("----------------------------\n")
    filewriter = txtfile.write(f"Total votes: {vote_count}\n")
    filewriter = txtfile.write("----------------------------\n")
#printing the header and total votes in the terminal
    print("Election Results")
    print("----------------------------")
    print(f"Total votes: {vote_count}")
    print("----------------------------")
#wrinting/printing the candidate and vote count from candidate dictionary
    for key in candidate:
        vote_percentage = (candidate[key]/vote_count)*100
        filewriter = txtfile.write(f"{key}: {vote_percentage:.3f}% ({candidate[key]})\n")
        print(f"{key}: {vote_percentage:.3f}% ({candidate[key]})")
#find and return the candidate with the most votes    
    winner = max(candidate, key=candidate.get)

#wrinting/printing the winner
    filewriter = txtfile.write("----------------------------\n")
    filewriter = txtfile.write(f"Winner: {winner}\n")
    filewriter = txtfile.write("----------------------------\n")

    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")
