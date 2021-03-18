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
    print('-------ระบบจองสายการเรียนชั้นมัธยมศึกษาตอนปลาย-------\nดูเกณฑ์การรับเข้าของแต่ละสายการเรียน     [s]\nคำนวณเกรดเฉลี่ย \t \t [c]\nทำการจองสายการเรียน\t \t[a]\nเปลี่ยนข้อมูล/สายการเรียน\t \t[e]\nยกเลิกกการจองสายการเรียน\t [d]\nดูรายชื่อการลงทะเบียน\t \t   [w]\nออกจากระบบ\t \t       [x]')
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
    c_sci = float(input('เกรดวิชาวิทยาศาสตร์ : '))
    c_math = float(input('เกรดวิชาคณิตศาสตร์ : '))
    c_thai = float(input('เกรดวิชาภาษาไทย : '))
    c_eng = float(input('เกรดวิชาภาษาอังกฤษ : '))
    c_soci = float(input('เกรดวิชาสังคมศึกษา : '))
    c_com = float(input('เกรดวิชาคอมพิวเตอร์ : '))
    c_all = (c_sci+c_math+c_thai+c_eng+c_soci+c_com)/6
    print('เกรดเฉลี่ยของคุณ = %.2f'%c_all)

def adddata():
    os.system('cls')
    print('-'*10+'โปรดระบุข้อมูลเพื่อจองสายการเรียน'+'-'*10)
    a_all = input('เกรดเฉลี่ย : ')
    if a_all >= '2.75' :
        print('  สายการเรียนที่สามารถเลือกลงได้มี\n1.วิทย์-คณิต     2.วิทย์-คอม\n3.ศิลป์-คำนวณ   4.ศิลป์-ภาษา')
        select = input('เลือกสายการเรียน : ')
        if select == '1' :
            s_sci = input('กรุณาระบุเกรดวิชาวิทยาศาสตร์ : ')
            s_math = input('กรุณาระบุเกรดวิชาคณิตศาสตร์ : ')
            if (s_sci and s_math >= '2.75') :
                print('   คุณสามารถลงสายการเรียนวิทย์-คณิตได้\nกรุณากรอกข้อมูลให้ครบถ้วนและถูกต้อง')
                a_name = input('ใส่ชื่อ : ')
                a_lname = input('ใส่นามสกุล : ')
                a_year = input('มัธยมศึกษาปีที่ : ')
                a_room = input('ห้อง : ')
                a_numroom = input('เลขที่ : ')
                a_grade = input('เกรดเฉลี่ย : ')
                a_study = input('เลือกเรียนสายการเรียน : ')
                c.execute('''INSERT INTO student(name,lname,year,room,numroom,grade,study) VALUES(?,?,?,?,?,?,?)''',
                    (a_name,a_lname,a_year,a_room,a_numroom,a_grade,a_study))
                conn.commit()
                print('!!!เพิ่มข้อมูลการลงทะเบียนเรียบร้อยแล้ว!!!')
            elif (s_sci >= '2.75' and s_math <= '2.75'):
                print('\t!!!ไม่สามารถเลือกสายการเรียนวิทย์-คณิตได้!!!\nเนื่องจากเกรดวิชาคณิตศาสตร์ไม่ถึงตามที่เกณฑ์ที่กำหนดไว้')
            elif (s_sci <= '2.75' and s_math >= '2.75'):
                print('\t!!!ไม่สามารถเลือกสายการเรียนวิทย์-คณิตได้!!!\nเนื่องจากเกรดวิชาวิทยาศาสตร์ไม่ถึงตามที่เกณฑ์ที่กำหนดไว้')
            elif (s_sci <= '2.75' and s_math <= '2.75'):
                print('\t!!!ไม่สามารถเลือกสายการเรียนวิทย์-คณิตได้!!!\nเนื่องจากเกรดวิชาวิทยาศาสตร์และคณิตศาสตร์ไม่ถึงตามที่เกณฑ์ที่กำหนดไว้')
        elif select == '2' :
            s_sci = input('กรุณาระบุเกรดวิชาวิทยาศาสตร์ : ')
            s_com = input('กรุณาระบุเกรดวิชาคอมพิวเตอร์ : ')
            if (s_sci and s_com >= '2.75') :
                print('   คุณสามารถลงสายการเรียนวิทย์-คอมได้\nกรุณากรอกข้อมูลให้ครบถ้วนและถูกต้อง')
                a_name = input('ใส่ชื่อ : ')
                a_lname = input('ใส่นามสกุล : ')
                a_year = input('มัธยมศึกษาปีที่ : ')
                a_room = input('ห้อง : ')
                a_numroom = input('เลขที่ : ')
                a_grade = input('เกรดเฉลี่ย : ')
                a_study = input('เลือกเรียนสายการเรียน : ')
                c.execute('''INSERT INTO student(name,lname,year,room,numroom,grade,study) VALUES(?,?,?,?,?,?,?)''',
                    (a_name,a_lname,a_year,a_room,a_numroom,a_grade,a_study))
                conn.commit()
                print('!!!เพิ่มข้อมูลการลงทะเบียนเรียบร้อยแล้ว!!!')
            elif (s_sci <= '2.75' and s_com >= '2.75') :
                print('\t!!!ไม่สามารถเลือกสายการเรียนวิทย์-คอมได้!!!\nเนื่องจากเกรดวิชาวิทยาศาสตร์ไม่ถึงตามที่เกณฑ์ที่กำหนดไว้')
            elif (s_sci >= '2.75' and s_com <= '2.75') :
                print('\t!!!ไม่สามารถเลือกสายการเรียนวิทย์-คอมได้!!!\nเนื่องจากเกรดวิชาคอมพิวเตอร์ไม่ถึงตามที่เกณฑ์ที่กำหนดไว้')
            elif (s_sci <= '2.75' and s_com <= '2.75') :
                print('\t!!!ไม่สามารถเลือกสายการเรียนวิทย์-คอมได้!!!\nเนื่องจากเกรดวิชาวิทยาศาสตร์และคอมพิวเตอร์ไม่ถึงตามที่เกณฑ์ที่กำหนดไว้')
    elif a_all <= '2.75' :
        print(' สายการเรียนที่สามารถเลือกลงได้มี\n1.ศิลป์-คำนวณ   2.ศิลป์ภาษา')
        select = input('เลือกสายการเรียน : ')
        if select == '1' :
            s_math = input('กรุณาระบุเกรดวิชาคณิตศาสตร์ : ')
            if s_math >= '2.75' :
                print(' คุณสามารถลงสายการเรียนศิลป์-คำนวณได้\nกรุณากรอกข้อมูลให้ครบถ้วนและถูกต้อง')
                a_name = input('ใส่ชื่อ : ')
                a_lname = input('ใส่นามสกุล : ')
                a_year = input('มัธยมศึกษาปีที่ : ')
                a_room = input('ห้อง : ')
                a_numroom = input('เลขที่ : ')
                a_grade = input('เกรดเฉลี่ย : ')
                a_study = input('เลือกเรียนสายการเรียน : ')
                c.execute('''INSERT INTO student(name,lname,year,room,numroom,grade,study) VALUES(?,?,?,?,?,?,?)''',
                    (a_name,a_lname,a_year,a_room,a_numroom,a_grade,a_study))
                conn.commit()
                print('!!!เพิ่มข้อมูลการลงทะเบียนเรียบร้อยแล้ว!!!')
            elif s_math<='2.75' :
                print('\t!!!ไม่สามารถเลือกสายการเรียนศิลป์-คำนวณได้!!!\nเนื่องจากเกรดวิชาคณิตศาสตร์ไม่ถึงตามที่เกณฑ์ที่กำหนดไว้')
        if select == '2' :
            print(' คุณสามารถลงสายการเรียนศิลป์ภาษาได้\nกรุณากรอกข้อมูลให้ครบถ้วนและถูกต้อง')
            a_name = input('ใส่ชื่อ : ')
            a_lname = input('ใส่นามสกุล : ')
            a_year = input('มัธยมศึกษาปีที่ : ')
            a_room = input('ห้อง : ')
            a_numroom = input('เลขที่ : ')
            a_grade = input('เกรดเฉลี่ย : ')
            a_study = input('เลือกเรียนสายการเรียน : ')
            c.execute('''INSERT INTO student(name,lname,year,room,numroom,grade,study) VALUES(?,?,?,?,?,?,?)''',
                (a_name,a_lname,a_year,a_room,a_numroom,a_grade,a_study))
            conn.commit()
            print('!!!เพิ่มข้อมูลการลงทะเบียนเรียบร้อยแล้ว!!!')

