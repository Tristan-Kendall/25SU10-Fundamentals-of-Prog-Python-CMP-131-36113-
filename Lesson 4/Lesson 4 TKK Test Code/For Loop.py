# Assume the variable n has been assigned a positive integer, so ignore the following line
n = int(input('Insert number:'))

# Start with a sum of 0
total = 0

# Loop through numbers from 1 to n
for x in range(1, n + 1):
    # Add each number to total
    total += x
# Calculating the average
average = total / n
# Printing the average
print(average)