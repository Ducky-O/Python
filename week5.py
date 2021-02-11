'''
class nisit:
    def __init__(self,name,sex,year,faculty,department,id,province) :
        self.name=name
        self.sex=sex
        self.year=year
        self.faculty=faculty
        self.department=department
        self.id=id
        self.province=province

    def showPHis(self):
        print('\tStudent Information')
        print('-'*45)
        print('ชื่อ-นามสกุล : ',self.name)
        print('เพศ : ',self.sex)
        print('ชั้นปีการศึกษา : ',self.year)
        print('คณะ : ',self.faculty)
        print('สาขาวิชา : ',self.department)
        print('รหัสนักศึกษา : ',self.id)
        print('มาจากจังหวัด : ',self.province)

a=str(input('ชื่อ-นามสกุล : '))
b=str(input('เพศ : '))
c=str(input('ชั้นปีการศึกษา : '))
d=str(input('คณะ : '))
e=str(input('สาขาวิชา : '))
f=str(input('รหัสนักศึกษา : '))
g=str(input('มาจากจังหวัด : '))

x=nisit(a,b,c,d,e,f,g)
x.showPHis()
'''

import os
name_list = ['ข้าวกะเพรา','ข้าวไข่เจียว','ข้าวหมูทอด','ข้าวผัดหมูสับ']
price_list = [50,30,35,40]
class market :
    def list_def(self):
        for x in range(0,len(name_list)):
            print(x+1,name_list[x],price_list[x],'บาท')
    def choose(self):
        print('**********อาหารตามใจคนทำ**********')
        print('\tแสดงรายการสินค้า กด 1\n\tเพิ่มรายการสินค้า  กด 2\n\tออกจากระบบ     กด 3')
    def input_choise(self):
        global choise
        choise = input('กรุณาเลือกคำสั่ง : ')
    def add_list(self):
        while True:
            print('เพิ่มรายการสินค้า หากต้องการ กรอก exit')
            add_name = input('เพิ่มชื่อสินค้า :')
            if add_name == 'exit':
                break
            else : 
                add_price = input('เพิ่มราคาสินค้า :')
                name_list.append(add_name)
                price_list.append(add_price)
            add = input ('ต้องการเพิ่มสินค้าอีกหรือไม่ [y/n] :')
            if add == 'n' :
                break
            elif add == 'y' :
                os.system('cls')

while True:
    x = market()
    x.choose()
    x.input_choise()
    if choise == '1' :
        os.system('cls')
        print('กรุณาเลือกคำสั่ง : ',choise)
        x.list_def()
    if choise == '2' :
        os.system('cls')
        print('กรุณาเลือกคำสั่ง : ',choise)
        x.add_list()
    if choise == '3' :
        os.system('cls')
        print('กรุณาเลือกคำสั่ง : ',choise)
        close = input('ต้องการปิดโปรแกรมหรือไม่ [y/n] : ')
        if close == 'n' :
            os.system('cls')
        if close == 'y' :
            os.system('cls')
            print('ปิดโปรแกรม')
            break