def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
arr = [12, 11, 13, 5, 6, 9, 8, 34, 67, 23, 87, 34, 69, 15]
insertion_sort(arr)
print("Sorted array is:", arr)
