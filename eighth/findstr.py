def findstr(sstr, fd):
    '该函数统计一个长度为 2 的子字符串在另一个字符串中出现的次数。'
    '例如：假定输入的字符串为'
    '“You cannot improve your past, but you can improve your future. Once time is wasted, life is wasted.”'
    '子字符串为“im”，函数执行后打印“子字母串在目标字符串中共出现 3 次”。'
    flag = 0
    num = -1
    while flag >= 0:
        flag = sstr.find(fd, flag+1)
        num += 1
    
    print('子字母串在目标字符串中共出现', num, '次')

findstr(sstr='You cannot improve your past, but you can improve your future. Once time is wasted, life is wasted.', fd='im')