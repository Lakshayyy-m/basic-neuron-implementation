import numpy as np

inputs = [1, 3, 4, 6]

weights = [[1, 2, 34, 54], [4, 3, 23, 14], [65, 56, 3, 56]]

bias = [2, 3, 0.6]

output = np.dot(weights, inputs) + bias


print(output)
