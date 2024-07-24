import numpy as np 
# arr = np.array([1,2,3,4,4,5,5,3,2])
# arr2 = arr[1:4]
# print(arr)
# print(arr2)
arr = np.ones((5,3))+9
print(arr)

arr1 = np.eye(3)
print(arr1)

arr2 = np.diag((1,4,7,9))
print(arr2)

# Correctly creating a 2D array
arr3 = np.array([[10, 20, 30], [10, 20, 30], [10, 20, 30]])
print("Array:")
print(arr3)

# Getting the diagonal elements
diagonal_elements = np.diagonal(arr3)
print("Diagonal elements:")
print(diagonal_elements)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Reshaping it to 4x3
arr4 = arr.reshape(4, 3)
print("Reshaped to 4x3 array:")
print(arr4)

# Accessing elements correctly in the reshaped array
print("Array value is ", arr4[0, 1])  # First row, second column
print("Array value is ", arr4[1, 0])  # Second row, first column

# Printing the shape of the array
print("Shape of arr4:", arr4.shape)

# Reshaping to a different shape while keeping the total number of elements constant
arr4 = arr4.reshape(-1, 4)
print("Reshaped to -1x4 array:")
print(arr4)

arr4 = arr4.reshape(2, -1)
print("Reshaped to 2x-1 array:")
print(arr4)



np.random.seed(134567)
arr5 = np.random.randint(1,500,30).reshape(6,5)
print(arr5)
print(arr5[2:,2:])
print(arr5[3:5,2:4])

ar = np.array([1,2,3,4,4,5,66,7,7,7,7,5,4])
slicing  = ar[4:9]
print(  

      
       

        
         
)