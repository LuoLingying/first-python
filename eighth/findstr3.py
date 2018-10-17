def findstr(string, key):
    count = 0
    length = len(string)
    for i in range(length-1):
        if string[i] == key[0]:
            if string[i+1] == key[1]:
                count += 1
    
    return count

string = input('请输入长字符串:')
key = input('请输入查找值:')
print('出现', findstr(string, key), '次')

        