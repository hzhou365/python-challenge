import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
#print("This is the csvpath:", csvpath)

with open(csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    #print("This is the csvreader:", csvreader)
    csv_header=next(csvreader)
    #print(f"csv Header: {csv_header}")
    print("\n")
    
    count_row_number=0
    total_net_amount=0
    the_greatest_increase=0
    the_greatest_decrease=0
    
    the_greatest_increase_month=""
    the_greatest_decrease_month=""    
        
    for row in csvreader:
        #print(row)
        count_row_number=count_row_number+1
        #print("Total Months:", count_row_number)
        total_net_amount=total_net_amount+int(row[1])
        #print("Total: $", total_net_amount)
        
        P_or_L=int(row[1])
        if P_or_L > the_greatest_increase:
            the_greatest_increase=P_or_L
            the_greatest_increase_month=row[0]
            
            #print("The greatest increase:", the_greatest_increase)
        elif P_or_L  < the_greatest_decrease:
            the_greatest_decrease=P_or_L
            the_greatest_decrease_month=row[0]

    #print to terminal        
    print("Financial Analysis")
    print("----------------------------------")
    print("Total Months:", count_row_number)
    print("Total: $", total_net_amount)
    print("Greatest Increase in Profits: ", str(the_greatest_increase_month), "($", the_greatest_increase, ")")
    print("Greatest Decrease in Profits: ", str(the_greatest_decrease_month), "($", the_greatest_decrease, ")")
    
    #export a text file with the results
    # Specify the file to write to
    output_path = os.path.join("new.csv")

    # Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=' ',quotechar=' ')

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])

    # Write the second row
    csvwriter.writerow(['----------------------------------'])
    csvwriter.writerow(['Total Months:', count_row_number])
    csvwriter.writerow(['Total: $', total_net_amount])
    csvwriter.writerow(['Greatest increase in Profits: ', str(the_greatest_increase_month), '($', the_greatest_increase, ')'])
    csvwriter.writerow(['Greatest decrease in Profits: ', str(the_greatest_decrease_month), '($', the_greatest_decrease, ')'])

                
                
        
        
