#!/usr/bin/env python
#mapper.py

import sys

for line in sys.stdin:
    line.strip().split()
    row, col, value = line.strip().split(",")
    print("{},{},{}".format(col, row, value))

