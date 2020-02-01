#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CS224N 2018-19: Homework 5
"""

### YOUR CODE HERE for part 1h
import torch
import torch.nn as nn
import torch.nn.functional as F

class Highway(nn.Module):
    def __init__(self, embed_size):
        super(Highway, self).__init__()
        self.embed_siez = embed_size
        self.proj = nn.Linear(input_size=embed_size, hidden_size=embed_size, bias=True)
        self.gate = nn.Linear(input_size=embed_size, hidden_size=embed_size, bias=True)

    def forward(self, x):
        x_proj = F.relu(self.proj(x))
        x_gate = F.sigmoid(self.gate(x))

        x_high = x_gate * x_proj + (1-x_gate) * x
        return x_high


### END YOUR CODE 

