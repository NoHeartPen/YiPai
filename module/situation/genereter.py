import os
from pathlib import Path
import shutil

# Main
Inputpath = os.getcwd()
p = Path(Inputpath)
ProcessFilePath = Inputpath + '\\.YiPai\\.process' + '\\'


# module\situation\md2md.py
def md2md(InputFile):
    InputFileName = os.path.basename(InputFile)
    ProcessFileName = ProcessFilePath + InputFileName
    shutil.copy(InputFileName, ProcessFileName)
    print("Done")


# Action

p = Path(Inputpath)
FileList = list(p.glob("**/*.md"))
file = (i for i in FileList)
allfile = len(FileList)
for i in range(allfile):
    ProcessFile = next(file)
    md2md(ProcessFile)
    Now = round((i / allfile) * 100)
    Done = '█' * int(Now)
    Undo = '_' * (100 - int(Now))
    print("\r{:^3.0f}%[{}->{}]".format(Now, Done, Undo), end='')