import os
from pathlib import Path
import shutil

# Main
Inputpath = os.getcwd()
p = Path(Inputpath)
ProcessFilePath = Inputpath + '\\.YiPai\\.process' + '\\'


## result\moveoutput.py
def moveoutput(file):
    oldname = os.path.abspath(file)
    newname = os.path.abspath(oldname).replace(".YiPai\.process", "")
    shutil.move(oldname, newname)


# Result
def Result():
    p = Path(ProcessFilePath)  # 请注意，这里的路径是工作文件夹
    print(p)
    FileList = list(p.glob("**/*"))
    for file in FileList:
        # 如果勾选了MD那么就必须
        moveoutput(file)


Result()