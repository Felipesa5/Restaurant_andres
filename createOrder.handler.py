import json
import boto3

ses = boto3.client('ses')

def handler(event):
   
    sqs = boto3.client('sqs')

  
    params = {
        'MessageBody': json.dumps(event) 
    }

    try:
       
        response = sqs.send_message(QueueUrl='https://sqs.us-east-1.amazonaws.com/101626206766/order-queue', MessageBody=params['MessageBody'])

      
        emailParams = {
            'Destination': {
                'ToAddresses': ['pl8973166gmail.com']  
            },
            'Message': {
                'Body': {
                    'Text': {
                        'Data': '¡Gracias por tu pedido!'  
                    }
                },
                'Subject': {
                    'Data': 'Confirmación de pedido' 
                }
            },
            'Source': 'morenofelipe513@gmail.com' 
        }

        response = ses.send_email(**emailParams)

      
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Pedido creado exitosamente'})
        }
    except Exception as error:
       
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error al crear el pedido'})
        }


"""import json


def handler(event):
  
    order_data = event['body']  # Se asume que los datos del pedido se encuentran en el campo 'body' del evento

  
   
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Pedido creado exitosamente'})
    }
"""
