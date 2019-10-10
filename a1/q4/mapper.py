#!/usr/bin/env python
#mapper.py

import sys
import re


for line in sys.stdin:
    # convert words to lower case
    line = line.strip()
    line = line.lower()

    # remove punctuations
    line = re.sub("[^a-zA-Z0-9\\s]", "", line)

    # split into words
    line_arr = line.split()

    for word in line_arr:
        # get key
        first_letter = str(word[0])
        if first_letter.isdigit():
            key = "42"
        else:
            key = first_letter
        print("{}\t{}\t{}".format(key, word, ""))
