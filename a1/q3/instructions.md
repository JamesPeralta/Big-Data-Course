## How to run:
1. Move scripts into cluster
    ```
    cd /Users/jamesperalta/Desktop/classes/SENG-550/SENG-550/a1/q3
    scp -i ../seng-550.pem -r ./ ubuntu@199.116.235.112:/home/ubuntu/a1/q3
    ```
2. Move text files onto hdfs
    ```
    hdfs dfs -copyFromLocal *.txt hdfs://10.1.2.220:9000/user/
    ```
3. Clear the hdfs output directory
    ```
    hdfs dfs -rm -r /user/assignment1/q3
    ```
3. Navigate into the q3 python files
    ```
    cd /home/ubuntu/a1/q3
    ```
4. Run the MapReduce job
    ```
    $HADOOP_HOME/bin/hadoop jar \
    $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar \
    -files ./mapper.py,./reducer.py \
    -input /user/text-files/ \
    -output /user/assignment1/q3/output \
    -mapper ./mapper.py \
    -reducer ./reducer.py
    ```
5. View the output
    ```
    hadoop fs -getmerge /user/assignment1/q3/output result.txt
    tail result.txt 
    ```
6. Sample output:
    ```
    zodiacs	shakespeare1.txt
    zogranda	moby.txt
    zone	moby.txt, shakespeare1.txt, jane.txt, iliad.txt
    zoned	moby.txt
    zones	moby.txt, iliad.txt, jane.txt
    zoology	moby.txt
    zoroaster	moby.txt
    zounds	shakespeare1.txt
    zwaggered	shakespeare1.txt
    zwounds	shakespeare1.txt
    ```