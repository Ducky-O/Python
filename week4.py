'''import os
choice = 0
filename = ''

def menu():
    global choice
    print('Menu\n 1.Open Microsoft Excel\n 2.Open Microsoft Word\n 3.Open Microsoft Powerpiont\n 4.Exit ')
    choice = input('Select Menu : ')

def openexcel():
    filename = '"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"'
    print('Excel Typing %s' %filename)
    os.system(filename)

def openword():
    filename = '"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"'
    print('Microsoft Word %s' %filename)
    os.system(filename)


while True:
    menu()
    if choice == '1':
        openexcel()
    elif choice == '2':
        openword()
    else:
        break
'''
#แบบฝึกหัดที่1
choice = 0
bucket_list = []
bucket = [0,0,0,0,0]
price = [19,18,17,16,15]
def brandandprice():
    print(' 1.โค้ก= 19 บาท\n 2.เป๊ปซี่ = 18 บาท\n 3.แฟนต้า = 17 บาท\n 4.สไปร์ท = 16 บาท\n 5.เอสโคล่า = 15 บาท')
def buy():
    a = 0
    while True :
        print(' 1.โค้ก\t\t2.เป๊ปซี่\n 3.แฟนต้า\t4.สไปร์ท\n 5.เอสโคล่า\t6.หยุดเลือกซื้อ')
        a = (input('เลือกเลขน้ำอัดลมที่ต้องการซื้อ : \n'))
        try :
            if int(a)==1 or a==1:
                bucket_list.append('โค้ก')
            elif int(a)==2 or a==2:
                bucket_list.append('เป๊ปซี่')
            elif int(a)==3 or a==3:
                bucket_list.append('แฟนต้า')
            elif int(a)==4 or a==4:
                bucket_list.append('สไปร์ท')
            elif int(a)==5 or a==5:
                bucket+list.append('เอสโคล่า')
            elif int(a)==6 or a==6:
                break
            else:
                print('กรุณากรอกหมายเลขให้ถูกต้อง')
        except:
            print('กรุณากรอกหมายเขให้ถูกต้อง : ')
            pass
def out():
    n=0
    while (True):
        print('สินค้าในตะกร้ามีดังนี้')
        for i in bucket_list:
            n+=1
            print('\t'+str(n)+'.'+i)
        n=0
        c=int(input('เลือกหมายเลขที่ต้องการหยิบสินค้าออก หรือพิมพ์ -1 เพื่อยกเลิกหยิบออก : '))
        try:
            if c<=len(bucket_list) and c!=-1:
                bucket_list.pop(c-1)
            elif c==0 and c<=len(bucket_list) and c!=-1:
                bucket_list.pop(c)
            elif c==-1:
                break
        except:
            print('กรุณากรอกหมายเลขให้ถูกต้อง : ')
def item():
    for i in bucket_list:
        if i == 'โค้ก':
            bucket[0]+=1
        elif i == 'เป๊ปซี่':
            bucket[1]+=1
        elif i == 'แฟนต้า':
            bucket[2]+=1
        elif i == 'สไปร์ท':
            bucket[3]+=1
        elif i == 'เอสโคล่า':
            bucket[4]+=1
    buckettt=bucket[0]+bucket[1]+bucket[2]+bucket[3]+bucket[4]
    pricett=bucket[0]*19+bucket[1]*18+bucket[2]*17+bucket[3]*16+bucket[4]*15
    print('')
    print('{0:_<10}{1}{0:_<12}'.format('','สินค้าที่คุณหยิบใส่ตะกร้า'))
    print('{0:_<6}{1}{0:_<6}{2}{0:_<5}{3}{0:_<10}'.format('','สินค้า','จำนวน','ราคา'))
    print('{0:_<40}'.format(''))
    if bucket[0]!=0:
        print('{0:_<6}{1}{0:_<9}{2}{0:_<8}{3}{0:_<10}'.format('','โค้ก',str(bucket[0]),str(bucket[0]*19)))
    if bucket[1]!=0:
        print('{0:_<6}{1}{0:_<8}{2}{0:_<8}{3}{0:_<10}'.format('','เป๊ปซี่',str(bucket[1]),str(bucket[1]*18)))
    if bucket[2]!=0:
        print('{0:_<6}{1}{0:_<7}{2}{0:_<8}{3}{0:_<10}'.format('','แฟนต้า',str(bucket[2]),str(bucket[2]*17)))
    if bucket[3]!=0:
        print('{0:_<6}{1}{0:_<7}{2}{0:_<8}{3}{0:_<10}'.format('','สไปร์ท',str(bucket[3]),str(bucket[3]*16)))
    if bucket[4]!=0:
        print('{0:_<6}{1}{0:_<7}{2}{0:_<8}{3}{0:_<10}'.format('','เอสโคล่า',str(bucket[4]),str(bucket[4]*15)))
    print('{0:_<40}'.format(''))
    print('{0:_<6}{1}{0:_<8}{2}{0:_<9}{3}{0:_<10}'.format('','รวม',str(buckettt),str(pricett)))
    print('')
