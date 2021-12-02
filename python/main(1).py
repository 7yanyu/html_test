import random
f = int(input("please input the required number of people:"))
g = 0
j = open('name.txt(1).txt',encoding='utf-8') 
name_list = j.readlines()
while g < f :
    i = random.randint(0,len(name_list)-1)
    print(name_list[i])
    name_list.pop(i)
    g=g+1