import pymysql

def lambda_handler(event, context):
    # Configura la conexión a MySQL
    connection = pymysql.connect(
        host='andres-restaurant-dev-mydatabase-zibgtqarvqcq.c2qhdzf7irsz.us-east-1.rds.amazonaws.com',
        user='admin',
        password='123456789',
        database='andres-restaurant-dev-mydatabase-zibgtqarvqcq'
    )
    
    try:
        with connection.cursor() as cursor:
            # Realiza una consulta
            sql = "SELECT * FROM tu_tabla"
            cursor.execute(sql)
            result = cursor.fetchall()
            
            # Imprime los resultados
            for row in result:
                print(row)
    finally:
        # Cierra la conexión a MySQL
        connection.close()