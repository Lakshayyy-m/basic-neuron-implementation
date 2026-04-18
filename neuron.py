inputs = [1, 3, 4, 6]

weights = [1, 2, 34, 54]

bias = 0.45
# 4 inputs therefore 4 weights and 1 bias since one neuron is takinfg the input and producing the output
output = (
    inputs[0] * weights[0]
    + inputs[1] * weights[1]
    + inputs[2] * weights[2]
    + inputs[3] * weights[3]
    + bias
)

print(output)
