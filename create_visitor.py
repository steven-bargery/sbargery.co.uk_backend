import json
import boto3
import uuid
import datetime


def lambda_handler(event, context):
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    # Get the table
    table = dynamodb.Table('sbargery_visitors')

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
    table.put_item(
        Item={
            'visitor_id': str(visitor_id),
            'date': datetimenow.isoformat(),
            'ip': source_ip
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('visitor logged')
    }