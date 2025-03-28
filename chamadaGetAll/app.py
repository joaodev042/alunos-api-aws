import boto3
import json
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # Initialize DynamoDB client
    dynamodb = boto3.resource('dynamodb')
    
    
    table_name = 'alunos-api-dev2-BedrockMetadataImagesS3Table-1J194EVNMXDQ3'
  
    table = dynamodb.Table(table_name)
    
    try:
        # Scan the table to get all items
        response = table.scan()
        items = response.get('Items', [])
        
        return {
            'statusCode': 200,
            'body': json.dumps(items)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }