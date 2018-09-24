str1 = '123'
str2 = 'abc'
str3 = '123abc'

print('--------isalnum()--------')
print(str1.isalnum())
print(str2.isalnum())
print(str3.isalnum())

print('--------isdigit()--------')
print(str1.isdigit())
print(str2.isdigit())
print(str3.isdigit())

print('--------isalpha()--------')
print(str1.isalpha())
print(str2.isalpha())
print(str3.isalpha())


'''
--------isalnum()--------
True
True
True
--------isdigit()--------
True
False
False
--------isalpha()--------
False
True
False

isalnum()是不是没用
'''

'''
课后新添
s 为字符串

s.isalnum()  所有字符都是数字或者字母，为真返回 True，否则返回 False。

s.isalpha()   所有字符都是字母，为真返回 True，否则返回 False。

s.isdigit()     所有字符都是数字，为真返回 True，否则返回 False。

s.islower()    所有字符都是小写，为真返回 True，否则返回 False。

s.isupper()   所有字符都是大写，为真返回 True，否则返回 False。

s.istitle()      所有单词都是首字母大写，为真返回 True，否则返回 False。

s.isspace()   所有字符都是空白字符，为真返回 True，否则返回 False。
         
例如：
>>> s = 'I LOVE FISHC'
>>> s.isupper()
>>> True
'''