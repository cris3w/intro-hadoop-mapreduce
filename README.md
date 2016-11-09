# Intro to Hadoop and MapReduce from Udacity

Set of scripts written in Python 2.7 for Udacity course [Intro to Hadoop and MapReduce](https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617).

These scripts can be used locally or creating MapReduce jobs in Hadoop.

To use locally, run the following command:

    cat example_data.csv | ./example_mapper.py | sort | ./example_reducer.py > results.txt
