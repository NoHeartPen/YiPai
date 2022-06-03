import os
from pathlib import Path

# Main
Inputpath = os.getcwd()
p = Path(Inputpath)
ProcessFilePath = Inputpath + '\\.YiPai\\.process' + '\\'


def split(file):
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

            if InputLine == '':
                continue

            if wordcount > SplitCount:  # 比较字数和分割标准
                wordcount += len(InputLine)
                OutputLine = InputLine + "\n\n# " + str(SplitCount)
                SplitTime += 1
                SplitCount = SplitStand * SplitTime  # 计算下一次分割标准
            else:
                wordcount += len(InputLine)
                OutputLine = InputLine
            OutputLines.append(OutputLine + "\n\n")
    with open(file, 'w', encoding='UTF-8') as OutPutFile:
        OutPutFile.writelines(OutputLines)
    OutPutFile.close()


# Action
def Action():
    p = Path(ProcessFilePath)
    FileList = list(p.glob("**/*.md"))
    for file in FileList:
        split(file)


Action()
