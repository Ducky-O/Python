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