import MySQLdb

db = MySQLdb.connect("localhost","root","adi9827","mysql")

cursor = db.cursor()

sql = """create database db1
"""

cursor.execute(sql)


data = cursor.fetchall()

print data

db.close()

#--------------------------------------------------------------------------------------------
db1 = MySQLdb.connect("localhost","root","adi9827","db1")

cursor1 = db1.cursor()

sql = """create database db2
"""

cursor1.execute(sql)

db1.commit()
data1 = cursor1.fetchall()

print data1

db1.close()

#-------------------------------------------------------------------------------------------------

db2 = MySQLdb.connect("localhost","root","adi9827","db2")

cursor2 = db2.cursor()
cursor3 = db2.cursor()
cursor4 = db2.cursor()

sql1="create table emp(select * from db1.emp)"
sql2="create table student(select * from db1.student)"
sql3="create table customer(select * from db1.customer)"

cursor2.execute(sql1)
cursor3.execute(sql2)
cursor4.execute(sql3)

db2.commit()

data2 = cursor2.fetchall()
data3 = cursor3.fetchall()
data4 = cursor4.fetchall()

print data2
print data3
print data4

db2.close()