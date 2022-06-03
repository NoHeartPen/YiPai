import os
from pathlib import Path

os.chdir('D:\#Temp\RWS实习\PDF')

ProcessFilePath = os.getcwd()

p = Path(ProcessFilePath)
FileList = list(p.glob("**/*.pdf"))

FileListNumber = len(FileList)

'''
def YieldProcessFile(FileList):
    print(FileList)
    for file in FileList:
        yield file
'''

file = (i for i in FileList) #这种要怎么才能进行遍历呢

print(file) # 不使用next激活的话，返回的是一个generate对象
'''
for i in range(len(FileList)):
    print(next(file))
'''
