import os

print ("\ncurrent working directory : '", os.getcwd(), "'")
print ("Files and folder in CWD are as : ", os.listdir() ) # by default it will show to files and folder whter the source file is locate

print ("Creating single directory : ")
#os.mkdir("newdir")
print ( "Creating multilevel directory : ")
#os.makedirs("new/subdir") # it can also be used to make single directory...

path = input("\n\nEnter the path eg:(/Users/jhon pc/Videos) to view detalist : ")
if(os.path.exists):
    os.chdir(path) #changing the current pointing directory to 'path'
else:
    print ("Path does't exists...")

print ( "\n\nCurrent working directory : ", os.getcwd())
print ( "Files and folder are as  : ", os.listdir())

fullPath = os.path.join("user\desktop", "imag.jpg")
print ("full path is as follows : ", fullPath)