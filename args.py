'''
4 types of parameters



1.positional ( how many arguments there are the same parameters)
2.default (arguments can be assigned, stand behind non-default (no assigned))

import time
def count(e,s = 0):
    for x in range(s,e+1):
        print(x)
        time.sleep(1)
    print('done!')

count(5)




3.keyword (allow to assign in call func without need of order)

def heli(hi,tit,fi,la):
    print(f'{hi} {tit} {fi} {la}')

heli('chao',la = 'nigga',tit = 'thang',fi = 'lol')




4.arbitrary
*args = allow to pass multiple non-key arguments (tuple) 

def add(*nums):
    total = 0 
    for arg in nums:
        total += arg
    return total

print(add(1,2,3,4,5))




**kargs = allow to pass multiple keyword-arguments (dict)
def add(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}:{value }')


add(dog ='sam' ,
    cat ='simy',
    dino ='sarus',
    fish ='nemo' )




'''
#default


def order(*args, **kwargs):
    for arg in args:# ==> iterables
        print(arg, end=' ')
    print()

    if 'numb' in kwargs:  # ==> membership operators ( in, not in)
        print(f"{kwargs.get('numb')}")

    for value in kwargs.values():
        print(value, end=' ')


order('Bo','Bu','Nguyen','I',
      street = 'nha ngoai',
      numb = 113,
      city = 'Bien hoa',
      state = 'cali')


