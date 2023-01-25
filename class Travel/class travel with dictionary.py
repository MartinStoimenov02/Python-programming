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
        print(str(self.id)+' - '+self.dest+' - '+self.fl+' - '+str(self.pr))
    
 
m=int(input("n="))
l=[]
for i in range (0, m):
    id=int(input("ID:"))
    dest=input("destination:")
    fl=input("flight:")
    pr=float(input("price:"))
    obj=Travel(id, dest, fl, pr)
    obj.Reduce()
    l.append(obj)

for j in range (0, len(l)):
    l[j].Prnt()