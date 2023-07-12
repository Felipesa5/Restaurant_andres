import json
import mysql.connector

def handler(event, context):
    # Obtener el orderId del evento recibido
    orderId = event['pathParameters']['orderId']

    # Obtener el pedido de la base de datos
    pedido = obtener_pedido(orderId)

    if pedido is not None:
        # Pedido encontrado
        return {
            'statusCode': 200,
            'body': json.dumps(pedido)
        }
    else:
        # Pedido no encontrado
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Pedido no encontrado'})
        }

def obtener_pedido(orderId):
    # Conexión a la base de datos
    connection = mysql.connector.connect(
        host='andres-restaurant-dev-mydatabase-zibgtqarvqcq.c2qhdzf7irsz.us-east-1.rds.amazonaws.com',
        database='andres-restaurant',
        user='admin',
        password='123456789'
    )

    # Obtener el pedido de la tabla "pedido" usando el orderId
    cursor = connection.cursor()
    query = "SELECT * FROM pedido WHERE orderId = %s"
    values = (orderId,)
    cursor.execute(query, values)

    # Obtener el resultado del pedido
    pedido = cursor.fetchone()

    # Cerrar cursor y conexión
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