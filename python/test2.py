import random               #导入随机模块
import pyttsx3              #导入第三方语音模块
listen = pyttsx3.init()     #初始化一个变量

txt_path = input('请输入txt文件的path:')		#使用者输入名单文件的路径(名单文件为txt，一行只能有一个姓名，姓名必须在行首不能有空格)
txt = open(f'{txt_path}','r',encoding='utf-8')		#打开名单文件
name_list = []								#创建空列表用于存储名单
for i in txt:								#for循环遍历
    i = i.replace('\n','')					#处理字符串将换行符去掉
    name_list.append(i)						#添加到姓名列表里

print(name_list)							#打印名单


txt.close()									#关闭名单文件

while True:									#永真无限循环
    if len(name_list) == 0:					#当名单里所有人都被点到过一次时结束
        print('结束')
        break
    r_num = random.randint(0, len(name_list) - 1)	#创建随机数
    a = input('输入b退出，其他值继续:')		#让用户选择继续点名还是退出点名
    if a == 'b':							#当用户输入b退出即退出
        print('结束')
        break
    else:									#否则就开始随机点名
        print(f'本次被点到名的是:{name_list[r_num]}')
        listen.say(f'{name_list[r_num]}')	#输出姓名语音
        listen.runAndWait()					#运行语言
        name_list.pop(r_num)				#将点过名的去除掉以防重复
        print()								#间隔作用
