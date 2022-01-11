class MyError(Exception):
    pass

class Student:
    def __init__(self, name, mark):
        self.name=name
        self.mark=mark
        
class StudentGroup:
    def __init__(self):
        self.lst=[]
        
    def add(self, obj):
        l=[]
        for i in self.lst:
            if i[0]==obj.name:
                return
        l.append(obj.name)
        l.append(obj.mark)
        self.lst.append(l)
    
    def prnt(self):
        return self.lst
    
    def remove(self):
        for i in self.lst:
            if i[1]<3:
                self.lst.remove(i)
                
    def av(self):
        s=0
        for i in self.lst:
            s=s+i[1]
        return str(s/len(self.lst))
    
    def Min(self):
        mi=self.lst[0][1]
        for i in self.lst:
            if i[1]<mi:
                mi=i[1]
        return str(mi) 
    
    def Max(self):
        ma=self.lst[0][1]
        for i in self.lst:
            if i[1]>ma:
                ma=i[1]
        return str(ma)
    
    def Move(self):
        l=[]
        for i in self.lst:
            if i[0][0]=='A':
                l.append(i)
        return l
    
    def delete(self):
        self.lst.clear()
        
st=StudentGroup()
while True:
    try:
        n=input("name:")
        if n=='end':
            break
        m=float(input("mark:"))
        m=round(m,2)
        if m<2 or m>6:
            raise MyError("Please input a valid mark!")
        obj=Student(n,m)
        st.add(obj)
    except MyError as error:
        print(error)
    except ValueError:
        print("Please input a valid mark!")
    except:
        print("Something wrong... Please try again!")
    
print(st.prnt())
st.remove()
print(st.prnt())
print("average mark:"+st.av())
print("min mark:"+st.Min())
print("max mark:"+st.Max())
print(st.Move())
st.delete()
print(st.prnt())