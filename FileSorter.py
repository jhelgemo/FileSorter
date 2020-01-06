import os
from os.path import join
import shutil
import re
from datetime import datetime
import threading


def FileSorter():

    username = os.getlogin()
    path = "C:/Users/" + username + "/Downloads/"
    fileList = [x for x in os.listdir(path) if os.path.isfile(join(path,x))]
    folder_names = ["Text Files", "Executables", "Compressed Files", "Images", "Excel Files", "Pdf Files"]

    compressedFilesRegExp = re.compile(r'\.(zip|rar)$', re.IGNORECASE)
    executablesRegExp = re.compile(r'\.(exe|msi)$', re.IGNORECASE)
    textFilesRegExp = re.compile(r'\.(txt|doc(x)?)$', re.IGNORECASE)
    imagesRegExp = re.compile(r'\.(jp(e)?g|png|tiff)$', re.IGNORECASE)
    excelFilesRegExp = re.compile(r'\.(xlsx|xlsm)$', re.IGNORECASE)
    pdfFilesRegExp = re.compile(r'\.(pdf)$', re.IGNORECASE)

    for i in folder_names:
        if not os.path.exists(path+i):
            os.mkdir(path+i)

    for file in fileList:
        if compressedFilesRegExp.search(file) and not os.path.exists(path+"Compressed Files/" + file):
            shutil.move(path+file, path+"Compressed Files/"+file)
        elif compressedFilesRegExp.search(file) and os.path.exists(path+"Compressed Files/" + file):
            os.rename(path + file, path + "duplicate_" + str(datetime.now().strftime("%d%m%Y%H%M%S")) + "_" + file)

        elif executablesRegExp.search(file) and not os.path.exists(path+"Executables/" + file):
            shutil.move(path+file, path+"Executables/"+file)
        elif executablesRegExp.search(file) and os.path.exists(path+"Executables/" + file):
            os.rename(path + file, path + "duplicate_" + str(datetime.now().strftime("%d%m%Y%H%M%S")) + "_" + file)

        elif textFilesRegExp.search(file) and not os.path.exists(path + "Text Files/" + file):
            shutil.move(path + file, path + "Text Files/" + file)
        elif textFilesRegExp.search(file) and os.path.exists(path + "Text Files/" + file):
            os.rename(path + file, path + "duplicate_" + str(datetime.now().strftime("%d%m%Y%H%M%S")) + "_" + file)

        elif imagesRegExp.search(file) and not os.path.exists(path + "Images/" + file):
            shutil.move(path + file, path + "Images/" + file)
        elif imagesRegExp.search(file) and os.path.exists(path + "Images/" + file):
            os.rename(path + file, path + "duplicate_" + str(datetime.now().strftime("%d%m%Y%H%M%S")) + "_" + file)

        elif excelFilesRegExp.search(file) and not os.path.exists(path + "Excel Files/" + file):
            shutil.move(path + file, path + "Excel Files/" + file)
        elif excelFilesRegExp.search(file) and os.path.exists(path + "Excel Files/" + file):
            os.rename(path + file, path + "duplicate_" + str(datetime.now().strftime("%d%m%Y%H%M%S")) + "_" + file)

        elif pdfFilesRegExp.search(file) and not os.path.exists(path + "Pdf Files/" + file):
            shutil.move(path + file, path + "Pdf Files/" + file)
        elif pdfFilesRegExp.search(file) and os.path.exists(path + "Pdf Files/" + file):
            os.rename(path + file, path + "duplicate_" + str(datetime.now().strftime("%d%m%Y%H%M%S")) + "_" + file)

    threading.Timer(10,FileSorter).start()
FileSorter()



















