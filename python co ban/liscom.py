# lis comprehension

'''
normal gain:
double = []
for x in range(1,11):
    double.append(x*2)

print(double)
'''
#list comprehension gain:
#double = [expression(return) for value in 'iterable' if 'condition']
double = [x*2 for x in range(1,11)]
triple = [y*3 for y in range(1,6)]


print(double)
print(triple)



