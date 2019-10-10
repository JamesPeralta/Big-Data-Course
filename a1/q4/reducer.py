#!/usr/bin/env python
#reducer.py

import sys

prev_key = None
for line in sys.stdin:
    line = line.rstrip()
    key, word = line.split()

    if prev_key is None:
        prev_key = word
    elif prev_key == word:
        continue
    else:
        print("{}\t{}".format(prev_key, ""))

        # reset variables
        prev_key = word

# catch the end of line
print("{}\t{}".format(prev_key, ""))
