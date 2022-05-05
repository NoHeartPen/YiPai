import os
from pathlib import Path
import re

#import all2half_number


# 其他字符半角(33-126)与全角(65281-65374)的对应关系是：均相差65248
def All2Half_(AllWideNums):
    HalfWideNumsList = []
    for num in AllWideNums:
        if ord(num) == 65292:  # 全角逗号
            HalfWideNumsList.append(num)
        elif 65281 <= ord(num) <= 65374:
            HalfWideNum = chr(int(ord(num) - 65248))
            HalfWideNumsList.append(HalfWideNum)
        else:
            HalfWideNumsList.append(num)
        HalfWideNums = " ".join(map(str, HalfWideNumsList))
    return HalfWideNums


# aciton\FormatMarkdown.py


def del_slash(inputline):
    if "。\n" in inputline:
        outputline = inputline
    elif "」\n" in inputline:
        outputline = inputline
    elif "”" in inputline:
        outputline = inputline
    else:
        outputline = inputline.replace("\n", "")
    return outputline


path = os.getcwd()
p = Path(path)

InputFileList = list(p.glob("**/*.md"))
for InputFile in InputFileList:
    with open(InputFile, 'r', encoding='UTF-8') as ProcessFile:
        OutputLines = []
        InputLines = ProcessFile.readlines()
        for InputLine in InputLines:
            if InputLine == "\n":  # 删掉空行
                continue
            else:
                OutputLine = re.sub(r"▼$", "。", InputLine)  # 删掉天声人语
                OutputLine = re.sub(r"^\s", "", OutputLine)
                #OutputLine = all2half_number.All2Half_(OutputLine)
                OutputLine = OutputLine.replace(" ", "")
                #OutputLine = format_ocr.del_slash(OutputLine)
                OutputLines.append(OutputLine)

    with open(InputFile, 'w', encoding='UTF-8') as OutPutFile:
        OutPutFile.writelines(OutputLines)
