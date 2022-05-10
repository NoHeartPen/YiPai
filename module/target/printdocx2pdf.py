from docx2pdf import convert 
import os
from pathlib import Path

# Main
Inputpath = os.getcwd()
p = Path(Inputpath)
ProcessFilePath = Inputpath + '\\.YiPai\\.process' + '\\'

# module\target\printdocx2pdf.py
def printdocx2pdf(file):
    InputFileName = os.path.basename(file)
    ProcessFileName = r".YiPai\.process\{}".format(InputFileName).replace(
        "docx", "pdf")
    ProcessFile = open(ProcessFileName, 'w')
    ProcessFile.close()
    convert(file, ProcessFileName
            )  # 注意file的数据类型是pathlib.WindowsPath，而ProcessFileName是字符串


def Print():
    p = Path(ProcessFilePath)
    FileList = list(p.glob("**/*.docx"))
    for file in FileList:
        printdocx2pdf(file)

Print()
