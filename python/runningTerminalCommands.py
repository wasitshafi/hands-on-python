import os
def runCMD(cmd):
  print("")
  status = os.system(cmd)
  print("Status : ", status)

while(True):
  os.system("clear")
  print("1-> to print git version.")
  print("2-> to create new file.")
  print("4-> to traceroute.")
  print("3-> to ping.")
  print("5-> to print present working directory.")
  print("6-> to print list of directories & files.")
  print("0-> to Quit.")
  choice = int(input("Enter your choice : "))
  if(choice == 1):
   runCMD("git --version")
  elif(choice == 2):
   fileName = input("Enter file name : ");
   runCMD("touch " + fileName)
  elif(choice == 3):
   ipAddress = input("Enter IP Address : ");
   runCMD("ping " + ipAddress)
  elif(choice == 4):
   ipAddress = input("Enter IP Address : ");
   runCMD("ping " + ipAddress)
  elif(choice == 5):
   runCMD("pwd")
  elif(choice == 6):
   runCMD("ls")
  elif(choice == 0):
   break;
  input("")

  
#  else
#   print("Invalid choice...! Try Again.")

print("End of main()")
#cmd = "python3 read.py"
