#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []
    total = 0
    max_sum = None

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for r in range(4):  # hour glass must have 3 rows, so don't look at the last 2
        for i in range(4):  # stop after the last 3-digits on a row
            total = arr[r][i] + arr[r][i+1] + arr[r][i+2]
            total += arr[r+1][i+1]
            total += arr[r+2][i] + arr[r+2][i+1] + arr[r+2][i+2]
            if max_sum is not None:
                max_sum = max(max_sum, total)
            else:
                max_sum = total
    print(max_sum)
