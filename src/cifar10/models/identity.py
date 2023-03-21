import torch.nn as nn
class Identity(nn.Module):
        r"""A placeholder identity operator that is argument-insensitive.
        """
        def __init__(self, *args, **kwargs):
            super(Identity, self).__init__()

        def forward(self, input):
            return input