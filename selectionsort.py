def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Get user input for the array
n = int(input("Enter the number of elements in the array: "))
arr = []
print("Enter the elements of the array:")
for _ in range(n):
    arr.append(int(input()))

# Perform selection sort
selection_sort(arr)

# Print the sorted array
print("Sorted array is:", arr)
