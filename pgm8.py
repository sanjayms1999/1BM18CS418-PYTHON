import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('student.db')
print("Connection Established")

cur = conn.cursor()

def create_table():
    cur.execute("CREATE TABLE STUDENT0 (SID int primary key, name text, age int, marks int)")
    conn.commit()
    print("STUDENT table created.")

def insertor():
    cur.execute("INSERT INTO STUDENT0(SID,NAME,AGE,MARKS) VALUES(1000, 'John', 20, 81)")
    cur.execute("INSERT INTO STUDENT0(SID,NAME,AGE,MARKS) VALUES(1001, 'Smith', 21, 80)")
    cur.execute("INSERT INTO STUDENT0(SID,NAME,AGE,MARKS) VALUES(1002, 'Virat', 21, 78)")
    cur.execute("INSERT INTO STUDENT0(SID,NAME,AGE,MARKS) VALUES(1003, 'Raju', 20, 70)")
    conn.commit()
    print("Values inserted into STUDENT0 Table.")

def DisplayAll():
    print('All Student\'s Data:')
    val = cur.execute('SELECT * FROM STUDENT0')
    for row in val:
        print('Student ID:', row[0])
        print('Student Name:', row[1])
        print('Student Age:', row[2])
        print('Student Marks:', row[3])
        print('')

def DisplayQuery():
    print('Students With Marks Less Than 75:')
    val = cur.execute('SELECT * FROM STUDENT0 WHERE marks<75')
    for row in val:
        print('Student ID:', row[0])
        print('Student Name:', row[1])
        print('Student Age:', row[2])
        print('Student Marks:', row[3])
        print('')

def updator():
    cur.execute('UPDATE STUDENT0 SET name = "Suraj" where SID = 1003')
    conn.commit()

def delete():
    cur.execute('DELETE FROM STUDENT0 WHERE SID = 1002')
    conn.commit()

n=0

while n==0:
    try:
        create_table()
        insertor()
        DisplayAll()
        DisplayQuery()
        updator()
        DisplayAll()
        delete()
        DisplayAll()
    except Error as e:
        print(e)
        n=1
