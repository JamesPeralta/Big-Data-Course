## How to run:
1. Move scripts into hdfs
    ```
    cd /Users/jamesperalta/Desktop/classes/SENG-550/SENG-550/a2/q3
    scp -i ../../../ssh/seng-550.pem -r ./ ubuntu@199.116.235.112:/home/ubuntu/a2/q3
    ```
2. Run locally
3.Copy to HDFS 
    ```
    hdfs dfs -copyFromLocal ./retail.dat hdfs://10.1.2.220:9000/user/text-files
    ```
3. Clear the hdfs output directory
    ```
    hdfs dfs -rm -r /user/assignment2/q3/
    ```
4. Navigate into the q2 python files
    ```
    cd /home/ubuntu/a1/q2
    ```
5. Run the MapReduce job
    ```
    $HADOOP_HOME/bin/hadoop jar \
    $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar \
    -D stream.num.map.output.key.fields=2 \
    -D mapreduce.partition.keypartitioner.options=-k1,1 \
    -D mapred.reduce.tasks=5 \
    -files ./mapper.py,./reducer.py \
    -input /user/text-files/retail.dat \
    -output /user/assignment2/q3/output \
    -mapper ./mapper.py \
    -reducer ./reducer.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
    ```
6. View the output
    ```
    hdfs dfs -copyToLocal hdfs://10.1.2.220:9000/user/assignment2/q3/output ./
    ```
7. Sample output:
    ```
    part-00000  part-00001  _SUCCESS

    ```