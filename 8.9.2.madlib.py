# coding:utf-8
import re
向 open()函数传入'r'，以读模式打开一个文本文件
f1 = open('madlib.txt','r')
strf1 = f1.read()
print("原文件内容为：")
print(strf1)
strf1_list = strf1.split(' ')
f1.close()
# 由于原文件需要被替换的单词都是大写的英文单词
# 使用正则表达式找出原文件中所有将被替换的单词
replist = re.findall(r'[A-Z]{2,}',strf1)
print("原文件中将被替换的单词为：")
print(replist)
print()

for rep in replist:
    inputstr = input("Enter %s " % rep)
    print(inputstr)
    # 先将替换后的单词插入到原列表对应的位置
    strf1_list.insert(strf1_list.index(rep),inputstr)
    # 再将原先的单词删除
    strf1_list.remove(rep)

# 将列表转换为字符串
newstr = ' '.join(strf1_list)
print("替换后的内容为：")
#print(newstr)
# 将新的字符串写入文件b.txt中，并打印到屏幕
# 向 open()函数传入'w'，以写模式打开一个文本文件
f2 = open('b.txt','w+')
f2.write(newstr)
f2.close()
f3 = open('b.txt','r')
print(f3.read())
f3.close()
