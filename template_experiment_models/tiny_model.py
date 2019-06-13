import torch.nn


class MyModel(torch.nn.Module):
    def forward(self, *input):
        return [i / 2 for i in input]
