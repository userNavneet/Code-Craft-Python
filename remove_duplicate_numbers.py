def remove_duplicates(numbers):
    # Use a set to store unique numbers while preserving their order
    unique_numbers = []
    seen = set()

    for num in numbers:
        if num not in seen:
            unique_numbers.append(num)
            seen.add(num)

    return unique_numbers

# Get user input for the list of numbers
numbers_input = input("Enter a list of numbers separated by spaces: ")

# Split the input string into a list of numbers
numbers_list = numbers_input.split()

# Convert the list of strings to a list of integers
numbers_list = [int(num) for num in numbers_list]

# Remove duplicates from the list
unique_numbers = remove_duplicates(numbers_list)

# Print the list with duplicates removed
print("List with duplicates removed:", unique_numbers)
