#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'weightCapacity' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY weights
#  2. INTEGER maxCapacity
#
def knapsack(weights, maxCapacity, i):
    if maxCapacity <= 0:
       return 0
     
    if i >= len(weights):
        return 0

    p1 = -1
    p2 = -1
    if weights[i] <= maxCapacity:
        p1 = knapsack(weights, maxCapacity-weights[i], i+1) + weights[i]
    p2 = knapsack(weights, maxCapacity, i+1)

    return max(p1, p2)
    
def weightCapacity(weights, maxCapacity):
    return knapsack(weights, maxCapacity, 0)
                

if __name__ == '__main__':
