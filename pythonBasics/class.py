class student:
    def getdata(self):
        self.rollno = int(input("Enter student rollno : "))
        self.name = input("Enter student name : ")
        self.age = int(input("Enter student age : "))
    
    def putdata(self):
        print ("Name = " , self.name, "\nRoll no : ", self.rollno, "\nAge : ", self.age)


class teacher:
    def __init__(self, name, id, salary):
        self.name= name
        self.id = id
        self.salary = salary
    
    def putdata(self):
        print ("Name = " , self.name, "\nId ", self.id, "\nSalary = ", self.salary)

s = student()
s.getdata()

#name = input("\n\nEnter teacher name : ")
#id = int(input("Enter teacher id :"))
#salary = int(input("Enter teacher salary"))
#e = teacher(name, id, salary)

print ("\nStudent data are as follows: ")
s.putdata()
print ("\nTeacher data are as follows: ")
#e.putdata()


newname = input("\nEnter student full name : ")
s.name = newname # we can access data member here as well 
s.putdata()

#'del s.name' for deleting attribute of class
#'del s' for deleting object