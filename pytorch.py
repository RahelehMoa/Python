#import

#import pytorch
import numpy as np 
import torch

print(torch.__version__)

#tensor Initialisation

data = [[1,2],[3,4]]
print(type(data))

data_Tensor = torch.tensor(data)
print(data_Tensor)

type = data_Tensor.dtype 
print(type)

#define dtype:

data_Tensor = torch.tensor(data, dtype=torch.int32)
print(data_Tensor)


print("-------------------------------------------------------")

data1 = [[1.,2.],[3.,4.]]
data_Tensor1 = torch.tensor(data1)
print(data_Tensor1)

type1 = data_Tensor1.dtype 
print(type1)

print("-----------------------------------------------------------")

data_array = np.array(data1)
print( data_array)

a = torch.from_numpy (data_array)
print(a)

b = torch.as_tensor(data_array)
print(b)

print("----------------------------------------------------------")

Zero_tensor = torch.zeros(3,4)
print(Zero_tensor)
print(Zero_tensor.dtype)

print("----------------------------------------------------------")

one_tensor = torch.ones(3,4)
print(one_tensor)
print(one_tensor.dtype)

print("----------------------------------------------------------")

eye_tensor = torch.eye(4,4)
print(eye_tensor)

print("----------------------------------------------------------")

rand_tensor = torch.rand(3,3)
print(rand_tensor)