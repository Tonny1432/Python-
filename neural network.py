import torch
from torch import nn,optim

model =nn.Linear(1,1)

x = torch.tensor([[1.0],[2.0],[3.0],[4.0],[5.0],[6.0]]) #input
y = torch.tensor([[2.0],[4.0],[6.0],[8.0],[10.0],[12.0]])#output

# input * weight +bias for each terms

optimizer = optim.SGD(model.parameters(),lr=0.017) # lr =learning rate
loss_fn = nn.MSELoss() #error calcauting

for i in  range(100):
    predictions = model(x)
    loss = loss_fn(predictions,y)
    
    optimizer.zero_grad() #clears old gradients . Gradient = how wrong you are + how to fix it
    loss.backward()  #calcuate the new Gradient.                 
    optimizer.step() #updates weights using gradients . weightage = importance of input .

    if i%10==0:
        print("value of i:",i)
        print("the loss of" ,i,"repatations:",loss.item())

test = torch.tensor([20.0])
test_case =model(test)
print("output of neural network:",test_case.item())   
print("weight:",model.weight.item()) #weight importances
print("bias:",model.bias.item()) # bias adjusment