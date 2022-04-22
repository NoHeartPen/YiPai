import os
from pathlib import Path

# Main
Inputpath = os.getcwd()
p = Path(Inputpath)


## result\moveoutput.py
def moveoutput(file):
    oldname = os.path.abspath(file)
    newname = os.path.abspath(oldname).replace(".YiPai\.process", "")
    shutil.move(oldname, newname)


# Result
def Result():
    ProcessFilePath = Inputpath + '\\' + '.YiPai\\.process' + '\\'
    p = Path(ProcessFilePath)
    FileList = list(p.glob("**/*"))
    for file in FileList:
        # 如果勾选了MD那么就必须
        moveoutput(file)


Result()