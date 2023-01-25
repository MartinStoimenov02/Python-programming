import mysql.connector

def get_laptop_detail(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='record_company',
                                             user='root',
                                             password='1234567')

        cursor = connection.cursor()
        sql_select_query = """select * from albums where id = %s"""
        # set variable in query
        cursor.execute(sql_select_query, (id,))
        # fetch result
        record = cursor.fetchall()

        for row in record:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Release yaer = ", row[2])
            print("band ID  = ", row[3], "\n")

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

a=int(input("id:"))
get_laptop_detail(a)