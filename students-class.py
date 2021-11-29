class Student:  #define class
    def __init__(self, fnum, name, mark):   #define method to initializing data, self - curent object(instance)
        self.fnum = fnum
        self.name = name
        self.mark = mark

    def __str__(self):  #define method to view data ordered, without that, it will print cell's memory code
        return '['+str(self.fnum)+', '+self.name+', '+str(self.mark)+']'

class StudentGroup:     #define second class
    def __init__(self):      #define method to initializing data, self - curent object(instance)
        self.group = []

    def append(self, student):  #function, that add elements; 
        self.group.append(student)      #name_of_object.name_variable.append(variable in main function)

    def __str__(self):
        # return str([str(student) for student in self.group])
        result = ''
        for student in self.group:
            result += str(student)+' '
        return result

    def min_mark(self):     #function tha find min mark of students
        min = self.group[0]
        for student in self.group:
            if (min.mark > student.mark):
                min = student
        return min

    def max_mark(self):
        max = self.group[0]
        for student in self.group:
            if (max.mark < student.mark):
                max = student
        return max

    def average_mark(self):
        sum = 0
        for student in self.group:
            sum += student.mark
        return sum/len(self.group)

    def sort(self):
        for i in range(len(self.group)):
            min = i
            for j in range(i+1, len(self.group)):
                if self.group[min].mark > self.group[j].mark:
                    min = j
            # temp = self.group[i]
            # self.group[i] = self.group[min]
            # self.group[min] = temp
            self.group[min], self.group[i] = self.group[i], self.group[min]

group = StudentGroup()      #create object in class StudentGroup

n=int(input("number of numbers:"))

for i in range(0, n):
    fn=int(input("fnum:"))
    nm=input("name:")
    gr=float(input("grade:"))
    st = Student(fn, nm, gr)    #this parameters go in init method of class Student
    group.append(st)    #that replace "student" in function append; we called object "group", of class StudentGroup

print()
print("group:"+group.__str__())
print()
print("max mark: {0}".format(group.max_mark()))
print()
print("min mark:"+str(group.min_mark()))
print()
print("average mark: %.2f"%(group.average_mark()))
print()
print("group:")
print(group)
print()
group.sort()
print('group sorted:')
print(group)

import time
time.sleep(30)