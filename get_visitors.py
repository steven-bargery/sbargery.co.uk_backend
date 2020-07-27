import json
import boto3

def lambda_handler(event, context):
    # Get the service resource.
    session = boto3.Session(
        aws_access_key_id=${{ secrets.AWS_ACCESS_KEY_ID }},
        aws_secret_access_key=${{ secrets.AWS_SECRET_ACCESS_KEY }},
        region_name = ${{ secrets.AWS_REGION }}
    )
    dynamodb = session.resource('dynamodb')
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
