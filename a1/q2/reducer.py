#!/usr/bin/env python
#reducer.py

import sys

prev_key = None
tot_count = 0
for line in sys.stdin:
    line = line.rstrip()
    ngram, count = line.split('\t')

    if prev_key is None:
        prev_key = ngram
        tot_count = int(count)
        continue
    if prev_key == ngram:
        tot_count = tot_count + int(count)
        continue
    if prev_key != ngram:
        print("{}\t{}".format(prev_key, tot_count))
        prev_key = ngram
        tot_count = int(count)

# catch the end of line
print("{}\t{}".format(prev_key, tot_count))
