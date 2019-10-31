## How to run:
1. Move scripts into hdfs
    ```
    cd /Users/jamesperalta/Desktop/classes/SENG-550/SENG-550/a2/q1
    scp -i ../../ssh/seng-550.pem -r ./ ubuntu@199.116.235.112:/home/ubuntu/a2/q1
    ```
2. Copy to HDFS 
    ```
    hdfs dfs -copyFromLocal ./shakespeare1.txt hdfs://10.1.2.220:9000/user/
    ```
3. Clear the hdfs output directory
    ```
    hdfs dfs -rm -r /user/assignment2/q2/output
    ```
4. Navigate into the q2 python files
    ```
    cd /home/ubuntu/a1/q2
    ```
5. Run the MapReduce job
    ```
    $HADOOP_HOME/bin/hadoop jar \
    $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar \
    -D mapred.reduce.tasks=2 \
    -files ./mapper.py \
    -input /user/assignment2/matrix.txt \
    -output /user/assignment2/q1/output \
    -mapper ./mapper.py \
    -reducer org.apache.hadoop.mapred.lib.IdentityReducer
    ```
6. View the output
    ```
    hdfs dfs -copyToLocal hdfs://10.1.2.220:9000/user/assignment2/q2/output ./
    hadoop fs -getmerge /user/assignment2/q2/output result.txt
    ```
7. Sample output:
    ```
    part-00000  part-00001  _SUCCESS

    ```