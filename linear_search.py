# import array
# def linearSearch(array, n, x):
#     for i in range(0, n):
#         if (array[i]==x):
#             return i
#     array=[]
# n = int(input("Enter the length of list: "))
# print("Enter the ",n,"elements")
# for i in range(0,n):
#     value=int(input())
#     array.append(value)
# key=int(input("Enter the value you want to search:"))
# result=linearSearch(array, n, key)
# if(result == -1):
#     print("Element not found")
# else:
#     print("Element found at index: ",result)    

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Get array input from the user
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))

# Get the target value from the user
target = int(input("Enter the value to search for: "))

# Perform linear search
result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print("Element not found in the array.")