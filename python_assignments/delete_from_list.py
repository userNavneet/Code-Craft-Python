# Create the list
L = [10, 20, 30]

# Print the initial list
print("Initial List:", L)

# Ask the user for the number to delete
number_to_delete = int(input("Enter the number you want to delete from the list: "))

# Check if the number is in the list
if number_to_delete in L:
    # Remove the number from the list
    L.remove(number_to_delete)
    print(f"The number {number_to_delete} has been deleted from the list.")
    # Print the updated list
    print("Updated List:", L)
else:
    print(f"The number {number_to_delete} is not in the list.")
