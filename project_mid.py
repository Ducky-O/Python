import sqlite3
import os
import time
allsub = []
sci = []
math = []
thai = []
eng = []
soci = []
com = []
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
    time.sleep(1)
    print('-'*10+'เกณฑ์การรับเข้าของแต่ละสายการเรียน'+'-'*10)
    print('1.สายการเรียนวิทย์-คณิต\n    เกณฑ์การรับเข้า เกรดเฉลี่ยต้องไม่ต่ำกว่า 2.75\n     -วิชาวิทยาศาสตร์ต้องไม่ต่ำว่า 2.75 และ วิชาคณิตศาสตร์ต้องไม่ต่ำกว่า 2.75')
    print('2.สายการเรียนวิทย์-คอม\n    เกณฑ์การรับเข้า เกรดเฉลี่ยต้องไม่ต่ำกว่า 2.75\n     -วิชาวิทยาศาสตร์ต้องไม่ต่ำกว่า 2.75 และ วิชาคอมพิวเตอร์ต้องไม่ต่ำกว่า 2.75')
    print('3.สายการเรียนศิลป์-คำนวณ\n   เกณฑ์การรับเข้า เกรดเฉลี่ยต้องไม่ต่ำกว่า 2.5\n      -วิชาคณิตศาสตร์ต้องไม่ต่ำกว่า 2.75')
    print('4.สายการเรียนศิลป์-ภาษา\n   เกณฑ์การรับเข้า ไม่มีเกรดเฉลี่ยขั้นต่ำ\n')
    time.sleep(1)

