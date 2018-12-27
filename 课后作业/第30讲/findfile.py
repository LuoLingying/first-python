import os
folder = input('请输入待查找的初始文件夹路径：')
fil = input('请输入需要查找的目标文件：')
def findfile(folder, fil):
    files = os.listdir(folder)
    for eachfile in files:
        if fil == eachfile:
            print(folder + '/' + fil)
        elif os.path.isdir(folder + '/' + eachfile):
            findfile(folder + '/' + eachfile, fil)
findfile(folder, fil)

