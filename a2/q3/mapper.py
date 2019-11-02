#!/usr/bin/env python
#mapper.py

import sys

for line in sys.stdin:
    line = line.strip()

    items = line.split()
    num_of_items = len(items)
    for i in range(0, num_of_items):
        for j in range(0, num_of_items):
            if i != j:
                print("{}\t{}\t1".format(items[i], items[j]))
                print("{}\t-\t".format(items[i]))
