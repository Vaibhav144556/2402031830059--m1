import numpy as np

# Basic NumPy usage
print('--- Basic NumPy ---')

# 1. Create a NumPy array from a Python list
arr = np.array([10, 20, 30, 40, 50])
print('array:', arr)
print('shape:', arr.shape)          # number of elements in each dimension
print('dtype:', arr.dtype)          # data type of elements
print('first element:', arr[0])
print('last element:', arr[-1])

# 2. Slicing and indexing
print('slice 1:4:', arr[1:4]) 
# elements from index 1 to 3
print('every other element:', arr[::2])

# 3. Array operations (elementwise)
print('add 5:', arr + 5)
print('multiply by 2:', arr * 2)
print('square:', arr ** 2)

# 4. Vectorized math functions
print('sum:', np.sum(arr))
print('mean:', np.mean(arr))
print('standard deviation:', np.std(arr))
print('maximum:', np.max(arr), 'minimum:', np.min(arr))

# Intermediate NumPy: 2D arrays and reshaping
print('\n--- Intermediate NumPy ---')

mat = np.array([[1, 2, 3], [4, 5, 6]])
print('matrix:\n', mat)
print('shape:', mat.shape)
print('element [1, 2]:', mat[1, 2])
print('first row:', mat[0])
print('second column:', mat[:, 1])

# Reshape a 1D array into 2D
arr2 = np.arange(12)
print('arange 12:', arr2)
arr2d = arr2.reshape((3, 4))
print('reshaped to 3x4:\n', arr2d)

# Transpose
print('transpose:\n', arr2d.T)

# Concatenate arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print('stack along rows:\n', np.concatenate([a, b], axis=0))
print('stack along columns:\n', np.concatenate([a, b], axis=1))

# Advanced NumPy: boolean indexing and broadcasting
print('\n--- Advanced NumPy ---')

x = np.array([10, 25, 30, 45, 50])
print('x:', x)
mask = x > 30
print('mask (x > 30):', mask)
print('values > 30:', x[mask])

# Broadcasting: add a smaller array to a larger array
big = np.array([[1, 2, 3], [4, 5, 6]])
small = np.array([10, 20, 30])
print('big:\n', big)
print('small:', small)
print('big + small (broadcasted):\n', big + small)

# Linear algebra with NumPy
print('\n--- Linear Algebra ---')
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print('A:\n', A)
print('B:\n', B)
print('matrix multiply A @ B:\n', A @ B)
print('inverse of A:\n', np.linalg.inv(A))
print('eigenvalues of A:', np.linalg.eigvals(A))

# Random arrays and sorting
print('\n--- Random and Sorting ---')
np.random.seed(0)
rand_arr = np.random.randint(0, 100, size=(3, 4))
print('random array:\n', rand_arr)
print('sorted each row:\n', np.sort(rand_arr, axis=1))
print('flattened sorted values:', np.sort(rand_arr, axis=None))

# Practical example: normalize each column of a 2D array
print('\n--- Practical Example ---')

scores = np.array([[80, 90, 70], [60, 75, 85], [90, 95, 100]], dtype=float)
print('scores:\n', scores)
col_mean = np.mean(scores, axis=0)
col_std = np.std(scores, axis=0)
print('column means:', col_mean)
print('column std dev:', col_std)
normalized = (scores - col_mean) / col_std
print('normalized scores:\n', normalized)

# How this script works
print('\n--- How it works ---')
print('1. Import NumPy with `import numpy as np`')
print('2. Use `np.array()` to create arrays from Python lists')
print('3. Use `shape`, `dtype`, indexing, and slicing to inspect arrays')
print('4. Use vectorized operations like `arr + 5`, `np.sum(arr)`, and `np.mean(arr)`')
print('5. Use `reshape`, `transpose`, and concatenation for 2D arrays')
print('6. Use boolean indexing, broadcasting, and linear algebra functions for advanced work')
