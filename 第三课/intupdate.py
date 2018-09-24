num = input('please input a num:')
numa = int(float(num))
numb = float(num) - numa
if(numb < 0.5):
    print('int:', numa)
else:
    print('int:', (numa + 1))