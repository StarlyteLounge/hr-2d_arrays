#!/bin/python3

import math
import os
import random
import re
import sys

# if __name__ == '__main__':

if __name__ == '__main__':
    arr = []
    total = 0

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for r in range(4):  # hour glass must have 3 rows, so don't look at the last 2
        for i in range(3):  # stop after the last 3-digits on a row
            if arr[r][i] * arr[r][i+1] * arr[r][i+2]:  # are all non-zero?
                # possible hourglass
                if arr[r+1][i+1]:
                    if arr[r+2][i] * arr[r+2][i+1] * arr[r+2][i+2]:
                        # we have an hour glass, sum the components
                        total = arr[r][i] + arr[r][i+1] + arr[r][i+2]
                        total += arr[r+1][i+1]
                        total += arr[r+2][i] + arr[r+2][i+1] + arr[r+2][i+2]
    print(total)
