import os
path=input("enter a path: ")
filecount=0
dircount=0
for dirpath, dirnames, filenames in os.walk(path):
    print("searching:",dirpath)
    for dirnames in path:
        dircount=dircount+1
    for filenames in path:
        filecount=filecount+1

print("no of files:", filecount)
print("no of directories:",dircount)
 
