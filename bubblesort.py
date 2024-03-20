def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Get user input for the array
n = int(input("Enter the number of elements in the array: "))
arr = []
print("Enter the elements of the array:")
for _ in range(n):
    arr.append(int(input()))

# Sort the array using bubble sort
bubble_sort(arr)

# Print the sorted array
print("Sorted array is:", arr)
