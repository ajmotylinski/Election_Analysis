
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

#Winning candidate information
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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

    with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        #Determine percentage of votes for each candidate by looping thorugh the candidates_votes dictionary
        for candidate_name in candidate_votes:
            #Get votes for candidate
            votes = candidate_votes[candidate_name]

            #Calculate percentage based on votes and total_votes
            vote_percentage = float(votes) / float(total_votes) *100

            #Print out candidate name, percentage, and raw votes
            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            
            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

            #Determine winning vote and percentage
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name
        
        #Variable for election summary output
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        
        # Printing summary to console
        print(winning_candidate_summary)
        #Print winning summary to file
        txt_file.write(winning_candidate_summary)