import numpy as np


ages = np.array([[17,11,12,3,53,23,75,43],
                 [9,5,33,76,48,79,54,34]])
kids = ages[ages < 12]

teens = ages[(ages > 14) & (ages < 18) | (ages < 16) ] # ages > 14 and < 18 or > 16

adults = np.where(ages >= 18, ages, 0) #neu >=18, giu nguyen, false thi tra ve 0
print(kids)
print(adults)
print(teens)



