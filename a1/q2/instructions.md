## How to run:
1. Move scripts into hdfs
    ```
    cd /Users/jamesperalta/Desktop/classes/SENG-550/SENG-550/a1/q2
    scp -i ../seng-550.pem -r ./ ubuntu@199.116.235.112:/home/ubuntu/a1/q2
    ```
2. Clear the hdfs output directory
    ```
    hdfs dfs -rm -r /user/assignment1/q2
    ```
3. Navigate into the q2 python files
    ```
    cd /home/ubuntu/a1/q2
    ```
4. Run the MapReduce job
    ```
    $HADOOP_HOME/bin/hadoop jar \
    $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar \
    -files ./mapper.py,./reducer.py \
    -input /user/assignment1/q1/shakespeare1.txt \
    -output /user/assignment1/q2/output \
    -mapper ./mapper.py \
    -reducer ./reducer.py
    ```
5. View the output
    ```
    hadoop fs -getmerge /user/assignment1/q2/output result.txt
    ```
6. Sample output:
    ```
    zounds where	1
    zounds who	1
    zounds ye	1
    zounds you	1
    zwaggered out	1
    zwounds an	1
    zwounds how	1
    zwounds i	3
    zwounds will	1
    zwounds ye	1
    ```