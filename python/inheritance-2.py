class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def putdata(self):
        print ("\nName = ", self.name, "\nAge = ", self.age)

class student(person):
    def __init__(self, name, age, rollno, marks):#Use the pass keyword when you do not want to add any other properties or methods to the class.
        person.__init__(self,name, age)          #Eg: class student(person):
        self.rollno = rollno                     #      pass
        self.marks = marks
    def putdata(self):
        person.putdata(self)
        print ("Roll no : ", self.rollno, "\nMarks : ", self.marks)

name = input("Enter name : ")
age = int(input("Enter age : "))
rollno = int(input("Enter rollno : "))
marks = float(input("Enter marks : "))

s1 = student(name, age, rollno, marks)
s1.putdata()