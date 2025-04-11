#!/bin/python3
import os

with open(os.environ['OUTPUT_PATH'], 'w') as f:
    f.write("Hello, world!" + '\n')
