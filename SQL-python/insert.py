import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='record_company',
                                         user='root',
                                         password='1234567')

    mySql_insert_query = """INSERT INTO albums (name, release_year, band_id) 
                           VALUES 
                           ('The HEll', 1990, '2') """ #id is generate automaticaly

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into albums table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into albums table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")