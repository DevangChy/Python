import mysql.connector as mydb

conn = mydb.connect(host="localhost", user="root", password="Devang@2004")

cur = conn.cursor()

cur.execute("create database class")

cur.execute("use class")

cur.execute('''create table monitor(
            roll int primary key,
            name varchar(50),
            months varchar(20)
            )''')

cur.execute('''create table marks(
            roll int primary key,
            name varchar(50),
            term varchar(50),
            s1 int not null,
            s2 int not null,
            s3 int not null,
            total int not null,
            percentage float not null
            )''')

cur.execute('''create table student(
            roll int primary key,
            name varchar(50),
            email varchar(50),
            phone varchar(20),
            address varchar(100)
            )''')

conn.commit()