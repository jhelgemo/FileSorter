import os
import shutil
import re


username = os.getlogin()
path = "C:/Users/" + username + "/Downloads/"
fileList = os.listdir(path)
folder_names = ["Text Files", "Executables", "Compressed Files", "Images", "Excel Files", "Pdf Files"]
compressedFilesRegExp = re.compile(r'\.(zip|rar)$',re.IGNORECASE)
executablesRegExp = re.compile(r'\.(exe|msi)$',re.IGNORECASE)
textFilesRegExp = re.compile(r'\.(txt|doc(x)?)$',re.IGNORECASE)
imagesRegExp = re.compile(r'\.(jp(e)?g|png|tiff)$',re.IGNORECASE)
excelFilesRegExp = re.compile(r'\.(xlsx|xlsm)$',re.IGNORECASE)
pdfFilesRegExp = re.compile(r'\.(pdf)$',re.IGNORECASE)


for i in folder_names:
    if not os.path.exists(path+i):
        os.mkdir(path+i)

for files in fileList:
    if compressedFilesRegExp.search(files) and not os.path.exists(path+"Compressed Files/" + files):
        shutil.move(path+files,path+"Compressed Files/"+files)
    elif executablesRegExp.search(files) and not os.path.exists(path+"Executables/" + files):
        shutil.move(path+files,path+"Executables/"+files)
    elif textFilesRegExp.search(files) and not os.path.exists(path + "Text Files/" + files):
        shutil.move(path + files, path + "Text Files/" + files)
    elif imagesRegExp.search(files) and not os.path.exists(path + "Images/" + files):
        shutil.move(path + files, path + "Images/" + files)
    elif excelFilesRegExp.search(files) and not os.path.exists(path + "Excel Files/" + files):
        shutil.move(path + files, path + "Excel Files/" + files)
    elif pdfFilesRegExp.search(files) and not os.path.exists(path + "Pdf Files/" + files):
        shutil.move(path + files, path + "Pdf Files/" + files)







