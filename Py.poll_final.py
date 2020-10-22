# Add our depenencies
import csv
import os
#assign a variable to load file from path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis, election_analysis.txt")

#1. Intialize total vote customer
total_votes = 0
#Print Canddidate Name
candidate_options= []
#1 Declare the empty dictionary
candidate_votes = {}


#open the election results and read the file
with open(file_to_load) as (election_data):
    file_reader = csv.reader(election_data)
    #Print headers Row
    headers = next(file_reader)
    print(headers)
    for row in file_reader:
        #2 add the total vote count
        total_votes+= 1

#Print total votes
  

        candidate_name = row[2]
    #Add candidate name to candidate last and make sure it is not double counted
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #2 begin tracking candidate votes
            candidate_votes[candidate_name]= 0
        else:
            candidate_votes[candidate_name] += 1 
    #Print candidate list
    
    print(candidate_options)
    print(candidate_votes)
    #1 Itierate throuhgh the candidate list
    for candidate_name in candidate_votes:
    #Get vote count of Candidate 
        votes = candidate_votes[candidate_name]
    # calcluate percentage of votes
        vote_percentage= float(votes)/float(total_votes) * 100
    #Print Candidate name and Percentage of votes
        candidate_results=(
            f"{candidate_name} : recieved {vote_percentage} % of the votes in this election.")
        print(candidate_results)