import os
folder = input('请输入待查找的初始文件夹路径：')
def findVideo(folder):
    files = os.listdir(folder)
    for eachfile in files:
        fullName = folder + '/' + eachfile
        if os.path.isdir(fullName):
            findVideo(fullName)
        else:
            exts = os.path.splitext(fullName)
            if exts[1] in ['.mp4', '.rmvb', '.avi', '.zip']:
                print(fullName)
findVideo(folder)

