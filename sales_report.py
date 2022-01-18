"""Generate sales report showing total melons each salesperson sold."""

# Lists of salespeople and list of melons sold
salespeople = []
melons_sold = []

# Open sales report text file
f = open('sales-report.txt')

# Read sales report text file and separate each value by the | symbol
for line in f:
    line = line.rstrip()
    entries = line.split('|')

    # Set the salesperson equal to the first element in the entries list
    salesperson = entries[0]

    # Set the number of melons equal to the entries list at the 3rd index 
    melons = int(entries[2])

    # If a salesperson exists set the position equal to that salesperson's index 
    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        # Add the number of melons sold to the salesperson's tally 
        melons_sold[position] += melons
    else:
        # If the salesperson does not already exist in the salespeople list, add them to the list
        salespeople.append(salesperson)
        
        # Add the number of melons sold to the melons list
        melons_sold.append(melons)

# For every element in the salespeople list print the salesperson's name and how many melons they sold

for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')

# The two for in statements could have been put inside functions and then invoked