def calculator():
    os.system('cls')
    time.sleep(1)
    print('-'*10+'คำนวณเกรด'+'-'*10)
    print('-วิชาวิทยาศาสตร์')
    c_sci1_1 = float(input('    มัธยม 1 เทอม 1 : '))
    c_sci1_2 = float(input('    มัธยม 1 เทอม 2 : '))
    c_sci2_1 = float(input('    มัธยม 2 เทอม 1 : '))
    c_sci2_2 = float(input('    มัธยม 2 เทอม 2 : '))
    c_sci3_1 = float(input('    มัธยม 3 เทอม 1 : '))
    c_sci3_2 = float(input('    มัธยม 3 เทอม 2 : '))
    c_all_sci = (c_sci1_1+c_sci1_2+c_sci2_1+c_sci2_2+c_sci3_1+c_sci3_2)/6
    sci.append(c_all_sci)
    print('-วิชาคณิตศาสตร์')
    c_math1_1 = float(input('  มัธยม 1 เทอม 1 : '))
    c_math1_2 = float(input('  มัธยม 1 เทอม 2 : '))
    c_math2_1 = float(input('  มัธยม 2 เทอม 1 : '))
    c_math2_2 = float(input('  มัธยม 2 เทอม 2 : '))
    c_math3_1 = float(input('  มัธยม 3 เทอม 1 : '))
    c_math3_2 = float(input('  มัธยม 3 เทอม 2 : '))
    c_all_math = (c_math1_1+c_math1_2+c_math2_1+c_math2_2+c_math3_1+c_math3_2)/6
    math.append(c_all_math)
    print('-วิชาภาษาไทย')
    c_thai1_1 = float(input('   มัธยม 1 เทอม 1 : '))
    c_thai1_2 = float(input('   มัธยม 1 เทอม 2 : '))
    c_thai2_1 = float(input('   มัธยม 2 เทอม 1 : '))
    c_thai2_2 = float(input('   มัธยม 2 เทอม 2 : '))
    c_thai3_1 = float(input('   มัธยม 3 เทอม 1 : '))
    c_thai3_2 = float(input('   มัธยม 3 เทอม 2 : '))
    c_all_thai = (c_thai1_1+c_thai1_2+c_thai2_1+c_thai2_2+c_thai3_1+c_thai3_2)/6
    thai.append(c_all_thai)
    print('-วิชาภาษาอังกฤษ')
    c_eng1_1 = float(input('   มัธยม 1 เทอม 1 : '))
    c_eng1_2 = float(input('   มัธยม 1 เทอม 2 : '))
    c_eng2_1 = float(input('   มัธยม 2 เทอม 1 : '))
    c_eng2_2 = float(input('   มัธยม 2 เทอม 2 : '))
    c_eng3_1 = float(input('   มัธยม 3 เทอม 1 : '))
    c_eng3_2 = float(input('   มัธยม 3 เทอม 2 : '))
    c_all_eng = (c_eng1_1+c_eng1_2+c_eng2_1+c_eng2_2+c_eng3_1+c_eng3_2)/6
    eng.append(c_all_eng)
    print('-วิชาสังคมศึกษา')
    c_soci1_1 = float(input('   มัธยม 1 เทอม 1 : '))
    c_soci1_2 = float(input('   มัธยม 1 เทอม 2 : '))
    c_soci2_1 = float(input('   มัธยม 2 เทอม 1 : '))
    c_soci2_2 = float(input('   มัธยม 2 เทอม 2 : '))
    c_soci3_1 = float(input('   มัธยม 3 เทอม 1 : '))
    c_soci3_2 = float(input('   มัธยม 3 เทอม 2 : '))
    c_all_soci = (c_soci1_1+c_soci1_2+c_soci2_1+c_soci2_2+c_soci3_1+c_soci3_2)/6
    soci.append(c_all_soci)
    print('-วิชาคอมพิวเตอร์')
    c_com1_1 = float(input('   มัธยม 1 เทอม 1 : '))
    c_com1_2 = float(input('   มัธยม 1 เทอม 2 : '))
    c_com2_1 = float(input('   มัธยม 2 เทอม 1 : '))
    c_com2_2 = float(input('   มัธยม 2 เทอม 2 : '))
    c_com3_1 = float(input('   มัธยม 3 เทอม 1 : '))
    c_com3_2 = float(input('   มัธยม 3 เทอม 2 : '))
    c_all_com = (c_com1_1+c_com1_2+c_com2_1+c_com2_2+c_com3_1+c_com3_2)/6
    com.append(c_all_com)
    c_allsub = (c_all_sci+c_all_math+c_all_thai+c_all_eng+c_all_soci+c_all_com)/6
    allsub.append(c_allsub)
    time.sleep(1)
    print('เกรดเฉลี่ยแต่ละวิชา\n -วิชาวิทยาศาสตร์ = %.2f\n'%c_all_sci+' -วิชาคณิตศาสตร์ = %.2f\n'%c_all_math+' -วิชาภาษาไทย = %.2f\n'%c_all_thai+' -วิชาภาษอังกฤษ = %.2f\n'%c_all_eng+' -วิชาสังคมศึกษา = %.2f\n'%c_all_soci+' -วิชาคอมพิวเตอร์ = %.2f'%c_all_com)
    print('เกรดเฉลี่ยของคุณ = %.2f\n'%c_allsub)
    time.sleep(1)


