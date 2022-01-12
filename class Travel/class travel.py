class Travel:
    def __init__(self, ID, Destination, Flight, Price):
        self.id=ID
        self.dest=Destination
        self.fl=Flight
        self.pr=Price 
        
    def Reduce(self):
        if self.pr>200:
            self.pr=self.pr-(self.pr*0.1)
            
    def Prnt(self):
        return str(self.id)+' - '+self.dest+' - '+self.fl+' - '+str(self.pr)
    
 
m=int(input("n="))
l=[]
l1=[]
for i in range (0, m):
    id=int(input("ID:"))
    dest=input("destination:")
    fl=input("flight:")
    pr=float(input("price:"))
    obj=Travel(id, dest, fl, pr)
    l.append(obj.Prnt())
    obj.Reduce()
    obj.Prnt()
    l1.append(obj.Prnt())
    
print(l)
print(l1)