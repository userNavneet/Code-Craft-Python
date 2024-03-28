def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Get array input from the user
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))

# Get the target value from the user
target = int(input("Enter the element you want to search: "))

# Perform linear search
result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print("Element not found in the array.")