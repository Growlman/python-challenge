import os
import csv

#find the file
pypoll_csv = os.path.join('Resources', 'election_data.csv')

#making open containers and setting their initial values
total_votes = 0
candidate_votes = {}
candidate_list = []
votes_count = []
percentage_voted_list = []
winner_votes_count = 0
cleaned_output = []

#read the actual csv file
with open(pypoll_csv) as polling:
	csv_reader = csv.reader(polling, delimiter = ",")
	csv_header = next(csv_reader)

#start the for loop
	for row in csv_reader:
#track the number of votes while looping
		total_votes = total_votes + 1

		candidate_name = row[2]

#if the candidate is already in the list then add another instance to the vote count for the candidate
		if candidate_name in candidate_list:
			candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
#if the candidate however is not in the list then add the candidate name and start them with a vote count of one
		else:
			candidate_list.append(candidate_name)
			candidate_votes[candidate_name] = 1

#trying to add to the percentage voted list to get those voting percentages. currently running into problems here where the i is being read as a string rather than an int
	for i in candidate_votes:
		percentage = (i/total_votes) * 100
		percentage = round(percentage)
		percentage = "%3f%%" % percentage
		percentage_voted_list.append(percentage)

	winner = max(candidate_votes)
	index = candidate_votes.index(winner)
	big_boss = candidates[index]

#print screens
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
	print(f""