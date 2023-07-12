import json
import boto3

ses = boto3.client('ses')

def handler(event):
    # Obtener los datos del pedido del evento recibido

    # Crear una instancia del servicio SQS
    sqs = boto3.client('sqs')

    # Configurar los parámetros del mensaje
    params = {
        'MessageBody': json.dumps(event)  # Agrega los datos del pedido aquí
    }

    try:
        # Enviar el mensaje a la cola
        response = sqs.send_message(QueueUrl='https://sqs.us-east-1.amazonaws.com/101626206766/order-queue', MessageBody=params['MessageBody'])

        # Enviar el correo electrónico al cliente
        emailParams = {
            'Destination': {
                'ToAddresses': ['pl8973166gmail.com']  # Reemplaza con la dirección de correo electrónico del cliente
            },
            'Message': {
                'Body': {
                    'Text': {
                        'Data': '¡Gracias por tu pedido!'  # Reemplaza con el cuerpo del mensaje que deseas enviar
                    }
                },
                'Subject': {
                    'Data': 'Confirmación de pedido'  # Reemplaza con el asunto del correo electrónico
                }
            },
            'Source': 'morenofelipe513@gmail.com'  # Reemplaza con tu dirección de correo electrónico
        }

        response = ses.send_email(**emailParams)

        # Retornar la respuesta al cliente
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Pedido creado exitosamente'})
        }
    except Exception as error:
        # En caso de error, manejarlo adecuadamente
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error al crear el pedido'})
        }


"""import json


def handler(event):
    # Obtener los datos del pedido del evento recibido
    order_data = event['body']  # Se asume que los datos del pedido se encuentran en el campo 'body' del evento

    # Realizar la lógica para crear el pedido en la base de datos
    # Aquí puedes agregar tu código para crear el pedido en la base de datos

    # Retornar la respuesta al cliente
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Pedido creado exitosamente'})
    }
"""
