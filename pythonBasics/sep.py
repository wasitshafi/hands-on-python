print ("date = ", end = "")
print (25, 9, 2001, sep = "-")

print ("date = ", end = "")
print (25, 9, sep = "-", end = "-2001")

print ("\nemailID = ", end = "")
print ("wasitshafi700", "gmail.com", sep = "@")

subjects = {"C Programming", "Data Structures", "Compiler Design", "Software Engineering", "Theory of Computation", "Design and Analysis of Algorithm"}

print("\nSubjects are as follows  : \n", subjects)

# using iterator
print ("\n\nSubjects are as follows (using for each loop) : ")
for i in subjects:
    print(i)

print ("\n\nSubjects are as follows (using ): ")
print (*subjects , sep = "\n") # don't forget that '*'




