import json
import csv



a = open('data.json','r')

data = json.load(a)

i = 16   #changing i value from 0 to 16

data1 = [data['themes'][i]['name'],data['themes'][i]['description'],data['themes'][i]['thumbnail'],
         data['themes'][i]['preview'],data['themes'][i]['css'],data['themes'][i]['cssMin'],
         data['themes'][i]['cssCdn'],data['themes'][i]['less'],data['themes'][i]['lessVariables'],
         data['themes'][i]['scss'],data['themes'][i]['scssVariables']]


b =open('new.csv','a')
writer = csv.writer(b)
writer.writerow(['name','description','thumbnail','preview','css','cssMin','cssCdn','less','lessVariables','scss','scssVariables'])

writer.writerow(data1)  #csv file will be created consists all rows
#---------------------------------------------------------------------------------------------------------------------------------------------------
#In Mysql with the help of this command
#"LOAD DATA LOCAL INFILE './new.csv' REPLACE INTO TABLE Themes FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';"
#We can load our csv file into database. 


#########################################################################################################################
#import MySQLdb


#db = MySQLdb.connect("localhost","root","adi9827","bootswatch_db")

#cursor = db.cursor()



#sql = """ create table Themes(name text ,description text,
#thumbnail text,preview text,css text,cssMin text,
#cssCdn text,less text,lessVariables text,scss text,scssVariables text)
#"""
#cursor.execute(sql)


#data = cursor.fetchall()
#db.commit()



#db.close()




















