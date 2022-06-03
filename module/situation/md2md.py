from pathlib import Path
import os
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


# MDSituation
def MDSituation():
    md2md_FileList = list(p.glob("**/*- 副本.md"))
    for md2md_File in md2md_FileList:
        md2md(md2md_File)


MDSituation()