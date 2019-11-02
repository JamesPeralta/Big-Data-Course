#!/usr/bin/env python
#reducer.py

import sys

last_key = None
second_key = None
count = 0
denominator = 0
for line in sys.stdin:
    line = line.strip()
    items = line.split("\t")
    key = items[0]
    key2 = items[1]

    if last_key is None:
        last_key = key
        second_key = key2
        denominator += 1
    elif last_key == key:
        if key2 == "-":
            denominator += 1
        elif second_key == "-":
            second_key = key2
            count += 1
        elif second_key == key2:
            count += 1
        else:
            print("{}\t{}\t{}".format(last_key, second_key, float(count) / float(denominator)))
            second_key = key2
            count = 1
    else:
        print("{}\t{}\t{}".format(last_key, second_key, float(count)/float(denominator)))
        last_key = key
        second_key = key2
        denominator = 1

print("{}\t{}\t{}".format(last_key, second_key, float(count)/float(denominator)))

