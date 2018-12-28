import os
keyword = input('请将该脚本放于待查找的文件夹内，请输入关键字：')
answer = input('请问是否需要打印关键字【%s】在文件夹中的具体位置：[yes/no]' % keyword)

def findkey(k, line, ind, num):
    if k in line:
        index = num + line.find(k) + 1
        ind.append(index-1)
        findkey(k, line[line.find(k)+1:], ind, index)
    return ind

def findkeyword(filepath):
    files = os.listdir(filepath)
    for eachfile in files:
        fpath = filepath + '/' + eachfile
        if os.path.isdir(fpath):
            findkeyword(fpath)
        else:
            f = open(fpath)
            i = 0
            flag = 0
            for eachline in f:
                i += 1
                if keyword in eachline:
                    flag += 1
                    if(flag == 1):
                        print('='*75)                        
                        print('在文件【%s】中找到关键字%s' % (os.getcwd() + '/' + eachfile, keyword))
                    inds = findkey(keyword, eachline, [], 0)
                    print('关键字出现在第%d行，第%s个位置' % (i, inds))

if answer == 'yes':
    findkeyword(os.curdir)


