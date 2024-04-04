import random
import string

def print_random_strings():
    random_strings = [''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 5))) for _ in range(10)]
    print("Random strings with length between 3 to 5:")
    print(random_strings)

# Example usage
print_random_strings()