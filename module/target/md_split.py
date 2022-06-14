import os
from pathlib import Path

# Main
Inputpath = os.getcwd()
p = Path(Inputpath)
ProcessFilePath = Inputpath + '\\.YiPai\\.process' + '\\'


# module\target\md_split.py
def Split(file):
    with open(file, 'r', encoding='UTF-8') as ProcessFile:
        FileTxt = ProcessFile.read()
        ProcessFile.close()
        InputLines = FileTxt.split('\n')
        wordcount = 0
        SplitStand = 800  # 分割标准
        SplitTime = 1  # 分割次数
        SplitCount = 800  # 分割时的字数，初始值
        OutputLines = []
        for InputLine in InputLines:
            wordcount += len(InputLine)

            if InputLine == '':
                continue

            if wordcount > SplitCount:  # 比较字数和分割标准
                OutputLine = InputLine + "\n\n# " + str(SplitCount)
                SplitTime += 1
                SplitCount = SplitStand * SplitTime  # 计算下一次分割标准
            else:
                OutputLine = InputLine
            OutputLines.append(OutputLine + "\n\n")
    with open(file, 'w', encoding='UTF-8') as OutPutFile:
        OutPutFile.writelines(OutputLines)
    OutPutFile.close()


# module\target\md_split.py
def TargetMD():
    p = Path(ProcessFilePath)
    FileList = list(p.glob("**/*.md"))
    for file in FileList:
        Split(file)


TargetMD()
