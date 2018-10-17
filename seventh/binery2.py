def num2bin(num):
    '十进制转化为二进制'
    result = ''
    while num:
        yu = num % 2
        num = num // 2
        result += str(yu)

    return result

print(num2bin(5))
print(num2bin.__doc__)
