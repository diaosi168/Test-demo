
#列
'''try:
    print(a)
except:        #通吃，不管你遇到什么问题都会处理
    print('你好皮！')
else:
    print('damon 你可以啊--这么皮！！')'''
#列2
'''try:
    print(a)
finally:
    print('damon 你可以啊--这么皮！！')     '''''

#列3
'''try:
    print(a)
except:
    print('皮一下')
finally:
    pass
list_1=[1,2,3,4]
for i in range(5):
    print(list_1[i])  '''

#列4
'''try:
    print(a)
except NameError as e:     #except通吃，不管你遇到什么问题都会处
    print("你这个捣蛋鬼，我帮你处理的错误是%s"%e)
    print('你好皮！')
finally:
    print('damon 你可以啊--这么皮！！') '''


#列5
'''try:
    print(a)
except:
    print('你怎么这么可爱')
finally:
    print("你真讨厌")  '''


#列6
'''try:
    file=open("aa.txt",'r+')
except Exception as e:
    print("错误是",e)
finally:
    file.close()  '''


#列7
'''try:
    file=open("test_1.txt",'r+')
except Exception as  e:
     print("错误是",e)
finally:
    file.close()
    print(file.closed) '''


#第一种异常
try:
    #try下面是监控你觉得可能会有问题的代码，或者是可能会出现一些违规操作的代码
    pass
except:
    #excapt下面是针对try监控你的代码出现异常的处理
    pass

#第二种异常
try:    #关键字
    #try下面是监控你觉得可能会有问题的代码，或者是可能会出现一些违规操作的代码
    pass
except:
    #excapt下面是针对try监控你的代码出现异常的处理
    pass
finally:
    #finally下面是针对不管你有没有发现异常，我都要进行finally下面的代码
    pass

#第三种异常
try:    #关键字
    #try下面是监控你觉得可能会有问题的代码，或者是可能会出现一些违规操作的代码
    pass
except:
    #excapt下面是针对try监控你的代码出现异常的处理
    pass
else:
    #如果异常发生就不执行else下面的代码.如果异常发生我就执行else下面的代码
    pass

#第四种异常
try:
    pass
finally:
    pass




#适合各位--》print()   万能的print()
#logging-->日志处理
#debug

'''def add(a,b):
    result=a+b
    return result
add(4,5)     '''

