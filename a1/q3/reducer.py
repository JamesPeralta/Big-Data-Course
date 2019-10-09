#!/usr/bin/env python
#reducer.py

import sys

prev_key = None
value_list = []
for line in sys.stdin:
    line = line.rstrip()
    word, file_name = line.split('\t')

    if prev_key is None:
        prev_key = word
        value_list.append(file_name)
    elif prev_key == word:
        if file_name not in value_list:
            value_list.append(file_name)
    else:
        # print out word with files as string
        files = ", ".join(value_list)
        print("{}\t{}".format(prev_key, files.strip()))

        # reset variables
        prev_key = word
        value_list = [file_name]

# catch the end of line
files = ", ".join(value_list)
print("{}\t{}".format(prev_key, files.strip()))
