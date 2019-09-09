#import modules
import os
import csv




#Path to collect the data 
budget_data = os.path.join("..", "pybank", "budget_data.csv")

# Reading using CSV module

with open('budget_data.csv', newline='') as budget_data:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budget_data, delimiter=',')

    #print(csvreader)

    # Read the header row first 
    header = next(csvreader)
    #print(f"Header: {header}")
    
    months=0
    net_profits = 0
    monthly_change = 0
    previous_month_profit = 0
    monthly_changes = []
    #max_change = 0
    #min_change = 0
      
    #Read each row of data after the header
    for row in csvreader:
        #print(row)
        profits = row[1]
        dates = row[0]
        #print(profits)
        months += 1
        monthly_change = 0
        total_changes = 0
        #max_change = 0
        #min_change = 0
        max_date = 0
        min_date = 0
        #net_profits = int(profits) +  net_profits 
     
        
        
        if months == 1:
           monthly_change = 0
           monthly_changes.append(monthly_change)
           previous_month_profit = profits
           total_changes = total_changes + monthly_change
           net_profits = int(profits) +  net_profits    
        else:
           monthly_change = int(profits) - int(previous_month_profit)
           monthly_changes.append(monthly_change)
           previous_month_profit = profits
           total_changes = total_changes + monthly_change
           net_profits = int(profits) +  net_profits  
           #print(monthly_change)
           
        #if monthly_change > max_change:
          # max_change = monthly_change
           #max_date = row[0]

average_change = round(sum(monthly_changes)/(len(monthly_changes)-1), 2)                
greatest_increase = max(monthly_changes)
greatest_decrease = min(monthly_changes)
greatest_increase_index = monthly_changes.index(greatest_increase)
greatest_decrease_index = monthly_changes.index(greatest_decrease) 
#max_date = csvreader(0,int(greatest_increase_index))
#print(max_date)
#min_date = 
#print(greatest_increase_index)
# I give !!!!No more time!  Please show me how to get the dates!
    
            
print("Financial Analysis")
print("-------------------------------------")
print("Total Months : " + str(months))  
print("Total: $" + str(net_profits)) 
#print(max_date)
#print(max_change)
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(max_date) + "($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(min_date) + "($" + str(greatest_decrease) + ")")  
    
#print to a text file        
# save summary to txt
with open('financial_analysis.txt', 'w+') as file:
    #Write results to file and close file 
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write("Total Months: " + str(months)+ '\n')
    file.write("Total Profit: $" + str(net_profits)+ '\n')
    file.write("Average Change: $" + str(average_change)+ '\n')
    file.write("Greatest Increase in Profit: " + str(max_date) + "  ($"+str(greatest_increase)+")\n")
    file.write("Greatest Decrease in Profit: " + str(min_date) + "  ($"+str(greatest_decrease)+")\n")
    file.write("----------------------------\n")
    file.close()        
