## assignment0 due date : 4/6
## Created by Jongsun Shinn : 4/3
## Feel free to edit and merge this file to enjoy confilcts!


import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import sklearn

# problem1
# Environment Setting

# problem2
# 1) vectorize_sumproducts
x1_list = np.arange(0,10)
x2_list = 2*np.arange(0,10)

sumproducts = np.matmul(x1_list,x2_list)

#print(sumproducts)

# 2) vectorize_Relu

#x = np.array([x1_list, x2_list])

x = torch.randn(np.random.randint(3,10),np.random.randint(3,10),np.random.randint(3,10))
y = F.relu(x)

# 3) vectorize_Prelu
a = torch.tensor(0.1)
y = F.prelu(x,a)

print(x)
print(x.shape)

# Problem 3
# 1) slice fixed point

def result_slice_fixed_points(df,length,position):
    for i in range(df.shape[0]):
        result = torch.tensor(df.shape)
        print(result.shape)
        #result[i] = df[position:position+length]
        print(df[position:position+length])
    return result

data = x
y = result_slice_fixed_points(data, 2, 2)
print(y)

# 2) slice last point
# 3) slice random point


real_data = [
         [0, 1, 2, 3, 4],
         [0, 1, 2, 3],
         [0, 1, 2, 3, 4,5],
         [0, 1, 2, 3, 4]
        ]

data = real_data
result = result_slice_fixed_points(real_data, 2, 2)
print(result)

# For any (uXlY) in data, X stands for the index of the utterance and Y
# stands for the index of the feature in the feature vector of the
# utterance X.

# result_slice_fixed_point = slice_fixed_point(data, 2, 1)
# >>>> print(result_slice_fixed_point)
# >>>>
# [[u0l1, u0l2],
# [u1l1, u1l2],
# [u2l1, u2l2],
# [u3l1, u3l2]]
# result_slice_last_point = slice_last_point(data, 3)
# >>>> print(result_slice_last_point)
# >>>>
# [[u0l2, u0l3, u0l4],
# [u1l1, u1l2, u1l3],
# [u2l3, u2l4, u2l5],
# [u3l2, u3l3, u3l4]]