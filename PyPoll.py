import csv
import os
dir(os)

file_to_load = 'Resources/election_results.csv'
with open(file_to_load) as election_data:
    print(election_data)
election_data = open(file_to_load, 'r')
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
outfile = open(file_to_save, "w")
outfile.write("\nCounties in the Election\nArapahoe\nDenver\njefferson")
file_reader = csv.reader(election_data)
headers =next(file_reader)
print(headers)
outfile.close()