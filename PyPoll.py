#The data we need to retrieve
# 1. Total number of votes
# 2. List of candidates that received votes
# 3. Percentage of votes for each candidate
# 4. Total number of votes for each candidate
# 5. Winner of election based on popular vote

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print the header rows.
    headers = next(file_reader)
    print (headers)