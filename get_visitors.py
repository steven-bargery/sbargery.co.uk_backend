import json
import boto3

def lambda_handler(event, context):
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    # Get the table
    table = dynamodb.Table('sbargery_visitors')

    # Get visitor count - takes 6 hours to update
    #visitor_count = table.item_count

    # Use scan to get visitor count - more reliable count
    visitors = table.scan()
    visitor_count = visitors['Count']

    return {
        'statusCode': 200,
        'body': visitor_count
    }