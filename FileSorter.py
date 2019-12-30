import os


username = os.getlogin()
path = "C:/Users/" + username + "/Downloads/"
fileList = os.listdir(path)

for files in fileList:
    print(files)





