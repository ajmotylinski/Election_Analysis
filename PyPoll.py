
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize Total number of votes to zero
total_votes = 0

#List to hold candidates
candidate_options= []

#Dictionary for votes for each candidate
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Loop throught each record in loaded file
    for row in file_reader:
        #increment total votes 
        total_votes = total_votes+1
        
        #read in candidate name from row
        candidate_name = row[2]
        
        #see if candidate name is in list of candidate options
        if candidate_name not in candidate_options:
            #append candidate to list of candidate_options 
            candidate_options.append(candidate_name)

            #Add candidate to candidate_votes dictionary with initial value of 0
            candidate_votes[candidate_name]=0

        #Increment votes for candidate
        candidate_votes[candidate_name] +=1

    #Determine percentage of votes for each candidate by looping thorugh the candidates_votes dictionary
    for candidate_name in candidate_votes:
        #Get votes for candidate
        votes = candidate_votes[candidate_name]

        #Calculate percentage based on votes and total_votes
        vote_percentage = float(votes) / float(total_votes) *100

        print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")