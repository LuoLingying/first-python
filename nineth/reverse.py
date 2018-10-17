def reverse(string):
    return string[::-1]

speak = input('请输入一句话:')
rspeak = reverse(speak)

if speak == rspeak:
    print('是回文联')
else:
    print('不是回文联')
