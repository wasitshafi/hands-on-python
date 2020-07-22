# program may generate some warnings due use of 'if not exists', when that entity exists
import pymysql

server = pymysql.connect(host="localhost", user = "root", passwd="")
cursor = server.cursor()

# creating new database if not exists
query = "create database if not exists python_mysql_db;"
cursor.execute(query)

query = "use python_mysql_db;"
cursor.execute(query)

query = "create table if not exists student_details(id integer, name varchar(30), primary key(id));"
cursor.execute(query)

query = "show tables"
cursor.execute(query)
print("List of tables in DB : ", cursor.fetchall())