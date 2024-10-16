import random


class Conv2D:
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0):
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        
        self.h_out = (len(input_matrix) - self.stride) + 2*self.padding -1 
        self.w_out = (len(input_matrix[0]) - self.stride) + 2*self.padding -1 
        self.output = [[0 for _ in range(self.w_out)] for _ in range(self.h_out)]

    def initaialize_weights(self):
        self.kernels = [[[random.uniform(0, 1) for _ in range(self.kernel_size)] for _ in range(self.kernel_size)] for _ in range(self.out_channels)]

        return self.kernels
    
    
    def shape(self):
        self.h_out = (len(input_matrix) - self.stride) + 2*self.padding -1 
        self.w_out = (len(input_matrix[0]) - self.stride) + 2*self.padding -1 
        self.kh = len(self.kernels)
        self.kw = len(self.kernels[0])

        return self.h_out, self.w_out, self.kh, self.kw
    
    
    def element_wise(x, w):
        w = Conv2D.initaialize_weights()
        h_out , w_out, kh, kw = Conv2D.shape()

        
        return w, h_out, w_out, kh, kw
    
    def forward(self, x):
        
        
        return Conv2D.element_wise(x, w[0])

input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
w = [
    [1, 0],
    [0, -1]
]

conv = Conv2D(in_channels=1,
                out_channels=3,
                kernel_size=3,
                )
output = conv.forward(input_matrix)
print(output)