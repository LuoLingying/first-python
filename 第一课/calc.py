snum = input('输一个1-10的数据:')
if snum.isdigit():
    num = int(snum)
    if (1<=num<=10):
        print('漂亮的')
    else:
        print('1-10!!')     
else:
    print('别乱输')