def adddata():
    os.system('cls')
    print('-'*10+'โปรดระบุข้อมูลเพื่อจองสายการเรียน'+'-'*10)
    a_all = float(allsub[0])
    if a_all >= float('2.75') :
        time.sleep(1)
        print('\n  สายการเรียนที่สามารถเลือกลงได้มี\n1.วิทย์-คณิต     2.วิทย์-คอม\n3.ศิลป์-คำนวณ   4.ศิลป์-ภาษา')
        select = input('เลือกสายการเรียน : ')
        if select == '1' :
            time.sleep(1)
            s_sci = sci[0]
            print('เกรดวิชาวิทยาศาสตร์ของคุณ : %.2f'%sci[0])
            s_math = math[0]
            print('เกรดวิชาคณิตศาสตร์ของคุณ : %.2f'%math[0])
            if (s_sci >= float('2.75') and s_math >= float('2.75')) :
                time.sleep(1)
                print('\n   คุณสามารถลงสายการเรียนวิทย์-คณิตได้\nกรุณากรอกข้อมูลให้ครบถ้วนและถูกต้อง\n'+'-'*30)
                a_name = input('ใส่ชื่อ : ')
                a_lname = input('ใส่นามสกุล : ')
                a_year = input('มัธยมศึกษาปีที่ : ')
                a_room = input('ห้อง : ')
                a_numroom = input('เลขที่ : ')
                a_grade = '%.2f'%allsub[0]
                a_study = 'วิทย์-คณิต'
                c.execute('''INSERT INTO student(name,lname,year,room,numroom,grade,study) VALUES(?,?,?,?,?,?,?)''',
                    (a_name,a_lname,a_year,a_room,a_numroom,a_grade,a_study))
                conn.commit()
                time.sleep(1)
                print('\n!!!เพิ่มข้อมูลการลงทะเบียนเรียบร้อยแล้ว!!!\n')
                time.sleep(1)
            elif (s_sci >= float('2.75') and s_math <= float('2.75')):
                print('\n\t!!!ไม่สามารถเลือกสายการเรียนวิทย์-คณิตได้!!!\nเนื่องจากเกรดวิชาคณิตศาสตร์ไม่ถึงตามที่เกณฑ์ที่กำหนดไว้\n')
                time.sleep(1)
            elif (s_sci <= float('2.75') and s_math >= float('2.75')):
                print('\n\t!!!ไม่สามารถเลือกสายการเรียนวิทย์-คณิตได้!!!\nเนื่องจากเกรดวิชาวิทยาศาสตร์ไม่ถึงตามที่เกณฑ์ที่กำหนดไว้\n')
                time.sleep(1)
            elif (s_sci <= float('2.75') and s_math <= float('2.75')):
                print('\n\t!!!ไม่สามารถเลือกสายการเรียนวิทย์-คณิตได้!!!\nเนื่องจากเกรดวิชาวิทยาศาสตร์และคณิตศาสตร์ไม่ถึงตามที่เกณฑ์ที่กำหนดไว้\n')
                time.sleep(1)
        elif select == '2' :
            time.sleep(1)
            s_sci = sci[0]
            print('เกรดวิชาวิทยาศาสตร์ของคุณ : '+float(sci[0]))
            s_com = com[0]
            print('เกรดวิชาคอมพิวเตอร์ของคุณ : '+float(com[0]))
            if (s_sci >= float('2.75') and s_com >= float('2.75')) :
                time.sleep(1)
                print('\n   คุณสามารถลงสายการเรียนวิทย์-คอมได้\nกรุณากรอกข้อมูลให้ครบถ้วนและถูกต้อง\n'+'-'*30)
                a_name = input('ใส่ชื่อ : ')
                a_lname = input('ใส่นามสกุล : ')
                a_year = input('มัธยมศึกษาปีที่ : ')
                a_room = input('ห้อง : ')
                a_numroom = input('เลขที่ : ')
                a_grade = '%.2f'%allsub[0]
                a_study = 'วิทย์-คอม'
                c.execute('''INSERT INTO student(name,lname,year,room,numroom,grade,study) VALUES(?,?,?,?,?,?,?)''',
                    (a_name,a_lname,a_year,a_room,a_numroom,a_grade,a_study))
                conn.commit()
                time.sleep(1)
                print('\n!!!เพิ่มข้อมูลการลงทะเบียนเรียบร้อยแล้ว!!!\n')
                time.sleep(1)
            elif (s_sci <= float('2.75') and s_com >= float('2.75')) :
                print('\n\t!!!ไม่สามารถเลือกสายการเรียนวิทย์-คอมได้!!!\nเนื่องจากเกรดวิชาวิทยาศาสตร์ไม่ถึงตามที่เกณฑ์ที่กำหนดไว้\n')
                time.sleep(1)
            elif (s_sci >= float('2.75') and s_com <= float('2.75')) :
                print('\n\t!!!ไม่สามารถเลือกสายการเรียนวิทย์-คอมได้!!!\nเนื่องจากเกรดวิชาคอมพิวเตอร์ไม่ถึงตามที่เกณฑ์ที่กำหนดไว้\n')
                time.sleep(1)
            elif (s_sci <= float('2.75') and s_com <= float('2.75')) :
                print('\n\t!!!ไม่สามารถเลือกสายการเรียนวิทย์-คอมได้!!!\nเนื่องจากเกรดวิชาวิทยาศาสตร์และคอมพิวเตอร์ไม่ถึงตามที่เกณฑ์ที่กำหนดไว้\n')
                time.sleep(1)
        elif select == '3' :
            time.sleep(1)
            s_math = math[0]
            print('เกรดวิชาคณิตศาสตร์ของคุณ : '+float(math[0]))
            if s_math >= float('2.75') :
                time.sleep(1)
                print('\n   คุณสามารถลงสายการเรียนศิลป์-คำนวณได้\nกรุณากรอกข้อมูลให้ครบถ้วนและถูกต้อง\n'+'-'*30)
                a_name = input('ใส่ชื่อ : ')
                a_lname = input('ใส่นามสกุล : ')
                a_year = input('มัธยมศึกษาปีที่ : ')
                a_room = input('ห้อง : ')
                a_numroom = input('เลขที่ : ')
                a_grade = '%.2f'%allsub[0]
                a_study = 'ศิลป์-คำนวณ'
                c.execute('''INSERT INTO student(name,lname,year,room,numroom,grade,study) VALUES(?,?,?,?,?,?,?)''',
                    (a_name,a_lname,a_year,a_room,a_numroom,a_grade,a_study))
                conn.commit()
                time.sleep(1)
                print('\n!!!เพิ่มข้อมูลการลงทะเบียนเรียบร้อยแล้ว!!!\n')
                time.sleep(1)
            elif s_math <= float('2.75') :
                print('\n\t!!!ไม่สามารถเลือกสายการเรียนศิลป์-คำนวณได้!!!\nเนื่องจากเกรดวิชาคณิตศาสตร์ไม่ถึงตามที่เกณฑ์ที่กำหนดไว้\n')
                time.sleep(1)
        elif select == '4' :
            time.sleep(1)
            print('\n   คุณสามารถลงสายการเรียนศิลป์-ภาษาได้\nกรุณากรอกข้อมูลให้ครบถ้วนและถูกต้อง\n'+'-'*30)
            a_name = input('ใส่ชื่อ : ')
            a_lname = input('ใส่นามสกุล : ')
            a_year = input('มัธยมศึกษาปีที่ : ')
            a_room = input('ห้อง : ')
            a_numroom = input('เลขที่ : ')
            a_grade = '%.2f'%allsub[0]
            a_study = 'ศิลป์-ภาษา'
            c.execute('''INSERT INTO student(name,lname,year,room,numroom,grade,study) VALUES(?,?,?,?,?,?,?)''',
                (a_name,a_lname,a_year,a_room,a_numroom,a_grade,a_study))
            conn.commit()
            time.sleep(1)
            print('\n!!!เพิ่มข้อมูลการลงทะเบียนเรียบร้อยแล้ว!!!\n')
            time.sleep(1)
    elif a_all <= float('2.75') :
        time.sleep(1)
        print(' สายการเรียนที่สามารถเลือกลงได้มี\n1.ศิลป์-คำนวณ   2.ศิลป์-ภาษา')
        select = input('เลือกสายการเรียน : ')
        if select == '1' :
            time.sleep(1)
            s_math = math[0]
            print('กรุณาระบุเกรดวิชาคณิตศาสตร์ : ')
            if s_math >= float('2.75') :
                time.sleep(1)
                print('\n   คุณสามารถลงสายการเรียนศิลป์-คำนวณได้\nกรุณากรอกข้อมูลให้ครบถ้วนและถูกต้อง\n'+'-'*30)
                a_name = input('ใส่ชื่อ : ')
                a_lname = input('ใส่นามสกุล : ')
                a_year = input('มัธยมศึกษาปีที่ : ')
                a_room = input('ห้อง : ')
                a_numroom = input('เลขที่ : ')
                a_grade = '%.2f'%allsub
                a_study = 'ศิลป์-คำนวณ'
                c.execute('''INSERT INTO student(name,lname,year,room,numroom,grade,study) VALUES(?,?,?,?,?,?,?)''',
                    (a_name,a_lname,a_year,a_room,a_numroom,a_grade,a_study))
                conn.commit()
                time.sleep(1)
                print('\n!!!เพิ่มข้อมูลการลงทะเบียนเรียบร้อยแล้ว!!!\n')
                time.sleep(1)
            elif s_math <= float('2.75') :
                time.sleep(1)
                print('\n\t!!!ไม่สามารถเลือกสายการเรียนศิลป์-คำนวณได้!!!\nเนื่องจากเกรดวิชาคณิตศาสตร์ไม่ถึงตามที่เกณฑ์ที่กำหนดไว้')
        if select == '2' :
            time.sleep(1)
            print(' คุณสามารถลงสายการเรียนศิลป์-ภาษาได้\nกรุณากรอกข้อมูลให้ครบถ้วนและถูกต้อง\n'+'-'*30)
            a_name = input('ใส่ชื่อ : ')
            a_lname = input('ใส่นามสกุล : ')
            a_year = input('มัธยมศึกษาปีที่ : ')
            a_room = input('ห้อง : ')
            a_numroom = input('เลขที่ : ')
            a_grade = '%.2f'%allsub
            a_study = 'ศิลป์-ภาษา'
            c.execute('''INSERT INTO student(name,lname,year,room,numroom,grade,study) VALUES(?,?,?,?,?,?,?)''',
                (a_name,a_lname,a_year,a_room,a_numroom,a_grade,a_study))
            conn.commit()
            time.sleep(1)
            print('\n!!!เพิ่มข้อมูลการลงทะเบียนเรียบร้อยแล้ว!!!\n')
            time.sleep(1)

