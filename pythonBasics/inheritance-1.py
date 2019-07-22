class person:
    def getdata(self):
        self.name = input("\nEnter name :")
        self.age = int(input("Enter age :"))
    def putdata(self):
        print ("\nName = ", self.name, "\nAge = ", self.age)

class student(person):
    def getdata(self):
        person.getdata(self)
        self.rollno = int(input("Enter student rollno : "))
        self.marks = float(input("Enter student marks : "))
    def putdata(self):
        person.putdata(self)
        print ("Roll no : ", self.rollno, "\nMarks : ", self.marks)

std1 = student()
std2 = student()

std1.getdata()
std2.getdata()

std1.putdata()
std2.putdata()

