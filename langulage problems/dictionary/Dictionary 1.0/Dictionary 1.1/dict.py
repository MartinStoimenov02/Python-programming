import dict
cmnd='a'    
while cmnd!='0':
    print('\n'+"YOUR DICTIONARY"+2*'\n'+"your choice:"+'\n'+"1. search word (BG/EN)"+'\n'+"2. add new word"+'\n'+"3. Delete word"+'\n'+"4. show all words in dictionary")
    cmnd=input("your choice(1-4, for end tab '0'): ")
    
    if cmnd=='1':
       dict.Translate() 
       
    elif cmnd=='2':
        dict.Add()
    
    elif cmnd=='3':
        dict.Delete()
    
    elif cmnd=='4':
        dict.All()