import numpy as np
rng=np.random.default_rng()
array = rng.integers(1,101,size=(5,5))
print(array)

max_val = np.max(array)
min_val = np.min(array)
mean_val = np.mean(array)

print("\nMaximum value:", max_val)
print("Minimum value:", min_val)
print("Mean value:", mean_val)

normalized_array = (array - min_val) / (max_val - min_val)
print("\nNormalized Matrix (values between 0 and 1):")
print(normalized_array)

flattened =array.flatten()
sorted_flattened = np.sort(flattened)
print("\nFlattened and Sorted Array:")
print(sorted_flattened)