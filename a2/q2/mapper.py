#!/usr/bin/env python
#mapper.py

import sys


WHITE = "WHITE"
GRAY = "GRAY"
BLACK = "BLACK"

for line in sys.stdin:
    line = line.strip()
    line_arr = line.split()

    # retrieve the key
    key = line_arr[0]

    # retrieve the values
    value_arr = line_arr[1].split("|")
    adj_list = value_arr[0]
    score = value_arr[1]
    colour = value_arr[2]
    parent = value_arr[3]

    # process Grey nodes
    if colour == GRAY:
        print("{}   {}|{}|{}|{}".format(key, adj_list, score, BLACK, parent))
        child_score = str(int(score) + 1)
        for child in adj_list.split(","):
            print("{}   {}|{}|{}|{}".format(child, "null", child_score, GRAY, key))
    else:
        # emit White and Black
        print(line)
