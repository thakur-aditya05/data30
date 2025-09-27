import numpy as np


# Create a 3x3 matrix using np.arange()
matrix = np.arange(1, 10).reshape(3, 3)

# Print the matrix
print("3x3 Matrix:")
print(matrix)

# Print its shape, size, and number of dimensions
print("\nShape:", matrix.shape)
print("Size:", matrix.size)
print("Number of Dimensions:", matrix.ndim)




# answer 2 

# Set parameters for the normal distribution
mean = 0
std_dev = 1
num_samples = 100

# Generate random numbers
random_numbers = np.random.normal(loc=mean, scale=std_dev, size=num_samples)

# Calculate mean and standard deviation
calculated_mean = np.mean(random_numbers)
calculated_std_dev = np.std(random_numbers)

# Print the results
print(f"\nGenerated {num_samples} random numbers with mean {mean} and standard deviation {std_dev}:")
print("Calculated Mean:", calculated_mean)
print("Calculated Standard Deviation:", calculated_std_dev)







# Create two NumPy arrays
array1 = np.arange(10)
array2 = np.arange(10)

result = array1 + array2
print(f"result: {result}")





# 1. np.array(): Convert a Python list to a NumPy array
list_data = [1, 2, 3, 4, 5]
array_from_list = np.array(list_data)

# 2. np.arange(): Create an array with evenly spaced values
array_arange = np.arange(0, 10, 2)  # start=0, stop=10, step=2

# 3. np.linspace(): Create an array with a specified number of evenly spaced values
array_linspace = np.linspace(0, 1, 5)  # start=0, stop=1, num=5

# 4. np.zeros(): Create an array filled with zeros
array_zeros = np.zeros((2, 3))  # 2x3 array of zeros

# 5. np.ones(): Create an array filled with ones
array_ones = np.ones((3, 3))  # 3x3 array of ones

# Display the arrays
print("Array from list:", array_from_list)
print("Array using arange:", array_arange)
print("Array using linspace:", array_linspace)
print("Array of zeros:", array_zeros)
print("Array of ones:", array_ones)













# Create a 1D array
arr = np.arange(12)

# Reshape to 3x4
reshaped_arr = arr.reshape(3, 4)

# Flatten the array
flattened_arr = reshaped_arr.flatten()

print("Original Array:", arr)
print("Reshaped Array:\n", reshaped_arr)
print("Flattened Array:", flattened_arr)




# Element-wise addition
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
sum_arr = arr1 + arr2

# Broadcasting
arr3 = np.array([1, 2, 3])
broadcasted_sum = arr3 + 10  # Adds 10 to each element

print("Sum of Arrays:", sum_arr)
print("Broadcasted Sum:", broadcasted_sum)







# random number generation 

# Generate a single random float
print(np.random.rand())

# Generate a 2x3 array of random floats
print(np.random.rand(2, 3))




# Generate a single random integer from 0 to 9
print(np.random.randint(10))

# Generate a 2x3 array of random integers from 10 to 50
print(np.random.randint(10, 50, size=(2, 3)))



