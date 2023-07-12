import pymysql

def lambda_handler(event, context):
    
    connection = pymysql.connect(
        host='andres-restaurant-dev-mydatabase-zibgtqarvqcq.c2qhdzf7irsz.us-east-1.rds.amazonaws.com',
        user='admin',
        password='123456789',
        database='andres-restaurant-dev-mydatabase-zibgtqarvqcq'
    )
    
    try:
        with connection.cursor() as cursor:
            
            sql = "SELECT * FROM tu_tabla"
            cursor.execute(sql)
            result = cursor.fetchall()
            
           
            for row in result:
                print(row)
    finally:
        
        connection.close()
