import os

file_path = 'C:/Users/quang/OneDrive/Desktop/py brocode/file/stuff/text1.txt'

if os.path.exists(file_path):
    print(f"The location ' {file_path} 'exists")
    if os.path.isfile(file_path):
        print('That is a file')

else:
    print('That Location Doesn\'t exist ')