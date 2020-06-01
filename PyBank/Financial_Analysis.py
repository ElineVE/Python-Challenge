# import the os module
import os
import csv

# Define path
csvpath = os.path.join('Resources', 'budget_data.csv')
file_to_output = os.path.join('Financial_Analysis.txt')

#Assign variables
sum_profit = 0
sum_loss = 0
totalPL = 0
profit = 0
net_change_list = []
avg_changes = 0
date = []
profit_change = 0
greatest_profit_increase = 0
greatest_profit_decrease = 0
increase_date = 0
decrease_date = 0
dates_list = []
values_list = []

# Read file CSV module
with open(csvpath) as csvfile:

    # specify delimiter and content
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header
    csv_header = next(csvreader)

    # Read each row of data after the header
    count_months = 0
    for row in csvreader:
        count_months += 1
        sum_profit = sum_profit + int(row[1])
        values_list.append(int(row[1]))

    i = 0

    # for loop knows how to increment, while doesn't
    while i < (count_months - 1):
    #tell it to increment, always has to be at the end
        a = values_list[i+1] - values_list[i]
        net_change_list.append(a)
        i = i + 1

 # calculate average
    avg_changes = sum(net_change_list)/(count_months - 1)

# calculate largest increase in profit and largest decrease in profit
   
    #min and max increase values
    greatest_profit_increase = max(net_change_list)
    greatest_profit_decrease = min(net_change_list)
   
    # min and max increase indicators
    position_min = net_change_list.index(min(net_change_list))
    position_max = net_change_list.index(max(net_change_list))

   
# Read file using CSV module
with open(csvpath) as csvfile:

    # specify delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header
    csv_header = next(csvreader)
 
    # Read each row of data after the header
    months = 0
    for row in csvreader:
        months += 1
        dates_list.append((row[0]))    
decrease_date = dates_list[position_min+1]

increase_date = dates_list[position_max+1]

# print values

print ("Financial Analysis")
print ("---------------------------------")
print (f"Total Months : {count_months}" )
print (f"Total  : ${sum_profit}" )
print (f"Average Change  : ${avg_changes}" )
print (f"Greatest Increase  : ${greatest_profit_increase}, {increase_date} " )
print (f"Greatest Decrease  : ${greatest_profit_decrease}, {decrease_date}" )


# publish to a text file
results = (
    f'\nFinancial Analysis\n'
    f'----------------------------\n'
    f'Total Months : {count_months}\n'
    f'Total : ${sum_profit}\n'
    f'Average Change : ${avg_changes}\n'
    f'Greatest Increase : ${greatest_profit_increase} ({increase_date})\n'
    f'Greatest Decrease : ${greatest_profit_decrease} ({decrease_date})')

with open(file_to_output, "w") as txt_file:
    
    txt_file.write(results)
