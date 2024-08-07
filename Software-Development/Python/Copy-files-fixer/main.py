import os

fromDir = "D:\\All Jpegs"
fromDirFiles = os.listdir(fromDir)

toDir = "C:\\Users\\cadma\\Downloads"
toDirFiles = os.listdir(toDir)

for x in fromDirFiles:
    if x in toDirFiles:
        print(x, "is in toDirFiles")
    else:
        print(x, "is not in toDirFiles")