import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='record_company',
                                         user='root',
                                         password='1234567')

    mySql_select_Query = "select * from albums"
    cursor = connection.cursor(buffered=True)
    cursor.execute(mySql_select_Query)
    record = cursor.fetchone()
    print(record)

except mysql.connector.Error as error:
    print("Error while connecting to MySQL", error)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

"""
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='record_company',
                                         user='root',
                                         password='1234567')
    sql_select_Query = "select * from albums"
    # MySQLCursorDict creates a cursor that returns rows as dictionaries
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    
    print("Fetching each row using column name")
    for row in records:
        id = row["Id"]
        name = row["Name"]
        price = row["Price"]
        purchase_date = row["Purchase_date"]
        print(id, name, price, purchase_date)

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")
"""       
