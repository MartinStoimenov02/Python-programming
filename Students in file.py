class Student:
    def __init__(self, ID, name, lg):
        self.ID=ID
        self.name=name
        self.lg=lg
    
    def get_ID(self):
        return self.ID
    
    def get_name(self):
        return self.name
    
    def get_language(self):
        return self.lg
 
def add_student(nom, ime, pr):
    with open ("student.txt", "a") as f:
        f.write(str(nom))
        f.write('\t')
        f.write(ime)
        f.write('\t')
        f.write(pr)
        f.write('\n')

def search(ez):
    with open ("student.txt", "r") as f:
        for line in f:
            if ez in line:
                print(line)

while True:
    print('\n') 
    print("To stop the woop, enter 'end'!")
    id=input("№") 
    if id=='end':
        break
    nam=input("name:")
    if nam=='end':
        break
    lan=input("programming language:")
    if lan=='end':
        break
    obj=Student(id, nam, lan)

    print(obj.get_ID())
    print(obj.get_name())
    print(obj.get_language())

    add_student(obj.ID, obj.name, obj.lg)

ezik=input("searching laguage:")
search(ezik)
