from pathlib import Path
from docx import Document
import os

# Main
Inputpath = os.getcwd()
p = Path(Inputpath)
ProcessFilePath = Inputpath + '\\.YiPai\\.process' + '\\'


# module\situation\docx2md.py
def docx2md(docx2md_File):
    file = Document(docx2md_File)
    paragraphs = []

    for p in file.paragraphs:  # 读取所有行
        paragraphs.append(p.text + "\n")

    with open("{}.md".format(
            ProcessFilePath +
            os.path.basename(docx2md_File).replace(".docx", "")),
              'w',
              encoding='UTF-8') as OutPutFile:
        OutPutFile.writelines(paragraphs)


# Situation
def Situation():
    docx2md_FileList = list(p.glob("**/*- 副本.docx"))
    for docx2md_File in docx2md_FileList:
        docx2md(docx2md_File)


Situation()