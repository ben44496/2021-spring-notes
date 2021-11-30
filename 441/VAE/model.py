import torch
import torch.nn as nn
import torch.nn.functional as F

# class Net(nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.encoder=nn.Sequential(
#                 nn.Linear(28*28,256),
#                 nn.ReLU(True),
#                 nn.Linear(256,128),
#                 nn.ReLU(True),
#                 nn.Linear(128,64),
#                 nn.ReLU(True)
#             )
    
#         self.decoder=nn.Sequential(
#                 nn.Linear(64,128),
#                 nn.ReLU(True),
#                 nn.Linear(128,256),
#                 nn.ReLU(True),
#                 nn.Linear(256,28*28),
#                 nn.Sigmoid(),
#             )

#     def forward(self,x):
#         x=self.encoder(x)
#         x=self.decoder(x)
        
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(28*28, 256)
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, 64)
        
        self.fc4 = nn.Linear(64, 128)
        self.fc5 = nn.Linear(128, 256)
        self.fc6 = nn.Linear(256, 28*28)
        
    def encoder(self, x):
        x = F.leaky_relu(self.fc1(x))
        x = F.leaky_relu(self.fc2(x))
        x = F.leaky_relu(self.fc3(x))
        return x
        
    def decoder(self, x):
        x = F.leaky_relu(self.fc4(x))
        x = F.leaky_relu(self.fc5(x))
        x = F.leaky_relu(self.fc6(x))
        # x = torch.reshape(28, 28, -1)
        return x

    def forward(self,x):
        # shape = x.shape
        shape = (-1, 1, 28, 28)
        x = torch.flatten(x, 1)
        x = self.encoder(x)
        x = self.decoder(x)
        # x = torch.reshape(x, shape)
        return x