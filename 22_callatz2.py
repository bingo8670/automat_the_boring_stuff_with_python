# -*- coding:utf-8 -*-
# 考拉咨猜想
def collatz(number):
    print(number)
    if number ==1:
        return number
    elif number % 2 ==0:
        return collatz(number//2)
    else:
        return collatz(3*number +1)

n = int(input('Input a number: '))
while True:
    try:
         if collatz(n) != 1:
          continue
         else:
          break
    except Exception as e:
        print('Error: Invalid argument.')
