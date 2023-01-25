import mysql.connector

def Read(mark, model, price_from, price_to, dvig, sk_kut, sust, year_from, year_to, pow_from, pow_to, probeg, colour, cupe_type, euro, city, order):
    lst=[]
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='cars',
                                             user='root',
                                             password='1234567')

        sql_select_query = """select * from car where"""
        cursor = connection.cursor()
        if mark!="":
            sql_select_query = sql_select_query+""" mark = %s"""
            lst.append(mark)
            sql_select_query=sql_select_query+""" and"""
        if model!="":
            sql_select_query = sql_select_query+""" model=%s"""
            lst.append(model)
            sql_select_query=sql_select_query+""" and"""
        if price_from!=0:
            sql_select_query = sql_select_query+""" price>=%s"""
            lst.append(price_from)
            sql_select_query=sql_select_query+""" and"""
        if price_to!=0:
            sql_select_query = sql_select_query+""" price<=%s"""
            lst.append(price_to)
            sql_select_query=sql_select_query+""" and"""
        if dvig!="":
            sql_select_query = sql_select_query+""" dvig=%s"""
            lst.append(dvig)
            sql_select_query=sql_select_query+""" and"""
        if sk_kut!="":
            sql_select_query = sql_select_query+""" sk_kut=%s"""
            lst.append(sk_kut)
            sql_select_query=sql_select_query+""" and"""
        if sust!="":
            sql_select_query = sql_select_query+""" sust=%s"""
            lst.append(sust)
            sql_select_query=sql_select_query+""" and"""
        if year_from!=0:
            sql_select_query = sql_select_query+""" year_pr>=%s"""
            lst.append(year_from)
            sql_select_query=sql_select_query+""" and"""
        if year_to!=0:
            sql_select_query = sql_select_query+""" year_pr<=%s"""
            lst.append(year_to)
            sql_select_query=sql_select_query+""" and"""
        if pow_from!=0:
            sql_select_query = sql_select_query+""" pow>=%s"""
            lst.append(pow_from)
            sql_select_query=sql_select_query+""" and"""
        if pow_to!=0:
            sql_select_query = sql_select_query+""" pow<=%s"""
            lst.append(pow_to)
            sql_select_query=sql_select_query+""" and"""
        if probeg!=0:
            sql_select_query = sql_select_query+""" probeg<=%s"""
            lst.append(probeg)
            sql_select_query=sql_select_query+""" and"""
        if colour!="":
            sql_select_query = sql_select_query+""" colour=%s"""
            lst.append(colour)
            sql_select_query=sql_select_query+""" and"""
        if cupe_type!="":
            sql_select_query = sql_select_query+""" cupe_type=%s"""
            lst.append(cupe_type)
            sql_select_query=sql_select_query+""" and"""
        if euro!=0:
            sql_select_query = sql_select_query+""" euro=%s"""
            lst.append(euro)
            sql_select_query=sql_select_query+""" and"""
        if city!="":
            sql_select_query = sql_select_query+""" city=%s"""
            lst.append(city)
            sql_select_query=sql_select_query+""" and"""
        if sql_select_query=="select * from car where":
            sql_select_query="select * from car"
        else:
            sql_select_query=sql_select_query[:-3]
        
        if order=="mark":
            sql_select_query=sql_select_query+" ORDER BY mark"
        elif order=="price_asc":
            sql_select_query=sql_select_query+" ORDER BY price"
        elif order=="price_desc":
            sql_select_query=sql_select_query+" ORDER BY price DESC"
        elif order=="year_man":
            sql_select_query=sql_select_query+" ORDER BY year_pr"
        elif order=="power":
            sql_select_query=sql_select_query+" ORDER BY pow"
        elif order=="kilo":
            sql_select_query=sql_select_query+" ORDER BY probeg"
        elif order=="euro_cat":
            sql_select_query=sql_select_query+" ORDER BY euro"
        elif order=="date":
            sql_select_query=sql_select_query+" ORDER BY date"
        
        # set variable in query
        cursor.execute(sql_select_query, lst)
        # fetch result
        record = cursor.fetchall()

        for row in record:
            print("\n\n", "Date upload = ", row[1])
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
            usr_id=row[16]
            sql_user = """select * from usr where id=%s"""
            cursor = connection.cursor()
            cursor.execute(sql_user, (usr_id,))
            record1 = cursor.fetchall()
            print("Info for seller:")
            for row in record1:
                print("name = ", row[1])
                print("number = ", row[2], "\n")
            
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()