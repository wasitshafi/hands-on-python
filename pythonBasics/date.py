import datetime as d


print( "dir(d) = ", dir(d))

x = d.datetime.now()
#The date contains year, month, day, hour, minute, second, and microsecond.

#print( "\nd.datetime.now() = ", d.datetime.now())
print ("\ndate & time = ", x) 
print ("\ntoday = ", x.today)
print ("\nyear = ", x.year)

mydate1 = d.datetime(2015, 5, 24, 5, 15 ,40) # args = year, month, date, hour, minute, second, microsecond, tzone
print ("\n\nmydate1 object is  : ", mydate1)       # the hour, minute, second, microsecond, tzone are optionals the have default value 0

mydate2 = d.datetime(2015, 5, 24)
print ("mydate2 object is  : ", mydate2)

print ("\n\ndatetime.now = ", d.datetime.now())
print ("strftime(\"%a\")  = ", x.strftime("%a")) #The datetime object has a method for formatting date objects into readable strings.
print ("strftime(\"%A\")  = ", x.strftime("%A"))
print ("strftime(\"%w\")  = ", x.strftime("%w"))
print ("strftime(\"%d\")  = ", x.strftime("%d"))
print ("strftime(\"%b\")  = ", x.strftime("%b"))
print ("strftime(\"%B\")  = ", x.strftime("%B"))
print ("strftime(\"%m\")  = ", x.strftime("%m"))
print ("strftime(\"%y\")  = ", x.strftime("%y"))
print ("strftime(\"%Y\")  = ", x.strftime("%Y"))
print ("strftime(\"%H\")  = ", x.strftime("%H"))
print ("strftime(\"%I\")  = ", x.strftime("%I"))
print ("strftime(\"%p\")  = ", x.strftime("%p"))
print ("strftime(\"%M\")  = ", x.strftime("%M"))
print ("strftime(\"%S\")  = ", x.strftime("%S"))
print ("strftime(\"%f\")  = ", x.strftime("%f"))
print ("strftime(\"%z\")  = ", x.strftime("%z"))
print ("strftime(\"%Z\")  = ", x.strftime("%Z"))
print ("strftime(\"%j\")  = ", x.strftime("%j"))
print ("strftime(\"%U\")  = ", x.strftime("%U"))
print ("strftime(\"%W\")  = ", x.strftime("%W"))
print ("strftime(\"%c\")  = ", x.strftime("%c"))
print ("strftime(\"%x\")  = ", x.strftime("%x"))
print ("strftime(\"%X\")  = ", x.strftime("%X"))
print ("strftime(\"%%\")  = ", x.strftime("%%"))
