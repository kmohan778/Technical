#!/bin/bash
BUCKET=s3-deploy-bucket-4c712a1
STACK=elk
#export AWS_PROFILE=my_aws
if aws s3api head-bucket --bucket "$BUCKET" 2>/dev/null;
then
    echo "bucket already exists"
else
    echo "bucket does not exists or there is no permission to view it."
    echo "Creating Bucket..."
    aws s3 mb s3://$BUCKET 
fi
aws cloudformation package                  \
    --template-file cloudformation.yaml      \
    --output-template-file output.yaml \
    --s3-bucket $BUCKET

aws cloudformation deploy                    \
    --s3-bucket $BUCKET                      \
    --template-file output.yaml              \
    --stack-name $STACK                      \
    --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM  CAPABILITY_AUTO_EXPAND         \
    --parameter-overrides  \
      InstanceType=t2.medium
      S3BucketName=s3-elk-bucket-4c712a

    

