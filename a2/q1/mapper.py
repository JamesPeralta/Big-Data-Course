#!/usr/bin/env python
#mapper.py

import sys

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
    if colour == "GRAY":
        child_score = str(int(score) + 1)
        for child in adj_list.split(","):
            print("{}   {}|{}|{}|{}".format(child, "null", child_score, "GREY", key))
    else:
        # emit Black
        # emit Grey
        print(line)
