def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
        # If x is greater, ignore left half
        elif arr[mid] < x:
            left = mid + 1
        # If x is smaller, ignore right half
        else:
            right = mid - 1
    # If element is not present in array
    return -1

# Get user input for the array
n = int(input("Enter the number of elements in the array: "))
arr = []
print("Enter the elements of the array:")
for _ in range(n):
    arr.append(int(input()))

# Sort the array
arr.sort()
print("Sorted Array: ",arr)

# Get user input for the element to search
x = int(input("Enter the element to search: "))

# Perform binary search
result = binary_search(arr, x)

# Print the result
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")