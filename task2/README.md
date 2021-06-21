# Task 2:

## Overview:
1. Provisioned one Ec2 instance with Nginx installed.
2. Provisioned another Ec2 instance with Elasticsearch and Kibana installed.
3. Associated the newly created Classic loadbalancer with the Nginx instance.
4. Configured loadbalancer to send logs to S3 bucket.
5. AWS Lambda will be invocked on each put action on the S3.
6. The invocked action will results in importing of the logs to Elasticsearch.

## Requirement:
1. t2.medium Instance.

## Steps: 
1. Clone the repo.
2. Checkout to the `Technical/task2` directory.
3. Run ./deploy.sh

## Images:
1. ELB logs imported to S3 bucket: 
![alt text](https://github.com/kmohan778/Technical/blob/main/Images/Screenshot%202021-06-20%20at%209.11.04%20PM.png "Logo Title Text 1")
2. Logs visualized by Kibana in response to Lambda trigger: 
![alt text](https://github.com/kmohan778/Technical/blob/main/Images/Screenshot%202021-06-21%20at%208.35.49%20AM.png "Logo Title Text 1")
3. Kibana index pattern.
![alt text](https://github.com/kmohan778/Technical/blob/main/Images/Screenshot%202021-06-21%20at%208.36.16%20AM.png "Logo Title Text 1")
4. Cloudwatch log which represents the lambda invocation and import S3 objects to elasticsearch.
![alt text](https://github.com/kmohan778/Technical/blob/main/Images/Screenshot%202021-06-21%20at%208.50.10%20AM.png "Logo Title Text 1")
