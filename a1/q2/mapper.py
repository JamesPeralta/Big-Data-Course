#!/usr/bin/env python
#mapper.py

import sys
import string
import re

for line in sys.stdin:
    # convert words to lower case
    line = line.strip()
    line = line.lower()

    # remove punctuations
    line = re.sub("[^a-zA-Z0-9\\s]", "", line)

    # split into words
    line_arr = line.split()

    # create 2-grams only if there are more 2 or more words
    if len(line_arr) > 1:
        for i in range(0, len(line_arr) - 1):
            first_word = line_arr[i].strip()
            second_word = line_arr[i + 1].strip()
            print("{} {}\t{}".format(first_word, second_word, 1))
