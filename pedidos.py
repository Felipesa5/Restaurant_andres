def insertar_cliente(nombre, cedula, direccion, correo):
    # Obtener información de conexión desde variables de entorno o alguna fuente segura
    connection_info = {
        'host': 'andres-restaurant-dev-mydatabase-zibgtqarvqcq.c2qhdzf7irsz.us-east-1.rds.amazonaws.com',
        'database': 'andres-restaurant',
        'user': 'admin',
        'password': '123456789'
    }

    # Conexión a la base de datos utilizando un administrador de contexto
    with mysql.connector.connect(**connection_info) as connection:
        # Inserción de datos en la tabla "cliente"
        cursor = connection.cursor()
        query = "INSERT INTO cliente (nombre, cedula, direccion, correo) VALUES (%s, %s, %s, %s)"
        values = (nombre, cedula, direccion, correo)
        cursor.execute(query, values)

        # Confirmar cambios (no es necesario cerrar explícitamente el cursor o la conexión)

def insertar_pedido(producto, cantidad, valor_unitario):
    # Obtener información de conexión desde variables de entorno o alguna fuente segura
    connection_info = {
        'host': 'andres-restaurant-dev-mydatabase-zibgtqarvqcq.c2qhdzf7irsz.us-east-1.rds.amazonaws.com',
        'database': 'andres-restaurant',
        'user': 'admin',
        'password': '123456789'
    }

    # Conexión a la base de datos utilizando un administrador de contexto
    with mysql.connector.connect(**connection_info) as connection:
        # Inserción de datos en la tabla "pedido"
        cursor = connection.cursor()
        query = "INSERT INTO pedido (producto, cantidad, valor_unitario) VALUES (%s, %s, %s)"
        values = (producto, cantidad, valor_unitario)
        cursor.execute(query, values)

        # Confirmar cambios (no es necesario cerrar explícitamente el cursor o la conexión)
