import logging                                                                                                          
import boto3                                                                                                            
from botocore.exceptions import ClientError 


def create_bucket(bucket_name, region=None):    
    
    try:                                                                                                                           
        if region is None:                                                                                                              
            s3_client = boto3.client('s3')                                                                                         
            s3_client.create_bucket(Bucket=bucket_name)                                                                     
        else:                                                                                                                          
            s3_client = boto3.client('s3', region_name=region)                                                                      
            location = {'LocationConstraint': region}                                                                               
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)                        
    except ClientError as e:                                                                                                        
            logging.error(e)                                                                                                        
            return False                                                                                                    
            return True                               
                                                               
bucket_name = 'devops-abdullah-s3'                                                                                      
region = 'eu-west-1'             
create_bucket(bucket_name,region)                                                                                       
print (create_bucket) 