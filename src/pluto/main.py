import torch
from torch import nn

VOCAB_SIZE = 32_000
D_MODEL = 768

embedding = nn.Embedding(VOCAB_SIZE, D_MODEL)

tokens = torch.tensor([12, 593])

output = embedding(tokens)

print(f"Input shape: {tokens.shape}")
print(f"Output shape: {output.shape}")
print(output)

