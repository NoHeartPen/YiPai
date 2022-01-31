from pathlib import Path
from docx import Document
import os

path = os.getcwd()
p = Path(path)

docx2md_FileList = list(p.glob("**/*.docx"))
for docx2md_File in docx2md_FileList:
    file = Document(docx2md_File)
    paragraphs = []

    for p in file.paragraphs:  # 读取所有行
        paragraphs.append(p.text + "\n")

    while paragraphs.count("\n") != 0:  # 删掉多余的空行，可以考虑后面统一处理
        paragraphs.remove("\n")

    with open("{}.md".format(
            os.path.basename(docx2md_File).replace(".docx", "")),
              'w',
              encoding='UTF-8') as OutPutFile:
        OutPutFile.writelines(paragraphs)
