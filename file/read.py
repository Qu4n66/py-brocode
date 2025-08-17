

import json
import csv

file_path = "C:\\Users\\quang\\OneDrive\\Desktop\\py brocode\\file\stuff\\t1.txt"

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('File not found Errorrrr')
    

file_path2 = "C:\\Users\\quang\\OneDrive\\Desktop\\py brocode\\file\\stuff\\output2.json"
with open(file_path2, 'r') as file:
    content2 = json.load(file)
    print(content2["dog"])



file_path3 = "C:\\Users\\quang\\OneDrive\\Desktop\\py brocode\\file\\stuff\\output2.csv"


with open(file_path3, 'r') as file:
    content3 = csv.reader(file)
    for line in content3:
        print(line)
    print(content3)
