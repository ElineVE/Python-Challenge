
# Import file
import os
import csv

# define path and text file path
csvpath = os.path.join('Resources', 'election_data.csv')
result_path = os.path.join('Election_ResultsPyPoll.txt')
# create dictionary to hold the votes
votes = {}
totalvotes = 0

# open and read csv file

with open(csvpath) as csvfile:
    # specify delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header
    csv_header = next(csvreader)
    # Read each row of data after the header
    for row in csvreader:
        # define position of "candidate" in row
        candidate = row[2]
        # if candidate is not yet in the dictionary, add candidate with first vote received
        totalvotes = totalvotes + 1
        if candidate not in votes:
            votes[candidate] = 1
        else: 
            votes[candidate] += 1

#add dict keys for vote total
values = votes.values()
totalvotes = sum(values)

#print to terminal
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {totalvotes}")
print(f"-------------------------")
for key, value in votes.items():
    print(f"{key}: {value / totalvotes:.3%} ({value})")
print(f"-------------------------")
print(f"Winner: {max(votes, key=votes.get)}")
print(f"-------------------------")

#output results to text file
with open(result_path, "w") as txt_file:
   
    datafile = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {totalvotes}\n"
        f"-------------------------\n")

    txt_file.write(datafile)

    # for loop outside of datafile
    for key, value in votes.items():
        votername = key
        votervotes = value
        #add a .write line for results
        txt_file.write(f"{votername}: {votervotes / totalvotes:.3%} ({votervotes})\n")
    
    txt_file.write(f"-------------------------\n"
        f"Winner: {max(votes, key=votes.get)}\n"
        f"-------------------------")    

