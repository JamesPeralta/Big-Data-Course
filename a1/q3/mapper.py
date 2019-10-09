#!/usr/bin/env python
#mapper.py

import sys
import re
import os

for line in sys.stdin:
    # convert words to lower case
    line = line.strip()
    line = line.lower()

    # remove punctuations
    line = re.sub("[^a-zA-Z0-9\\s]", "", line)

    # split into words
    line_arr = line.split()

    # print out the word with it's location
    location = os.environ['mapreduce_map_input_file']
    location = location.split("/")
    location = location[-1]
    for word in line_arr:
        print("{}\t{}".format(word, location))
