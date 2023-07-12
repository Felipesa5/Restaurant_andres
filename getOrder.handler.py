import json
import mysql.connector

def handler(event, context):
   
    orderId = event['pathParameters']['orderId']

  
    pedido = obtener_pedido(orderId)

    if pedido is not None:
        
        return {
            'statusCode': 200,
            'body': json.dumps(pedido)
        }
    else:
      
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Pedido no encontrado'})
        }

def obtener_pedido(orderId):
   
    connection = mysql.connector.connect(
        host='andres-restaurant-dev-mydatabase-zibgtqarvqcq.c2qhdzf7irsz.us-east-1.rds.amazonaws.com',
        database='andres-restaurant',
        user='admin',
        password='123456789'
    )

    
    cursor = connection.cursor()
    query = "SELECT * FROM pedido WHERE orderId = %s"
    values = (orderId,)
    cursor.execute(query, values)

   
    pedido = cursor.fetchone()

    
    cursor.close()
    connection.close()

    return pedido














"""import json

def handler(event):
    # Obtener el ID del pedido del evento recibido
    order_id = event['orderId']

    # Realizar la lógica para obtener el pedido de la base de datos utilizando el ID
    # Aquí puedes agregar tu código para obtener el pedido de la base de datos

    # Retornar la respuesta al cliente
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Pedido obtenido exitosamente'})
    }
"""
