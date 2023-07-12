def insertar_cliente(nombre, cedula, direccion, correo):
    
    connection_info = {
        'host': 'andres-restaurant-dev-mydatabase-zibgtqarvqcq.c2qhdzf7irsz.us-east-1.rds.amazonaws.com',
        'database': 'andres-restaurant',
        'user': 'admin',
        'password': '123456789'
    }

    # Conexión a la base de datos 
    with mysql.connector.connect(**connection_info) as connection:
        
        cursor = connection.cursor()
        query = "INSERT INTO cliente (nombre, cedula, direccion, correo) VALUES (%s, %s, %s, %s)"
        values = (nombre, cedula, direccion, correo)
        cursor.execute(query, values)

        

def insertar_pedido(producto, cantidad, valor_unitario):
    
    connection_info = {
        'host': 'andres-restaurant-dev-mydatabase-zibgtqarvqcq.c2qhdzf7irsz.us-east-1.rds.amazonaws.com',
        'database': 'andres-restaurant',
        'user': 'admin',
        'password': '123456789'
    }

    
    with mysql.connector.connect(**connection_info) as connection:
        
        cursor = connection.cursor()
        query = "INSERT INTO pedido (producto, cantidad, valor_unitario) VALUES (%s, %s, %s)"
        values = (producto, cantidad, valor_unitario)
        cursor.execute(query, values)

        
