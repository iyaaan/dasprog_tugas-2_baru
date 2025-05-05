# Create an empty list
numbers = []

# Take 10 inputs from the user
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate the sum 
total = sum(numbers)

# Display the list and the total sum
print("List of numbers: ", numbers)
print("Total sum: ", total)