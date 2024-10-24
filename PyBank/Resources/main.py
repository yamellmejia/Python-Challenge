# Dependencies
import csv
import os

#File to load and output
file_to_load = os.path.join(
    "/Users", "yamellmejia", "Desktop", "UM Data Analytics BootCamp", "Python Challenge", 
    "Python-Challenge", "PyBank", "Resources", "budget_data.csv")
file_to_output = os.path.join(
    "/Users", "yamellmejia", "Desktop", "UM Data Analytics BootCamp", "Python Challenge", 
    "Python-Challenge", "PyBank", "Analysis", "budget_data.txt")

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
previous_net = None
net_change_list = []
months = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])
    months.append(first_row[0])

    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1
        months.append(row[0])

        # Track the net change
        total_net += int(row[1])
        net_change = int(row[1]) - previous_net
        net_change_list.append(net_change)
        previous_net = int(row[1])

        # Calculate the greatest increase in profits (month and amount)
        greatest_increase = max(net_change_list)
        greatest_increase_month = months[net_change_list.index(greatest_increase) + 1]

        # Calculate the greatest decrease in losses (month and amount)
        greatest_decrease = min(net_change_list)
        greatest_decrease_month = months[net_change_list.index(greatest_decrease) + 1]

# Calculate the average net change across the months
average_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary
output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
    )

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
