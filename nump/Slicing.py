import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

print(array.ndim)
print('')
print(array[0:4]) #print(everythings in a row)
print('')
print(array[:, 1 ])# print(row, column)
print('')
print(array[:,0:3]) #1 to 3 column
print('')
print(array[2:, 0:2]) #print row and column respectively 