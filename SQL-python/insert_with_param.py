import mysql.connector

def insert_varibles_into_table(name, release_year, band_id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='record_company',
                                             user='root',
                                             password='1234567')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO albums (name, release_year, band_id) 
                                VALUES (%s, %s, %s) """

        record = (name, release_year, band_id)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into albums table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

name=input("name:")
year=int(input("release year:"))
bid=int(input("band id:"))
insert_varibles_into_table(name, year, bid)