import sys
sys.path.append('C:\Users\Usuario\Documents\Programación AWS\Proyecto-final\andres_restaurant/packages')

import mysql.connector




conexion = mysql.connector.connect(user='admin', password = '123456789',
                                   host= 'andres-restaurant-dev-mydatabase-zibgtqarvqcq.c2qhdzf7irsz.us-east-1.rds.amazonaws.com',
                                   database = 'andres-restaurant',
                                   port = '3306')

print(conexion)
