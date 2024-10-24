# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join(
    "/Users", "yamellmejia", "Desktop", "UM Data Analytics BootCamp", "Python Challenge", 
    "Python-Challenge", "PyPoll", "Resources", "election_data.csv")  
file_to_output = os.path.join(
    "/Users", "yamellmejia", "Desktop", "UM Data Analytics BootCamp", "Python Challenge", 
    "Python-Challenge", "PyPoll", "analysis", "election_analysis.txt") 

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_votes = {}  # Dictionary to track votes per candidate
winning_candidate = ""  # To track the name of the winning candidate

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Increment the total vote count
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate does not already exist in candidate_votes, add them
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0  # Initialize their vote count

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    
    # Print the total vote count (to terminal and text file)
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )
    print(election_results, end="")
    txt_file.write(election_results)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = (votes / total_votes) * 100

        # Check if the current candidate is the winning candidate
        if votes > candidate_votes.get(winning_candidate, 0):
            winning_candidate = candidate

        # Print each candidate's vote count and percentage (to terminal and text file)
        candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(candidate_results, end="")
        txt_file.write(candidate_results)

    # Generate and print the winning candidate summary (to terminal and text file)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
