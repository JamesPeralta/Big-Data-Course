#!/usr/bin/env python
#mapper.py

import sys
import string

for line in sys.stdin:
    # convert words to lower case
    line = line.lower()

    # remove punctuations
    for char in line:
        if char in string.punctuation:
            line = line.replace(char, "")

    # remove white spaces
    line = line.strip()

    # split into words
    line_arr = line.split(" ")

    # create 2-grams only if there are more 2 or more words
    if len(line_arr) > 1:
        for i in range(0, len(line_arr) - 1):
            first_word = line_arr[i]
            second_word = line_arr[i + 1]
            print("{} {}\t{}".format(first_word, second_word, 1))
