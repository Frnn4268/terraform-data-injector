import json
import random
import boto3
import os

rds_client = boto3.client('rds')

def lambda_handler(event, context):
    random_data = {"value": random.randint(0, 100)}
    
    # Connect to RDS and insert random_data
    rds_client.execute_statement(
        secretArn=os.environ['DB_SECRET_ARN'],
        resourceArn=os.environ['DB_RESOURCE_ARN'],
        sql='INSERT INTO mytable (data) VALUES (:data)',
        parameters=[
            {'name': 'data', 'value': {'stringValue': json.dumps(random_data)}}
        ]
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(random_data)
    }
