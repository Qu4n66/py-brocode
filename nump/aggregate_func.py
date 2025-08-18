import numpy as np

array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

print(np.min(array))
print(np.sum(array))
print(np.std(array)) #do lech chuan
print(np.var(array)) # phuong sai
print(np.mean(array) ) # so trung binh
print(np.argmin(array)) # index cua min

print(np.sum(array, axis=0)) # cong theo cot
print(np.sum(array, axis=1)) # cong theo hang

