#แบบฝึกหัดที่1
print('\tเลือกเมนูเพื่อทำรายการ')
print('#'*35) 
x = int(input('กด 1 เลือกจ่ายเพิ่ม\nกด 2 เลือกเหมาจ่าย\n'))
if x == 1 :
    y = int(input('กรุณากรอกระยะทาง : '))
    if y < 25 :
        print('ค่าใช้จ่าย รวมทั้งหมด 25 บาท')
    elif y >= 25 :
        print('ค่าใช้จ่าย รวมทั้งหมด 55 บาท')
if x == 2:
    y = int(input('กรุณากรอกระยะทาง : '))
    if y < 25 :
        print('ค่าใช้จ่าย รวมทั้งหมด 25 บาท')
    elif y >= 25 :
        print('ค่าใช้จ่าย รวมทั้งหมด 80 บาท')

#แบบฝึกหัดที่2
i = 1
sum = 0
x = int(input('กรุณากรอกจำนวนครั้งการรับค่า : '))
while(i <= x) :
    y = int(input('กรอกตัวเลข : '))
    sum +=y
    i +=1
print('ผลรวมที่รับค่ามาทั้งหมด = ',sum)

#แบบฝึกหัดที่3
i = 1
foodlist = []
print('ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม')
while (True) :
    food = input('อาหารโปรดอันดับที่ '+str(i)+' คือ : ')
    foodlist.append(food)
    if (food == 'exit') :
        break
    i +=1
foodlist.pop()
print('อาหารสุดโปรดของคุณมีดังนี้ : ')
for x in range (1,i) :
    print(x,'',foodlist[x-1],end = ' ')

a=[]
while (True) :
    b = input('---ร้านเครื่องดนตรีเป็ดโปร---\n เพิ่ม [a]\nแสดง [s]\nออกจากระบบ [x]\n')
    b = b.lower()
    if b == 'a' :
        c = input('ป้อนรายชื่อลูกค้า(รหัส:ชื่อ:จังหวัด)')
        a.append(c)
        print('\n*****ข้อมูลได้เข้าสู่ระบบแล้ว*****\n')
    elif b == 's':
        print('{0:-<6}{0:-<10}{0:-<10}'.format(''))
        print('{0:-<8}{1:-<10}{2:10}'.format('รหัส','ชื่อ','จังหวัด'))
        print('{0:-<6}{0:-<10}{0:-<10}'.format(''))
        for d in a :
            e = d.split(':')
            print('{0[0]:<6}{0[1]:<10}{0[2]:<10}'.format(e))
            continue
    elif b == 'x' :
        break
print('ทำคำสั่งถัดไป')

student = int(input('please enter student :'))
print('-'*30)
total = [0 , 0 , 0 , 0 , 0 , 0]
score = ['90-100 :','80-89 :','70-79 :','60-69 :','50-59 : ','0-49 :']
x = 1
while x <= student :
    point = int(input('please enter score :'))
    if point <= 100 and point >= 90 :
        total[0] += 1
    elif point < 90 and point >= 80 :
        total[1] += 1
    elif point < 80 and point >= 70 :
        total[2] += 1
    elif point < 70 and point >= 60 :
        total[3] += 1
    elif point < 60 and point >= 50 :
        total[4] += 1
    elif point < 50 and point >= 0 :
        total[5] +=1
    x = x+1
for x in range(0,6) :
    print(score[x],'*'*total[x])
