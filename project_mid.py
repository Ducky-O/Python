#คิดว่าจะทำเป็นโปรแกรมป๊อปอั
import sqlite3
import os
from sqlite3.dbapi2 import connect
conn = sqlite3.connect('C:\Phudit_python\project-mid.db')
c = conn.cursor()
#c.execute('''CREATE TABLE student (id integer PRIMARY KEY AUTOINCREMENT,
#    name varchar(50) NOT NULL,
#    lname varchar(50) NOT NULL,
#    year varchar(2) NOT NULL,
#    room varchar(2) NOT NULL,
#    numroom varchar(2) NOT NULL,
#    grade varchar(50) NOT NULL,
#    study varchar(50) NOT NULL)''')

def menu():
    global choice
    print('-------ระบบจองสายการเรียนชั้นมัธยมศึกษาตอนปลาย-------\nดูเกณฑ์การรับเข้าของแต่ละสายการเรียน     [s]\nคำนวณเกรดเฉลี่ย \t \t [c]\nทำการจองสายการเรียน\t \t[a]\nเปลี่ยนข้อมูล/สายการเรียน\t \t[e]\nยกเลิกกการจองสายการเรียน\t [d]\nออกจากระบบ\t \t       [x]')
    choice = input('กรุณากรอกหัวข้อที่ต้องการทำรายการ : ')

def seedata():
    os.system('cls')
    print('-'*10+'เกณฑ์การรับเข้าของแต่ละสายการเรียน'+'-'*10)
    print('1.สายการเรียนวิทย์-คณิต\n    เกณฑ์การรับเข้า เกรดเฉลี่ยต้องไม่ต่ำกว่า 2.75\n     -วิชาวิทยาศาสตร์ต้องไม่ต่ำว่า 2.75 และ วิชาคณิตศาสตร์ต้องไม่ต่ำกว่า 2.75')
    print('2.สายการเรียนวิทย์-คอม\n    เกณฑ์การรับเข้า เกรดเฉลี่ยต้องไม่ต่ำกว่า 2.75\n     -วิชาวิทยาศาสตร์ต้องไม่ต่ำกว่า 2.75 และ วิชาคอมพิวเตอร์ต้องไม่ต่ำกว่า 2.75')
    print('3.สายการเรียนศิลป์-คำนวณ\n   เกณฑ์การรับเข้า เกรดเฉลี่ยต้องไม่ต่ำกว่า 2.5\n      -วิชาคณิตศาสตร์ต้องไม่ต่ำกว่า 2.75')
    print('4.สายการเรียนศิลป์-ภาษา\n   เกณฑ์การรับเข้า ไม่มีเกรดเฉลี่ยขั้นต่ำ')

def calculator():
    os.system('cls')
    print('-'*10+'คำนวณเกรด'+'-'*10)
    c_sci = input('เกรดวิชาวิทยาศาสตร์ : ')
    c_math = input('เกรดวิชาคณิตศาสตร์ : ')
    c_thai = input('เกรดวิชาภาษาไทย : ')
    c_eng = input('เกรดวิชาภาษาอังกฤษ : ')
    c_soci = input('เกรดวิชาสังคมศึกษา : ')
    c_com = input('เกรดวิชาคอมพิวเตอร์ : ')
    #บวกทุกวิชาแล้วหาร 6 รอถามเพื่อน
    #และคิดจะมีบอกด้วยว่ามีสายการเรียนไหนที่สามารถเลือกเรียนได้บ้าง
    print('เกรดเฉลี่ยของคุณ = ')

