import os
from os.path import join, getsize, isfile, isdir, splitext
def GetFolderSize(path):
    TotalSize = 0
    for item in os.walk(path):
        for file in item[2]:
            try:  ## add path root + file name
                TotalSize = TotalSize + getsize(join(item[0], file))
            except:
                print("error with file:  " + join(item[0], file))
    return TotalSize

print(float(GetFolderSize("C:\\")) /1024 /1024 /1024)
