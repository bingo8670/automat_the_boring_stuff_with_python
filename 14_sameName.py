#-*- coding: UTF-8 -*-
def spam():
    eggs = 'spam local'
    # 名为 eggs 的变量，存在于 spam()被调用时的局部作用域
    print(eggs) # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    # 名为 eggs 的变量，存在于 bacon()被调用时的局部作用域;
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'

eggs = 'global'
# 名为 eggs 的变量，存在于全局作用域。
bacon()
print(eggs) # prints 'global'
