def is_palindrome(num):
    # Convert the number to a string for easier manipulation
    num_str = str(num)
    
    # Check if the number is equal to its reverse
    if num_str == num_str[::-1]:
        return True
    else:
        return False

# Get user input
user_input = input("Enter a number: ")

try:
    # Convert the user input to an integer
    user_number = int(user_input)
    if is_palindrome(user_number):
        print("Yes, the number is a palindrome!")
    else:
        print("No, the number is not a palindrome.")
except ValueError:
    print("Please enter a valid integer.")