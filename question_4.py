import numpy as np
rng=np.random.default_rng()
array=rng.integers(1,101,size=(5,5))

middle_array = array[1:4, 1:4]
first_row = middle_array[0, :]
last_column = middle_array[:, -1]

dot_product = np.dot(first_row, last_column)
print(dot_product)