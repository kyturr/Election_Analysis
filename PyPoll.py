# The data we need to retrieve
#2 A complete list of candidates who received votes
#3. The percentagoe fo votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.

# 1. The total number of votes cast
total_votes=0

#Candidates init
candidate_options=[]
#votes init
candidate_votes = {}
#open csv & read
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #print(row)
        #2. add vote to count
        total_votes +=1
        # Print the candidate name from each row
        candidate_name = row[2]
        #uniq candidates
        if candidate_name not in candidate_options:
            #add candidate to candidate list
            candidate_options.append(candidate_name)
            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

    # count vote
        candidate_votes[candidate_name]+=1


# #3 print total votes
# print(candidate_votes)
# print(candidate_options)
# print(total_votes)
with open(file_to_save, "w") as txt_file:

    election_results=(
        f"\nElectionResults\n---------------------------\n"
        f"Total Votes: {total_votes:,}\n--------------------------------------\n"
        f"\n\n"
    )
    print(election_results,end="")
    txt_file.write(election_results)

#WINNING
    winning_candidate=""
    winning_count=0
    winning_percentage=0
    for candidate_name in candidate_votes:
    
        votes=candidate_votes[candidate_name]
        votes_percentage=float(votes)/float(total_votes)*100
        candidate_results=(f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        if (votes > winning_count) and(votes_percentage > winning_percentage):
            winning_count=votes
            winning_candidate=candidate_name
            winning_percentage=winning_count/total_votes*100

    win_sum=(f"--------------------------------\n"
        f"The winner of the election is {winning_candidate} \n{winning_count:,} votes \n{winning_percentage:.1f}% of the popular vote\n"
        f"---------------------------------\n")
    print(win_sum)
    txt_file.write(win_sum)
#print(win_sum)
#declare in text

# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#      print(election_data)

# # Close the file.
# election_data.close()

    # Using the open() function with the "w" mode we will write data to the file.
    #Delete: outfile=open(file_to_save, "w")
    # Write some data to the file.
    #Delete:outfile.write("Hello World")
# Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file.
#     txt_file.write("Counties in the")
#     txt_file.write("")
#     txt_file.write("Arapahoe\nDenver\nJefferson")

# # Close the file
# txt_file.close()