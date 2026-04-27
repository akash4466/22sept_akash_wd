import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()

cur.execute("create table if not exists student(id int, name text)")
cur.execute("insert into student values(1,'Akash')")
con.commit()

cur.execute("select * from student")
print(cur.fetchall())

con.close()