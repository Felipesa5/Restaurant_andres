import json
import boto3

sqs = boto3.client('sqs')

def handler(event):
    try:
       
        queue_url = 'https://sqs.us-east-1.amazonaws.com/101626206766/order-queue' 
        params = {
            'QueueUrl': queue_url,
            'AttributeNames': ['All'],
            'MessageAttributeNames': ['All'],
            'MaxNumberOfMessages': 10,
            'VisibilityTimeout': 30,
            'WaitTimeSeconds': 0,
        }
        response = sqs.receive_message(**params)
        messages = response.get('Messages', [])

        
        if messages:
            for message in messages:
                pedido = json.loads(message['Body'])

                
                delete_params = {
                    'QueueUrl': queue_url,
                    'ReceiptHandle': message['ReceiptHandle'],
                }
                sqs.delete_message(**delete_params)

        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'{len(messages)} pedidos procesados'}),
        }
    except Exception as error:
       
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error al procesar los pedidos'}),
        }
