def mybin(x):
    if x==0:
        res = '0'
    elif x ==1:
        res = '1'
    else:
        res = str(mybin(x//2)) + str(x%2)
    return res

num = int(input('please input a num:'))
print(mybin(num)) 