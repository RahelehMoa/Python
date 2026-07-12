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

print("----------------------------------------------------------")

randn_tensor = torch.randn(4,4)
print(randn_tensor)

print("----------------------------------------------------------")

randint_tensor = torch.randint(1, 10 , (4,4))
print(randint_tensor)

print("----------------------------------------------------------")

base = [[1,2,3],
        [4,5,6],
        [7,8,9]]

base_tensor = torch.tensor(base, dtype= torch.float32)
print(base_tensor)

rand_like_tensor = torch.rand_like(base_tensor)
print(rand_like_tensor)

print("----------------------------------------------------------")

randint_like_tensor = torch.randint_like(base_tensor,1,10)
print(randint_like_tensor)

print("----------------------------------------------------------")

zeros_like_tensor = torch.zeros_like(base_tensor)
print(zeros_like_tensor)

print("----------------------------------------------------------")

ones_like_tensor = torch.ones_like(base_tensor)
print(ones_like_tensor)

print("----------------------------------------------------------")

empty_tensor = torch.empty(4,4)
print(empty_tensor)

print("----------------------------------------------------------")

torchrand = torch.rand(3)
print(torchrand)

diag_tensor = torch.diag(torchrand)
print(diag_tensor)

#numbers in torchrand are in diag_tensor in Diametera!!
print("----------------------------------------------------------")

arange_tensor = torch.arange (6)
print(arange_tensor)
arange_tensor1 = torch.arange (1,5)
print(arange_tensor1)
arange_tensor2 = torch.arange (1,5,0.5)
print(arange_tensor2)

print("----------------------------------------------------------")

linspace_torch = torch.linspace(3,10, steps = 5)
print(linspace_torch)

print("----------------------------------------------------------")

my_tensor = torch.rand(3,4)

#same commands: shape = size 
print(f'Tensor shape is : {my_tensor.shape}')
print(f'Tensor size is : {my_tensor.size()}')

print("----------------------------------------------------------")

print(f'Tensor Data Type : {my_tensor.dtype}')

print("----------------------------------------------------------")

print(f'Tensor Device : {my_tensor.device}')

print("----------------------------------------------------------")
#indexing start from 0 :
Tensor_operation = torch.randint(1,10,(4,4))
print(Tensor_operation)

print(f'First row : ' , Tensor_operation [0])
print(f'First Column :' , Tensor_operation[: , 0])
print(Tensor_operation[-1,-1])
print(Tensor_operation[2,3])

Tensor_operation[:,1] = 5
print(Tensor_operation)

print("----------------------------------------------------------")
#Join 
join_tensor1 = torch.randint(1,5,(4,4))
join_tensor2 = torch.randint(5,10,(4,4))

concatenate_tensor = torch.cat((join_tensor1,join_tensor2),dim=1)
print(concatenate_tensor)

print("----------------------------------------------------------")
concatenate_tensor = torch.cat((join_tensor1,join_tensor2),dim=0)
print(concatenate_tensor)

print("----------------------------------------------------------")
stack_tensor = torch.stack((join_tensor1,join_tensor2),dim=0)
print(stack_tensor)

print("----------------------------------------------------------")

x= torch.rand(16)
print(x)

y= x.view(4,4)
print(y)

print("----------------------------------------------------------")

z= torch.arange(4)
print(z)

reshape_tensor = torch.reshape(z,(2,2))
print(reshape_tensor)
