#!/usr/bin/env python
#mapper.py

# To run without using a reducer:
#   -D mapreduce.job.reduces=0

import sys
import random

for line in sys.stdin:
    line = line.strip()
    random_int = random.randint(1, 10)
    if random_int == 1:
        print("{}\t{}".format(line, ""))
