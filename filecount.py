import os
path=input("enter a path: ")
files=os.listdir(path)
print(files)
filecount=len(os.listdir(path))
print(filecount)
