#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simple_image_flip' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER row_len
#  2. INTEGER col_len
#  3. 2D_INTEGER_ARRAY image
#  4. STRING direction
#

def simple_image_flip(row_len, col_len, image, direction):
    if direction == 'vertical' or direction == 'Vertical':
        image.reverse()
        return image
    
    elif direction == 'horizontal' or direction == 'Horizontal':
        for i in range(len(image)):
            image[i].reverse()
        return image

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    row_len = int(first_multiple_input[0])

    col_len = int(first_multiple_input[1])

    direction = input()

    image = []

    for _ in range(row_len):
        image.append(list(map(int, input().rstrip().split())))

    result = simple_image_flip(row_len, col_len, image, direction)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
