class Student:
    def __init__(self, name, mark):
        self.name=name
        self.mark=mark

class StudentGroup:
    def __init__(self):
        self.dict={}
        
    def add(self, obj):
        for i in self.dict:
            if obj.name==i:
                return
        self.dict[obj.name]=obj.mark
        
    def remove(self):
        self.dict={k:v for k, v in self.dict.items() if v>2.99}
        
    def Prnt(self):
        return self.dict
    
    def Av(self):
        s=0
        for i in self.dict:
            s=s+self.dict[i]
        return str(s/len(self.dict))
    
    def Min(self):
        m=min(self.dict.values())
        return str(m)
    
    def Max(self):
        ma=max(self.dict.values())
        return str(ma)
    
    def Move(self):
        d={}
        for i in self.dict:
            if i[0]=='A':
                d[i]=self.dict[i]
        return d
    
    def Del(self):
        self.dict.clear()

st=StudentGroup()
        
while True:
    nam=input("name:")
    mar=float(input("mark:"))
    mar=round(mar,2)
    obj=Student(nam, mar)
    if nam=='0' or mar==0:
        break
    st.add(obj)
    
print(st.Prnt())
st.remove()
print(st.Prnt())
print("Avarage mark: "+st.Av())
print("Min mark: "+st.Min())
print("Max mark: "+st.Max())
print(st.Move())
st.Del()
print(st.Prnt())