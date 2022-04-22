from docx2pdf import convert
import os
from pathlib import Path

# Main
Inputpath = os.getcwd()
p = Path(Inputpath)


def printdocx2pdf(file):
    InputFileName = os.path.basename(file)
    ProcessFileName = r".YiPai\.process\{}".format(InputFileName).replace(
        "docx", "pdf")
    ProcessFile = open(ProcessFileName, 'w').close()
    convert(file, ProcessFileName)


ProcessFilePath = os.getcwd() + '\\.YiPai\\.process' + '\\'
p = Path(ProcessFilePath)
FileList = list(p.glob("**/*.docx"))
for file in FileList:
    printdocx2pdf(file)