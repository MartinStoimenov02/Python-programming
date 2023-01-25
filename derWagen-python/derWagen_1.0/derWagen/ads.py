import mysql.connector

def Connection():
    global connection
    connection = mysql.connector.connect(host='localhost',
                                             database='cars',
                                             user='root',
                                             password='1234567')



def Add(mark, model, price, dvig, sk_kut, sust, year_pr, pow, probeg, colour, cupe_type, euro, city, opis, usr_name, password):
    try:
        Connection()
        cursor = connection.cursor()
        
        strg="""SELECT id FROM usr WHERE usr_name=%s AND pass=%s"""
        cursor.execute(strg, (usr_name, password))
        record1 = cursor.fetchall()
        id_usr=record1[0][0]
        
        mySql_insert_query = """INSERT INTO car (date, mark, model, price, dvig, sk_kut, sust, year_pr, pow, probeg, colour, cupe_type, euro, city, opis, id_usr) 
                                VALUES (CURDATE(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

        record = (mark, model, price, dvig, sk_kut, sust, year_pr, pow, probeg, colour, cupe_type, euro, city, opis, id_usr)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record saved successfully")

    except mysql.connector.Error as error:
        print(error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()



def MyAds(usr_name, password): 
    Connection()
    id_query = """select id from usr where usr_name=%s AND pass=%s"""
    cursor = connection.cursor()
    # set variable in query
    cursor.execute(id_query, (usr_name, password))
    # fetch result
    record = cursor.fetchall()
    id_usr=record[0][0]
    global list_ids
    list_ids=[]
    try:
        sql_select_query = """select * from car where id_usr=%s"""
        cursor = connection.cursor()
                
        # set variable in query
        cursor.execute(sql_select_query, (id_usr,))
        # fetch result
        record = cursor.fetchall()

        i=1
        if len(record)==0:
            return 0
        for row in record:
            print("\n\n", i, ":")
            i+=1
            list_ids.append(row[0])
            print("Date upload = ", row[1])
            print("Mark = ", row[2])
            print("Model = ", row[3])
            print("Price = ", row[4])
            print("Engine = ", row[5])
            print("Transmision  = ", row[6])
            print("State = ", row[7])
            print("year of manufacture = ", row[8])
            print("Power = ", row[9])
            print("Kilometres  = ", row[10])
            print("Colour = ", row[11])
            print("coupe type = ", row[12])
            print("euro category = ", row[13])
            print("City = ", row[14])
            print("description = ", row[15], "\n")
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    
    
            
def Delete():
    Connection()
    dlt=int(input("Index of ads to delete:"))
    if dlt-2>len(list_ids)==0:
        print("Out of index of ads!")
        return
    try:
        cursor = connection.cursor()
        sql_Delete_query = """Delete from car where id = %s"""
        # row to delete
        cursor.execute(sql_Delete_query, (list_ids[dlt-1],))
        connection.commit()
        print("Ad Deleted successfully ")

    except:
        print("error")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
            

def EditAd():
    while True:
        ind=int(input("Index of ads to edit:"))
        print(ind-1)
        print(len(list_ids))
        if ind-1>=len(list_ids):
            print("Out of index of ads!")
            continue
        else:
            break
        
    try:
        Connection()         
        sql_select_query = """select * from car where id=%s"""
        cursor = connection.cursor()
                    
            # set variable in query
        cursor.execute(sql_select_query, (list_ids[ind-1],))
            # fetch result
        record = cursor.fetchall()
        if len(record)==0:
            print("Car with this index doesn't exist!")
            return 0
        print("\n\n", ind, ":")
        print("Date upload = ", record[0][1])
        print("Mark = ", record[0][2])
        print("Model = ", record[0][3])
        print("Price = ", record[0][4])
        print("Engine = ", record[0][5])
        print("Transmision  = ", record[0][6])
        print("State = ", record[0][7])
        print("year of manufacture = ", record[0][8])
        print("Power = ", record[0][9])
        print("Kilometres  = ", record[0][10])
        print("Colour = ", record[0][11])
        print("coupe type = ", record[0][12])
        print("euro category = ", record[0][13])
        print("City = ", record[0][14])
        print("description = ", record[0][15], "\n")
        
        ed=input("Edit(Mark, Model, Price, Engine, Transmision, State, YearMan, Power, Km, Colour, CoupeType, Euro, City, Description):")
        
        if ed=="Mark":
            mark=input("new mark:")
            cursor = connection.cursor()
            sql_update_query = """Update car set mark = %s where id = %s"""
            cursor.execute(sql_update_query, (mark, list_ids[ind-1]))
            connection.commit()
            print("Mark Updated successfully ")
            
        elif ed=="Model":
            model=input("new model:")
            cursor = connection.cursor()
            sql_update_query = """Update car set model = %s where id = %s"""
            cursor.execute(sql_update_query, (model, list_ids[ind-1]))
            connection.commit()
            print("Model Updated successfully ")
                
        elif ed=="Price":
            price=input("new price:")
            cursor = connection.cursor()
            sql_update_query = """Update car set price = %s where id = %s"""
            cursor.execute(sql_update_query, (price, list_ids[ind-1]))
            connection.commit()
            print("Price Updated successfully ")
            
        elif ed=="Engine":
            dvig=input("new engine type:")
            cursor = connection.cursor()
            sql_update_query = """Update car set dvig = %s where id = %s"""
            cursor.execute(sql_update_query, (dvig, list_ids[ind-1]))
            connection.commit()
            print("Engine type Updated successfully ")
                
        elif ed=="Transmision":
            trans=input("new Transmision type:")
            cursor = connection.cursor()
            sql_update_query = """Update car set sk_kut = %s where id = %s"""
            cursor.execute(sql_update_query, (trans, list_ids[ind-1]))
            connection.commit()
            print("Transmision type Updated successfully ")
                
        elif ed=="State":
            state=input("new state:")
            cursor = connection.cursor()
            sql_update_query = """Update car set sust = %s where id = %s"""
            cursor.execute(sql_update_query, (state, list_ids[ind-1]))
            connection.commit()
            print("State Updated successfully ")
            
        elif ed=="YearMan":
            y=input("new year of manufacture:")
            cursor = connection.cursor()
            sql_update_query = """Update car set year_pr = %s where id = %s"""
            cursor.execute(sql_update_query, (y, list_ids[ind-1]))
            connection.commit()
            print("Year of manufucture Updated successfully ")
                
        elif ed=="Power":
            power=input("new power:")
            cursor = connection.cursor()
            sql_update_query = """Update car set pow = %s where id = %s"""
            cursor.execute(sql_update_query, (power, list_ids[ind-1]))
            connection.commit()
            print("Power Updated successfully ")
            
        elif ed=="Km":
            km=input("new kilometres:")
            cursor = connection.cursor()
            sql_update_query = """Update car set probeg = %s where id = %s"""
            cursor.execute(sql_update_query, (km, list_ids[ind-1]))
            connection.commit()
            print("Kilometres Updated successfully ")
            
        elif ed=="Colour":
            col=input("new colour:")
            cursor = connection.cursor()
            sql_update_query = """Update car set colour = %s where id = %s"""
            cursor.execute(sql_update_query, (col, list_ids[ind-1]))
            connection.commit()
            print("Colour Updated successfully ")
            
        elif ed=="CoupeType":
            ct=input("new Coupe Type:")
            cursor = connection.cursor()
            sql_update_query = """Update car set cupe_type = %s where id = %s"""
            cursor.execute(sql_update_query, (ct, list_ids[ind-1]))
            connection.commit()
            print("Coupe Type Updated successfully ")
            
        elif ed=="Euro":
            euro=input("new Euro category:")
            cursor = connection.cursor()
            sql_update_query = """Update car set euro = %s where id = %s"""
            cursor.execute(sql_update_query, (euro, list_ids[ind-1]))
            connection.commit()
            print("Euro category Updated successfully ")
            
        elif ed=="City":
            city=input("new city:")
            cursor = connection.cursor()
            sql_update_query = """Update car set city = %s where id = %s"""
            cursor.execute(sql_update_query, (city, list_ids[ind-1]))
            connection.commit()
            print("City Updated successfully ")
            
        elif ed=="Description":
            des=input("new description:")
            cursor = connection.cursor()
            sql_update_query = """Update car set opis = %s where id = %s"""
            cursor.execute(sql_update_query, (des, list_ids[ind-1]))
            connection.commit()
            print("Description Updated successfully ")
                    
    except mysql.connector.Error as error:
            print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()