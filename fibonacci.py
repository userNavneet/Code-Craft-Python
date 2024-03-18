def fibonacci(limit):
    # Initialize the first two Fibonacci numbers
    fib_sequence = [0, 1]
    
    # Loop to generate Fibonacci numbers until the limit
    while fib_sequence[-1] + fib_sequence[-2] <= limit:
        # Calculate the next Fibonacci number
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        
        # Append the next Fibonacci number to the sequence
        fib_sequence.append(next_fib)
    
    return fib_sequence

# Get the limit from the user
limit = int(input("Enter the limit for Fibonacci sequence: "))

# Call the fibonacci function and print the result
print("Fibonacci sequence up to", limit, ":", fibonacci(limit))