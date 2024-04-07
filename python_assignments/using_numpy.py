# Importing NumPy
import numpy

# Creating a 1D array
arr1d = numpy.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr1d)
print()

# Creating a 2D array
arr2d = numpy.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:")
print(arr2d)
print()

# Accessing elements of an array
print("Element at index 0 in arr1d:", arr1d[0])
print("Element at index (0, 1) in arr2d:", arr2d[0, 1])
print()

# Array operations
arr1 = numpy.array([1, 2, 3])
arr2 = numpy.array([4, 5, 6])

print("Addition:")
print(arr1 + arr2)
print()

print("Subtraction:")
print(arr2 - arr1)
print()

print("Multiplication:")
print(arr1 * arr2)
print()

print("Division:")
print(arr2 / arr1)
print()

# Matrix operations
mat1 = numpy.array([[1, 2], [3, 4]])
mat2 = numpy.array([[5, 6], [7, 8]])

print("Matrix Multiplication:")
print(numpy.dot(mat1, mat2))
print()

print("Matrix Transpose:")
print(numpy.transpose(mat1))
print()

# Statistical operations
arr = numpy.array([1, 2, 3, 4, 5])

print("Mean:", numpy.mean(arr))
print("Median:", numpy.median(arr))
print("Standard Deviation:", numpy.std(arr))
print("Variance:", numpy.var(arr))