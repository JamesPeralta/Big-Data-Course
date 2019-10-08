#!/usr/bin/env python
#mapper.py

import sys
import random

for line in sys.stdin:
    line = line.strip()
    random_int = random.randint(1, 10)
    if random_int == 1:
        print(line)
