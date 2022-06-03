import os
from pathlib import Path

# Main
Inputpath = os.getcwd()
p = Path(Inputpath)
ProcessFilePath = Inputpath + '\\.YiPai\\.process' + '\\'


file = (i for i in ProcessFileList) # 注意，这里返回的是一个生成器对象
allfile = len(ProcessFileList)
for i in range(allfile):
    ProcessFile = next(file)
    Now = round((i / allfile) * 100)
    Done = '█' * int(Now)
    Undo = '_' * (100 - int(Now))
    print("\r{:^3.0f}%[{}->{}]".format(Now, Done, Undo), end='')
print("恭喜！文件转换完毕")


# Action
def Action():
    p = Path(ProcessFilePath)
    FileList = list(p.glob("**/*.md"))
    for file in FileList:
        formatmd(file)


Action()
