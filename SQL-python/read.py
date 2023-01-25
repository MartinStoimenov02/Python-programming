import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='record_company',
                                         user='root',
                                         password='1234567')

    sql_select_Query = "select * from albums"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Release year  = ", row[2])
        print("Band ID  = ", row[3], "\n")

except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")