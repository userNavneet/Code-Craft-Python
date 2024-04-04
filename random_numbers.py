import random

def print_random_numbers(n):
    random_numbers = [random.randint(100, 500) for _ in range(n)]
    print("Random numbers from 100 to 500:")
    print(random_numbers)

# Example usage
print_random_numbers(5)  # Change 5 to any desired number of random numbers