def editdata():
    os.system('cls')
    time.sleep(1)
    print('{0: <10}{1: <20}{2: <20}{3: <20}{4: <8}{5: <10}{6: <15}{7: <15}'.format('ลำดับที่','ชื่อ','สกุล','มัธยมศึกษาปีที่','ห้อง','เลขที่','เกรดเฉลี่ย','เลือกสายการเรียน'))
    c.execute('''SELECT * FROM student''')
    result = c.fetchall()
    for x in result:
        print('{0: <7}{1: <20}{2: <27}{3: <11}{4: <7}{5: <10}{6: <13}{7: <15}'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))
    print('-'*10+'กรอกข้อมูลที่ต้องการแก้ไข'+'-'*10)
    line = input('ใส่หมายเลขแถวที่จะแก้ : ')
    a_name = input('ใส่ชื่อที่ต้องการแก้ไข : ')
    a_lname = input('ใส่นามสกุลที่ต้องการแก้ไข : ')
    a_year = input('ใส่ชั้นปีที่ต้องการแก้ไข : ')
    a_room = input('ใส่ห้องที่ต้องการแก้ไข : ')
    a_numroom = input('ใส่เลขที่ที่ต้องการแก้ไข : ')
    a_grade = '%.2f'%allsub
    data = (a_name,a_lname,a_year,a_room,a_numroom,a_grade,line)
    c.execute('''UPDATE student SET name=?,lname=?,year=?,room=?,numroom=?,grade=? WHERE id=?''',data)
    conn.commit()
    time.sleep(1)
    print('\n!!!แก้ไขข้อมูลนักเรียนเรียบร้อยแล้ว!!!\n')
    time.sleep(1)

def deletedata():
    os.system('cls')
    print('{0: <10}{1: <20}{2: <20}{3: <20}{4: <8}{5: <10}{6: <15}{7: <15}'.format('ลำดับที่','ชื่อ','สกุล','มัธยมศึกษาปีที่','ห้อง','เลขที่','เกรดเฉลี่ย','เลือกสายการเรียน'))
    c.execute('''SELECT * FROM student''')
    result = c.fetchall()
    for x in result:
        print('{0: <7}{1: <20}{2: <27}{3: <11}{4: <7}{5: <10}{6: <13}{7: <15}'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))
    print('-'*10+'กรอกหมายเลขที่ต้องการลบข้อมูล'+'-'*10)
    delete = input('ใส่เลขที่ต้องการลบข้อมูล : ')
    c.execute('''DELETE FROM student WHERE id=?''',delete)
    conn.commit()
    time.sleep(1)
    print('\n!!!ทำการลบข้อมูลเรียบร้อยแล้ว!!!\n')
    time.sleep(1)

def showdata():
    os.system('cls')
    time.sleep(1)
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