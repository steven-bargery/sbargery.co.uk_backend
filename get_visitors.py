import boto3
import os

# Get the service resource
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # Get the table from an environment variable
    table = dynamodb.Table(os.environ['dbName'])

    # Get visitor count - takes 6 hours to update
    #visitor_count = table.item_count

    # Use scan to get visitor count - more reliable count
    #visitors = table.scan()
    #visitor_count = visitors['Count']

    # Update 5th Aug 2020 - now tracking visitor count with just a single item
    visitor_count = table.get_item(Key={'visitor_key': "count"})

    return {
        'statusCode': 200,
        'body': int(visitor_count['Item']['visitor_count'])
    }