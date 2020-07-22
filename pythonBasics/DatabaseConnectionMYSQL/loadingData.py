import pymysql

def load_data_from_file(cursor):
    data = open("datafile.txt")
        
    for line in data:
        id, name = line.split(",")
        query = "insert into student_details values(" + id + ", '" + name + "');"
        cursor.execute(query)
    query = "select * from student_details;"
    cursor.execute(query)
    print(cursor.fetchall())

if __name__ == "__main__":
    db = pymysql.connect(host = "localhost", user = "root", passwd="", db = "python_mysql_db")
    cursor = db.cursor()
    load_data_from_file(cursor)
    db.commit()
    db.close()