print('โปรแกรมซื้อของ')
while (True):
    print('1. แสดงสินค้าและราคาสินค้า')
    print('2. ซื้อสินค้า')
    print('3. หยิบสินค้าออก')
    print('4. แสดงรายการสินค้า')
    print('5. ปิดโปรแกรม')
    choice = input('เลือกหมายเลขที่ต้องการทำรายการ : ')
    if choice == '1':
        brandandprice()
    elif choice == '2':
        buy()
    elif choice == '3':
        out()
    elif choice == '4':
        item()
    else :
        break

'''
def Introduce(arg1, arg2 = 'com' , arg3 = 'ed' , arg4 = 'kku') :
    print('Hello, I am '+arg1+', '+arg2+' '+arg3+' '+arg4)
Introduce('Python')
Introduce(arg1 = 'Python')
Introduce(arg1 = 'Python', arg3 = 'sci')
Introduce('Python',arg4 = 'CMU')
'''
#แบบฝึกหัดที่2
choice=0
i=5
dictionary = {
    'advise':'{0:<15}{1:<15}'.format('n.','คำแนะนำ'),
    'born':'{0:<15}{1:<15}'.format('n.','เกิด'),
    'can':'{0:<15}{1:<15}'.format('v.','สามารถ'),
    'donate':'{0:<15}{1:<15}'.format('v.','บริจาค'),
    'enough':'{0:<15}{1:<15}'.format('adj.','พอ'),
}
def menu():
    global choice
    print('_'*25+'\nพจนานุกรม\n'+'_'*25+'\n 1.เพิ่มคำศัพท์\n 2.แสดงคำศัพท์\n 3.ลบคำศัพท์\n 4.ออกจากโปรแกรม\n'+'-'*25)
    choice = input('เลือกหัวข้อ : ')
def add():
    print('เพิ่มคำศัพท์')
    print('-'*30)
    a = input('ป้อนคำศัพท์ที่จะเพิ่ม : ')
    b = input('ชนิดของคำศัพท์(n.,v.,adj.,adv.) : ')
    c = input('ความหมาย : ')
    dictionary[a]='{0:<15}{1:<15}'.format(b,c)
    print('*'*15+'\nเพิ่มคำศัพท์เรียบร้อยแล้ว\n'+'*'*15)
def show():
    print('-'*30,'\n\tคำศัพท์ทั้งหมด',i,'คำ\n'+'*'*30)
    print('{0: <15}{1: <15}{2: <15}'.format('คำศัพท์','ประเภท','ความหมาย'))
    print('-'*35)
    for k,v in dictionary.items():
        print('{0:<15}{1:<15}'.format(k,v))
def delete():
    remove = input('พิมพ์คำศัพท์ที่ต้องการลบ : ')   
    x = input('ต้องการลบ'+remove+'ใช่หรือไม่ (y/n) : ')
    if x=='y':
        dictionary.pop(remove)
        print('ลบ',remove,'เรียบร้อยแล้ว')
    elif x=='n':
        print('')
while True : 
    menu()
    if choice=='1':
        add()
        i+=1
    elif choice=='2':
        show()
    elif choice=='3':
        delete()
        i-=1
    else:
        exitt=input('ต้องการออกจากโปรแกรมใช่หรือไม่ (y/n) : ')
        if exitt=='y':
            break
        elif exitt=='n':
            continue

#แบบฝึกหัดที่3
import time
name = []
score = []
timing = []
hits = []
def time_():
    timeis = time.localtime()
    a = time.strftime('%d %B %Y, %H:%M:%S',timeis)
    print(a)
num = int(input('กรุณาพิมพ์จำนวนผู้ซ้อมยิงปืน : '))
for i in range(num):
    print('ป้อนข้อมูลคนที่ ',1+i)
    n = input('ชื่อผู้ซ้อม : ')
    s = float(input('คะแนน : '))
    t = float(input('ระยะเวลาที่ใช้ : '))
    name.append(n)
    score.append(s)
    timing.append(t)
    hits.append(s/t)
for i in range(num):
    j = i
    for j in range(num):
        if hits[i] > hits[j]:
            a,b,c,d = hits[i],name[i],score[i],timing[i]
            hits[i],name[i],score[i],timing[i] = hits[j],name[j],score[j],timing[j]
            hits[j],name[j],score[j],timing[j] = a,b,c,d
timeis = time.localtime()
a = time.strftime('%A',timeis)
b = time.strftime('%Y',timeis)
print('Shortgun '+a+' Training',b,'\nCondtion : 1')
time_()
print('-'*77)
print('{0:-<6}{1:-<6}{2:-<8}{3:-<17}{4:-<12}{5:-<15}{6}'.format('NO.','PTS','TIME','COMPETITOR#Name','HIT FACTOR','STATE POINTS','STATE PRECENT'))
print('-'*77)
for i in range(num):
    stawe_po = (hits[i]/hits[0])*50
    stawe_pe = (stawe_po/(hits[0]/hits[0]*50))*100
    print('{0:<6}{1:<6}{2:<8}{3:<17}{4:<12}{5:<15}{6}'.format(i+1,int(score[i]),int(timing[i]),name[i],'%.4f'%hits[i],'%.4f'%stawe_po,'%.2f'%stawe_pe))
