#1.txt中存了很多数据，一行为一个请求数据，怎么样才能把这些数据读取到并且存到list中。数据的存储格式见txt附件

#请把数据从TXT里面读取出来，然后存储为这种数据格式：

'''[{'url':'http://119.23.241.154:8080/futureloan/mvc/api/member/login',
  'mobilephone':'1376246701','pwd':'123456'} ,
 {'url':'http://119.23.241.154:8080/futureloan/mvc/api/member/login',
  'mobilephone':'15678934551','pwd':'234555'}]'''


#可以考虑readline 和readlines


'''file=open('test_1.txt','r+')
rusult_1=file.readlines()
list_1=[]
for items in rusult_1:
    rusult_2=items.strip('\n').split(',')
    dict_1={}
    for item in rusult_2:
        rusult_3=item.split(':',1)
        dict_1[rusult_3[0]]=rusult_3[1]
    list_1.append(dict_1)
print(list_1)
file.close()'''


def score(file):
    file=open(file,'r')
    list_1=[]
    for line in file.readlines():
        dict_1={}
        for lines in line.strip(':').split(','):
            dict_1[lines.split(':',1)[0]]=lines.split(':',1)[1]
            list_1.append(dict_1)

    print(list_1)
    file.close()
score('test_1.txt')