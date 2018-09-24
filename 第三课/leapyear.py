num = int(input('please input a year num:'))
if((num % 4 == 0 and num % 100 != 0) or (num % 400 == 0)):
    print('this is a leap year')
else:
    print("this isn't a leap year")