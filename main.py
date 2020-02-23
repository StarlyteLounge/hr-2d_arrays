#!/bin/python3

import math
import os
import random
import re
import sys

# if __name__ == '__main__':
def main():
    arr = []
    total = 0
    print('halp')

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for l in range(4):
        print(f'line: {l+1}: {arr[l]}')
        for i in range(3):
            print(f'{i+1}: {i}')
            if arr[l][i] * arr[l][i+1] * arr[l][i+2]:
                print('possible hourglass')
                if arr[l+1][i+1]:
                    if arr[l+2][i] * arr[l+2][i+1] * arr[l+2][i+2]:
                        total = arr[l][i] + arr[l][i+1] + arr[l][i+2]
                        total += arr[l+1][i+1]
                        total += arr[l+2][i] + arr[l+2][i+1] + arr[l+2][i+2]
    print(total)

main()
