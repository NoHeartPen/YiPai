'''
只在单一文件转换时启用该功能，另外尤其注意Windows的路径中包含空格时的处理方法
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
        filepath = '"' + os.path.abspath(
            File) + '"'  # 防止路径中的空格造成干扰，必须要把路径用""包裹起来
        programpath = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"  # 请注意，这里必须使用r指定为原生字符串，否则无法正确解析地址
        windowspath = '"' + programpath + '"' + ' ' + filepath
        command = '"' + windowspath + '"'  # 要正确解析命名，必须再用""包裹一次
        os.system(command)


Open()
