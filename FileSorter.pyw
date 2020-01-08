import os
from os.path import join
import shutil
import re
from datetime import datetime
import threading


def FileSorter():

    username = os.getlogin()
    path = "C:/Users/" + username + "/Downloads/"
    fileList = [x for x in os.listdir(path) if os.path.isfile(join(path, x))]
    folder_names = ["Text Files", "Executables", "Compressed Files", "Images", "Excel Files", "Pdf Files", "XML Files"]

    compressedFilesRegExp = re.compile(r'\.(zip|rar)$', re.IGNORECASE)
    executablesRegExp = re.compile(r'\.(exe|msi)$', re.IGNORECASE)
    textFilesRegExp = re.compile(r'\.(txt|doc(x)?|log)$', re.IGNORECASE)
    imagesRegExp = re.compile(r'\.(jp(e)?g|png|tiff|eps|psd)$', re.IGNORECASE)
    excelFilesRegExp = re.compile(r'\.(xls(x)?|xlsm|csv)$', re.IGNORECASE)
    pdfFilesRegExp = re.compile(r'\.(pdf)$', re.IGNORECASE)
    XMLFilesRegExp = re.compile(r'\.(xml)$', re.IGNORECASE)

    for i in folder_names:
        if not os.path.exists(path + i):
            os.mkdir(path + i)

    for file in fileList:

        splitFileName = os.path.splitext(file)

        if compressedFilesRegExp.search(file) and not os.path.exists(path + "Compressed Files/" + file):
            shutil.move(path + file, path + "Compressed Files/" + file)
        elif compressedFilesRegExp.search(file) and os.path.exists(path + "Compressed Files/" + file):
            os.rename(path + file,
                      path + "duplicate_" + splitFileName[0] + "_" + datetime.now().strftime("%d-%m-%Y-%H.%M.%S")
                      + splitFileName[1])

        elif executablesRegExp.search(file) and not os.path.exists(path + "Executables/" + file):
            shutil.move(path + file, path + "Executables/" + file)
        elif executablesRegExp.search(file) and os.path.exists(path + "Executables/" + file):
            os.rename(path + file,
                      path + "duplicate_" + splitFileName[0] + "_" + datetime.now().strftime("%d-%m-%Y-%H.%M.%S")
                      + splitFileName[1])

        elif textFilesRegExp.search(file) and not os.path.exists(path + "Text Files/" + file):
            shutil.move(path + file, path + "Text Files/" + file)
        elif textFilesRegExp.search(file) and os.path.exists(path + "Text Files/" + file):
            os.rename(path + file,
                      path + "duplicate_" + splitFileName[0] + "_" + datetime.now().strftime("%d-%m-%Y-%H.%M.%S")
                      + splitFileName[1])

        elif imagesRegExp.search(file) and not os.path.exists(path + "Images/" + file):
            shutil.move(path + file, path + "Images/" + file)
        elif imagesRegExp.search(file) and os.path.exists(path + "Images/" + file):
            os.rename(path + file,
                      path + "duplicate_" + splitFileName[0] + "_" + datetime.now().strftime("%d-%m-%Y-%H.%M.%S")
                      + splitFileName[1])

        elif excelFilesRegExp.search(file) and not os.path.exists(path + "Excel Files/" + file):
            shutil.move(path + file, path + "Excel Files/" + file)
        elif excelFilesRegExp.search(file) and os.path.exists(path + "Excel Files/" + file):
            os.rename(path + file,
                      path + "duplicate_" + splitFileName[0] + "_" + datetime.now().strftime("%d-%m-%Y-%H.%M.%S")
                      + splitFileName[1])

        elif pdfFilesRegExp.search(file) and not os.path.exists(path + "Pdf Files/" + file):
            shutil.move(path + file, path + "Pdf Files/" + file)
        elif pdfFilesRegExp.search(file) and os.path.exists(path + "Pdf Files/" + file):
            os.rename(path + file,
                      path + "duplicate_" + splitFileName[0] + "_" + datetime.now().strftime("%d-%m-%Y-%H.%M.%S")
                      + splitFileName[1])

        elif XMLFilesRegExp.search(file) and not os.path.exists(path + "XML Files/" + file):
            shutil.move(path + file, path + "XML Files/" + file)
        elif XMLFilesRegExp.search(file) and os.path.exists(path + "XML Files/" + file):
            os.rename(path + file,
                      path + "duplicate_" + splitFileName[0] + "_" + datetime.now().strftime("%d-%m-%Y-%H.%M.%S")
                      + splitFileName[1])

    threading.Timer(5, FileSorter).start()


FileSorter()
