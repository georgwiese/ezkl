from torch import nn

from ezkl import export


class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()

        self.conv1 = nn.Conv2d(in_channels=1, out_channels=2, kernel_size=5, stride=2)
        self.conv2 = nn.Conv2d(in_channels=2, out_channels=3, kernel_size=5, stride=2)
        
        self.relu = nn.ReLU()

        self.d1 = nn.Linear(48, 48)
        self.d2 = nn.Linear(48, 10)

    def forward(self, x):
        print("== Forward pass")
        print("Input shape:", x.shape)
        x = self.conv1(x)
        x = self.relu(x)
        print("After conv1:", x.shape)
        x = self.conv2(x)
        x = self.relu(x)

        print("After conv2:", x.shape)

        x = x.flatten(start_dim = 1)

        print("After flatten:", x.shape)

        x = self.d1(x)
        x = self.relu(x)

        print("After d1:", x.shape)


        logits = self.d2(x)

        print("After d2:", logits.shape)       
        return logits

circuit = MyModel()
export(circuit, input_shape = [1,28,28])


    
