import mysql.connector
    
def lambda_handler(event, context):
    # Obtiene la información de conexión desde los argumentos de la función Lambda
    db_endpoint = "andres-restaurant-dev-mydatabase-zibgtqarvqcq.c2qhdzf7irsz.us-east-1.rds.amazonaws.com"
    db_name = "andres-restaurant"
    db_user = "admin"  # El nombre de usuario de la base de datos
    db_password = "123456789"  # La contraseña de la base de datos
    
    
    # Crea la conexión a la base de datos
    connection = mysql.connector.connect(
        host=db_endpoint,
        user=db_user,
        password=db_password,
        database=db_name
    )
    
    # Realiza operaciones en la base de datos (consultas, inserciones, etc.)
    
    # Crea las tablas en la base de datos
    create_clientes_table = """
    CREATE TABLE clientes (
        id_cliente INT PRIMARY KEY,
        nombre_completo VARCHAR(100),
        cedula VARCHAR(10),
        correo_electronico VARCHAR(100)
    )
    """

    create_productos_table = """
    CREATE TABLE productos (
        id_producto INT PRIMARY KEY,
        producto VARCHAR(100),
        precio DECIMAL(10, 2),
        inventario INT
    )
    """

    create_pedido_table = """
    CREATE TABLE pedido (
        id_pedido INT PRIMARY KEY,
        id_producto INT,
        precio_producto DECIMAL(10, 2),
        cantidad_pedido INT,
        valor_pagar DECIMAL(10, 2),
        id_cliente INT,
        FOREIGN KEY (id_producto) REFERENCES productos(id_producto),
        FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
    )
    """

    # Ejecuta las sentencias SQL para crear las tablas
    cursor = connection.cursor()
    cursor.execute(create_clientes_table)
    cursor.execute(create_productos_table)
    cursor.execute(create_pedido_table)
    connection.commit()

    # Cierra la conexión a la base de datos
    cursor.close()
    connection.close()
