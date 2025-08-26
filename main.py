from numpy import random
import numpy as np

print("NumPy Data Explorer\n")

arr = np.array([3, 1, 7, 2, 9, 5])
print(f"Original Array: \n {arr}\n")

print(f"Search: Index of 7 -> {np.where(arr == 7)}\n")

print(f"Sorted Array: \n {np.sort(arr)}\n")

filter_arr = arr > 4
newarr = arr[filter_arr]
print(f"Filtered Array (values > 4): \n {newarr}\n")

rand = np.random.randint(100, size=5)
print(f"Random Integers (size=5): \n {rand}\n")

rand_normal = np.random.normal(100, size=5)
print(f"Random Normal Distribution (5 numbers): \n {rand_normal}\n")

rand_perm = np.random.permutation(arr)
print(f"Random Permutation of Original Array: \n {rand_perm}\n")
