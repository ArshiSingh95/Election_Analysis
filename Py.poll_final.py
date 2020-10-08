# Add our depenencies
import csv
import os
#assign a variable to load file from path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis, election_analysis.txt")

#open the election results and read the file
with open(file_to_load) as (election_data):
    file_reader = csv.reader(election_data)
    #Print headers Row
    headers = next(file_reader)
    print(headers)