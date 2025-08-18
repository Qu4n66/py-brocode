


import numpy as np



array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                  [['J','K','L'],['M','N','O'],['P','Q','R']],
                  [['S','T','U'],['V','W','X'],['Y','Z',' ']]])


print(array.ndim)
print(array.shape) #(layer,row, column)
word = array[0,0,2] + array[0,0,0] + array[0,0,2]
print(word)