import os
import shutil

path = input("Enter The Name Of the Directory To Be Sorted :-")
listOfFiles = os.listdir(path)
for files in listOfFiles:
    name,ext = os.path.splitext(files)
    ext = ext[1:]
    if ext == '':
        continue
    if os.path.exists(path+'/'+ext): 
        shutil.move(path+'/'+files, path+'/'+ext+'/'+files)
    else: 
       os.makedirs(path+'/'+ext) 
       shutil.move(path+'/'+files, path+'/'+ext+'/'+files)