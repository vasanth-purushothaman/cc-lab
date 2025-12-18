import numpy as np

user_input = input("Enter numbers separated by commas: ")

arr = np.array([str(x) for x in user_input.split(',')])
print(arr[::-1])
