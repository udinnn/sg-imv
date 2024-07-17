#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jabat_tangan' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def jabat_tangan(n):
    # Write your code here
#     if(n < 0):
#         print("Masukan tidak boleh bernilai < 0")
#     elif(n == 0 or n == 1):
#         return 0
#     else:
#         return n - 1 + jabat_tangan(n - 1)
# runtime error idk why, maybe cuz the test case input number is too big? who knows

    try:
        hasil = 0

        if n == 0 or n == 1:
            return 0
        elif n < 0:
            raise ValueError("Masukan tidak boleh bernilai < 0 ")
        else:
            for i in range(n, 0, -1):
                hasil += (i - 1)
            return hasil
    except (ValueError, TypeError) as err:
        print(f"Terdapat kesalahan: {err}")
        return None

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = jabat_tangan(n)

        fptr.write(str(result) + '\n')

    fptr.close()
