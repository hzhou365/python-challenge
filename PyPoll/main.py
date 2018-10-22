import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
print("This is the csvpath:", csvpath)

with open(csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    print("This is the csvreader:", csvreader)
    csv_header=next(csvreader)
    print(f"csv Header: {csv_header}")
    print("\n")
 
    total_row_number=0
    candidate_dict={}
    total_votes_for_the_candidate=0
    current_key=""
    
    for row in csvreader:
        total_row_number=total_row_number+1
        current_key=row[2]

        if current_key in candidate_dict.keys():
            candidate_dict[current_key]=candidate_dict[current_key]+1
        else:
            candidate_dict[current_key]=1
                  
    #print(candidate_dict)
   
    #print to terminal
    print("Election Results")
    print("----------------------------------")
    print("Total Votes:", total_row_number)
    print("----------------------------------")    
    
    current_winner_votes=0
    winner=""
    
    for key in candidate_dict:
        
        votes=candidate_dict[key]
        votes_in_percentage = '{0:.3f}'.format((votes / total_row_number * 100))
        #return votes_in_percentage
        
        print(key, ":", votes_in_percentage, "%", "(", votes, ")") 
        
        if int(votes) > current_winner_votes:
            winner = key
            current_winner_votes=int(votes)        
        
    print("----------------------------------")
    print("Winner: ", winner)
    print("----------------------------------")
    
    
#export a text file with the results
    # Specify the file to write to
    output_path = os.path.join("result.csv")

    # Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=' ',quotechar=' ')

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------------"])
    csvwriter.writerow(["Total Votes:", total_row_number])
    csvwriter.writerow(["----------------------------------"])  
    
    for key in candidate_dict:
        
        votes=candidate_dict[key]
        votes_in_percentage = '{0:.3f}'.format((votes / total_row_number * 100))
        #return votes_in_percentage
        
        csvwriter.writerow([key, ":", votes_in_percentage, "%", "(", votes, ")"]) 
        
    csvwriter.writerow(["----------------------------------"])
    csvwriter.writerow(["Winner: ", winner])
    csvwriter.writerow(["----------------------------------"])
                        


    
    
              
            
            
            
    