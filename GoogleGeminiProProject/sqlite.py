### PROJECT-- TEXT TO SQL LLM APPLICATION

# This file code is responsible for inserting any records in sqlite database 
# and also help in connecting python with sqlite

# Import libraries
import sqlite3

# Connect to sqlite database
connection=sqlite3.connect("student.db")   # it creates database and connect to that database

#Create a cursor object to insert record, create table
cursor=connection.cursor()  #responsible in going through all the records in the table

#create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), 
SECTION VARCHAR(25), MARKS INT);
"""
cursor.execute(table_info)  # this creates the table

#Insert some records
cursor.execute('''Insert Into STUDENT values('Nidhi','Data Science','A',100)''')
cursor.execute('''Insert Into STUDENT values('Krish','Data Science','B',85)''')
cursor.execute('''Insert Into STUDENT values('Santosh','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Harsha','Dev Ops','A',45)''')
cursor.execute('''Insert Into STUDENT values('Ratan','Dev Ops','A',60)''')

#Display all the records
print("Inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

# commit changes in database
connection.commit()
connection.close()


