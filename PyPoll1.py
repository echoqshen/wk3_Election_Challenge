import os
import csv
# assign a variable for the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")
# assign a variable save the file to a
#  path
file_to_save = os.path.join("analysis", "election_analysis.txt")

results_dict = {"counties_dict": {}, "candidate_dict": {}   }
# open election results and read the file
with open(file_to_load) as election_data:
    # read the file object with the reader function
    file_reader=csv.reader(election_data)

    # define header row
    headers=next(file_reader)
    
    for row in file_reader:
        county = row[1]
        if county not in results_dict["counties_dict"]:            
            results_dict["counties_dict"][county]=0
            # print(results_dict["counties_dict"])           
        # add votes to current county
        results_dict["counties_dict"][county]=results_dict["counties_dict"][county]+1
    # print(results_dict["counties_dict"])

        # populate candidate dict using the same
        candidate = row[2]
        if candidate not in results_dict["candidate_dict"]:            
            results_dict["candidate_dict"][candidate]=0
            # print(results_dict["candidate_dict"])           
        # add votes to current county
        results_dict["candidate_dict"][candidate]=results_dict["candidate_dict"][candidate]+1
    # print(results_dict["candidate_dict"])

results = results_dict
total_County_votes=sum(results["counties_dict"].values())

# start:



print(f"Election Results\n"
        f"----------------------------------\n"
        f"Total Votes: {total_County_votes: ,} \n"
        f"----------------------------------\n"
        f"County Votes: ")
for k, v in results_dict["counties_dict"].items():
        percentage_vote = v / total_County_votes * 100
        print(f"{k}: {percentage_vote: .1f}%  ({v: ,})")

max_county = max(results['counties_dict'], key=results['counties_dict'].get)
print(f"------------------------------------")
print("Largest County Turnout: ", max_county)
print(f"------------------------------------\n")

for k, v in results_dict["candidate_dict"].items():
    percentage_candidate=v/total_County_votes * 100
    print(f"{k}: {percentage_candidate: .1f}% ({v: ,}) ")    
print(f"------------------------------------\n")

winner = max(results['candidate_dict'], key=results['candidate_dict'].get)
print("Winnter: ",winner)
winning_count = results['candidate_dict'][winner]
print(f"Winning vote Count:  {winning_count: ,} ")
# print(f"Winning vote Count: " , winning_count )
winning_percent = winning_count/ total_County_votes * 100
print(f"Winning Percentage: {winning_percent: .1f}% \n")








# # with open(file_to_save,"w") as txt_file:
