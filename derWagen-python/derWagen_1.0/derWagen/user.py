import mysql.connector

def Connection():
    global connection
    connection = mysql.connector.connect(host='localhost',
                                             database='cars',
                                             user='root',
                                             password='1234567')



def AddNew(name, number, usr_name, password):
    try:
        Connection()
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO usr (name, number, usr_name, pass) 
                                VALUES (%s, %s, %s, %s) """

        record = (name, number, usr_name, password)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("User added successfully")

    except mysql.connector.Error as error:
        print(error)
        return 0

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
            
            
def Check(usr_name, password):
    Connection()
    try:
        sql_select_query = """select * from usr where usr_name=%s AND pass=%s"""
        cursor = connection.cursor()
        # set variable in query
        cursor.execute(sql_select_query, (usr_name, password))
        # fetch result
        record = cursor.fetchall()

        if len(record)==0:
            return 0            
            
    except mysql.connector.Error as error:
        print(error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            


def Del_usr(usr_name, password):
    Connection()
    dlt=input("Password:")
    if dlt==password:
        try:
            cursor = connection.cursor()
            sql_Delete_query = """Delete from usr where pass = %s AND usr_name=%s"""
            # row to delete
            cursor.execute(sql_Delete_query, (dlt, usr_name))
            connection.commit()
            print("Account Deleted successfully ")
            return 0

        except mysql.connector.Error as error:
            print(error)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    else:
        print("Wrong password!")
        

def ForgotPassword(usr_name):
    try:
        Connection()
        sql_select_query = """select number from usr where usr_name=%s"""
        cursor = connection.cursor()
        # set variable in query
        cursor.execute(sql_select_query, (usr_name,))
        # fetch result
        record = cursor.fetchall()
        if len(record)==0:
            print("This User name doesn't exist!")
            return 0
        num=record[0][0]
        while True:
            number=input("number:")
            print(num)
            print(number)
            if number==num:
                break
            else:
                print("wrong number")
                continue
        password=input("new password:")
        cursor = connection.cursor()
        sql_update_query = """Update usr set pass = %s where number = %s AND usr_name=%s"""
        cursor.execute(sql_update_query, (password, number, usr_name))
        connection.commit()
        print("Password Updated successfully ")

    except mysql.connector.Error as error:
        print(error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            


def EditUser(ed, usr_name, password):
    try:
        Connection()
        if ed=="Name":
            name=input("new name:")
            cursor = connection.cursor()
            sql_update_query = """Update usr set name = %s where pass = %s AND usr_name=%s"""
            cursor.execute(sql_update_query, (name, password, usr_name))
            connection.commit()
            print("Name Updated successfully ")
        elif ed=="Number":
            number=input("new number:")
            cursor = connection.cursor()
            sql_update_query = """Update usr set number = %s where pass = %s AND usr_name=%s"""
            cursor.execute(sql_update_query, (number, password, usr_name))
            connection.commit()
            print("Number Updated successfully ")
        elif ed=="UserName":
            user_n=input("new user name:")
            cursor = connection.cursor()
            sql_update_query = """Update usr set usr_name = %s where pass = %s AND usr_name=%s"""
            cursor.execute(sql_update_query, (user_n, password, usr_name))
            connection.commit()
            print("User name Updated successfully ")
        elif ed=="Password":
            pas=input("new password:")
            cursor = connection.cursor()
            sql_update_query = """Update usr set pass = %s where pass = %s AND usr_name=%s"""
            cursor.execute(sql_update_query, (pas, password, usr_name))
            connection.commit()
            print("Password Updated successfully ")

    except mysql.connector.Error as error:
        print(error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()