import os
keyword = input('请将该脚本放于待查找的文件夹内，请输入关键字：')
answer = input('请问是否需要打印关键字【%s】在文件夹中的具体位置：[yes/no]' % keyword)

def findkeyword(filepath):
    files = os.listdir(filepath)
    for eachfile in files:
        if os.path.isdir(fullName):
            findkeyword(eachfile)
        else:
            f = open(os.curdir + '/' + eachfile)
            i = 0
            for eachline in f:
                i += 1
                if keyword in eachline:
                    print()

def findkey(k, line, ind, num):
    if k in line:
        index = num + line.find(k) + 1
        ind.append(index-1)
        findkey(k, line[line.find(k)+1:], ind, index)
    return ind
print(findkey('aa', 'aadfefdreeweaawra', [], 0))
