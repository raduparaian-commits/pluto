import torch
from torch import nn


D_MODEL = 768


class RMSNorm(nn.Module):
    def __init__(self, dim):
        super().__init__()

        self.weight = nn.Parameter(torch.ones(dim))

    def forward(self, x):
        rms = torch.sqrt(torch.mean(x ** 2, dim=-1, keepdim=True))
        x = x / (rms + 1e-6)

        return x * self.weight


norm = RMSNorm(D_MODEL)

x = torch.randn(2, 768)

output = norm(x)

print("Input shape:", x.shape)
print("Output shape:", output.shape)