def spam():
       print(eggs) # ERROR!
       eggs = 'spam local'
       # print(eggs) # 'spam local'

eggs = 'global'
spam()
