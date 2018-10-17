def count(*string):
    for i in range(len(string)):
        a = 0
        b = 0
        c = 0
        d = 0
        print('第', i+1, '个字符串共有:', end=' ')
        for each in string[i]:
            if each.isalpha():
                a += 1
            elif each.isdigit():
                b += 1
            elif each == ' ':
                c += 1
            else:
                d += 1
        print('英文字符', a, '个, 数字', b, '个, 空格', c, '个, 其他字符', d, '个.')

count('I love fishc.com.', 'I love you, you love me')