def editdata():
    os.system('cls')
    print('-'*10+'กรอกข้อมูลที่ต้องการแก้ไข'+'-'*10)
    line = input('ใส่หมายเลขแถวที่จะแก้ : ')
    a_name = input('ใส่ชื่อที่ต้องการแก้ไข : ')
    a_lname = input('ใส่นามสกุลที่ต้องการแก้ไข : ')
    a_year = input('ใส่ชั้นปีที่ต้องการแก้ไข : ')
    a_room = input('ใส่ห้องที่ต้องการแก้ไข : ')
    a_numroom = input('ใส่เลขที่ที่ต้องการแก้ไข : ')
    a_grade = input('ใส่เกรดเฉลี่ยที่ต้องการแก้ไข : ')
    a_study = input('ใส่สายการเรียนที่ต้องการจะแก้ไข : ')
    data = (a_name,a_lname,a_year,a_room,a_numroom,a_grade,a_study,line)
    c.execute('''UPDATE student SET name=?,lname=?,year=?,room=?,numroom=?,grade=?,study=? WHERE id=?''',data)
    print('!!!แก้ไขข้อมูลนักเรียนเรียบร้อยแล้ว!!!')
    conn.commit()

def deletedata():
    os.system('cls')
    print('-'*10+'กรอกหมายเลขที่ต้องการลบข้อมูล'+'-'*10)
    delete = input('ใส่เลขที่ต้องการลบข้อมูล : ')
    c.execute('''DELETE FROM student WHERE id=?''',delete)
    print('!!!ทำการลบข้อมูลดรียบร้อยแล้ว!!!')
    conn.commit()

def showdata():
    os.system('cls')
    print('{0: <10}{1: <20}{2: <20}{3: <20}{4: <8}{5: <10}{6: <15}{7: <15}'.format('ลำดับที่','ชื่อ','สกุล','มัธยมศึกษาปีที่','ห้อง','เลขที่','เกรดเฉลี่ย','เลือกสายการเรียน'))
    c.execute('''SELECT * FROM student''')
    result = c.fetchall()
    for x in result:
        print('{0: <7}{1: <20}{2: <27}{3: <11}{4: <7}{5: <10}{6: <13}{7: <15}'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))

while True:
    menu()
    if choice == 's':
        seedata()
    elif choice == 'c':
        calculator()
    elif choice == 'a':
        adddata()
    elif choice == 'e' :
        editdata()
    elif choice == 'd' :
        deletedata()
    elif choice == 'w' :
        showdata()
    elif choice == 'x':
        exitt = input('ต้องการออกจากระบบใช่หรือไม่ [y/n] : ')
        if exitt == 'y':
            print('!!!ออกจากโปรแกรม!!!')
            break
        elif exitt == 'n':
            os.system('cls')
            continue