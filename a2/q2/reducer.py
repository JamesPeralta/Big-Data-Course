#!/usr/bin/env python
#reducer.py

import sys

WHITE = "WHITE"
GRAY = "GRAY"
BLACK = "BLACK"


def colour_check(node_colour):
    if m_colour == BLACK or node_colour == BLACK:
        return BLACK
    elif m_colour == WHITE and node_colour == GRAY:
        return GRAY
    elif m_colour == GRAY and node_colour == GRAY:
        return GRAY
    elif m_colour == GRAY and node_colour == WHITE:
        return GRAY


last_key = None
m_adj_list = None
m_score = None
m_colour = None
m_parent = None
m_keep_going = False
for line in sys.stdin:
    line = line.strip()
    line_arr = line.strip().split()

    # retrieve the key
    key = line_arr[0]

    # retrieve the values
    value_arr = line_arr[1].split("|")
    adj_list = value_arr[0]
    score = value_arr[1]
    colour = value_arr[2]
    parent = value_arr[3]

    if colour != BLACK:
        m_keep_going = True

    if last_key is None:
        last_key = key
        if adj_list != "null":
            m_adj_list = adj_list
        m_score = score
        m_colour = colour
        m_parent = parent
    elif last_key == key:
        # Add an adjacency list
        if adj_list != "null":
            m_adj_list = adj_list

        if score < m_score:
            m_score = score
            m_parent = parent

        m_colour = colour_check(colour)
    else:
        print("{}\t{}|{}|{}|{}".format(last_key, m_adj_list, m_score, m_colour, m_parent))

        last_key = key
        m_adj_list = adj_list
        m_score = score
        m_colour = colour
        m_parent = parent

print("{}\t{}|{}|{}|{}".format(last_key, m_adj_list, m_score, m_colour, m_parent))

if m_keep_going:
    sys.stderr.write("reporter:counter:CUSTOM,keep_going,1")
