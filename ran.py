import random

cuoc = int(input('Nhap tien cuoc:'))
chon = input('Tai hay Xiu:')
n = ''
xx1 = random.randint(1,6)
xx2 = random.randint(1,6)
xx3 = random.randint(1,6)

kq = xx1 + xx2 + xx3

if kq > 10:
    print(xx1 , xx2 , xx3)
    print(xx1 + xx2 + xx3)
    n = 'Tai'
    if xx1 == xx2 == xx3:
        no = 'NO HU'
        print('Ban no hu roi')
        print(f'So tien ban thang la {3*cuoc}')
    if n == chon.lower():
        print('Ban thang roi')
        print(f'So tien ban thang la: {2*cuoc}')
    else:
        print('Ban thua roi thang ngu')
else:
    print(xx1 , xx2 , xx3)
    print(xx1 + xx2 + xx3)
    print('Xiu')
    n = 'Xiu'
    if xx1 == xx2 == xx3:
        no = 'NO HU'
        print('Ban no hu roi')
        print(f'So tien ban thang la {3*cuoc}')
    if n == chon.lower():
        print('Ban thang roi')
        print(f'So tien ban thang la: {2*cuoc}')
    else:
        print('Ban thua roi thang ngu')