def adddata():
    os.system('cls')
    print('-'*10+'โปรดระบุข้อมูลเพื่อจองสายการเรียน'+'-'*10)
    a_all = input('เกรดเฉลี่ย : ')
    if a_all >= '2.75' :
        print('  สายการเรียนที่สามารถเลือกลงได้มี\n1.วิทย์-คณิต     2.วิทย์-คอม\n3.ศิลป์-คำนวณ   4.ศิลป์-ภาษา')
        select = input('เลือกสายการเรียน : ')
        if select == '1' :
            s_sci = input('กรุณาระบุเกดวิชาวิทยาศาสตร์ : ')
            s_math = input('กรุณาระบุเกรดวิชาคณิตศาสตร์ : ')
            if (s_sci and s_math >= '2.75') :
                print('   คุณสามารถลงสายการเรียนนี้ได้\nกรุณากรอกข้อมูลให้ครบถ้วนและถูกต้อง')
                a_name = input('ใส่ชื่อ : ')
                a_lname = input('ใส่นามสกุล : ')
                a_year = input('มัธยมศึกษาปีที่ : ')
                a_room = input('ห้อง : ')
                a_numroom = input('เลขที่ : ')
                a_grade = input('เกรดเฉลี่ย : ')
                a_study = input('เลือกเรียนสายการเรียน')
                c.execute('''INSERT INTO students(name,lname,year,room,numroom,grade,study) VALUES(?,?,?,?,?,?,?)''',
                    (a_name,a_lname,a_year,a_room,a_numroom,a_grade,a_study))
                conn.commit()
                print('!!!เพิ่มข้อมูลการลงทะเบียนเรียบร้อยแล้ว!!!')
            elif (s_sci >= '2.75' and s_math <= '2.75'):
                print('\t!!!ไม่สามารถเลือกสายการเรียนนี้ได้!!!\nเนื่องจากเกรดวิชาคณิตศาสตร์ไม่ถึงตามที่เกณฑ์ที่กำหนดไว้')
            elif (s_sci <= '2.75' and s_math >= '2.75'):
                print('\t!!!ไม่สามารถเลือกสายการเรียนนี้ได้!!!\nเนื่องจากเกรดวิชาวิทยาศาสตร์ไม่ถึงตามที่เกณฑ์ที่กำหนดไว้')
            elif (s_sci <= '2.75' and s_math <= '2.75'):
                print('\t!!!ไม่สามารถเลือกสายการเรียนนี้ได้!!!\nเนื่องจากเกรดวิชาวิทยาศาสตร์และคณิตศาสตร์ไม่ถึงตามที่เกณฑ์ที่กำหนดไว้')
        elif select == '2' :
            s_sci = input('กรุณาระบุเกดวิชาวิทยาศาสตร์ : ')
            s_com = input('กรุณาระบุเกดวิชาคอมพิวเตอร์ : ')
            if (s_sci and s_com >= '2.75') :
                print('   คุณสามารถลงสายการเรียนนี้ได้\nกรุณากรอกข้อมูลให้ครบถ้วนและถูกต้อง')
                a_name = input('ใส่ชื่อ : ')
                a_lname = input('ใส่นามสกุล : ')
                a_year = input('มัธยมศึกษาปีที่ : ')
                a_room = input('ห้อง : ')
                a_numroom = input('เลขที่ : ')
                a_grade = input('เกรดเฉลี่ย : ')
                a_study = input('เลือกเรียนสายการเรียน')
                c.execute('''INSERT INTO students(name,lname,year,room,numroom,grade,study) VALUES(?,?,?,?,?,?,?)''',
                    (a_name,a_lname,a_year,a_room,a_numroom,a_grade,a_study))
                conn.commit()
                print('!!!เพิ่มข้อมูลการลงทะเบียนเรียบร้อยแล้ว!!!')
            elif (s_sci <= '2.75' and s_com >= '2.75') :
                print('\t!!!ไม่สามารถเลือกสายการเรียนนี้ได้!!!\nเนื่องจากเกรดวิชาวิทยาศาสตร์ไม่ถึงตามที่เกณฑ์ที่กำหนดไว้')
            elif (s_sci >= '2.75' and s_com <= '2.75') :
                print('\t!!!ไม่สามารถเลือกสายการเรียนนี้ได้!!!\nเนื่องจากเกรดวิชาคอมพิวเตอร์ไม่ถึงตามที่เกณฑ์ที่กำหนดไว้')
            elif (s_sci <= '2.75' and s_com <= '2.75') :
                print('\t!!!ไม่สามารถเลือกสายการเรียนนี้ได้!!!\nเนื่องจากเกรดวิชาวิทยาศาสตร์และคอมพิวเตอร์ไม่ถึงตามที่เกณฑ์ที่กำหนดไว้')
    elif a_all <= '2.75' :
        print(' สายการเรียนที่สามารถเลือกลงได้มี\n1.ศิลป์คำนวณ   2.ศิลป์ภาษา')
        select = input('เลือกสายการเรียน : ')
        if select == '1' :
            s_math = input('a : ')
            if s_math >= '2.75' :
                print('')
#คิดว่าจะทำแค่ให้กรอกข้อมูลอย่างเดียว แต่จะติดปัญหาตรงที่ว่า ถ้าไม่คัดแล้วคนเกรดไม่ถึงจะลงในสายการเรียนมั่ว

while True:
    menu()
    if choice == 's':
        seedata()
    elif choice == 'c':
        calculator()
    elif choice == 'a':
        adddata()
    elif choice == 'x':
        exitt = input('ต้องการออกจากระบบใช่หรือไม่ [y/n] : ')
        if exitt == 'y':
            print('!!!ออกจากโปรแกรม!!!')
            break
        elif exitt == 'n':
            os.system('cls')
            continue