import sqlite3
import os
from sqlite3.dbapi2 import connect
conn = sqlite3.connect('C:\Phudit_python\week6-work.db')
c = conn.cursor()
#c.execute('''CREATE TABLE students (id integer PRIMARY KEY AUTOINCREMENT,
#    name varchar(50) NOT NULL,
#    lname varchar(50) NOT NULL,
#    email varchar(50) NOT NULL,
#    gender varchar(10) NOT NULL,
#    old varchar (10) NOT NULL,
#    year varchar (2) NOT NULL)''')

def menudata():
    global choice
    print('-----ระบบข้อมูลนักเรียน-----\n เพิ่มนักเรียน [a]\n แสดงข้อมูลนักเรียน [s]\n แก้ไขข้อมูลนักเรียน [e]\n ลบข้อมูลนักเรียน [d]\n ออกจากโปรแกรม [x]''')
    choice = input('เลือกทำรายการ : ')

def adddata():
    os.system('cls')
    print('-'*10+'กรอกข้อมูลตามหัวข้อ'+'-'*10)
    a_name = input('ใส่ชื่อ : ')
    a_lname = input('ใส่นามสกุล : ')
    a_email = input('ใส่อีเมลล์ : ')
    a_gender = input('ใส่เพศ : ')
    a_old = input('ใส่อายุ : ')
    a_year = input('ใส่ชั้นปี : ')
    c.execute('''INSERT INTO students(name,lname,email,gender,old,year) VALUES(?,?,?,?,?,?)''',
        (a_name,a_lname,a_email,a_gender,a_old,a_year))
    conn.commit()
    print('!!!เพิ่มข้อมูลนักเรียนเสร็จเรียบร้อยแล้ว!!!')

def showdata():
    os.system('cls')
    print('{0: <10}{1: <20}{2: <20}{3: <20}{4: <15}{5: <15}{6: <1}'.format('ลำดับที่','ชื่อ','สกุล','อีเมลล์','เพศ','อายุ','ชั้นปี'))
    c.execute('''SELECT * FROM students''')
    result = c.fetchall()
    for x in result:
        print('{0: <7}{1: <20}{2: <20}{3: <20}{4: <15}{5: <15}{6: <1}'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
    
def editdata():
    os.system('cls')
    print('-'*10+'กรอกข้อมูลที่ต้องการแก้ไข'+'-'*10)
    line = input('ใส่หมายเลขแถวที่จะแก้ : ')
    ename = input('ใส่ชื่อที่ต้องการแก้ไข : ')
    elname = input('ใส่นามสกุลที่ต้องการแก้ไข : ')
    eemail = input('ใส่emailที่ต้องการแก้ไข : ')
    egender = input('ใส่เพศที่ต้องการแก้ไข : ')
    eold = input('ใส่อายุที่ต้องการแก้ไข : ')
    eyear = input('ใส่ชั้นปีที่ต้องการแก้ไข : ')
    data = (ename,elname,eemail,egender,eold,eyear,line)
    c.execute('''UPDATE students SET name=?,lname=?,email=?,gender=?,old=?,year=? WHERE id=?''',data)
    print('!!!แก้ไขข้อมูลนักเรียนเรียบร้อยแล้ว!!!')
    conn.commit()

def deletedata():
    os.system('cls')
    print('-'*10+'กรอกหมายเลขที่ต้องการลบข้อมูล'+'-'*10)
    delete = input('ใส่เลขที่ต้องการลบข้อมูล : ')
    c.execute('''DELETE FROM students WHERE id=?''',delete)
    print('!!!ทำการลบข้อมูลดรียบร้อยแล้ว!!!')
    conn.commit()

while True:
    menudata()
    if choice == 'a':
        adddata()
    elif choice == 's':
        showdata()
    elif choice == 'e':
        editdata()
    elif choice == 'd':
        deletedata()
    elif choice == 'x':
        exitt = input('ต้องการออกจากโปรแกรมใช่หรือไม่ (y/n) : ')
        if exitt == 'y':
            print('!!!ออกจากโปรแกม!!!')
            break
        elif exitt == 'n':
            os.system('cls')
            continue