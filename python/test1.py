i = int(input("Please input one nuber"))            #输入查询人数
g = 0
n = 5                                               #n值为名单总人数 
list_xingming =["张三","李四","王五","王麻子","张麻子","李麻子"]
while g < i:
    import random as rd
    a = rd.randint(0,n)                             #随机生成数a
    print( "幸运儿是：",list_xingming[a])            #a为名单列表的下标
    list_xingming.pop(a)
    g=g+1
    n=n-1
    