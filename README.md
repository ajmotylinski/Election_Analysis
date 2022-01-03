# Election Analysis

## Project Overivew
There was a local election and the Colorado Board of Elections requested the creation of an election audit tool. This tool needs to be able to 
1. Calculate total number of ballots cast
2. List of Counties
3. Tabulated votes for each of the counties
4. Calculate percentage of total votes in each county
5. List of candidates who received votes.
6. Tabulate votes each candidate received.
7. Calculate percentage of total votes each candidate received
8. Determine winner of election based on popular vote.

## Resources
- Data source: election_results.csv
- Software: Python 3.9, VS Code

## Results
The analysis of the elections shows that:
- There were 369,711 votes cast in the election
- The counties were:
    - Jefferson
    - Denver
    - Arapahoe
- The county votes were:
    - Jefferson had 38,855 votes which made up 10.5% of the total number of votes.
    - Denver had 306,055 votes which made up 82.8% of the total number of votes.
    - Arapahoe had 24,801 votes which made up 3.1% of the total number of votes.
- The county with the highest number of votes was:
    - Denver county who had 306,055 votes.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    - Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was:
    - Diana DeGette who received 73.8% of the vote and 272,892 votes.

## Summary
This script could be leveraged to help with auditing other races within an election. If there were more races in this election, this script could be modified to read in those races also. For example if the ballot had a presidential election as well as state representatives. One modification that would need to be made is to have logic to populate a list of the presidential candidiates and another list of state representatives. We would use the similar logic to tabulate the counts for each of these offices. To make this script flexible to work for any election, the script would need to read in the header row to determine all the races on the ballot. After reading in the header, you would need to create a list and dictions for each race to populate the options and vote counts for the given race.
