### Elasticsearch prefix for index name
INDEX_PREFIX = "awslogs"

#################################################
### ELB access log format keys
S3_KEYS = ["timestamp", "elb", "client_ip", "client_port", "backend_ip", "backend_port", "request_processing_time", "backend_processing_time", "response_processing_time", "elb_status_code", "backend_status_code", "received_bytes", "sent_bytes", "request_method", "request_url", "request_version", "user_agent"]

### ELB access log format regex
S3_REGEX = '^(.[^ ]+) (.[^ ]+) (.[^ ]+):(\\d+) (.[^ ]+):(\\d+) (.[^ ]+) (.[^ ]+) (.[^ ]+) (.[^ ]+) (.[^ ]+) (\\d+) (\\d+) \"(\\w+) (.[^ ]+) (.[^ ]+)\" \"(.+)\"'

#################################################

import boto3
import re
import os 
from datetime import datetime
from dateutil import parser, tz, zoneinfo
from elasticsearch import Elasticsearch
from elasticsearch import helpers

from time import time
ES_HOST = os.environ.get('pubip')
R = re.compile(S3_REGEX)
INDEX = INDEX_PREFIX + "-" + datetime.strftime(datetime.now(), "%Y%m%d")
URL = "http://" + ES_HOST + "/_bulk"


def handler(event, context):
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    s3 = boto3.client("s3")
    obj = s3.get_object(
        Bucket=bucket,
        Key=key
    )

    body = obj["Body"].read().decode('utf-8')

    es = Elasticsearch(host=ES_HOST, port=9200)
    actions = []
    elb_name = ""

    for line in body.strip().split("\n"):
        match = R.match(line)
        if not match:
            continue

        values = match.groups(0)
        if not elb_name:
            elb_name = values[1]
        doc = dict(zip(S3_KEYS, values))

        actions.append({"_index": INDEX, "_type": elb_name, "_source": doc})

        if len(actions) > 1000:
            helpers.bulk(es, actions)
            actions = []

    if len(actions) > 0:
        helpers.bulk(es, actions)
