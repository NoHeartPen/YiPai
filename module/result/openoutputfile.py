'''
只在单一文件转换时启用该功能
'''

import os
from pathlib import Path

# Main
Inputpath = os.getcwd()
p = Path(Inputpath)
ProcessFilePath = Inputpath + '\\.YiPai\\.process' + '\\'


# Situation
def Open():
    FileList = list(p.glob("**/*- 副本.docx"))
    for File in FileList:
        filename = "\""+os.path.abspath(File)+"\""
        command = r'"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE" ' +filename
        print(command)
        os.system(command)

Open()