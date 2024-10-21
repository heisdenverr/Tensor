import random

class Conv2D:
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0):
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        
        # Assuming input_matrix dimensions will be passed to forward() method.
        self.kernels = self.initialize_weights()

    def initialize_weights(self):
        # Initialize random weights for kernels
        kernels = [[[random.uniform(0, 1) for _ in range(self.kernel_size)] for _ in range(self.kernel_size)] for _ in range(self.out_channels)]
        return kernels

    def compute_output_size(self, input_height, input_width):
        # Calculate output dimensions based on kernel size, stride, and padding
        h_out = ((input_height - self.kernel_size + 2 * self.padding) // self.stride) + 1
        w_out = ((input_width - self.kernel_size + 2 * self.padding) // self.stride) + 1
        return h_out, w_out
    
    def element_wise(self, x, kernel):
        # Apply the kernel to the input x element-wise.
        # We'll simplify this as a placeholder for now.
        return sum(a * b for a_row, b_row in zip(x, kernel) for a, b in zip(a_row, b_row))

    def forward(self, input_matrix):
        input_height = len(input_matrix)
        input_width = len(input_matrix[0])

        # Calculate the output size
        h_out, w_out = self.compute_output_size(input_height, input_width)
        
        # Initialize the output matrix
        output = [[0 for _ in range(w_out)] for _ in range(h_out)]
        
        # Perform the convolution operation
        for i in range(h_out):
            for j in range(w_out):
                # For simplicity, assume stride = 1 and no padding (you can extend this)
                # Extract the patch from input_matrix to apply the kernel
                input_patch = [row[j:j + self.kernel_size] for row in input_matrix[i:i + self.kernel_size]]
                
                # Apply each kernel and sum the results
                for kernel in self.kernels:
                    output[i][j] += self.element_wise(input_patch, kernel)
        
        return output

# Example usage
input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

conv = Conv2D(in_channels=1, out_channels=1, kernel_size=2)
output = conv.forward(input_matrix)

print("Output:")
for row in output:
    print(row)