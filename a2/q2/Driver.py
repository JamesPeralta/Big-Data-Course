#!/usr/bin/env python
#Driver.py

import subprocess

keep_going = True
iteration = 0
input_file = "/user/text-files/graph.txt"
output_file = "/user/assignment2/q2/output{}".format(iteration)

while keep_going:
    print("Input: {} \nOutput: {}".format(input_file,output_file))
    hadoop_args = '$HADOOP_HOME/bin/hadoop' + \
                  ' jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar' + \
                  ' -D mapred.reduce.tasks=2' + \
                  ' -files ./mapper.py,./reducer.py' + \
                  ' -input {}'.format(input_file) + \
                  ' -output {}'.format(output_file) + \
                  ' -mapper ./mapper.py' + \
                  ' -reducer ./reducer.py'

    keep_going = False
    map_reduce = subprocess.Popen(hadoop_args,
                                  shell=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)

    end_of_pipe = map_reduce.stderr
    for line in end_of_pipe:
        line = line.decode('utf-8').strip()
        if "keep_going" in line:
            keep_going = True
            input_file = "/user/assignment2/q2/output{}".format(iteration)
            iteration = iteration + 1
            output_file = "/user/assignment2/q2/output{}".format(iteration)

print("Converged")