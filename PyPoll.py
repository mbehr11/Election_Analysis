#The data we need to retrieve: Add our dependencies
import csv
import os

#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#. Initalize a total vote counter.
total_votes = 0

#Candidate Options and Candidate votes.
candidate_options = []

#1. Declare the empty dictionary
candidate_votes = {}

    #Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data) 
  
        #Read the header row.
    headers = next(file_reader)

         #Print each row in the CSV file
    for row in file_reader: 
        #2. Add the to the total vote count.
        total_votes= total_votes + 1

    #Print the candidate name from each row.
        candidate_name = row[2]

#If the candidate does not match any existing candidate.
if candidate_name not in candidate_options:
    #Add the candidate name to the candidate list.
    candidate_options.append(candidate_name)
#2. Begin tracking that candidate's vote count.
candidate_votes[candidate_name] = 0



    #Print the candiate vote in dictionary 
print(candidate_votes)
       #3. Print the total votes.
       # print(total_votes)
       

#with open(file_to_save, "w") as txt_file:
#Write three counties to the file
    #txt_file.write("Counties in the Election\n")
    #txt_file.write("------------------------")
    #txt_file.write("\nArapahoe\nDenver\nJefferson")

#close the file

# Assign a variable to load a file and the path.
