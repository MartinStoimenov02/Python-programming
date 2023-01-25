import derWagen

def Input():
    global mark, model, price, dvig, sk_kut, sust, year_pr, pow, probeg, colour, cupe_type, euro, city, opis
    mark=input("mark:")
    model=input("model:")
    price=float(input("price:"))
    dvig=input("engine:")
    sk_kut=input("transmission:")
    sust=input("state:")
    year_pr=int(input("year of manufacture:"))
    pow=int(input("power:"))
    probeg=int(input("kilometre:"))
    colour=input("colour:")
    cupe_type=input("coupe type:")
    euro=int(input("euro-category:"))
    city=input("city:")
    opis=input("description:")
    print("\n")
    
def Signup():
    global usr_name, password
    name=input("name:")
    number=input("number:")
    usr_name=input("user name:")
    password=input("password:")
    if(derWagen.AddNew(name, number, usr_name, password))==0:
        return 0
    
def Profil():
    while True:
        ncm=input("Yo're loged in(Ads/User):")
        if ncm=="Ads":
            while True:
                ad=input("Ads management(Add/Edit/Delete/MyAds/Back(for Edit or Delete Run 'MyAds' first(to view indexes))):")
                if ad=="Add":
                    Input()
                    derWagen.Add(mark, model, price, dvig, sk_kut, sust, year_pr, pow, probeg, colour, cupe_type, euro, city, opis, usr_name, password)

                elif ad=="MyAds":
                    if(derWagen.MyAds(usr_name, password))==0:
                        print("There isn't any ads in your profil!")
                        
                elif ad=="Delete":
                    derWagen.Delete()
                
                elif ad=="Edit":
                    if(derWagen.EditAd())==0:
                        break
                
                elif ad=="Back":
                    break

        elif ncm=="User":
            while True:
                usr=input("User management(Edit/Logout/Delete/Back):")
                if usr=="Logout":
                    print("You're loged out! ")
                    return 0

                elif usr=="Delete":
                    if(derWagen.Del_usr(usr_name, password))==0:
                        return

                elif usr=="Edit":
                    while True:
                        ed=input("Edit(Name/Number/UserName/Password/Back):")
                        if(ed=="Name" or ed=="Number" or ed=="UserName" or ed=="Password"):
                            derWagen.EditUser(ed, usr_name, password)
                        elif ed=="Back":
                            break

                elif usr=="Back":
                    break

while True:
    op=input("command (Search, Login/Signup, End):")
    
    if op=="Login":
        usr_name=input("user name:")
        password=input("password:")
        if(derWagen.Check(usr_name, password))==0:
            r=input("Wrong user name or password OR This user doesn't exist! Signup/ForgotPassword\n")
            if r=="Signup":
                if(Signup())==0:
                    continue
            elif r=="ForgotPassword":
                if(derWagen.ForgotPassword(usr_name))==0:
                    continue
            else:
                continue
        else:
            print("\nYour ads:")
            if(derWagen.MyAds(usr_name, password))==0:
                print("There isn't any ads in your profil!")
        Profil()
    
    elif op=="Signup":
        if(Signup())==0:
            continue
        Profil()
                     
    if op=='Search':
        mark=input("mark:")
        model=input("model:")
        try:
            price_from=float(input("price (from):"))
        except:
            price_from=0
        try:
            price_to=float(input("price (to):"))
        except:
            price_to=0
        dvig=input("engine:")
        sk_kut=input("transmission:")
        sust=input("state:")
        try:
            year_from=int(input("year of manufacture (from):"))
        except:
            year_from=0
        try:
            year_to=int(input("year of manufacture (to):"))
        except:
            year_to=0
        try:
            pow_from=int(input("power(from):"))
        except:
            pow_from=0
        try:
            pow_to=int(input("power(to):"))
        except:
            pow_to=0
        try:
            probeg=int(input("max kilometre:"))
        except:
            probeg=0
        colour=input("colour:")
        cupe_type=input("coupe type:")
        try:
            euro=int(input("euro-category:"))
        except:
            euro=0
        city=input("city:")
        order=input("Order by (mark, price_asc, price_desc, year_man, power, kilo, euro_cat, date):")
        derWagen.Read(mark, model, price_from, price_to, dvig, sk_kut, sust, year_from, year_to, pow_from, pow_to, probeg, colour, cupe_type, euro, city, order)

    elif op=='End':
        break