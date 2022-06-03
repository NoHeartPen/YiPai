import time

scale = 6000

print('开始')
starttime = time.clock()
with open ('新建 文本文档.txt','r',encoding='UTF-8') as file:
    filetext = file.readall()
    scale = len(filetext)
    percent = 100
    per = scale//percent
    for i in range 