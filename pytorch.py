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

print("----------------------------------------------------------")

# Create two tensors
view_as_tensor1 = torch.randn(12)
view_as_tensor2 = torch.randn(3, 4)
 
# Use view_as to reshape tensor1 to have the same shape as tensor2
reshaped_tensor = view_as_tensor1.view_as(view_as_tensor2)

#print
print(view_as_tensor1)
print(view_as_tensor2)
print(reshaped_tensor)

print(f"Original tensor shape: {view_as_tensor1.shape}")
print(f"Target tensor shape: {view_as_tensor2.shape}")
print(f"Reshaped tensor shape: {reshaped_tensor.shape}")

print("----------------------------------------------------------")

tensor_a = torch.tensor([[1,2],[1,3]])
tensor_b = torch.tensor([[2,3],[0,4]])

#Addition
print(tensor_a + tensor_b)

#Subtraction
print(tensor_a - tensor_b)

#Maltiplication
print(tensor_a * tensor_b)

#Division
print(tensor_a / tensor_b)

#Exponent
print(tensor_a ** tensor_b)

#Matrix Maltiplication
Matrix_tensor = torch.randint (1,5,(4,4))
Matrix_multi = Matrix_tensor @ Matrix_tensor.T

print(Matrix_multi)
print(Matrix_tensor)

#Matrix Maltiplication way 2
Matrix_multi_New = Matrix_tensor.matmul(Matrix_tensor.T)
print(Matrix_multi_New)

print("----------------------------------------------------------")
Matrix_tensor = torch.randint (1,5,(4,4))
print(Matrix_tensor)

Sum_tensor = Matrix_tensor.sum()
print(Sum_tensor)

agg_item = Sum_tensor.item()
print(agg_item)

print("----------------------------------------------------------")

x1 = torch.rand(1)
y1 = torch.rand(1)

print(x1)
print(y1)

#Normal Addition 
z1 = x1 + y1
print(z1)

#In_place Addition 
z2 = x1.add_(y1)
print(z2)
print(x1)

print("----------------------------------------------------------")

# we often change shape tensor 
# 3 * 256 * 256 - Image Size
# N * 3 * 256 * 256 - N is the Batch Size

a1 = torch.rand(3,256,256)
b1 = a1.unsqueeze(0)

print(a1.shape)
print(b1.shape)

print("----------------------------------------------------------")

c1 = torch.rand(1,1,1,1,1,1)
print(c1)

a2 = torch.rand(1,20)
print(a2.shape)
print(a2)

b2 = a2.squeeze(0)
print(b2.shape)
print(b2)

print("----------------------------------------------------------")

#Numpay and Pytorch

numpay_array = np.ones((2,3))
print(numpay_array)

pytorch_tensor = torch.from_numpy(numpay_array)
print(pytorch_tensor)

print(numpay_array.dtype)
print(pytorch_tensor.dtype)

pytorch_rand = torch.rand(2,3)
print(pytorch_rand)

numpay_rand = pytorch_rand.numpy()
print(numpay_rand)

print("----------------------------------------------------------")
