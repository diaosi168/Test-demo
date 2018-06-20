

#第一题
#利用课堂说的的for循环和range()函数，完成1-100的累加计算

'''shu=list(range(1,101))
print (shu)'''

'''shu=list(range(1,101,1))
print (shu)'''

'''for i in range(1,101):
    print(i)'''

'''sum=0
for i in range(1,101):
    sum+=i
    print(sum)  '''



def sum_1(m,n):
   sum=0
   for i in range(m,n):
       sum+=i
   print(sum)
sum_1(1,101)


#第二题
#完成这个列表的输出a=[5,6,7,9,10,23,45],要求是：把数据按照倒序输出。

'''a=[5,6,7,9,10,23,45]
for i in reversed(a):
    print(i)'''

'''a=[5,6,7,9,10,23,45]
a.reverse()
print(a)'''


#第三题    有问题
#一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，
# 会给10%的折扣，如果购买金额大于100元会给20%折扣。
# 编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格

'''score=int(input("请输入您的购买价格:"))
if 0<score<50:
    print('您输入的购买价格没有折扣')
elif 50<=score<=100:
    print(优惠折扣:10%,折后金额%s'\%'(score*(1-0.1)))
elif score>=100:
    print(优惠折扣:20%,折后金额%s'\%'(score*(1-0.2)))
else:
    print('请输入正确的价格')'''


#第四题
#输入一个数，判断一个数n能同时被3和5整除

'''n=int(input('请输入一个数：'))
if n%3==0 and n%5==0:
    print('该数可以同时被3和5整除！')
else:
    print('请重新输入：')'''



#第五题
#输入一个年份，输出是否为闰年 #闰年条件：能被4整除但不能被100整除，或者能被400整除的年份都是闰年

'''a=int(input('请输入当前的年份：'))
if a%4==0 and a%400==0:
    print('当前年份是闰年')
elif a%100!=0:
    print('当前年份不是闰年')
else:
    print('请输入正确的年份')'''



#第六题    询问10次后，输出满足条件的总人数？
#一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。编写一个程序，
# 询问用户的性别（m表示男性，f表示女性）和年龄，然后显示一条消息指出这个人是否可以加入球队，
# 询问10次后，输出满足条件的总人数。
'''a=int(input('请输入您的年纪：'))
b=input('请输入您的性别：')
if a>=10 and a<=12:
    print('您输入的年纪满足 足球队的加入！')
elif b==m:
    print('男性')
elif b==f:
    print('女性')'''


#age 年龄
#sex 性别

#满足足球队的条件   10<age<=12   and  sex='f'
#input()函数   从控制台获取用户的信息 年龄 性别
#结果值：满足条件的总人数sum
num=0
for i in range(10):
    age=int(input('请输入您的年龄：'))
    sex=input('请输入你的性别：男生m,女生f')
    if 10<=age<=12 and sex=='f':
        num+=1
        print('满足条件，可以加入足球队')
    else:
        print('很遗憾，不满足条件')
        print('满足条件的总人数：',sum)


'''num=0
conunt=10
while True:
    age=int(input('请输入您的年龄：'))
    sex=input('请输入你的性别：男生m,女生f')
    if 10<=age<=12 and sex=='f':
        num+=1
        print('满足条件，可以加入足球队')
    else:
        print('很遗憾，不满足条件')
    print('满足条件的总人数：',sum)'''











#第七题
#生成随机整数，从1-9取出来。然后输入一个数字，来猜，如果大于，则打印bigger。 小了，则打印less。如果相等，则打印equal

'''import random
a=random.randint(1,9)
print("a is %d"%a)
b=int(input('请输入一个数字：'))
if b>a:
    print('bigger')
elif b<a:
    print('less')
elif b==a:
    print('equal')'''





#第八题
#输出99乘法表
'''for i in range(1,10):
    for j in range(i,10):
        print('%d*%d=%2d % (i,j,i*j), end='')
    print('\n')  '''


'''for i in range (1,10):
    for j in range(1,10):
        print(j,"x",i,"=",i*j,"\t",end="")
        if i==j:
            print("")
            break
                   '''

#第九题
#输入num为四位数，对其按照如下的规则进行加密： 1）每一位分别加5，然后分别将其替换为该数除以10取余后的结果 2）
# 将该数的第1位和第4为互换，第二位和第三位互换 3）最后合起来作为加密后的整数输出

num=input('请输入4位数：')

list=[]
for i in num:
    print(i)
    i=(int(i)+5)%10
    list.append(i)
list.reverse()
print(list)





#第十题

#1：有一个列表：list1 = [[2, 3, 8, 4, 9, 5, 6],[5, 6, 10, 17, 11, 2]]，
# 请把list1列表里面的子列表的元素都一个个的输出来

#方法1
'''list_1=[[2,3,8,4,9,5,6],[5,6,10,17,11,2]]
print(list_1[0][1])
print(list_1[0][2])
print(list_1[0][3])
print(list_1[0][4])
print(list_1[0][5])
print(list_1[0][6])
print(list_1[1][1])
print(list_1[1][2])
print(list_1[1][3])
print(list_1[1][4])
print(list_1[1][5])
print(list_1[1][6])'''


#方法2
'''list_1=[[2,3,8,4,9,5,6],[5,6,10,17,11,2]]
for element in  list_1:
    for item in element:
        print(item)'''



#方法3
'''list_1 = [[2, 3, 8, 4, 9, 5, 6], [5, 6, 10, 17, 11, 2]]
new_list_1=list_1[0]
for item in new_list_1:
    new_list_2=list_1[1]
    for item2 in new_list_2:
        print(item,item2)   '''


















































































