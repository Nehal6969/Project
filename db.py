import pymysql
import mysql.connector
from tkinter import messagebox as mb

#For creating a connection
mypass = "Mubashira@855"
con = mysql.connector.connect(host="localhost",user="root",password=mypass)
cur = con.cursor()
cur.execute("CREATE DATABASE studentdatabase")

#To check if database is created or not
cur.execute("SHOW DATABASES")
for x in mycursor:
    if x == "studentdatabse":
        stud()


def stud():
    #establishing connection after creating a database
    mypass = "Mubashira@855"
    mydatabase="studentdatabase"
    con = mysql.connector.connect(host="localhost",user="root",password=mypass, database=mydatabase)
    cur = con.cursor()
    #creating a table for students registration
    cursor.execute("CREATE TABLE stud(First_Name VARCHAR(25), Last_Name VARCHAR(25), email VARCHAR(25), username varchar(10), create_password varchar(10),reenter password varchar(10), dob varchar(11), phone number varchar(10), alternate_Number varchar(10), gender varchar(10), branch varchar(10), resume varchar(10))")
    
def log(username, passwd):
    studloguser = username
    studlogpass = passwd
    mypass = "Mubashira@855"
    mydatabase="studentdatabase"
    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()
    cur.execute("select * from stud where username=%s and create_password =%s",(studloguser,studlogpass))
    row=cur.fetchone()
    if row == None:
        mb.showerror("Error!","Invalid USERNAME & PASSWORD")
    else:
        mb.show("Success", "Login Success")



