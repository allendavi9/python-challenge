#!/usr/bin/env python
# coding: utf-8

# In[2]:


# PyPoll Homework

# Setup Dependencies 

import csv
import os

# files load/output

file_to_load = os.path.join("election_data.csv")
file_to_output = os.path.join("election_analysis.txt")


# Total Vote Counter
total_votes = 0

# Candidate options and vote counter
candidate_options = []
candidate_votes = { }

# Winning candidate and winning count tracker

winning_candidate = ""

winning_count = 0

# Read and convert csv into list
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    
    # Read header
    header = next(reader)
    
    for row in reader:
        # Run loader animation
        #print(". ", end ="")
        
        # Add to the total vote count
        
        total_votes = total_votes + 1
        
        # Extract candidate name from rows
        candidate_name = row[2]
        
        
        # If candidate does not match existing candidates
        
        # Loop is discovering candidates as it runs
        
        if candidate_name not in candidate_options:
            
            # Add candidate_name to list of candidates
            candidate_options.append(candidate_name)
            
            # Begin tracking candidate voter count
            candidate_votes[candidate_name] = 0
            
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        
with open(file_to_output, "w") as txt_file:
    
    # Print final vote count
    
    election_results = (
    
        f"\n\nElection Results\n"
        f"====================\n"
        f"Total Votes: {total_votes}\n"
        f"====================\n"
    )
    
    #print(election_results, end="")
    
    # Save final vote count to text file
    
    txt_file.write(election_results)
    
    # Elect winner by looping through counts
    
    for candidate in candidate_votes:
        
        # Retrieve vote count and percentage
        
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # Calculate winning vote count and candidate
        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            
        # Print each candidates count and percentage
        
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        
        #print(voter_output, end ="")
        
        txt_file.write(voter_output)
        
    # Print winning candidates
    
    winning_candidate_summary = (
        f"===================\n"
        f"Winner: {winning_candidate}\n"
        f"===================\n"
    )
    #print(winning_candidate_summary)
    
    # Save winning candidate name to text file
    
    txt_file.write(winning_candidate_summary)
    
        
        
        
        


# In[ ]:




