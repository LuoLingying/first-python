import os
folder = input('请输入文件夹路径：').strip()
files = os.listdir(folder)
for eachfile in files:
    fullName = folder + '/' + eachfile    
    if os.path.isfile(fullName):
        print('%s【 %d Bytes】' % (eachfile, os.path.getsize(fullName)))
