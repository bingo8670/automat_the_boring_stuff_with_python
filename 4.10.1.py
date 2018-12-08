#-*-coding:utf-8-*-

#将列表各元素转换为字符串并以规定的形式连接返回
#例如输入spam = ['apples', 'bananas', 'tofu', 'cats'
# 则返回值为：'apples, bananas, tofu, and cats'
def listToStr(inputList):
    ListLen=len(inputList)
    s=''
    if ListLen == 0:           #注意转换为字符串形式输出
        return 'The input is empty'
    elif ListLen == 1 :
        return str(inputList[0])
    else:
        for i in range(ListLen-1):
            s = s + str(inputList[i]) + ','
        s = s + 'and ' + str(inputList[-1])
        return s

#考虑各种输入的情况
# spam = ['apples','bananas','tofu','cats']
# spam = []
# spam = [1,2]
# spam = [1,2,3,4,5,6,7]

#输入列表元素
spam = []
while True:
    print('please enter an element of List'   #依次输入列表元素，以空格回车结束
          ' (Or enter nothing to stop):')      #注意考虑各种输入情况
    name = input()
    if name == '':
        break
    spam +=  [name]

output = listToStr(spam)
print(output)
