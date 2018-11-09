data = "1000,小甲鱼,男"
MyDict = {}
# 还记得字符串的分割方法吧
(MyDict['id'], MyDict['name'], MyDict['sex']) = data.split(',')
(MyDict['id'], MyDict['name'], MyDict['sex']) = "1000,小甲鱼,男".split(',')



# print(MyDict)
# print("ID:   " + MyDict['id'])
# print("Name: " + MyDict['name'])
# print("Sex   " + MyDict['sex'])