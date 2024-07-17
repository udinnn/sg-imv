#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'magic_square_check' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY M
#

def magic_square_check(n, M):
    # Write your code here
    hasil_baris, hasil_kolom, hasil_diag1, hasil_diag2 = 0,0,0,0
    hasil_b, hasil_k, hasil_d1, hasil_d2 = [],[],0,0
    status_b, status_k, status_d1, status_d2 = True, True, True, True

    for i in range(n):
        for j in range(n):
            hasil_baris += M[i][j]
        hasil_b.append(hasil_baris)
        hasil_baris = 0

    for i in range(n):
        for j in range(n):
            hasil_kolom += M[j][i]
        hasil_k.append(hasil_kolom)
        hasil_kolom = 0

    for i in range(n):
        for j in range(n):
            if i == j:
                hasil_diag1 += M[i][j]
    hasil_d1 = hasil_diag1

    for i in range(n):
        for j in range(n):
            if n - 1 - i == j:
                hasil_diag2 += M[i][j]
    hasil_d2 = hasil_diag2

    for i in hasil_b:
        if i != hasil_b[0]:
            status_b = False

    for i in hasil_k:
        if i != hasil_k[0]:
            status_k = False

    if hasil_d1 != hasil_b[0]:
        status_d1 = False

    if hasil_d2 != hasil_b[0]:
        status_d2 = False

    if status_b and status_k and status_d1 and status_d2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    M = []

    for _ in range(n):
        M.append(list(map(int, input().rstrip().split())))

    result = magic_square_check(n, M)

    fptr.write(str(result) + '\n')

    fptr.close()
