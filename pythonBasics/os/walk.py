import os

for (r, d, f) in os.walk(os.getcwd()):
        print ("Root      :", r)
        print ("Directory :", d)
        print ("Files     :", f)
        print ("------------------------------------", end = "\n\n")