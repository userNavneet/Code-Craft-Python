# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Create the list
L = [10, 20, 30, 7, 11, 13]

# Print the initial list
print("Initial List:", L)

# Calculate the sum of all prime numbers in the list
sum_of_primes = sum(num for num in L if is_prime(num))

# Print the sum
print("Sum of all prime numbers in the list:", sum_of_primes)
