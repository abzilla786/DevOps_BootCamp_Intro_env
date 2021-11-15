import boto3

s3 = boto3.client('s3')
s3.download_file('devops-abdullah-s3', 'test.md', 'test2.md')