# This is numpy array 
import numpy as np
#1. Convert the below list into numpy array then display the array
#Input: my list[1,2,3,4,5]

my_list=[1,2,3,4,5]

arr = np.array(my_list)

print(arr)



#2. Convert the below list into a numpy array then display the array than display the first and last index and then multiply each element by 2 and display the result.

array = np.array(my_list)

# Display the array
print("Array:", array)

# Display the first and last index
print("First index:", array[0])
print("Last index:", array[-1])

# Multiply each element by 2 and display the result
multiplied_array = array * 2
print("Array multiplied by 2:", multiplied_array)



# Write A Numpy program to create an array of 10zeros,10ones,and 10 fives 
zeros = np.zeros(10,dtype=int)
ones= np.ones(10,dtype=int)
fives = np.full(10,5,dtype=int)

print("Arrya with 10 zeros:",zeros)
print("Arrya with 10 ones:",ones)
print("Arrya with 10 fives:",fives)


# write a numpy program to create a 3*3 matrix with  the values 2 to 10
values = np.arange(2, 11).reshape(3, 3)

# Display the 3x3 matrix
print("3x3 matrix with values from 2 to 10:")
print(values)
