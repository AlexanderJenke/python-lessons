import torch.nn as nn
import torch.nn.functional as F
import torch


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 20, kernel_size=5)  # [1x28x28] -> [20x12x12]
        self.conv2 = nn.Conv2d(20, 40, kernel_size=5)  # [20x12x12] -> [40x4x4]
        self.dropout = nn.Dropout2d()
        self.fc1 = nn.Linear(4 * 4 * 40, 100)
        self.fc2 = nn.Linear(100, 10)

    def forward(self, x):
        # conv1
        x = self.conv1(x)  # convolutional filter: [1x28x28] -> [20x24x24]
        x = F.max_pool2d(x, 2)  # max value out of 4: [20x24x24] -> [20x12x12]
        x = F.leaky_relu(x)

        # conv2
        x = self.conv2(x)  # convolutional filter: [20x12x12] -> [40x8x8]
        x = F.max_pool2d(x, 2)  # max value out of 4: [40x8x8] -> [40x4x4]
        x = F.leaky_relu(x)
        x = self.dropout(x)

        x = x.view(-1, 640)  # reshape: [40x4x4] -> [640]

        # fc1
        x = self.fc1(x)  # fully connected: [640] -> [50]
        x = F.leaky_relu(x)
        x = F.dropout(x, training=self.training)

        # fc2
        x = self.fc2(x)  # fully connected: [50] -> [10]
        return F.softmax(x, dim=1)

    def save(self, path):
        torch.save(self.state_dict(), path)

    def load(self, path):
        self.load_state_dict(torch.load(path))
