#.txt (text), .json(key:value), .csv(excel)


import json
import csv
animals_speak = [['name','age','job'],
                 ['bu',18,'president'],
                 ['bao',17,'bus'],
                 ['bff',18,'cu']]

file_path = "output2.csv"

#w for override
#x for write file didn't exist
#a for append new data
try:
    with open(file_path,'w', newline= '') as file:
        writer = csv.writer(file)
        for row in animals_speak:
            writer.writerow(row)
        print(f"csv file {file_path} was created")
except FileExistsError:
    print('That file is already exists')


'''
with open(file_path, 'a' ) as file:
    json.dump(animals_speak, file)
    print(f'json file {file_path} was created ')
    '''