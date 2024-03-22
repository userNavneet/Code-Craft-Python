# Prompt the user to enter numbers separated by spaces
numbers_input = input("Enter a list of numbers separated by spaces: ")

# Split the input string into a list of numbers
numbers_list = numbers_input.split()

# Convert the list of strings to a list of integers
numbers_list = [int(num) for num in numbers_list]

# Check if the list is empty
if not numbers_list:
    print("List is empty. No maximum value.")
else:
    # Find the maximum value in the list
    max_value = max(numbers_list)
    print("The maximum value is:", max_value)
