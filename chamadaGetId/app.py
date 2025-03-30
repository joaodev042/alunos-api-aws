import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table_name = 'alunos-api-dev2-BedrockMetadataImagesS3Table-1J194EVNMXDQ3'  
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        # Extract the ID from the path parameters
        id = event['pathParameters']['id']
        
        # Get the item from DynamoDB
        response = table.get_item(Key={'id': id})
        
        if 'Item' in response:
            return {
                'statusCode': 200,
                'body': json.dumps(response['Item'])
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Item not found'})
            }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid request, ID is required'})
        }