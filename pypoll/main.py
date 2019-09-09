# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:01:14 2019

@author: Eileen
"""

#import modules
import os
import csv

#Path to collect the data 
poll_data = os.path.join("..", "pypoll", "election_data.csv")

# Reading using CSV module
with open('election_data.csv', newline='') as poll_data:

    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(poll_data, delimiter=',')

    print(csvreader)

    # Read the header row first 
    header = next(csvreader)
    print(f"Header: {header}")

    #create the variables needed
    ballot_list = []
    ballot_counts = [0, 0, 0, 0]
    ballot_percent = [0, 0, 0, 0]
    total = 0
       
            
    # create list of candidates
    for row in csvreader:
        candidate = row[2]
        total +=1 
        
        if candidate not in ballot_list:
            ballot_list.append(candidate)
            print (ballot_list)
           
        #Count votes for each candidate    
        if candidate == ballot_list[0]:
            ballot_counts[0] +=1
        
        elif candidate == ballot_list[1]:
            ballot_counts[1] +=1 
   
        elif candidate == ballot_list[2]:
            ballot_counts[2] +=1 
        
        elif candidate == ballot_list[3]:
            ballot_counts[3] +=1 
                
 #Determine percent of votes to 3 decimals
ballot_percent[0] = round((int(ballot_counts[0]) / int(total))*100,0)
ballot_percent.append(ballot_percent[0])

ballot_percent[1] = round((int(ballot_counts[1]) / int(total))*100,0)
ballot_percent.append(ballot_percent[1])

ballot_percent[2] = round((int(ballot_counts[2]) / int(total))*100,0)
ballot_percent.append(ballot_percent[2])

ballot_percent[3] = round((int(ballot_counts[3]) / int(total))*100,0)
ballot_percent.append(ballot_percent[3])

max_votes = (max(ballot_counts))
winner_index = ballot_counts.index(max_votes)
winner_name = ballot_list[winner_index]


# create election summary file
summary = zip(ballot_list, ballot_percent, ballot_counts)

#Loop through & print summary
# Print results
print("Election Result")
print("---------------------")
print("Total Votes:" + str(total)+ "")
print("---------------------")

#loop through summary
for row in summary:
    print(row[0] + ":", str(row[1]) + "%", "(" + str(row[2]) + ")")
print("---------------------")
print("Winner : " + str(winner_name)) 
print("---------------------")

# Save results to file, print lines in file

with open('Election_Results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(total) + "\n")
    text.write("---------------------------------------\n")
    
    for i in range(len(set(ballot_list))):
        text.write(ballot_list[i] + ": " + str(ballot_percent[i]) +"% (" + str(ballot_counts[i]) + ")\n")
    
    text.write("---------------------------------------\n")
    text.write("Winner : " + str(winner_name) + "\n")
    text.write("---------------------------------------\n")









     
        
        
          
    
#need to open file again    
#vote_count = sum(1 for row in poll_data) 
#print(vote_count)