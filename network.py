from torch import nn
import numpy as np
import torch.nn.functional as F


## Define Neural network model
class Net(nn.Module):
    def __init__(self, len_featrue=None):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(len_featrue, 32)
        self.fc2 = nn.Linear(32, 64)
        self.fc3 = nn.Linear(64, 64)
        self.fc4 = nn.Linear(64, 32)
        self.fc5 = nn.Linear(32, 1)

    def forward(self, x):
        hidden_output1 = F.relu(self.fc1(x))
        hidden_output2 = F.relu(self.fc2(hidden_output1))
        hidden_output3 = F.relu(self.fc3(hidden_output2))
        hidden_output4 = F.relu(self.fc4(hidden_output3))
        y = self.fc5(hidden_output4).view(-1)
        return y


class Target_Net(nn.Module):
    def __init__(self, source_model, len_new, len_old):
        super(Target_Net, self).__init__()
        # introduce a new layer with randomly initialized weights while transfer learning
        # To adapt changed input dimensions
        self.fc0 = nn.Linear(len_new, len_old)
        self.fc1 = source_model.fc1
        self.fc2 = source_model.fc2
        self.fc3 = source_model.fc3
        self.fc4 = source_model.fc4
        self.fc5 = source_model.fc5

    def forward(self, x):
        hidden_output1 = F.relu(self.fc0(x))
        hidden_output2 = F.relu(self.fc1(hidden_output1))
        hidden_output3 = F.relu(self.fc2(hidden_output2))
        hidden_output4 = F.relu(self.fc3(hidden_output3))
        hidden_output5 = F.relu(self.fc4(hidden_output4))
        y = self.fc5(hidden_output5).view(-1)

        return y