# First we'll import the os module
# This will allow us to create file paths across operating systems
import pathlib
import csv

# Point to the data file
csvpath = pathlib.Path("Resources/budget_data.csv")

# open empty lists to store data of date, and profit/loss 
date = []
profit_loss=[]

with open(file=csvpath, mode='r') as csvfile:
# CSV reader determines delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

# Read the header row first to skip it, since we don't want to include it in our column lists
    csv_header = next(csvreader)

# Add each row after the header to the date and profit_loss lists we created above
    for row in csvreader:
        date.append(row[0]) 
        profit_loss.append(float(row[1]))

    # Take first difference of the Profit list    
    Difference = [profit_loss[i + 1] - profit_loss[i] for i in range(len(profit_loss)-1)]

    # calculate  Total;datelenght;avrage; higher difference; lower defference on the lists we created
    Total = round(sum(profit_loss))
    DateLength = len(date)
    Average_Change = round(sum(Difference)/len(Difference),2)
    higher_Difference = round(max(Difference)) 
    higher_Index = Difference.index(higher_Difference)  
    higher_IndexDate = date[higher_Index+1]
    lower_Difference = round(min(Difference))
    lower_Index = Difference.index(lower_Difference) 
    lower_IndexDate = date[lower_Index+1]

# Print our results to the terminal
print(f"Financial Analysis")
print("-----------------")
print(f"Total months: {DateLength}")
print(f"Total: ${Total}")
print(f"Average Change: ${Average_Change}")
print(f"Greatest Increase in Profits: {higher_IndexDate} (${higher_Difference})")
print(f"Greatest Decrease in Profits: {lower_IndexDate} (${lower_Difference})")

# determine the file to write to
output_path = pathlib.Path("analysis/Pybank_output.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(file=csvpath, mode='w') as csvfile:

    # drive to csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total months', 'Total', 'Average_Change', 'Greatest_Increase in Profits_Date', 'Greatest Increase in Profits', 'Greatest Decrease in Profits Date', 'Greatest Decrease in Profts'])
    
    # Fill in the data rows
    csvwriter.writerow(["DateLength","Total","Average_Change","higher_IndexDate","higher_Difference","lower_IndexDate","lower_Difference"])

# Exporting to .txt file
output = open("output.txt", "w")

# Write the first row (column headers)
csvwriter.writerow(['Total months', 'Total', 'Average_Change', 'Greatest_Increase in Profits_Date', 'Greatest Increase in Profits', 'Greatest Decrease in Profits Date', 'Greatest Decrease in Profts'])
    
    # Fill in the data rows
csvwriter.writerow(["DateLength","Total","Average_Change","higher_IndexDate","higher_Difference","lower_IndexDate","lower_Difference"])









