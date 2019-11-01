#!/usr/bin/env python

import subprocess

cat = subprocess.Popen(["cat", "graph.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

map = subprocess.Popen(["./mapper.py"],
                       stdin=cat.stdout,
                       stdout=subprocess.PIPE)

run_times = 2
for i in range(0, run_times):
    sort = subprocess.Popen(["sort"],
                            stdin=map.stdout,
                            stdout=subprocess.PIPE)

    reduce = subprocess.Popen(["./reducer.py"],
                              stdin=sort.stdout,
                              stdout=subprocess.PIPE)

    if i == run_times - 1:
        break

    map = subprocess.Popen(["./mapper.py"],
                           stdin=reduce.stdout,
                           stdout=subprocess.PIPE)


end_of_pipe = reduce.stdout
for line in end_of_pipe:
    print(line.decode('utf-8').strip())
