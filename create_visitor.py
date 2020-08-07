import json
import boto3
import uuid
import datetime
import os

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # Get the tables
    visitor_table = dynamodb.Table(os.environ['dbName_visitors'])
    count_table = dynamodb.Table(os.environ['dbName'])

    # Create random ID
    visitor_id = uuid.uuid4()

    # Get current date and time
    datetimenow = datetime.datetime.now()

    # Get source IP
    source_ip = event['sourceIP']

    if source_ip == "69.138.64.135":
        # don't log
        return {
            'statusCode': 200,
            'body': json.dumps('visitor not logged')
        }

    # Put item
    visitor_table.put_item(
        Item={
            'visitor_id': str(visitor_id),
            'date': datetimenow.isoformat(),
            'ip': source_ip
        }
    )

    # Get current count
    v_info = count_table.get_item(Key={'visitor_key': "count"})
    v_count = int(v_info['Item']['visitor_count']) + 1

    # Update count item
    count_table.update_item(
        Key={'visitor_key': "count"},
        UpdateExpression='SET visitor_count = :val1, last_update = :val2',
        ExpressionAttributeValues={
            ':val1': v_count,
            ':val2': datetimenow.isoformat()
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('visitor logged')
    }