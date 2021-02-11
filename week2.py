
a = input('Input First Number : ')
b = input('Input Second Number : ')
print(a,'=',b,a==b)
print(a,'<',b,a<b)
print(a,'>',b,a>b)

'''
a = 60
b = 13
c = 0

c = a & b
print(c)

c = a | b
print(c)

c = ~a
print(c)

c = a << 2
print(c)

c = a >> 2
print(c)
'''

print('Day Converter Program')
a = int (input('Input number of Days : '))
print(a,'Days --> Hour',a*24,'Hours')
print(a,'Days --> Minutes',a*24*60,'Minutes')
print(a,'Days --> Seconds',a*24*60*60,'Seconds')

'''  
friend=['jan','cream','phu','bam','aom','pee','bas','kong','da','james']
friend.append('dome')
friend.append('poondang')
friend.insert(1,'csa')
friend.insert(8,'ped')
friend.remove('aom')
friend.pop()
friend.pop(3)
del friend[7]
friend.clear()
del friend
print(friend)
'''
'''
animal={'cat','dog','rat','pig','ant'}
animal.add('monkey')
animal.update(['python','capibara','spider','wombat','penguin','crocodile'])
print(animal)
'''

print('ตะกร้าใส่ของ')
a = input('สินค้าชิ้นที่ 1 : ')
b = input('สินค้าชิ้นที่ 2 : ')
c = input('สินค้าชิ้นที่ 3 : ')
d = input('สินค้าชิ้นที่ 4 : ')
e = input('สินค้าชิ้นที่ 5 : ')
print('สินค้าที่หยิบใส่ตะกร้า')
bucket=[a,b,c,d,e]
print('สินค้าชิ้นที่ 1 : ',bucket[0])
print('สินค้าชิ้นที่ 2 : ',bucket[1])
print('สินค้าชิ้นที่ 3 : ',bucket[2])
print('สินค้าชิ้นที่ 4 : ',bucket[3])
print('สินค้าชิ้นที่ 5 : ',bucket[4])

price = [[25,30,45,55,60],[45,45,75,90,100],[60,70,110,130,140]]
car = ['4 ล้อ','6 ล้อ','มากกว่า 6 ล้อ']
print('โปรแกรมคำนวณค่าผ่านทางมอเตอร์เวย์')
print('*'*29)
print('รถยนต์ 4 ล้อ\t\tกด 1')
print('รถยนต์ 6 ล้อ\t\tกด 2')
print('รถยนต์มากกว่า 6 ล้อ\t กด 3')
a = int(input('เลือกประเภทยานพาหนะ : '))
print('\t\t   = รถยนต์ '+car[a-1])
print('\tค่าบริการรถยนต์')
print('-'*29)
print('ลาดกะบัง --> บางบ่อ     '+str(price[a-1][0])+' บาท')
print('ลาดกะบัง --> บางประกง  '+str(price[a-1][1])+' บาท')
print('ลาดกะบัง --> พนัสนิคม    '+str(price[a-1][2])+' บาท')
print('ลาดกะบัง --> บ้านบึง     '+str(price[a-1][3])+' บาท')
print('ลาดกะบัง --> บางพระ    '+str(price[a-1][4])+' บาท')
