import json
import boto3

sqs = boto3.client('sqs')

def handler(event):
    try:
        # Obtener los pedidos acumulados de la cola
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

        # Procesar cada pedido
        if messages:
            for message in messages:
                pedido = json.loads(message['Body'])

                # Realizar las acciones necesarias para procesar el pedido
                # Ejemplo: enviar el pedido al restaurante

                # Eliminar el mensaje de la cola después de procesarlo
                delete_params = {
                    'QueueUrl': queue_url,
                    'ReceiptHandle': message['ReceiptHandle'],
                }
                sqs.delete_message(**delete_params)

        # Retornar la respuesta indicando el número de pedidos procesados
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'{len(messages)} pedidos procesados'}),
        }
    except Exception as error:
        # Manejar errores
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error al procesar los pedidos'}),
        }
