# Task 1:

## Overview:
1. Provisioned Jenkins as container with pre-installed Gitlab plugin.
2. Provisioned Filebeat as container for collecting Jenkins job logs.
3. Filebeat will pass the harvested logs to Logstash.
4. Logstash will ingest the logs sent from Filebeat and parse the logs.
5. ElasticSearch will store the parsed logs sent from Logstash and index for fast searches.
6. We can visualize all the logs using Kiban GUI.

## Requirement:
1. t2.medium Instance.

## Steps: 
1. Clone the repo.
2. Checkout to the `Technical/task1` directory.
3. Run ./startup.sh
 
 ## Images:
 1. Jenkins Console Output: 
![alt text](https://github.com/kmohan778/Technical/blob/main/Images/Screenshot%202021-06-17%20at%206.03.47%20PM.png "Logo Title Text 1")

 2. Kibana Console Output: 
![alt text](https://github.com/kmohan778/Technical/blob/main/Images/Screenshot%202021-06-17%20at%206.04.09%20PM.png "Logo Title Text 1")

 3. Docker container: 
![alt text](https://github.com/kmohan778/Technical/blob/main/Images/Screenshot%202021-06-17%20at%206.18.33%20PM.png "Logo Title Text 1")

 4. File beat container logs: 
![alt text](https://github.com/kmohan778/Technical/blob/main/Images/Screenshot%202021-06-17%20at%206.18.53%20PM.png "Logo Title Text 1")
