import numpy 

# Function to print the 2D array
def print2D(arr):
    for row in arr:
        print(row)

array = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print2D(array)