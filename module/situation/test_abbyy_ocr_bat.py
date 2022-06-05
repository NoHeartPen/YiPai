from importlib import import_module
'''
具体的参数官网的手册
https://help.abbyy.com/zh-cn/finereader/15/user_guide/commandline/
'''

import os

programpath = 'D:/03Program/ABBYY/ABBYY FineReader 15/FineReaderOCR.exe'  # /一个反斜杠
filepath = 'D:/Document/03Code/02Python/demand_oriented_programming/vbs/pdf2excel/50173 representation_ invoice-OPPO - 副本.pdf'
lang = '/lang English'
commandtext = '"' + '"' + programpath + '" ' + '"' + filepath + '" ' + lang + '"'
print(commandtext)
os.system(commandtext)