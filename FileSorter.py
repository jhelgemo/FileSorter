import os
import shutil


username = os.getlogin()
path = "C:/Users/" + username + "/Downloads/"
fileList = os.listdir(path)
folder_name = ['Text Files', 'Executables', 'Zip Files']

for i in range(0,3):
    if not os.path.exists(path+folder_name[i]):
        os.mkdir(path+folder_name[i])

for files in fileList:
    if ".zip" in files and not os.path.exists(path+"Zip Files/"+files):
        shutil.move(path+files,path+"Zip Files/"+files)
    if ".exe" in files or ".msi" in files and not os.path.exists(path+"Executables/"+files):
        shutil.move(path+files,path+"Executables/"+files)
    if ".txt" in files or ".docx" in files and not os.path.exists(path + "Text Files/" + files):
        shutil.move(path + files, path + "Text Files/" + files)






