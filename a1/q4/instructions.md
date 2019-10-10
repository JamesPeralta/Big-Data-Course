## How to run:
1. Move scripts into cluster
    ```
    cd /Users/jamesperalta/Desktop/classes/SENG-550/SENG-550/a1/q4
    scp -i ../seng-550.pem -r ./ ubuntu@199.116.235.112:/home/ubuntu/a1/q4
    ```
2. Move text files onto hdfs
    ```
    hdfs dfs -copyFromLocal shakespeare1.txt hdfs://10.1.2.220:9000/user/
    ```
3. Clear the hdfs output directory
    ```
    hdfs dfs -rm -r /user/assignment1/q4
    ```
3. Navigate into the q3 python files
    ```
    cd /home/ubuntu/a1/q4
    ```
4. Run the MapReduce job
    ```
    $HADOOP_HOME/bin/hadoop jar \
    $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar \
    -D stream.num.map.output.key.fields=2 \
    -D mapreduce.job.reduces=27 \
    -D mapreduce.partition.keypartitioner.options=-k1,1 \
    -files ./mapper.py,./reducer.py \
    -input /user/text-files/shakespeare1.txt \
    -output /user/assignment1/q4/output \
    -mapper ./mapper.py \
    -reducer ./reducer.py \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
    ```
5. View the output
    ```
    see hdfs dir:
    hdfs dfs -copyToLocal hdfs://10.1.2.220:9000/user/assignment1/q4/output ./
    
    hadoop fs -getmerge /user/assignment1/q4/output result.txt
    tail result.txt 
    
    Cat all output correctly:
    cat part-00016 file2.txt file3.txt file4.txt > ./mergedfile.txt
    ```