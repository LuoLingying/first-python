import os
folder = input('请输入文件夹路径：')
files = os.listdir(folder)
fileDic = dict()
for each_file in files:
    fullName = folder + '/' + each_file
    if os.path.isdir(fullName):
        if '文件夹' in fileDic.keys():
            fileDic['文件夹'] += 1
        else:
            fileDic['文件夹'] = 1
    else:
        exts = os.path.splitext(fullName)
        if exts[1] in fileDic.keys():
            fileDic[exts[1]] += 1
        else:
            fileDic[exts[1]] = 1
print('该文件夹下共有：')
for tp in fileDic:
    print('类型为【 %s 】的文件%d个' % (tp, fileDic[tp]))

    
