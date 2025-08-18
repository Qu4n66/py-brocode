import numpy as np

#scalar arithmetic ( vo huong)
array = np.array([1,2,3])

print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5)
print('')
print('')
print('')
#vectorized math funcs

array2 = np.array([1.5,2.6,3.9])

print(np.sqrt(array))
print(np.round(array)) 
print(np.pi)
print('')
print('')
print('')

#combine 2 section above
radius = array
print(np.pi * radius ** 2) # area of square
print('')
print('')
print('')

#element-wise arithmetic
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 ** array2)
print('')
print('')
print('')
#comparison operators

score = np.array([7.5,8,6.75,10])
score[score > 5] = 8
print(score)

